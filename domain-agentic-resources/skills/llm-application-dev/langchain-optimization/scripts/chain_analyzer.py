#!/usr/bin/env python3
"""
Chain Analyzer for LangChain Applications

Analyzes LangChain chain execution to identify performance bottlenecks,
token usage patterns, and optimization opportunities.

Usage:
    python chain_analyzer.py --chain <chain_module> --input "test query"
    python chain_analyzer.py --trace-file <langsmith_trace.json>
"""

import argparse
import json
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from collections import defaultdict


@dataclass
class ChainMetrics:
    """Metrics collected for a single chain execution."""
    chain_name: str
    total_time_ms: float = 0.0
    llm_time_ms: float = 0.0
    retrieval_time_ms: float = 0.0
    tool_time_ms: float = 0.0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    llm_calls: int = 0
    retrieval_calls: int = 0
    tool_calls: int = 0
    errors: List[str] = field(default_factory=list)


@dataclass
class AnalysisReport:
    """Complete analysis report for chain execution."""
    metrics: ChainMetrics
    bottlenecks: List[str]
    recommendations: List[str]
    cost_estimate_usd: float


class ChainAnalyzer:
    """Analyze LangChain execution for optimization opportunities."""

    # Cost per 1K tokens (as of 2024)
    COST_PER_1K = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "claude-3-opus": {"input": 0.015, "output": 0.075},
        "claude-3-sonnet": {"input": 0.003, "output": 0.015},
    }

    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.timings: Dict[str, List[float]] = defaultdict(list)
        self.token_counts: Dict[str, int] = defaultdict(int)
        self.call_counts: Dict[str, int] = defaultdict(int)
        self.errors: List[str] = []

    def create_callback_handler(self):
        """Create a LangChain callback handler for profiling."""
        try:
            from langchain.callbacks.base import BaseCallbackHandler
        except ImportError:
            print("LangChain not installed. Install with: pip install langchain")
            return None

        analyzer = self

        class ProfilerCallback(BaseCallbackHandler):
            def __init__(self):
                self._start_times = {}

            def on_llm_start(self, serialized, prompts, **kwargs):
                self._start_times["llm"] = time.time()
                analyzer.call_counts["llm"] += 1

            def on_llm_end(self, response, **kwargs):
                if "llm" in self._start_times:
                    elapsed = (time.time() - self._start_times["llm"]) * 1000
                    analyzer.timings["llm"].append(elapsed)

                # Extract token counts if available
                if hasattr(response, "llm_output") and response.llm_output:
                    usage = response.llm_output.get("token_usage", {})
                    analyzer.token_counts["prompt"] += usage.get("prompt_tokens", 0)
                    analyzer.token_counts["completion"] += usage.get("completion_tokens", 0)

            def on_retriever_start(self, serialized, query, **kwargs):
                self._start_times["retrieval"] = time.time()
                analyzer.call_counts["retrieval"] += 1

            def on_retriever_end(self, documents, **kwargs):
                if "retrieval" in self._start_times:
                    elapsed = (time.time() - self._start_times["retrieval"]) * 1000
                    analyzer.timings["retrieval"].append(elapsed)

            def on_tool_start(self, serialized, input_str, **kwargs):
                self._start_times["tool"] = time.time()
                analyzer.call_counts["tool"] += 1

            def on_tool_end(self, output, **kwargs):
                if "tool" in self._start_times:
                    elapsed = (time.time() - self._start_times["tool"]) * 1000
                    analyzer.timings["tool"].append(elapsed)

            def on_llm_error(self, error, **kwargs):
                analyzer.errors.append(f"LLM Error: {str(error)}")

            def on_chain_error(self, error, **kwargs):
                analyzer.errors.append(f"Chain Error: {str(error)}")

        return ProfilerCallback()

    def analyze_trace_file(self, trace_path: str) -> AnalysisReport:
        """Analyze a LangSmith trace export."""
        with open(trace_path, "r") as f:
            trace_data = json.load(f)

        # Parse trace data (LangSmith format)
        self._parse_langsmith_trace(trace_data)
        return self._generate_report("trace_analysis")

    def _parse_langsmith_trace(self, trace_data: Dict[str, Any]):
        """Parse LangSmith trace format."""
        runs = trace_data.get("runs", [trace_data])

        for run in runs:
            run_type = run.get("run_type", "unknown")
            start_time = run.get("start_time")
            end_time = run.get("end_time")

            if start_time and end_time:
                # Parse ISO format timestamps
                from datetime import datetime
                start = datetime.fromisoformat(start_time.replace("Z", "+00:00"))
                end = datetime.fromisoformat(end_time.replace("Z", "+00:00"))
                elapsed_ms = (end - start).total_seconds() * 1000
                self.timings[run_type].append(elapsed_ms)
                self.call_counts[run_type] += 1

            # Extract token usage
            if "token_usage" in run.get("outputs", {}):
                usage = run["outputs"]["token_usage"]
                self.token_counts["prompt"] += usage.get("prompt_tokens", 0)
                self.token_counts["completion"] += usage.get("completion_tokens", 0)

            # Process child runs recursively
            for child in run.get("child_runs", []):
                self._parse_langsmith_trace(child)

    def _generate_report(self, chain_name: str) -> AnalysisReport:
        """Generate analysis report from collected metrics."""
        metrics = ChainMetrics(
            chain_name=chain_name,
            total_time_ms=sum(sum(t) for t in self.timings.values()),
            llm_time_ms=sum(self.timings.get("llm", [])),
            retrieval_time_ms=sum(self.timings.get("retrieval", [])),
            tool_time_ms=sum(self.timings.get("tool", [])),
            prompt_tokens=self.token_counts["prompt"],
            completion_tokens=self.token_counts["completion"],
            total_tokens=self.token_counts["prompt"] + self.token_counts["completion"],
            llm_calls=self.call_counts.get("llm", 0),
            retrieval_calls=self.call_counts.get("retrieval", 0),
            tool_calls=self.call_counts.get("tool", 0),
            errors=self.errors
        )

        bottlenecks = self._identify_bottlenecks(metrics)
        recommendations = self._generate_recommendations(metrics, bottlenecks)
        cost_estimate = self._estimate_cost(metrics)

        return AnalysisReport(
            metrics=metrics,
            bottlenecks=bottlenecks,
            recommendations=recommendations,
            cost_estimate_usd=cost_estimate
        )

    def _identify_bottlenecks(self, metrics: ChainMetrics) -> List[str]:
        """Identify performance bottlenecks."""
        bottlenecks = []

        if metrics.total_time_ms > 0:
            llm_pct = (metrics.llm_time_ms / metrics.total_time_ms) * 100
            retrieval_pct = (metrics.retrieval_time_ms / metrics.total_time_ms) * 100

            if llm_pct > 80:
                bottlenecks.append(f"LLM calls dominate ({llm_pct:.1f}% of total time)")
            if retrieval_pct > 50:
                bottlenecks.append(f"Retrieval is slow ({retrieval_pct:.1f}% of total time)")

        if metrics.llm_calls > 5:
            bottlenecks.append(f"High LLM call count ({metrics.llm_calls} calls)")

        if metrics.total_tokens > 4000:
            bottlenecks.append(f"High token usage ({metrics.total_tokens} tokens)")

        avg_llm_time = metrics.llm_time_ms / max(metrics.llm_calls, 1)
        if avg_llm_time > 2000:
            bottlenecks.append(f"Slow average LLM response ({avg_llm_time:.0f}ms)")

        return bottlenecks

    def _generate_recommendations(self, metrics: ChainMetrics, bottlenecks: List[str]) -> List[str]:
        """Generate optimization recommendations."""
        recommendations = []

        for bottleneck in bottlenecks:
            if "LLM calls dominate" in bottleneck:
                recommendations.append("Consider enabling LLM caching with SQLiteCache or SemanticCache")
                recommendations.append("Use streaming for perceived performance improvement")

            if "Retrieval is slow" in bottleneck:
                recommendations.append("Consider adding a reranking step with smaller initial k")
                recommendations.append("Evaluate vector index parameters (HNSW ef_search, IVF nprobe)")

            if "High LLM call count" in bottleneck:
                recommendations.append("Batch LLM calls where possible using generate()")
                recommendations.append("Consider combining chain steps to reduce round-trips")

            if "High token usage" in bottleneck:
                recommendations.append("Implement memory trimming or switch to ConversationSummaryMemory")
                recommendations.append("Use contextual compression to reduce retrieved document size")

            if "Slow average LLM response" in bottleneck:
                recommendations.append("Consider using a faster model (gpt-3.5-turbo) for simple tasks")
                recommendations.append("Implement request timeouts and fallback strategies")

        if not recommendations:
            recommendations.append("Performance looks good! Consider adding monitoring for production.")

        return recommendations

    def _estimate_cost(self, metrics: ChainMetrics) -> float:
        """Estimate cost in USD."""
        costs = self.COST_PER_1K.get(self.model, self.COST_PER_1K["gpt-4"])
        input_cost = (metrics.prompt_tokens / 1000) * costs["input"]
        output_cost = (metrics.completion_tokens / 1000) * costs["output"]
        return input_cost + output_cost

    def print_report(self, report: AnalysisReport):
        """Print formatted analysis report."""
        print("\n" + "=" * 60)
        print("LANGCHAIN PERFORMANCE ANALYSIS REPORT")
        print("=" * 60)

        print(f"\nChain: {report.metrics.chain_name}")
        print(f"\n--- Timing Breakdown ---")
        print(f"Total Time:      {report.metrics.total_time_ms:.2f}ms")
        print(f"  LLM Time:      {report.metrics.llm_time_ms:.2f}ms ({report.metrics.llm_calls} calls)")
        print(f"  Retrieval:     {report.metrics.retrieval_time_ms:.2f}ms ({report.metrics.retrieval_calls} calls)")
        print(f"  Tool Calls:    {report.metrics.tool_time_ms:.2f}ms ({report.metrics.tool_calls} calls)")

        print(f"\n--- Token Usage ---")
        print(f"Prompt Tokens:     {report.metrics.prompt_tokens}")
        print(f"Completion Tokens: {report.metrics.completion_tokens}")
        print(f"Total Tokens:      {report.metrics.total_tokens}")
        print(f"Estimated Cost:    ${report.cost_estimate_usd:.4f}")

        if report.metrics.errors:
            print(f"\n--- Errors ({len(report.metrics.errors)}) ---")
            for error in report.metrics.errors:
                print(f"  - {error}")

        print(f"\n--- Bottlenecks Identified ({len(report.bottlenecks)}) ---")
        for bottleneck in report.bottlenecks:
            print(f"  [!] {bottleneck}")

        print(f"\n--- Recommendations ---")
        for i, rec in enumerate(report.recommendations, 1):
            print(f"  {i}. {rec}")

        print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Analyze LangChain chain performance")
    parser.add_argument("--trace-file", type=str, help="Path to LangSmith trace JSON export")
    parser.add_argument("--model", type=str, default="gpt-4", help="Model for cost estimation")
    parser.add_argument("--output", type=str, help="Output JSON report path")

    args = parser.parse_args()

    analyzer = ChainAnalyzer(model=args.model)

    if args.trace_file:
        report = analyzer.analyze_trace_file(args.trace_file)
    else:
        print("Usage: Provide --trace-file with a LangSmith trace export")
        print("\nTo collect traces, use the ProfilerCallback in your chain:")
        print("  callback = analyzer.create_callback_handler()")
        print("  chain.invoke(input, config={'callbacks': [callback]})")
        return

    analyzer.print_report(report)

    if args.output:
        import dataclasses
        with open(args.output, "w") as f:
            json.dump(dataclasses.asdict(report), f, indent=2)
        print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
