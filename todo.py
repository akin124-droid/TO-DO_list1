import json
import os

FILENAME="todo.json"
#load up the tasks
def loadtasks():
    if os.path.exists(FILENAME):
        with open(FILENAME,"r") as file:
            return json.load(file)
    return []
#save tasks
def savetasks(tasks):
    with open(FILENAME,"w") as file:
        json.dump(tasks,file,indent=4)

#show all the tasks
def showtasks(tasks):
    if not tasks:
        print("No tasks yet")
    else:
        for i,task in enumerate(tasks):
            status="g" if task["done"] else "X"
            print(f"{i + 1}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    savetasks(tasks)

#mark a task as done
def completetask(tasks):
    showtasks(tasks)
    index=int(input("task number completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        savetasks(tasks)

#delete a task
def deletetask(tasks):
    showtasks(tasks)
    index = (int(input("Task number to delete: ")) - 1)
    if 0 <=index < len(tasks):
        tasks.pop(index)
        savetasks(tasks)

#menu
def main():
    tasks = loadtasks()
    while True:
        print("\n ---TO-DO LIST---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        choice = input("choose one: ")

        if choice== "1":
            showtasks(tasks)
        elif choice== "2":
            add_task(tasks)
        elif choice== "3":
            completetask(tasks)
        elif choice== "4":
            deletetask(tasks)
        elif choice== "5":
            break
        else :
            print("invalid choice.")
if __name__ == "__main__":
    main()


