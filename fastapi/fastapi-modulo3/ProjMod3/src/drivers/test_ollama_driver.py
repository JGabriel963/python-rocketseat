from unittest.mock import patch, Mock
from src.drivers.ollama_driver import OllamaDriver

@patch('src.drivers.ollama_driver.requests.post')
def test_send_prompt_success(mock_post):
    # Mock da resposta da API
    mock_response = Mock()
    mock_response.json.return_value = {'response': 'Resposta da LLM'}
    mock_response.raise_for_status.return_value = None
    mock_post.return_value = mock_response

    driver = OllamaDriver()
    prompt = 'Olá, LLM!'
    resposta = driver.send_prompt(prompt)

    assert resposta == 'Resposta da LLM'
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert kwargs['json']['prompt'] == prompt
