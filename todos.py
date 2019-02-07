
import manager
import items

man = manager.Manager()

what_do = input('What would you like to do?: ')

# adds a new item to todos.txt
if what_do == "add":

    print('What is the name of the task you\'d like to add?')
    task_name = input('> ')
    new_task = items.Item(task_name)
    man.add_item(new_task)

    print(f'added the task {task_name}')

# gets a list of the items currently in todos.txt
elif what_do == "list":
    man.current_list()

# completes an item in the todos.txt
elif what_do == "complete":
    print("What is the name of the task you'd like to mark as completed?")
    task_name = input('> ')
    man.complete_item(task_name)

else:
    print("sorry, the thing you said made no sense. The commands are:")
    print('-' * 10)
    print("add - lets you add an item to the list. You will be asked what the name of the task you'd like to complete is")
    print('-' * 10)
    print("list - lets you view your to-do list")
    print('-' * 10)
    print("complete - lets you finish a task on your list. You will be asked what the name of the task you'd like to mark off is")
    print('-' * 10)
