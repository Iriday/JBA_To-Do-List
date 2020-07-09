from todolist import view

while True:
    option = view.menu()

    if option == 1:
        view.output_tasks(())
    elif option == 2:
        view.get_task()
        # view.output("The task has been added!")
    elif option == 0:
        view.output("Bye!")
        break
    view.output("")
