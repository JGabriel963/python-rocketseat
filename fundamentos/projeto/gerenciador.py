tasks = []

def add_task(title):
    task = {"title": title, "completed": False}
    tasks.append(task)
    print(f"Tarefa '{title}' adicionada com sucesso!")
    return

def view_tasks():
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for index, task in enumerate(tasks):
            status = "👍" if task["completed"] else " "
            ## print(f"{index + 1} [{'👍' if task['completed'] else ' '}]", task['title'])
            print(f"{index}. [{status}] {task['title']}")
    return

def update_task_title(index, new_title):
    tasks[index]["title"] = new_title
    print(f"Tarefa '{tasks[index]['title']}' atualizada para '{new_title}'")
    return

def complete_task(index):
    tasks[index]["completed"] = True
    print(f"Tarefa '{tasks[index]['title']}' completada!")
    return 

def delete_completed_tasks():
    for task in tasks:
        if task["completed"]:
            tasks.remove(task)
    print("Tarefas completadas deletadas com sucesso!")
    return

while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    option = input("Digite a sua escolha: ")

    if option == "1":
        title = input("Digite o título da tarefa: ")
        add_task(title)
    elif option == "2":
        view_tasks()
    elif option == "3":
        view_tasks()
        index = int(input("Digite o índice da tarefa a ser atualizada: "))
        new_title = input("Digite o novo título da tarefa: ")
        update_task_title(index, new_title)
    elif option == "4":
        view_tasks()
        index = int(input("Digite o índice da tarefa a ser completada: "))
        complete_task(index)

    if option == "6":
        break

print("Programa finalizado.")