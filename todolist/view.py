from datetime import datetime


def menu():
    print("1) Today's tasks", "2) Add task", "3) All tasks", "0) Exit", sep="\n")

    while True:
        option = input()
        if option in ("1", "2", "3", "0"):
            return int(option)
        else:
            print("Incorrect input, please try again!")


def get_task():
    print("Enter task")
    return input()


def get_deadline():
    while True:
        print('Enter deadline (example: "2020-06-15")')
        try:
            return datetime.strptime(input(), "%Y-%m-%d")
        except ValueError:
            print("Error. Incorrect date, please try again\n")


def output_today_tasks(tasks):
    print("Today " + datetime.today().strftime("%d %b") + ":")
    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        i = 0
        while i < len(tasks):
            print(f"{i + 1}.", tasks[i])
            i += 1


def output_all_tasks(tasks):
    print("All tasks:")
    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        i = 0
        while i < len(tasks):
            print(f"{i + 1}.", f"{tasks[i]}.", tasks[i].deadline.strftime("%d %b"))
            i += 1


def output(data):
    print(data)
