# Compression and Cost

Token reduction, cache-friendly restructuring, few-shot pruning, system-prompt slimming, model downsize decisions, and latency redesign.

| File | Description |
|------|-------------|
| `compression_token_audit.md` | Section-by-section token vs load-bearing audit |
| `compression_lossless_rewrite.md` | Behavior-preserving token reduction |
| `compression_lossy_with_test_set.md` | Bounded lossy compression inside a tolerance |
| `compression_cache_friendly_restructure.md` | Maximize stable prefix length for caching |
| `compression_few_shot_pruner.md` | Drop examples by ablation evidence |
| `compression_system_prompt_skinnier.md` | Move conditional rules to JIT or developer prompt |
| `cost_model_downsize_decision.md` | Smaller-model viability with escalation rule |
| `latency_streaming_redesign.md` | Order schema for time-to-first-useful-token |
