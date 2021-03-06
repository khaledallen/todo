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
        c.execute('''CREATE TABLE IF NOT EXISTS lists (id INTEGER PRIMARY KEY, name TEXT)''')
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

    def get_all_lists(self):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        lists = conn.execute('SELECT * FROM lists')
        list_list = []
        for list in lists:
            list_list.append(list)
        conn.close()
        return list_list

    def get_by_list(self, list):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        tasks = c.execute('SELECT * FROM tasks WHERE list=?', (list,))
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

    def clean_task_properties(self, task):
        if task.due_date != None:
            due_date = task.due_date.strftime('%Y-%m-%d')
        else:
            due_date = None

        if task.priority != None:
            priority = task.priority.value
        else:
            priority = None

        return (due_date, priority)

    def add_task(self, task):
        due_date, priority = self.clean_task_properties(task)

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

    def add_list(self, list_name):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        conn.execute('INSERT INTO lists (name) VALUES (?)', (list_name,))
        conn.commit()
        conn.close()

    def get_task(self, task_id):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        t = c.execute('SELECT * FROM tasks WHERE id=?', (str(task_id),)).fetchone()
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

    def get_list(self, list_id):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        list = c.execute('SELECT * FROM lists WHERE id=?', (str(list_id),)).fetchone()
        conn.close()
        return list

    def get_list_by_name(self, list_name):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        list = c.execute('SELECT * FROM lists WHERE name=?', (str(list_name),)).fetchone()
        conn.close()
        return list

    def update_task(self, task):
        due_date, priority = self.clean_task_properties(task)
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
                            due_date,
                            priority,
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
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        c = conn.cursor()
        t = c.execute('''DELETE FROM tasks 
                            WHERE id=?''',
                            (str(task.id),)) 
        conn.commit()
        conn.close()
        return task

    def delete_completed(self):
        conn = sqlite3.connect(self.database_name, detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES) 
        conn.execute('''DELETE FROM tasks WHERE complete=1''')
        conn.commit()
        conn.close()
