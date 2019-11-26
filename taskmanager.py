import os.path
from task import Task
from databaseManager import DBManager

class TaskManager:
    def __init__(self, task_db):
        self.dbm = DBManager(task_db)

    def add(self, task_name = None, task_due_date = None, task_priority = None, task_details = None, task_list = None):
        if task_name == None:
            task_name = input('Task name: ')
            task_due_date = input('Due date: ')
            task_priority = input('Priority ([H]i, [M]edium, [L]ow): ')
            task_details = input('Details (optional): ')
            task_list = input('Task list/category (optional): ')

        task_obj = Task(name = task_name, due_date = task_due_date, priority = task_priority, details = task_details, list = task_list)

        self.dbm.add_task(task_obj)

    def list(self):
        tasks = self.dbm.get_all()
        print('{:<6} {:<8}{:<30}{:>9}'.format('Id', 'Status', 'Name', 'Due Date'))
        print('-' * 60)
        for task in tasks:
            print(task.print_abbrv())
        print('_' * 60)    
        print('- "todo do [id]" to print details for a task')
        print('- "todo comp [id]" to mark the task complete')

    def do(self, task_id):
        task = self.dbm.get_task(int(task_id))
        print(task)

    def complete(self, task_id):
        task = self.dbm.get_task(int(task_id))
        task.complete = True
        self.dbm.update_task(task)

