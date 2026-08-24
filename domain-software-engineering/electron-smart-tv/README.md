# Electron Smart TV Launcher Prompts

Prompts for AI coding agents working on Electron-based smart TV launchers — apps that provide a full-screen, remote-controlled interface for curated streaming content (YouTube channels, Disney+) with parental controls, offline caching, and kiosk-mode deployment.

## Prompt Index

### Security & Safety
| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [Electron IPC & Preload Security Audit](electron_ipc_preload_security_audit.md) | Audit IPC channels, contextBridge exposures, and preload scripts for privilege escalation | Advanced |
| [Content Safety & Webview Sandboxing Review](content_safety_webview_sandboxing_review.md) | Verify content whitelisting, navigation controls, and parental control bypass resistance | Advanced |

### Architecture & Lifecycle
| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [Multi-Window Lifecycle & Memory Management](electron_multi_window_lifecycle_analysis.md) | Analyze BrowserWindow creation/destruction, reference cleanup, and memory leak patterns | Advanced |
| [Electron Packaging & Cross-Platform Distribution](electron_packaging_cross_platform_review.md) | Review resource bundling, environment handling, asar compatibility, and production hardening | Intermediate |

### Performance
| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [Electron App Performance & Startup Profiling](electron_app_performance_profiling.md) | Profile startup latency, renderer performance, memory growth, and low-power hardware suitability | Intermediate |

### YouTube API & Caching
| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [YouTube Cache Manager Correctness Review](youtube_cache_manager_correctness_review.md) | Review cache integrity, incremental refresh logic, persistence safety, and concurrent access | Advanced |
| [API Quota Strategy & Rate Limiting Review](api_quota_strategy_rate_limiting_review.md) | Verify quota cost calculations, daily budget allocation, and defensive exhaustion handling | Intermediate |

### Network & Resilience
| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [Network Resilience & Offline Graceful Degradation](network_resilience_offline_graceful_degradation.md) | Analyze offline fallback, error communication, and recovery behavior | Intermediate |

### Navigation & Input
| Prompt | Description | Difficulty |
|--------|-------------|------------|
| [10-Foot Spatial Navigation & Accessibility Audit](spatial_navigation_10ft_accessibility_audit.md) | Audit spatial navigation reachability, focus indicators, and cross-context focus transitions | Intermediate |
| [Remote-First Input Handling & Focus Management](remote_input_handling_focus_management.md) | Review key event propagation, Back/Home behavior chains, and focus restoration | Intermediate |

## Recommended Usage Order

For a comprehensive review of a new Electron smart TV launcher:

1. **Security first:** IPC Security Audit → Content Safety Review
2. **Architecture:** Multi-Window Lifecycle → Packaging Review
3. **Core subsystems:** Cache Manager Review → API Quota Review
4. **Resilience:** Network Resilience Analysis
5. **User experience:** Spatial Navigation Audit → Remote Input Handling
6. **Performance:** Performance Profiling (best done after other issues are addressed)

## Cross-References

These prompts are designed to work with the broader prompt collection:

- General security: `domain-software-engineering/analysis/security/`
- General performance: `domain-software-engineering/analysis/performance/`
- Accessibility: `domain-frontend-development/accessibility/`
- DevOps/CI: `domain-software-engineering/devops/`
