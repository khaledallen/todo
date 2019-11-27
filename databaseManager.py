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
                      action TEXT,
                      complete INTEGER
                     )''')
        conn.commit()  
        conn.close()

    def get_all(self):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
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
                action = task[6],
                complete = task[7] 
                ))
        conn.close()
        return task_list

    def add_task(self, task):
        if task.due_date != None:
            due_date = task.due_date.strftime('%Y-%m-%d')
        else:
            due_date = None

        if task.priority != None:
            priority = task.priority.value
        else:
            priority = None

        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        c.execute('INSERT INTO tasks (name, due_date, priority, details, list, action, complete) VALUES (?, ?, ?, ?, ?, ?, ?)',
                    (task.name,
                    due_date,
                    priority,
                    task.details,
                    task.list,
                    task.action,
                    int(task.complete)))
        conn.commit()
        conn.close()

    def get_task(self, task_id):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        t = c.execute('SELECT * FROM tasks WHERE id=?', str(task_id)).fetchone()
        task = Task(
                id = t[0],
                name = t[1],
                due_date = t[2],
                priority = t[3],
                details =  t[4],
                list = t[5],
                action = t[6],
                complete = t[7])
        conn.close()
        return task

    def update_task(self, task):
        print(task.id)
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        t = c.execute('''UPDATE tasks 
                            SET name=?,
                                due_date=?,
                                priority=?,
                                details=?,
                                list=?,
                                action=?,
                                complete=?
                            WHERE id=?''',
                            (task.name, 
                            task.due_date.strftime('%Y-%m-%d'),
                            task.priority.value,
                            task.details,
                            task.list,
                            task.action,
                            int(task.complete),
                            str(task.id))) 
        task = self.get_task(task.id)
        conn.commit()
        conn.close()
        return task

    def delete_task(self, task):
        print('not implemented')
