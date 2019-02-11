
import items
import datetime

# one object of this class should be made when you run the script
class Manager(object):

    # should print all the to-do items in the list
    def current_list(self):

        file = open("todos.txt", "r")

        # makes a list representation of all the lines in the txt file
        lines_list = file.readlines()

        # should print the info out to the terminal
        for line in lines_list:
            # split each individual line at the separators (comma in this case)
            contents = line.split(",")
            # print the task name out
            print(f"Task: {contents[0]}")
            # print the task timestamp out
            print(f"Time created: {contents[1]}")
            # tell user whether item's is_completed = True or False
            if contents[2] == "True":
                print("Task Status: Complete")
            else:
                print("Task Status: Not Yet Completed")

            if contents[3] != '\n':
                print(f"Due: {contents[3]}")
            else:
                print(f"No defined due date")
            # added separation between items
            print("-" * 10)

    # should be able to add a new item to the list (database, todos.txt)
    def add_item(self, item):
        # should open up text file with append capabilities
        file = open("todos.txt", "a")
        # write item's attributes to the file
        file.write(f"{item.job},{item.timestamp},{item.is_complete},{item.due_date}\n")
        file.close()

    # should be able to mark an item as complete
    def complete_item(self, job):

        file = open("todos.txt", "r+")

        # make a list of all the lines in the file
        lines_list = file.readlines()

        # loop through the lines in lines_list, if you find a line that has the task,
        # then replace the False with True
        index = 0
        for line in lines_list:
            # checks if the task name is in the line
            if job in line:
                # split the line at its separators
                contents = line.split(",")
                # check that the is_completed attribute is False
                if contents[2] == "False":
                    contents[2] = 'True'
                    # change the list at the current index (representing the current line) to have is_completed = True
                    lines_list[index] = f"{contents[0]},{contents[1]},{contents[2]},{contents[3]}"
                    # escape the loop so we don't change anything else
                    break

            index += 1
        # this else statement is attached to the for loop, and will activate only when the loop terminates without hitting the break statement
        else:
            print("Sorry, the task was either already completed or just not found")

        # delete contents of file entirely
        file.truncate(0)

        # rewrite the file entirely with the new, revised lines_list
        for line in lines_list:
            file.write(line)

        file.close()

    def convert_to_item(self, line):

        stripped_line = line.strip('\n')

        contents = stripped_line.split(',')

        timestamp = datetime.datetime.strptime(contents[1], '%Y-%m-%d %H:%M:%S.%f')

        completion = False

        if contents[2] == "True":
            completion = True


        due_date = ''
        if contents[3] != '':
            due_date = datetime.datetime.strptime(contents[3], '%Y-%m-%d %H:%M:%S')

        return items.Item(contents[0], completion, timestamp, due_date)

    # finds the task that is due the soonest of all the tasks in the list, and prints it.
    def urgent_task(self):

        file = open("todos.txt", "r")

        # make a list of all lines
        lines_list = file.readlines()

        # make another list of all lines with a due date who aren't complete yet
        items_list = []

        # loop through lines and put items of each line into items_list
        for line in lines_list:
            items_list.append(self.convert_to_item(line))

        # create a list of only items who aren't complete and who have a due date
        final_list = []

        # put items w/ due date and who aren't complete into final_list
        for item in items_list:
            if item.is_complete == False:
                if item.due_date != '':
                    final_list.append(item)


        # create datetime object representing current time, also an empty value which represents the line with the soonest time
        current_time = datetime.datetime.now()
        # object representing the task that is the closest to the current time
        if len(final_list) > 0:
            soonest_item = final_list[0]

            # loop through the due date line list and compare amount of time between due date and current time
            for item in final_list:
                # if the time is shorter between item and current time than the soonest_item and current time, set that to be new soonest value
                if item.due_date - current_time < soonest_item.due_date - current_time:
                    soonest_item = item

            # print out the line with the soonest time.
            print(soonest_item.job)
        elif len(items_list) > 0:
            print(items_list[0].job)
        else:
            print('No values in to-do list')
