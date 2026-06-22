import requests
import json

class OllamaDriver:
    """
    Driver responsável pela comunicação com a LLM hospedada no Ollama
    utilizando a biblioteca Requests
    """
    
    def __init__(self, base_url="http://localhost:3001"):
        """
        Inicializa o driver com a URL do Ollama e modelo padrão
        """
        self.base_url = base_url
        self.endpoint = f"{self.base_url}/generate"
    
    def send_prompt(self, prompt):
        """
        Envia o prompt para a LLM e retorna a resposta
        """
        # Payload da requisição
        payload = {
            "user_prompt": prompt,
        }
        
        try:
            # Requisição POST usando biblioteca Requests
            response = requests.post(
                self.endpoint,
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            # Verifica sucesso da requisição
            response.raise_for_status()
            
            # Extrai resposta da LLM
            result = response.json()
            return result.get('response', 'Erro ao obter resposta')
            
        except requests.exceptions.RequestException as e:
            # Tratamento de erros de conexão
            return f"Erro na comunicação com Ollama: {str(e)}"
        except json.JSONDecodeError:
            # Tratamento de erros de parsing
            return "Erro ao processar resposta da LLM"