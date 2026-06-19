from publisher import rabbit_mq_publisher

print("Bot do Instagram")


def menu():
    print("1. Enviar mensagem")
    print("2. Sair")


option = 0
while True:
    menu()
    while True:
        option = int(input("Escolha uma opção: "))
        if option in [1, 2]:
            break
        print("Opção inválida. Tente novamente.")
    if option == 1:
        message = input("Digite a mensagem: ")
        rabbit_mq_publisher.send_message({"msg": message})
    elif option == 2:
        break
