import sys

from src.motivational_api import get_motivational_quote
from src.task_manager import add_task, complete_task, list_tasks


def main():
    if len(sys.argv) < 2:
        print("Uso:")
        print("python src/main.py add 'Nova tarefa'")
        print("python src/main.py list")
        print("python src/main.py done <indice>")
        print("python src/main.py quote")
        return

    command = sys.argv[1]

    if command == "add":
        add_task(sys.argv[2])

    elif command == "list":
        tasks = list_tasks()

        for i, task in enumerate(tasks):
            status = "completo" if task["done"] else "pendente"
            print(f"{i} - {task['title']} [{status}]")

    elif command == "done":
        complete_task(int(sys.argv[2]))

    elif command == "quote":
        print(get_motivational_quote())

    else:
        print("Comando inválido")


if __name__ == "__main__":
    main()