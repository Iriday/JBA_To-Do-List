from todolist import view
from todolist import model

while True:
    option = view.menu()

    if option == 1:
        view.output_today_tasks(model.get_today_tasks())
    elif option == 2:
        view.output_week_tasks(model.get_week_tasks())
    elif option == 3:
        view.output_all_tasks(model.get_all_tasks())
    elif option == 4:
        view.output_missed_tasks(model.get_tasks_before_today())
    elif option == 5:
        model.add_task(view.get_task(), view.get_deadline())
        view.output("The task has been added!")
    elif option == 0:
        view.output("Bye!")
        break
    else:
        view.output("Something when wrong")
    view.output("")
