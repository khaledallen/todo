import unittest
import sqlite3
import datetime
from task import Task
from priority import Priority
from databaseManager import DBManager

class TestDatabaseManagerMethods(unittest.TestCase):
    def setup(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT,
                due_date DATE,
                priority INTEGER,
                details TEXT,
                list TEXT,
                complete INTEGER)''')
        conn.commit()
        conn.close()

    def test_get_all(self):
        self.setup()

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        tasks = [('task1', '2019-11-01', 1, 'detailstext', 'list1', 0),
                 ('task2', '2019-11-02', 1, 'detailstext', 'list1', 0),
                 ('task3', '2019-11-03', 1, 'detailstext', 'list1', 0),
                 ('task4', '2019-11-04', 1, 'detailstext', 'list1', 0),
                 ('task5', '2019-11-05', 1, 'detailstext', 'list1', 0)]
        c.executemany('INSERT INTO tasks (name, due_date, priority, details, list, complete) VALUES (?,?,?,?,?,?)', tasks)
        conn.commit()
        conn.close()

        dbm = DBManager('test.db')
        tasks = dbm.get_all()
        for i in range(0,4):
            with self.subTest(i=i):
                self.assertEqual(tasks[i].name, Task(
                    name = 'task' + str(i+1),
                    due_date = '2019-11-01',
                    priority = Priority.MEDIUM,
                    details = 'detailstext',
                    list = 'list1',
                    complete = False
                    ).name)

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('DROP TABLE tasks')

    def test_add_task(self):
        dbm = DBManager('test.db')
        task = Task(
                name = 'Task1',
                due_date = '2019-11-01',
                priority = Priority.LOW,
                details = 'detailstext',
                list = 'list1',
                complete = False)
        dbm.add_task(task)

        conn = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE name='Task1'")
        dbtask = c.fetchone()
        self.assertEqual(dbtask[1], task.name)

        c.execute('DROP TABLE tasks')
        conn.commit()
        conn.close()

    def test_get_task(self):
        task = Task(
                name = 'Task1',
                due_date = '2019-11-01',
                priority = Priority.HIGH,
                details = 'detailstext',
                list = 'list1',
                complete = True)
        conn = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                name TEXT,
                due_date DATE,
                priority INTEGER,
                details TEXT,
                list TEXT,
                complete INTEGER)''')
        c.execute('INSERT INTO tasks (name, due_date, priority, details, list, complete) VALUES (?, ?, ?, ?, ?, ?)', 
            (task.name,
            task.due_date,
            task.priority.value,
            task.details,
            task.list,
            int(task.complete)))
        conn.commit()
        conn.close()

        dbm = DBManager('test.db')
        task_from_db = dbm.get_task(1)
        self.assertEqual(task_from_db.name, task.name)

        conn = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute('DROP TABLE tasks') 
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()
