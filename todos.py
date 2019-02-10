
import manager
import items
import datetime

man = manager.Manager()

what_do = input('What would you like to do?: ')

# adds a new item to todos.txt
if what_do == "add":

    print('What is the name of the task you\'d like to add?')
    task_name = input('> ')

    print("would you like to include due date? (Y/N)")
    answer = input('> ')

    if 'N' in answer or 'n' in answer:
        new_task = items.Item(task_name)
        man.add_item(new_task)
        print(f'added the task {task_name}')
    else:

        print("Please input the due date in YYYY-MM-DD HR:MM format")
        date = input('> ')

        try:
            due_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M')
            man.add_item(items.Item(task_name, False, '', due_date))
            print(f'added the task {task_name}')
        except:
            print('That is not the correct format. Please try again')


# gets a list of the items currently in todos.txt
elif what_do == "list":
    man.current_list()

# completes an item in the todos.txt
elif what_do == "complete":
    print("What is the name of the task you'd like to mark as completed?")
    task_name = input('> ')
    man.complete_item(task_name)

elif what_do == "urgent":
    man.urgent_task()

else:
    print("sorry, the thing you said made no sense. The commands are:")
    print('-' * 10)
    print("add - lets you add an item to the list. You will be asked what the name of the task you'd like to complete is")
    print('-' * 10)
    print("list - lets you view your to-do list")
    print('-' * 10)
    print("complete - lets you finish a task on your list. You will be asked what the name of the task you'd like to mark off is")
    print('-' * 10)
    print("urgent - Lets you see which task's due date is the soonest")
    print('-' * 10)
