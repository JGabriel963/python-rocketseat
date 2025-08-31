class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        return f"Olá, meu nome é {self.name} e eu tenho {self.age} anos."


person = Person("John", 23)
print(person)
print(person.name)
print(person.age)

message = person.greetings()
print(message)