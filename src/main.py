import sys
from task_manager import add_task, list_tasks, complete_task

def main():
    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])
    elif command == "list":
        tasks = list_tasks()
        for i, t in enumerate(tasks):
            status = "completo" if t["done"] else "pendente"
            print(f"{i} - {t['title']} [{status}]")
    elif command == "done":
        complete_task(int(sys.argv[2]))

if __name__ == "__main__":
    main()