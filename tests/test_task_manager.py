from src.task_manager import add_task, list_tasks

def test_add_task():
    add_task("Test Task")
    tasks = list_tasks()
    assert any(t["title"] == "Test Task" for t in tasks)

def test_empty_task_list():
    tasks = list_tasks()
    assert isinstance(tasks, list)

def test_complete_invalid_task():
    from src.task_manager import complete_task
    complete_task(999)  # não deve quebrar