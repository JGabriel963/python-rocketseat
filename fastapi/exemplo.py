class ContextoSimples:

    def __enter__(self):
        print("Iniciar conexao...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Fechando conexão com segurança!")


with ContextoSimples() as cs:
    print("Execuções em banco de dados!")