import sqlite3
import datetime
from task import Task

class DBManager:
    connection_string = ''

    def __init__(self, connection_string):
        self.connection_string = connection_string

        conn = sqlite3.connect(self.connection_string, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks 
        (name text, due_date date, priority integer, details text, complete integer)''')
        conn.commit()  
        conn.close()

    def get_all(self):
        conn = sqlite3.connect(self.connection_string)
        c = conn.cursor()
        tasks = c.execute('SELECT * FROM tasks')
        task_list = []
        for task in tasks:
            task_list.append(Task(task[0], task[1], task[2], task[3], task[4]))
        return task_list

    def add_task(self, task):
        conn = sqlite3.connect(self.connection_string, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        c.execute('INSERT INTO tasks VALUES (?, ?, ?, ?, ?)', (task.name, task.due_date.strftime('%Y-%m-%d'), task.priority.value, task.details, task.complete))
        conn.commit()
        conn.close()

    def get_task(self, task_id):
        print('not implemented')

    def update_task(self, task):
        print('not implemented')

    def delete_task(self, task):
        print('not implemented')
