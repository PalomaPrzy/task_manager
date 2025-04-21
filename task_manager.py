tasks = []

def show_menu(): #Show menu to user
    print('-------MENU-------')
    print('1 - Add task')
    print('2 - List tasks')
    print('3 - Mark task as complete')
    print('4 - Remove task')
    print('5 - Leave system')

def add_task(): #Adding task
    name = input('Enter task name: ')
    tasks.append({'name': name, 'completed': False}) #Add new task (default: not completed)
    print('Task added')

def list_tasks(): #Listing tasks
    if len(tasks) == 0: #If there are no tasks
        print('No tasks found')
        return  #End the function
    
    print('Task list:')
    print('-' * 20)

    # Loop through each task and show its status
    for index, task in enumerate(tasks): #Get task and its position in the list
        name_task = task['name']
        was_completed = task['completed']

        if was_completed: #True if completed (default: False)
            status = 'Completed'
        else:
            status = 'Pending'

        print(f'{index + 1}. {name_task} [{status}]') #{index+1 = Show task number starting from 1}

def conclude_task(): #Mark task as complete
    list_tasks()
    try:
        idx = int(input('Enter the number of the complete task: '))-1 #Get task inex from user (0-based)
        tasks[idx]['completed'] = True #Mark task as completed
        print('Task marked as completed')
    except:
        print('Invalid number')

def remove_task(): #Remove task
    list_tasks()
    try:
        idx =  int(input('Enter the task number to remove: '))-1
        tasks.pop(idx)
        print('Task removed')
    except:
        print('Invalid number')

while True:
    show_menu()
    option = input('Choose one option: ')

    if(option == '1'):
        add_task()
    elif(option == '2'):
        list_tasks()
    elif(option == '3'):
        conclude_task()
    elif(option == '4'):
        remove_task()
    elif(option == '5'):
        print('Leaving...')
        break
    else:
        print('Invalid option')