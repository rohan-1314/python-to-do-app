from functions import get_todo, write_todo
import time

time = time.strftime("%b %d,%y %H:%M:%S")
print("it is", time)
while True:
    user_input = input("Enter add,show,edit,complete or exit: ")
    user_input.strip()
    user_input = user_input.lower()
    if user_input.startswith('add'):
        todo = user_input[4:]
        todos = get_todo()
        todos.append(todo + '\n')
        write_todo(todos)
    elif user_input.startswith('show'):
        todos = get_todo()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            print(number)
            number -= 1
            todos = get_todo()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todo(todos)
        except ValueError:
            print("your command is not valid")
            continue
    elif user_input.startswith('complete'):
        num = int(user_input[9:])
        todos = get_todo()
        index = num - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        write_todo(todos)
    elif user_input.startswith("exit"):
        break
