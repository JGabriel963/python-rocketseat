input = input("Digite sua idade: ")

age = int(input)

if age >= 18 and age < 60:
    print("Você é maior de idade")
elif age >= 15 and age < 18:
    print("Você é um adolescente")
elif age >= 6 and age < 15:
    print("Você é uma criança")
elif age >= 60:
    print("Você é um idoso")
else:
    print("Você é menor de idade")