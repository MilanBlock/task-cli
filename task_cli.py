"""Task Tracking CLI-Programm"""
import datetime
import json
import sys


POSIBLE_STATES = ("todo", "in-progress", "done")


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
    elif sys.argv[1] == "rename":
        renaming(tasks)
    elif sys.argv[1] == "delete":
        deleting(tasks)
    elif sys.argv[1] == "mark":
        marking(tasks)
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


def renaming(tasks):
    """Change the name of a task"""
    if len(sys.argv) < 4:
        print("Usage: task_cil.py rename [index old task] [new task name]")
        return

    index = int(sys.argv[2])
    new_name = sys.argv[3]

    for task in tasks:
        if task["id"] == index:
            task["description"] = new_name
            task["updatedAt"] = str(datetime.datetime.now())
            break


def deleting(tasks):
    """Delete task"""
    if len(sys.argv) < 3:
        print("Usage: task_cil.py delete [index task to delete]")
        return
    
    index = int(sys.argv[2])

    for task in tasks:
        if task["id"] == index:
            tasks.remove(task)
            break


def marking(tasks):
    """Set status of task"""
    if len(sys.argv) < 4:
        print("Usage: task_cil.py mark [index task] [status]")
        return
    
    index = int(sys.argv[2])
    status = sys.argv[3]

    if status not in POSIBLE_STATES:
        print(f"Not a possible state. Posible states are: {POSIBLE_STATES}")

    for task in tasks:
        if task["id"] == index:
            task["status"] = status
            task["updatedAt"] = str(datetime.datetime.now())
            break


def listing(tasks):
    """List all tasks according to filter given"""
    if len(sys.argv) == 2:
        filter = list(POSIBLE_STATES)
    elif sys.argv[2] not in POSIBLE_STATES:
        print(f"Not a possible state. Posible states are: {POSIBLE_STATES}")
        return
    else:
        filter = [sys.argv[2]]
    
    for task in tasks:
        if task["status"] in filter:
            index = task["id"]
            description = task["description"]
            status = task["status"]
            print(f"ID: {index}; Status: {status}; Description: {description}")


main()

# # Adding a new task
# task-cli add "Buy groceries"
# # Output: Task added successfully (ID: 1)

# # Rename and deleting tasks
# task-cli rename 1 "Buy groceries and cook dinner"
# task-cli delete 1

# # Marking a task as in progress or done
# task-cli mark 1 in-progress
# task-cli mark 1 done

# # Listing all tasks
# task-cli list

# # Listing tasks by status
# task-cli list done
# task-cli list todo
# task-cli list in-progress
