from app.models import Task, TaskList


class StatusObserver:
    def __init__(self, task_list):
        self.task_list = task_list

    def update(self, task):
        print(f'Статус задачи "{task.title}" изменился на {task.status}')
        if task.status == 'Выполнена':
            self.task_list.remove_task(task)


class TaskController:
    def __init__(self, task_list):
        self.task_list = task_list
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, task):
        for observer in self.observers:
            observer.update(task)

    def add_task(self, title, description):
        task = Task(title, description)
        self.task_list.add_task(task)

    def remove_task(self, task):
        self.task_list.remove_task(task)

    def complete_task(self, task):
        task.status = "Выполнена"
        self.notify_observers(task)

    def fail_task(self, task):
        task.status = "Провалена"
        self.notify_observers(task)


controller = TaskController(TaskList())
status_observer = StatusObserver(controller.task_list)
controller.add_observer(status_observer)
