import streamlit as st

class ChatView:
    def __init__(self, ollama_driver):
        """
        Inicializa a view com o driver Ollama
        """
        self.ollama_driver = ollama_driver
    
    def render(self):
        """
        Renderiza todos os componentes visuais do chat
        """
        # Título do chat
        st.title("🚀 Rocket Chat")

        # Campo de entrada e botão de envio
        self._render_input_area()
        
        # Área de exibição de mensagens
        self._render_messages()
    
    def _render_messages(self):
        """
        Renderiza o histórico de mensagens do chat
        """
        # Container para mensagens
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.messages:
                # Mensagem do usuário
                if message['role'] == 'user':
                    with st.chat_message("user"):
                        st.write(message['content'])
                # Resposta da LLM
                elif message['role'] == 'assistant':
                    with st.chat_message("assistant"):
                        st.write(message['content'])
    
    def _render_input_area(self):
        """
        Renderiza o campo de entrada de texto e botão de envio
        """
        # Formulário para entrada de prompt
        with st.form(key='chat_form', clear_on_submit=True):
            # Campo de texto para o prompt
            user_input = st.text_input(
                "Digite sua mensagem:",
                placeholder="Escreva seu prompt aqui...",
                key="user_input"
            )
            
            # Botão de confirmação
            submit_button = st.form_submit_button("Enviar")
            
            # Processamento ao enviar
            if submit_button and user_input:
                self._handle_submit(user_input)
    
    def _handle_submit(self, user_input):
        """
        Processa o envio do prompt à LLM
        """
        # Adiciona mensagem do usuário ao histórico
        st.session_state.messages.append({
            'role': 'user',
            'content': user_input
        })
        
        # Envia prompt para Ollama e obtém resposta
        response = self.ollama_driver.send_prompt(user_input)
        
        # Adiciona resposta da LLM ao histórico
        st.session_state.messages.append({
            'role': 'assistant',
            'content': response
        })
        
        # Força atualização da interface
        st.rerun()