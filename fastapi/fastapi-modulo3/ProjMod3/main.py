import streamlit as st
from src.views.chat_view import ChatView
from src.drivers.ollama_driver import OllamaDriver

def main():
    """
    Configuração inicial e execução do sistema Rocket Chat
    """
    # Configuração da página
    st.set_page_config(
        page_title="Rocket Chat",
        page_icon="🚀",
        layout="centered"
    )

    # Inicialização do driver Ollama
    if 'ollama_driver' not in st.session_state:
        st.session_state.ollama_driver = OllamaDriver()

    # Inicialização do histórico de mensagens
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Renderização da view do chat
    chat_view = ChatView(st.session_state.ollama_driver)
    chat_view.render()

if __name__ == "__main__":
    main()
