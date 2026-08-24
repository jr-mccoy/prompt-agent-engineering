# Voice & Conversational UI Domain

**Purpose:** Comprehensive prompt collection for designing, building, and optimizing voice interfaces, chatbots, dialog systems, and multi-modal conversational experiences.

**Total Resources:** 28 prompts across 8 categories

---

## Overview

This domain provides production-grade prompts for voice and conversational UI development, covering the full lifecycle from conversation design through NLU training to analytics optimization. All prompts follow Tier 1 quality standards with false-positive prevention, confidence levels, and detailed examples.

## Categories

| Category | Prompts | Focus |
|----------|---------|-------|
| [voice-design/](voice-design/) | 5 | Voice UI architecture, interaction models, VUI prompt writing |
| [chatbot-design/](chatbot-design/) | 5 | Conversation flows, personality, error handling, LLM-powered bots |
| [dialog-architecture/](dialog-architecture/) | 4 | State machines, intent taxonomies, context management, slot filling |
| [voice-ux/](voice-ux/) | 3 | UX audits, accessibility, error recovery patterns |
| [multimodal/](multimodal/) | 3 | Voice+screen, adaptive interfaces, gesture integration |
| [nlu-training/](nlu-training/) | 3 | Training data generation, intent/entity design, model evaluation |
| [platform-specific/](platform-specific/) | 3 | Alexa Skills, Dialogflow CX/ES, Rasa |
| [analytics/](analytics/) | 2 | Conversation metrics, log-based optimization |

---

## Quick Reference

### By Task

| Task | Prompt |
|------|--------|
| Design an Alexa Skill interaction model | [voice_design_alexa_skill_architecture.md](voice-design/voice_design_alexa_skill_architecture.md) |
| Review a Google Actions project | [voice_design_google_action_review.md](voice-design/voice_design_google_action_review.md) |
| Architect a custom voice assistant | [voice_design_custom_voice_assistant.md](voice-design/voice_design_custom_voice_assistant.md) |
| Build a voice interaction model | [voice_design_interaction_model_builder.md](voice-design/voice_design_interaction_model_builder.md) |
| Write spoken prompts for voice UI | [voice_design_vui_prompt_writing.md](voice-design/voice_design_vui_prompt_writing.md) |
| Design chatbot conversation flows | [chatbot_design_conversation_flow.md](chatbot-design/chatbot_design_conversation_flow.md) |
| Define chatbot personality | [chatbot_design_personality_framework.md](chatbot-design/chatbot_design_personality_framework.md) |
| Design conversational error handling | [chatbot_design_error_handling_patterns.md](chatbot-design/chatbot_design_error_handling_patterns.md) |
| Build enterprise customer service bot | [chatbot_design_enterprise_customer_service.md](chatbot-design/chatbot_design_enterprise_customer_service.md) |
| Architect LLM-powered chatbot | [chatbot_design_llm_powered_architecture.md](chatbot-design/chatbot_design_llm_powered_architecture.md) |
| Design dialog state machine | [dialog_architecture_state_machine_design.md](dialog-architecture/dialog_architecture_state_machine_design.md) |
| Create intent taxonomy | [dialog_architecture_intent_taxonomy.md](dialog-architecture/dialog_architecture_intent_taxonomy.md) |
| Design context management | [dialog_architecture_context_management.md](dialog-architecture/dialog_architecture_context_management.md) |
| Plan slot filling strategy | [dialog_architecture_slot_filling_strategy.md](dialog-architecture/dialog_architecture_slot_filling_strategy.md) |
| Audit voice UX best practices | [voice_ux_best_practices_audit.md](voice-ux/voice_ux_best_practices_audit.md) |
| Review conversational accessibility | [voice_ux_accessibility_review.md](voice-ux/voice_ux_accessibility_review.md) |
| Design voice error recovery | [voice_ux_error_recovery_patterns.md](voice-ux/voice_ux_error_recovery_patterns.md) |
| Design voice+screen interactions | [multimodal_voice_screen_interaction.md](multimodal/multimodal_voice_screen_interaction.md) |
| Create adaptive interface strategy | [multimodal_adaptive_interface_strategy.md](multimodal/multimodal_adaptive_interface_strategy.md) |
| Integrate voice with gesture/touch | [multimodal_voice_gesture_integration.md](multimodal/multimodal_voice_gesture_integration.md) |
| Generate NLU training data | [nlu_training_data_generation.md](nlu-training/nlu_training_data_generation.md) |
| Design intent and entity schema | [nlu_intent_entity_design.md](nlu-training/nlu_intent_entity_design.md) |
| Evaluate and improve NLU model | [nlu_model_evaluation_improvement.md](nlu-training/nlu_model_evaluation_improvement.md) |
| Develop Alexa Skill end-to-end | [platform_alexa_skill_development.md](platform-specific/platform_alexa_skill_development.md) |
| Design Dialogflow agent | [platform_dialogflow_agent_design.md](platform-specific/platform_dialogflow_agent_design.md) |
| Architect Rasa system | [platform_rasa_architecture.md](platform-specific/platform_rasa_architecture.md) |
| Build conversation analytics | [analytics_conversation_metrics_framework.md](analytics/analytics_conversation_metrics_framework.md) |
| Optimize conversations from logs | [analytics_conversation_optimization.md](analytics/analytics_conversation_optimization.md) |

### By Concern

**Voice UI Design:**
- Platform-agnostic interaction model creation
- Alexa and Google Actions architecture
- Custom voice assistant design
- VUI prompt writing and refinement

**Chatbot Design:**
- End-to-end conversation flow mapping
- Bot personality and tone-of-voice frameworks
- Error handling and fallback strategies
- Enterprise customer service automation
- LLM-powered conversational agents

**Dialog Architecture:**
- Finite-state and frame-based dialog management
- Intent taxonomy and entity modeling
- Multi-turn context and memory management
- Slot filling and form completion

**Voice UX:**
- VUI/CUI best practices auditing
- Accessibility for conversational interfaces
- Error recovery and reprompt patterns

**Multi-Modal:**
- Voice + screen synchronized experiences
- Context-adaptive modality switching
- Voice + gesture fusion patterns

**NLU & Training:**
- Training data generation and augmentation
- Intent/entity schema design
- Model evaluation and improvement

**Platforms:**
- Amazon Alexa (ASK SDK v2, APL)
- Google Dialogflow (CX and ES)
- Rasa (open-source conversational AI)

**Analytics:**
- Conversation metrics and KPI frameworks
- Log analysis and optimization

---

## Prompt Quality

All prompts in this domain follow **Tier 1 (Production-Grade)** standards:

- Clear objective and instructions
- False-Positive Prevention sections
- Confidence levels for findings
- Detailed example outputs
- Techniques documented
- Customization guides

---

## Getting Started

1. **Identify your need** using the task table above
2. **Read the prompt** and understand the methodology
3. **Execute** the prompt with your project context
4. **Customize** using the guide at the bottom of each prompt

---

## Related Resources

- [domain-conversation-practice/](../domain-conversation-practice/) - Conversation simulation for language learning
- [domain-software-engineering/api/](../domain-software-engineering/api/) - API design prompts (webhook/fulfillment patterns)
- [domain-frontend-development/accessibility/](../domain-frontend-development/accessibility/) - Accessibility auditing
- [techniques/MASTER_TECHNIQUE_INDEX.md](../techniques/MASTER_TECHNIQUE_INDEX.md) - Prompt engineering techniques

---

**Last Updated:** 2026-03-19
**Version:** 1.0.0
