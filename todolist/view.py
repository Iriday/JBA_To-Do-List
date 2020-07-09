def menu():
    print("1) Today's tasks", "2) Add task", "0) Exit", sep="\n")

    while True:
        option = input()
        if option in ("1", "2", "0"):
            return int(option)
        else:
            print("Incorrect input, please try again!")


def get_task():
    print("Enter task")
    return input()


def output_tasks(tasks):
    print("Today:")
    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        i = 0
        while i < len(tasks):
            print(f"{i + 1}.", tasks[i])
            i += 1


def output(data):
    print(data)
