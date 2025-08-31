## Inteiros
age = 30
print(age)
print(type(age))

## Flutuantes
pi = 3.14
print(pi)
print(type(pi))

## Operações aritiméticas
print("Soma")
print(10 + 10)

print("Subtração")
print(10 - 5)

print("Multiplicação")
print(10 * 10)

print("Divisão")
print(10 / 2)

print("Exponenciação")
print(5 ** 2)

print("Divisão inteira")
print(10 // 3)

print("Resto da divisão")
print(10 % 3)

## Textos
full_name = "João Gabriel da Conceição Oliveira"
bio = """
    Desenvolvedor Web JavaScript.
    Atualmente estudando python na Rocketseat
"""
print(full_name, bio)

## Formatação
name = "João Gabriel"
print(f'{name} tem {age} anos')

## Métodos de texto
print(name.upper())
print(name.lower())
print(name.count("o"))
print(name.lower().find("g"))
print(name.encode())

phone = "+55 (86) 98892-3098"
print(phone.replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))

print(name.startswith("J"))
print(name.endswith("a"))
print("ão" in name)
print("ã" not in name)


## List
fruits = []
fruits.append("Laranja")
fruits.append("Maçã")

print(fruits)

## fruits.pop()
fruits.remove(fruits[0])

print(fruits)


## Diconário
people = {"nome": "João", "age": 23, "city": "São Paulo", "job": ["Web Development", "Backend", "Fullstack"]}
print(people)

print(people["nome"])
print(people["age"])
print(people["job"])
people["last_name"] = "Oliveira"
print(people["last_name"])

keys = list(people.keys())
print(keys)
values = list(people.values())
print(values)
items = list(people.items())
print(items)