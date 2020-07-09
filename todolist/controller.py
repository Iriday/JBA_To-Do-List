from todolist import view
from todolist import model

while True:
    option = view.menu()

    if option == 1:
        view.output_tasks(model.get_all_tasks())
    elif option == 2:
        model.add_task(view.get_task())
        view.output("The task has been added!")
    elif option == 0:
        view.output("Bye!")
        break
    view.output("")
