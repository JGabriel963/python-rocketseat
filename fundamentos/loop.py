for i in range(10):
    print(i + 1)

users = [{"name": "João", "age": 23}, {"name": "Maria", "age": 28}]

for user in users:
    print(user["name"])
    print(user["age"])
    
user = {"name": "João", "age": 23}

for key in user:
    print(user[key])

for values in user.values():
    print(values)

for key, values in user.items():
    print(key, values)