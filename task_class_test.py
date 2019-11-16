import unittest
from datetime import date
from datetime import timedelta
from todo import Task, Priority


class TestTaskMethods(unittest.TestCase):

    def test_process_due_date(self):
        task = Task()
        with self.subTest():
            self.assertEqual(task.process_due_date(), None )
        with self.subTest():
            self.assertEqual(task.process_due_date('today'), date.today() )
        with self.subTest():
            self.assertEqual(task.process_due_date('tomorrow'), date.today() + timedelta(1))
        with self.subTest():
            self.assertEqual(task.process_due_date('11/30/2019'), date(2019, 11, 30))
        with self.subTest():
            self.assertEqual(task.process_due_date('11/30/19'), date(2019, 11, 30))
        with self.subTest():
            self.assertEqual(task.process_due_date('11/30'), date(2019, 11, 30))

    def test_process_priority(self):
        task = Task()
        with self.subTest():
            self.assertEqual(task.process_priority(), Priority.NONE)
        with self.subTest():
            self.assertEqual(task.process_priority('H'), Priority.HIGH)
        with self.subTest():
            self.assertEqual(task.process_priority('M'), Priority.MEDIUM)
        with self.subTest():
            self.assertEqual(task.process_priority('L'), Priority.LOW)
        with self.subTest():
            self.assertEqual(task.process_priority('h'), Priority.HIGH)
        with self.subTest():
            self.assertEqual(task.process_priority('m'), Priority.MEDIUM)
        with self.subTest():
            self.assertEqual(task.process_priority('l'), Priority.LOW)
        with self.subTest():
            self.assertEqual(task.process_priority('high'), Priority.HIGH)
        with self.subTest():
            self.assertEqual(task.process_priority('medium'), Priority.MEDIUM)
        with self.subTest():
            self.assertEqual(task.process_priority('low'), Priority.LOW)
        with self.subTest():
            self.assertEqual(task.process_priority('HIGH'), Priority.HIGH)
        with self.subTest():
            self.assertEqual(task.process_priority('MEDIUM'), Priority.MEDIUM)
        with self.subTest():
            self.assertEqual(task.process_priority('LOW'), Priority.LOW)


if __name__ == '__main__':
    unittest.main()
