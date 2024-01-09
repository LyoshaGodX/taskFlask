import sqlite3


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Task:
    def __init__(self, task_id, title, description, status="Не выполнена"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status


class TaskList(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def add_task(self, task):
        self.cursor.execute('''
            INSERT INTO Task (title, description, status)
            VALUES (?, ?, ?)
        ''', (task.title, task.description, 'Не выполнена'))
        self.connection.commit()

    def remove_task(self, task_id):
        self.cursor.execute('''
            DELETE FROM Task WHERE id=?
        ''', (task_id,))
        self.connection.commit()

    def complete_task(self, task_id):
        self.cursor.execute('''
            UPDATE Task SET status='Выполнена' WHERE id=?
        ''', (task_id,))
        self.connection.commit()

    def fail_task(self, task_id):
        self.cursor.execute('''
            UPDATE Task SET status='Провалена' WHERE id=?
        ''', (task_id,))
        self.connection.commit()

    def get_all_tasks(self):
        self.cursor.execute('''
            SELECT * FROM Task
        ''')
        tasks_data = self.cursor.fetchall()
        tasks = [Task(*task_data) for task_data in tasks_data]
        return tasks

    def get_task_by_id(self, task_id):
        for task in self.get_all_tasks():
            if task.task_id == task_id:
                return task
        return None
