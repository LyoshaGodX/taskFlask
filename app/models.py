import sqlite3


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Task:
    def __init__(self, title, description, status="Не выполнена"):
        self.title = title
        self.description = description
        self.status = status


class TaskList(metaclass=SingletonMeta):
    def __init__(self):
        self.tasks = []
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def complete_tasks(self, task):
        task.status = "Выполнена"

    def fail_task(self, task):
        task.status = "Провалена"
