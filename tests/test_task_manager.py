from src.task_manager import add_task, list_tasks, complete_task


def test_add_task():
    add_task("Teste")
    tasks = list_tasks()
    assert any(t["title"] == "Teste" for t in tasks)


def test_list_returns_list():
    tasks = list_tasks()
    assert isinstance(tasks, list)


def test_complete_invalid_task():
    complete_task(999)  # não deve quebrar
