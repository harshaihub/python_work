tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index] += " (Done)"

add_task("Finish homework")
add_task("Go for a walk")
view_tasks()
mark_done(0)
view_tasks()
