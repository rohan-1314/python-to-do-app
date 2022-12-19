FILEPATH = "todos.txt"


def get_todo(filepath=FILEPATH):
    """read the todos file and return the items in list"""
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todo(todos_arg, filepath=FILEPATH):
    """write the items in the todos file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)