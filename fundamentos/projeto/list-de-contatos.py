print("Projeto Lista de Contatos")
contatos = []

def add_contato(nome, telefone, email):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")
    return

def ver_contatos(list_contatos):
    if not list_contatos:
        print("Nenhum contato encontrado")
    else:
        for index, contato in enumerate(list_contatos):
            status_favorito = "⭐ " if contato["favorito"] else ''
            print(f'{index}. {status_favorito}{contato["nome"]} - {contato["telefone"]} - {contato["email"]}')
    return

def ver_favoritos():
    print("Lista de contatos favoritos")
    favoritos = []
    for contato in contatos:
        if contato["favorito"]:
            favoritos.append(contato)
    ver_contatos(favoritos)

def editar_contato(index, nome, telefone, email):
    contatos[index]["nome"] = nome
    contatos[index]["telefone"] = telefone
    contatos[index]["email"] = email
    print("Contato atualizado com sucesso!")
    return

def marcar_desmarcar_contato(index, bool):
    contatos[index]["favorito"] = bool
    if bool:
        print(f"Contato {contatos[index]["nome"]} adicionado aos favoritos.")
    else:
        print(f"Contato {contatos[index]["nome"]} removido dos favoritos.")
    return

def delete_contato(index):
    contatos.remove(contatos[index])
    print("Contato removido!")

while True:
    print("\nMenu Lista de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Remover contato dos favorito")
    print("6. Ver favoritos")
    print("7. Deletar contato")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        add_contato(nome, telefone, email)
    elif opcao == "2":
        ver_contatos(contatos)
    elif opcao == "3":
        ver_contatos(contatos)
        index = int(input("Digite o índice do contato: "))
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o e-mail: ")
        editar_contato(index, nome, telefone, email)
    elif opcao == "4":
        ver_contatos(contatos)
        index = int(input("Digite o índice do contato: "))
        marcar_desmarcar_contato(index, True)
    elif opcao == "5":
        ver_contatos(contatos)
        index = int(input("Digite o índice do contato: "))
        marcar_desmarcar_contato(index, False)
    elif opcao == "6":
        ver_favoritos()
    elif opcao == '7':
        ver_contatos(contatos)
        index = int(input("Digite o índice do contato: "))
        delete_contato(index)

    if opcao == "8":
        break