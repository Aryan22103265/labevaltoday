
tasks = {}

def adding_task():
    task_id = input("Enter task ID: ")
    task_name = input("Enter task name: ")
    task_status = input("Enter task status: ")
    
    if task_id in tasks:
       print("Task ID already exists choose a unique ID.")
       return
    
    tasks[task_id] = {"name": task_name, "status": task_status}
    print(f"Task '{task_name}' added successfully!")

def update_task():    
    task_id = input("Enter task ID to update: ")
    if task_id not in tasks:
        print("Task ID not found.")
        return

    new_name = input("Enter new task name")
    new_status = input("Enter new task status")

    if new_name:
        tasks[task_id]["name"] = new_name
    if new_status:
        tasks[task_id]["status"] = new_status

    print("Task updated successfully!")

def delete_task():
    task_name = input("Enter task name to delete: ")
    for task_id, task_info in tasks.items():
        if task_info["name"] == task_name:
            del tasks[task_id]
            print(f"Task '{task_name}' deleted successfully!")
            return
    print(f"Task '{task_name}' not found.")
    

def display_tasks():
    for id in tasks.keys():
          print(id ,"is",tasks[id])

def searching_tasks():
    key = input("Id of task to be searched")
    for id in tasks.keys():
        if id == key:
            print(id ,"is",tasks[id])
            return
    
    print("No task found with this id")
        

n = int(input("Enter number of data to be entered"))
for i in range(n):
    adding_task()
    
display_tasks()
update_task()
display_tasks()
delete_task()
display_tasks()
searching_tasks()


