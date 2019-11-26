import sqlite3
import datetime
from task import Task

class DBManager:
    database_name = ''
    connection = None

    def __init__(self, database):
        self.database_name = database
        self.connection = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 

        conn = self.connection
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks 
                     (id INTEGER PRIMARY KEY,
                      name TEXT,
                      due_date DATE,
                      priority INTEGER,
                      details TEXT,
                      list TEXT,
                      complete INTEGER
                     )''')
        conn.commit()  
        conn.close()

    def get_all(self):
        conn = self.connection
        c = conn.cursor()
        tasks = c.execute('SELECT * FROM tasks')
        task_list = []
        for task in tasks:
            task_list.append(Task(
                id = task[0],
                name = task[1],
                due_date = task[2],
                priority = task[3],
                details = task[4],
                list = task[5],
                complete = task[6] 
                ))
        conn.close()
        return task_list

    def add_task(self, task):
        conn = self.connection
        c = conn.cursor()
        c.execute('INSERT INTO tasks (name, due_date, priority, details, list, complete) VALUES (?, ?, ?, ?, ?, ?)',
                    (task.name,
                    task.due_date.strftime('%Y-%m-%d'),
                    task.priority.value,
                    task.details,
                    task.list,
                    int(task.complete)))
        conn.commit()
        conn.close()

    def get_task(self, task_id):
        conn = sqlite3.connect(self.database_name)
        print('not implemented')

    def update_task(self, task):
        print('not implemented')

    def delete_task(self, task):
        print('not implemented')
