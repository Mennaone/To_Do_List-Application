"""
To Do list Application

"""

tasks = [{'task': 'go to school', 'status': 'Not Completed'},
         {'task': 'make my homework', 'status': 'Not Completed'},
         {'task': 'visit my granmother', 'status': 'Not Completed'},
         {'task': 'make some exercises', 'status': 'Not Completed'},
         {'task': 'read a book', 'status': 'Not Completed'},
         {'task': 'study courses', 'status': 'Not Completed'}]

# Main logic to the do_list App
def main():
    while True:
        Default_Message()
        choice = input("Please Enter Your Choice: ")
        if choice == "1":
            add_tasks()
        elif choice == "2":
            mark_tasks_complete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            remove_tasks()
        elif choice == "5":
            print("The App Closed Successfully 😊")
            break
        else:
            print("Oops!! 😥, Invalid Input, PLease Be Sure that you entered a number between 1 and 5 ")
            
# Main Features of the Application
def Default_Message():
    message = '''\n*****************😊To Do List Application😊*****************\n
1_ Add Tasks to the List
2_ Mark Tasks as Complete
3_ View All the Tasks
4_ Remove Tasks From the List
5_ Close To Do List App
'''
    print(message)
    
# Add Tasks
def add_tasks():
    # start taking tasks from the user
    task = input("Enter your task: ")
    
    # define the task status
    tasks_info = {"task":task, "status": "Not Completed"}
    
    # add  task to the list
    tasks.append(tasks_info)
    print("\nSuccessfully Added 😊")

# Mark tasks Completed 
def mark_tasks_complete():
    # define the not complete tasks
    incomplete_tasks = [task for task in tasks if task["status"] == "Not Completed"]
    
    # if the lsit is empty, then return
    if not incomplete_tasks:
        print("There is no incomplete tasks 😥")
        return
    
    # display them to the user
    for index, task in enumerate(incomplete_tasks):
        print(f"{index+1}_ {task['task']} " )
    print("*" * 30)
    
    # take the task from the user 
    # handle user errors
    try:
        task_number = int(input("Choose the task number that is completed: "))
        # chceck if the index is in the length range 
        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid Task Number 😮")
            return         
        # mark tasks as completed
        incomplete_tasks[task_number-1]["status"] = "Completed"
        print("\nSuccessfully Marked Completed 🥰")
    except ValueError:
        print("Invalid Input, PLease check your task number 😮")
    
# Dispalying the tasks
def view_tasks():
    # if the list is empty, then return
    if not tasks:
        print("Your List is empty")
        return 
    
    # display the tasks
    print("Your to_do List: ")
    for index, task in enumerate(tasks):
        status = '✔' if task['status'] == 'Completed' else  '❌'  
        print(f"{index+1}. {task['task']} {status}" )
    print("*" * 30)
          
# Removing tasks
def remove_tasks():
    # get a view from the list
    view_tasks()
    # take the task from the user to remove
    task_number = int(input("Enter the task to remove from the list: "))
    # check the removing task number
    if task_number < 1 or task_number > len(tasks):
        print("Invalid Task Number 😮")
        return 
    del tasks[task_number-1]
    print("\nThe task is removed Successfully 😊")
    
# Start the Application 
welcome_message = "\nWelcome to To Do list App 🥰🥰, Let's start to organize your dailt tasks "
print(welcome_message)

main()
 

    