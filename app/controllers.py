from app.models import Task, TaskList


class StatusObserver:
    def __init__(self, task_list):
        self.task_list = task_list

    def update(self, task_id):
        task = self.task_list.get_task_by_id(task_id)
        if task:
            print(f'Добавлена задача "{task.title}". Текущий статус: {task.status}')


class TaskController:
    def __init__(self, task_list):
        self.task_list = task_list
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, task_id):
        for observer in self.observers:
            observer.update(task_id)

    def add_task(self, title, description):
        task_id = len(self.task_list.get_all_tasks()) + 1
        task = Task(task_id, title, description)
        self.task_list.add_task(task)
        self.notify_observers(task_id)

    def remove_task(self, task_id):
        self.task_list.remove_task(task_id)

    def complete_task(self, task_id):
        self.task_list.complete_task(task_id)

    def fail_task(self, task_id):
        self.task_list.fail_task(task_id)


controller = TaskController(TaskList())
status_observer = StatusObserver(controller.task_list)
controller.add_observer(status_observer)