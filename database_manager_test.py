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
        c.execute('CREATE TABLE IF NOT EXISTS tasks (name text, due_date date, priority integer, details text, complete integer)')
        conn.commit()
        conn.close()

    def test_get_all(self):
        self.setup()

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        tasks = [('task1', '2019-11-01', 1, 'detailstext', 0),
                 ('task2', '2019-11-02', 1, 'detailstext', 0),
                 ('task3', '2019-11-03', 1, 'detailstext', 0),
                 ('task4', '2019-11-04', 1, 'detailstext', 0),
                 ('task5', '2019-11-05', 1, 'detailstext', 0)]
        c.executemany('INSERT INTO tasks VALUES (?,?,?,?,?)', tasks)
        conn.commit()
        conn.close()

        dbm = DBManager('test.db')
        tasks = dbm.get_all()
        for i in range(0,4):
            with self.subTest(i=i):
                self.assertEqual(tasks[i].name, Task('task' + str(i+1), '2019-11-01', Priority.MEDIUM, 'detailstext').name)

        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('DROP TABLE tasks')

    def test_add_task(self):
        dbm = DBManager('test.db')
        task = Task('Task1', '2019-11-01', 2, 'detailstext', 0)
        dbm.add_task(task)

        conn = sqlite3.connect('test.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE name='Task1'")
        dbtask = c.fetchone()
        self.assertEqual(dbtask[0], task.name)

        c.execute('DROP TABLE tasks')
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()
