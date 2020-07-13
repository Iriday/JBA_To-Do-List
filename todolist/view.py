from datetime import datetime, timedelta


def menu():
    print("1) Today's tasks", "2) Week's tasks", "3) All tasks", "4) Missed tasks", "5) Add task", "6) Delete task",
          "7) Delete all missed tasks", "0) Exit", sep="\n")

    while True:
        option = input()
        if option in ("1", "2", "3", "4", "5", "6", "7", "0"):
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


def output_week_tasks(tasks):
    dt = datetime.today()
    day_counter = 0
    while day_counter < 7:
        date_adjusted = (dt + timedelta(days=day_counter)).date()
        print(date_adjusted.strftime("%A %d %b") + ":")

        tasks_filtered = [t for t in tasks if t.deadline == date_adjusted]
        if len(tasks_filtered) == 0:
            print("Nothing to do!")
        else:
            i = 0
            while i < len(tasks_filtered):
                print(f"{i + 1}.", tasks_filtered[i])
                i += 1
        if day_counter != 6:
            print()
        day_counter += 1


def output_all_tasks(tasks):
    print("All tasks:")
    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        i = 0
        while i < len(tasks):
            print(f"{i + 1}.", f"{tasks[i]}.", tasks[i].deadline.strftime("%d %b"))
            i += 1


def output_missed_tasks(tasks):
    print("Missed tasks:")
    if len(tasks) == 0:
        print("Nothing is missed!")
    else:
        i = 0
        while i < len(tasks):
            print(f"{i + 1}.", f"{tasks[i]}.", tasks[i].deadline.strftime("%d %b"))
            i += 1


def get_task_to_del(tasks):
    if len(tasks) == 0:
        print("Task list is empty!")
    else:
        print("Choose the number of the task you want to delete:")
        i = 0
        while i < len(tasks):
            print(f"{i + 1}.", f"{tasks[i]}.", tasks[i].deadline.strftime("%d %b"))
            i += 1
        try:
            task_num = int(input())
        except ValueError:
            print("Error, incorrect input, please try again")
        else:
            if 1 <= task_num <= len(tasks):
                return tasks[task_num - 1]
            else:
                print("Error, incorrect input, please try again")


def output(data):
    print(data)
