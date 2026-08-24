#!/usr/bin/env python3
"""
Memory Profiler for LangChain Applications

Profiles memory usage in LangChain applications, tracking token consumption,
context window utilization, and memory object sizes.

Usage:
    python memory_profiler.py --memory-dump <memory_state.json>
    python memory_profiler.py --interactive
"""

import argparse
import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MemoryProfile:
    """Profile of a LangChain memory object."""
    memory_type: str
    message_count: int
    total_tokens: int
    estimated_chars: int
    context_utilization_pct: float
    token_breakdown: Dict[str, int]
    warnings: List[str]
    recommendations: List[str]


class MemoryProfiler:
    """Profile LangChain memory objects for optimization."""

    # Context window sizes by model
    CONTEXT_WINDOWS = {
        "gpt-4": 8192,
        "gpt-4-32k": 32768,
        "gpt-4-turbo": 128000,
        "gpt-3.5-turbo": 4096,
        "gpt-3.5-turbo-16k": 16384,
        "claude-3-opus": 200000,
        "claude-3-sonnet": 200000,
    }

    # Approximate tokens per character
    TOKENS_PER_CHAR = 0.25

    def __init__(self, model: str = "gpt-4", reserved_tokens: int = 1000):
        """
        Initialize profiler.

        Args:
            model: Target model for context window calculations
            reserved_tokens: Tokens reserved for system prompt and response
        """
        self.model = model
        self.context_window = self.CONTEXT_WINDOWS.get(model, 8192)
        self.reserved_tokens = reserved_tokens
        self.available_tokens = self.context_window - reserved_tokens

    def count_tokens(self, text: str) -> int:
        """Count tokens in text."""
        try:
            import tiktoken
            encoding = tiktoken.encoding_for_model(self.model)
            return len(encoding.encode(text))
        except ImportError:
            # Fallback to character-based estimation
            return int(len(text) * self.TOKENS_PER_CHAR)

    def profile_memory(self, memory: Any) -> MemoryProfile:
        """
        Profile a LangChain memory object.

        Args:
            memory: A LangChain memory object (ConversationBufferMemory, etc.)

        Returns:
            MemoryProfile with detailed analysis
        """
        memory_type = type(memory).__name__
        messages = []
        token_breakdown = {}

        # Extract messages based on memory type
        if hasattr(memory, "chat_memory") and hasattr(memory.chat_memory, "messages"):
            messages = memory.chat_memory.messages
        elif hasattr(memory, "buffer"):
            if isinstance(memory.buffer, str):
                messages = [{"content": memory.buffer}]
            elif isinstance(memory.buffer, list):
                messages = memory.buffer

        # Count tokens by role
        total_tokens = 0
        for msg in messages:
            if hasattr(msg, "content"):
                content = msg.content
                role = msg.type if hasattr(msg, "type") else "unknown"
            elif isinstance(msg, dict):
                content = msg.get("content", str(msg))
                role = msg.get("role", "unknown")
            else:
                content = str(msg)
                role = "unknown"

            tokens = self.count_tokens(content)
            total_tokens += tokens
            token_breakdown[role] = token_breakdown.get(role, 0) + tokens

        utilization = (total_tokens / self.available_tokens) * 100

        # Generate warnings
        warnings = []
        if utilization > 90:
            warnings.append(f"CRITICAL: Memory at {utilization:.1f}% of available context")
        elif utilization > 70:
            warnings.append(f"WARNING: Memory at {utilization:.1f}% of available context")

        if len(messages) > 50:
            warnings.append(f"High message count ({len(messages)}). Consider using windowed memory.")

        # Generate recommendations
        recommendations = self._generate_recommendations(
            memory_type, len(messages), total_tokens, utilization
        )

        return MemoryProfile(
            memory_type=memory_type,
            message_count=len(messages),
            total_tokens=total_tokens,
            estimated_chars=int(total_tokens / self.TOKENS_PER_CHAR),
            context_utilization_pct=utilization,
            token_breakdown=token_breakdown,
            warnings=warnings,
            recommendations=recommendations
        )

    def profile_from_dict(self, memory_state: Dict[str, Any]) -> MemoryProfile:
        """Profile memory from a dictionary representation."""
        memory_type = memory_state.get("type", "Unknown")
        messages = memory_state.get("messages", [])
        buffer = memory_state.get("buffer", "")

        total_tokens = 0
        token_breakdown = {}

        if messages:
            for msg in messages:
                content = msg.get("content", "")
                role = msg.get("role", "unknown")
                tokens = self.count_tokens(content)
                total_tokens += tokens
                token_breakdown[role] = token_breakdown.get(role, 0) + tokens
        elif buffer:
            total_tokens = self.count_tokens(buffer)
            token_breakdown["buffer"] = total_tokens

        utilization = (total_tokens / self.available_tokens) * 100

        warnings = []
        if utilization > 90:
            warnings.append(f"CRITICAL: Memory at {utilization:.1f}% of available context")
        elif utilization > 70:
            warnings.append(f"WARNING: Memory at {utilization:.1f}% of available context")

        recommendations = self._generate_recommendations(
            memory_type, len(messages), total_tokens, utilization
        )

        return MemoryProfile(
            memory_type=memory_type,
            message_count=len(messages),
            total_tokens=total_tokens,
            estimated_chars=int(total_tokens / self.TOKENS_PER_CHAR),
            context_utilization_pct=utilization,
            token_breakdown=token_breakdown,
            warnings=warnings,
            recommendations=recommendations
        )

    def _generate_recommendations(
        self,
        memory_type: str,
        message_count: int,
        total_tokens: int,
        utilization: float
    ) -> List[str]:
        """Generate optimization recommendations."""
        recommendations = []

        if utilization > 70:
            if "Buffer" in memory_type and "Window" not in memory_type:
                recommendations.append(
                    "Switch to ConversationBufferWindowMemory with k=10-20 to limit history"
                )
            if "Summary" not in memory_type:
                recommendations.append(
                    "Consider ConversationSummaryMemory to compress older messages"
                )
            recommendations.append(
                "Implement token-based trimming to stay under budget"
            )

        if message_count > 30 and "Window" not in memory_type:
            recommendations.append(
                f"High message count ({message_count}). Use windowed memory or periodic summarization."
            )

        if total_tokens > 2000 and "Vector" not in memory_type:
            recommendations.append(
                "Consider VectorStoreRetrieverMemory for semantic relevance-based retrieval"
            )

        # Memory-type specific recommendations
        if "ConversationBufferMemory" in memory_type:
            recommendations.append(
                "Good for short conversations. Monitor token usage as conversation grows."
            )
        elif "ConversationSummaryMemory" in memory_type:
            recommendations.append(
                "Summaries add LLM calls. Balance compression vs latency."
            )
        elif "ConversationBufferWindowMemory" in memory_type:
            recommendations.append(
                "Tune k parameter based on typical conversation length."
            )

        if not recommendations:
            recommendations.append("Memory usage is healthy. No immediate optimizations needed.")

        return recommendations

    def suggest_memory_type(self, use_case: str) -> Dict[str, Any]:
        """Suggest optimal memory type for use case."""
        suggestions = {
            "short_chat": {
                "type": "ConversationBufferMemory",
                "reason": "Simple and efficient for conversations < 10 turns",
                "config": {"return_messages": True}
            },
            "long_chat": {
                "type": "ConversationSummaryBufferMemory",
                "reason": "Keeps recent messages verbatim, summarizes older ones",
                "config": {"max_token_limit": 2000, "return_messages": True}
            },
            "entity_tracking": {
                "type": "ConversationEntityMemory",
                "reason": "Tracks information about entities mentioned in conversation",
                "config": {"return_messages": True}
            },
            "knowledge_retrieval": {
                "type": "VectorStoreRetrieverMemory",
                "reason": "Retrieves semantically relevant past interactions",
                "config": {"k": 5}
            },
            "bounded_context": {
                "type": "ConversationBufferWindowMemory",
                "reason": "Fixed window of recent messages, predictable token usage",
                "config": {"k": 10, "return_messages": True}
            }
        }

        return suggestions.get(use_case, suggestions["short_chat"])

    def print_profile(self, profile: MemoryProfile):
        """Print formatted memory profile."""
        print("\n" + "=" * 50)
        print("LANGCHAIN MEMORY PROFILE")
        print("=" * 50)

        print(f"\nMemory Type: {profile.memory_type}")
        print(f"Model: {self.model} (Context: {self.context_window:,} tokens)")
        print(f"Reserved Tokens: {self.reserved_tokens:,}")
        print(f"Available for Memory: {self.available_tokens:,}")

        print(f"\n--- Memory Usage ---")
        print(f"Messages: {profile.message_count}")
        print(f"Total Tokens: {profile.total_tokens:,}")
        print(f"Estimated Characters: {profile.estimated_chars:,}")
        print(f"Context Utilization: {profile.context_utilization_pct:.1f}%")

        # Progress bar
        bar_length = 40
        filled = int(bar_length * min(profile.context_utilization_pct, 100) / 100)
        bar = "=" * filled + "-" * (bar_length - filled)
        print(f"[{bar}] {profile.context_utilization_pct:.1f}%")

        if profile.token_breakdown:
            print(f"\n--- Token Breakdown by Role ---")
            for role, tokens in sorted(profile.token_breakdown.items(), key=lambda x: -x[1]):
                pct = (tokens / max(profile.total_tokens, 1)) * 100
                print(f"  {role}: {tokens:,} tokens ({pct:.1f}%)")

        if profile.warnings:
            print(f"\n--- Warnings ---")
            for warning in profile.warnings:
                print(f"  [!] {warning}")

        print(f"\n--- Recommendations ---")
        for i, rec in enumerate(profile.recommendations, 1):
            print(f"  {i}. {rec}")

        print("\n" + "=" * 50)


def main():
    parser = argparse.ArgumentParser(description="Profile LangChain memory usage")
    parser.add_argument("--memory-dump", type=str, help="Path to memory state JSON")
    parser.add_argument("--model", type=str, default="gpt-4", help="Target model")
    parser.add_argument("--reserved", type=int, default=1000, help="Reserved tokens")
    parser.add_argument("--suggest", type=str, help="Suggest memory type for use case")
    parser.add_argument("--output", type=str, help="Output JSON path")

    args = parser.parse_args()

    profiler = MemoryProfiler(model=args.model, reserved_tokens=args.reserved)

    if args.suggest:
        suggestion = profiler.suggest_memory_type(args.suggest)
        print(f"\nRecommended Memory Type for '{args.suggest}':")
        print(f"  Type: {suggestion['type']}")
        print(f"  Reason: {suggestion['reason']}")
        print(f"  Config: {suggestion['config']}")
        return

    if args.memory_dump:
        with open(args.memory_dump, "r") as f:
            memory_state = json.load(f)
        profile = profiler.profile_from_dict(memory_state)
        profiler.print_profile(profile)

        if args.output:
            import dataclasses
            with open(args.output, "w") as f:
                json.dump(dataclasses.asdict(profile), f, indent=2)
            print(f"\nProfile saved to: {args.output}")
    else:
        print("LangChain Memory Profiler")
        print("\nUsage Examples:")
        print("  python memory_profiler.py --memory-dump state.json --model gpt-4")
        print("  python memory_profiler.py --suggest long_chat")
        print("  python memory_profiler.py --suggest knowledge_retrieval")
        print("\nUse Cases for --suggest:")
        print("  - short_chat: Quick conversations (<10 turns)")
        print("  - long_chat: Extended conversations")
        print("  - entity_tracking: Track people/places/things")
        print("  - knowledge_retrieval: Semantic memory retrieval")
        print("  - bounded_context: Fixed-size memory window")


if __name__ == "__main__":
    main()
