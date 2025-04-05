"""Task Tracking CLI-Programm"""
import datetime
import json
import sys


def main():
    """Loading tasks, calling correct update funcion and saving task"""
    # Loading task
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {
            "lastId": 0,
            "tasks": []
        }
    tasks = data["tasks"]
    last_id = data["lastId"]

    if len(sys.argv) < 2:
        print("Usage: task_cli.py [action] [additional arguments]")
    elif sys.argv[1] == "add":
        last_id = adding(tasks, last_id)
    elif sys.argv[1] == "update":
        updating(tasks)
    elif sys.argv[1] == "delete":
        deleting(tasks)
    elif sys.argv[1] == "list":
        listing(tasks)

    data["lastId"] = last_id

    # Saving task
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def adding(tasks, last_id):
    """Add a new task"""
    if len(sys.argv) < 3:
        print("Usage: task_cil.py add [task name]")
        return last_id

    last_id += 1
    current_date = str(datetime.datetime.now())
    tasks.append({
        "id": last_id,
        "description": sys.argv[2],
        "status": "todo",
        "createdAt": current_date,
        "updatedAt": current_date
    })

    print(f"Task added successfully (ID: {last_id})")

    return last_id


def updating(tasks):
    """Changing the name of a task"""
    if len(sys.argv) < 4:
        print("Usage: task_cil.py update [index old task] [new task name]")
        return
    
    print("hi")


def deleting(tasks):
    """Delete task"""
    print("Deleted Task TODO")


def listing(tasks):
    """Calling correct listing function"""
    print("List tasks TODO")


def listing_all(tasks):
    """Lists all tasks"""
    print("List all TODO")


def listing_done(tasks):
    """Listing all tasks that are done"""
    print("List done TODO")


def listing_todo(tasks):
    """Listing all tasks that are todo"""
    print("List todo TODO")


def listing_in_progress(tasks):
    """Listing all tasks that are in-progress"""
    print("List in-progress TODO")


main()

# # Adding a new task
# task-cli add "Buy groceries"
# # Output: Task added successfully (ID: 1)

# # Updating and deleting tasks
# task-cli update 1 "Buy groceries and cook dinner"
# task-cli delete 1

# # Marking a task as in progress or done
# task-cli mark-in-progress 1
# task-cli mark-done 1

# # Listing all tasks
# task-cli list

# # Listing tasks by status
# task-cli list done
# task-cli list todo
# task-cli list in-progress
