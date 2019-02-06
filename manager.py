
import items

# one object of this class should be made when you run the script
class Manager(object):

    # should print all the to-do items in the list
    def current_list(self):

        file = open("todos.txt", "r")

        lines_list = file.readlines()

        # should print the info out to the terminal
        for line in lines_list:
            contents = line.split(",")
            print(f"Task: {contents[0]}")
            print(f"Time created: {contents[1]}")
            if contents[2] == "True\n":
                print("Task Status: Complete")
            else:
                print("Task Status: Not Yet Completed")

            print("-" * 10)

    # should be able to add a new item to the list (database, todos.txt)
    def add_item(self, item):
        # should open up text file with append capabilities
        file = open("todos.txt", "a")
        file.write(f"{item.job},{item.timestamp},{item.is_complete}\n")
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
            if job in line:
                contents = line.split(",")
                if contents[2] == "False\n":
                    contents[2] = 'True\n'
                    lines_list[index] = f"{contents[0]},{contents[1]},{contents[2]}"
                    break
            index += 1
        # this else statement is attached to the for loop, and will activate only when the loop terminates without any lines changed
        else:
            print("Sorry, the task was either already completed or just not found")

        # delete contents of file entirely
        file.truncate(0)

        # rewrite the file entirely with the new, revised line
        for line in lines_list:
            file.write(line)

        file.close()
