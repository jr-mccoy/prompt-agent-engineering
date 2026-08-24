# LangChain Optimization — Error Recovery Patterns and Testing

## Error Recovery Patterns

```python
from langchain.schema import OutputParserException
from tenacity import retry, stop_after_attempt, wait_exponential

class RobustChain:
    def __init__(self, chain, fallback_chain=None):
        self.chain = chain
        self.fallback = fallback_chain

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def invoke_with_retry(self, inputs):
        return self.chain.invoke(inputs)

    def invoke(self, inputs):
        try:
            return self.invoke_with_retry(inputs)
        except Exception as e:
            if self.fallback:
                return self.fallback.invoke(inputs)
            raise
```

---

## Testing Patterns

### 1. Chain Testing

```python
import pytest
from unittest.mock import Mock, patch

def test_chain_output_format():
    """Test that chain produces expected output structure."""
    with patch('langchain.chat_models.ChatOpenAI') as mock_llm:
        mock_llm.return_value.predict.return_value = "Test response"

        result = chain.invoke({"query": "test"})

        assert "result" in result
        assert isinstance(result["result"], str)

def test_chain_handles_empty_input():
    """Test graceful handling of edge cases."""
    result = chain.invoke({"query": ""})
    assert result is not None

def test_chain_respects_token_limits():
    """Test that chain doesn't exceed token limits."""
    with get_openai_callback() as cb:
        chain.invoke({"query": "long " * 1000})
        assert cb.total_tokens < 8000
```

### 2. Agent Testing

```python
def test_agent_tool_selection():
    """Test agent selects correct tool for task."""
    debugger = AgentDebugger()
    agent.invoke(
        {"input": "What is 25 * 4?"},
        config={"callbacks": [debugger]}
    )

    actions = [s for s in debugger.steps if s["type"] == "action"]
    assert any(a["tool"] == "calculator" for a in actions)

def test_agent_max_iterations():
    """Test agent respects iteration limits."""
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        max_iterations=3
    )

    result = agent_executor.invoke({"input": "impossible task"})
    # Should not hang or loop forever
    assert result is not None
```
