"""Task Tracking CLI-Programm"""
import datetime
import json
import sys


def main():
    """Loading tasks, calling correct update funcion and saving task"""
    # Loading task
    tasks = []
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

    if len(sys.argv) < 2:
        print("Usage: task_cli.py [action] [additional arguments]")
    elif sys.argv[1] == "add":
        adding(tasks)
    elif sys.argv[1] == "update":
        updating(tasks)
    elif sys.argv[1] == "delete":
        deleting(tasks)
    elif sys.argv[1] == "list":
        listing(tasks)

    # Saving task
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def adding(tasks):
    """Add a new task"""
    if len(sys.argv) < 3:
        print("Usage: task_cil.py add [task name]")
        return

    tasks.append({
        "description": sys.argv[2],
        "status": "todo",
        "createdAt": str(datetime.datetime.now()),
        "updatedAt": str(datetime.datetime.now())
    })


def updating(tasks):
    """Changing the name of a task"""
    print("Updated Task TODO")


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
