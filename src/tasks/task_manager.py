# display the lists of tasks
def display_tasks(task_list):
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def filter_tasks(task_list, keyword):
    """Filter tasks that contain the keyword (case-insensitive)."""
    filtered = [task for task in task_list if keyword.lower() in task.lower()]
    return filtered

def task_generator(task_list, keyword):
    """Generator for filtering tasks that contain the keyword (case-insensitive)."""
    for task in task_list:
        if keyword.lower() in task.lower():
            yield task
