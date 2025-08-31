print("Exeções")
while True:
    try:
        number = int(input("Digite um número: "))
        result = 100 / number
        print(f"Resultado: {result}")
        break
    except ValueError as e:
        print(f"Erro de value error: {e}")
    except Exception as e:
        print(f"Erro: {e}")