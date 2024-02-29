FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads the text file and returns the list of to-do items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes to-do items list in the text file. """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

# below statement is only executed if this file is run. If you run another file that imports this whole file, then
# it won't show in the execution. Normally, e.g. print statement, would be executed during import, if not under this:

if "__name__" == "__main__":
    print("Hello")
