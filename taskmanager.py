import os.path
from task import Task
from datetime import date
from databaseManager import DBManager
from operator import attrgetter

class TaskManager:
    def __init__(self, task_db):
        self.dbm = DBManager(task_db)

    def add(self, task_name = None, task_due_date = None, task_priority = None, task_details = None, task_list = None, task_action = None, quick_input = False):
        if task_name == None:
            task_name = input('Task name: ')
        if not quick_input:    
            if task_due_date == None:
                task_due_date = input('Due date: ')
            if task_priority == None:
                task_priority = input('Priority ([H]i, [M]edium, [L]ow): ')
            if task_details == None:
                task_details = input('Details (optional): ')
            if task_action == None:
                task_action = input('Enter a shell action to do the task: ')
            if task_list == None:
                task_list = input('Task list/category (optional): ')

        task_obj = Task(name = task_name, due_date = task_due_date, priority = task_priority, details = task_details, list = task_list, action = task_action)

        self.dbm.add_task(task_obj)

    def list(self, list=None, priority_sort=False, due_date_sort=False):
        if list != None:
            tasks = self.dbm.get_by_list(list)
        else:
            tasks = self.dbm.get_all()

        if priority_sort and due_date_sort:
            tasks.sort(key=lambda t: (t.due_date if t.due_date else date.max, t.priority.value))
        elif priority_sort:
            tasks.sort(key=lambda t: t.priority.value)
        elif due_date_sort:
            tasks.sort(key=lambda t: t.due_date if t.due_date else date.max)
            #tasks = sorted(tasks, key=attrgetter('due_date'))

        print('{:<6} {:<8}{:<30}{:>9}'.format('Id', 'Status', 'Name', 'Due Date'))
        print('-' * 60)
        for task in tasks:
            print(task.print_abbrv())
        print('_' * 60)    
        print('- "todo details [id]" to print details for a task')
        print('- "todo complete [id]" to mark the task complete')

    def details(self, task_id):
        task = self.dbm.get_task(int(task_id))
        print(task.print_detail())
    
    def do(self, task_id):
        task = self.dbm.get_task(int(task_id))
        os.system(task.action)

    def complete(self, task_id, uncomplete = False):
        try:
            task = self.dbm.get_task(int(task_id))
        except TypeError:
            print('Error: Can\'t find task with ID {}. Make sure you entered the correct ID.'.format(task_id))
        else:
            if not uncomplete:
                task.complete = True
            else:
                task.complete = False
            task = self.dbm.update_task(task)
            if(task):
                print('Task with ID {} successfully completed.'.format(task_id))

    def delete(self, task_id):
        try:
            task = self.dbm.get_task(int(task_id))
        except TypeError:
            print('Error: Can\'t find task with ID {}. Did you mistype the ID or delete the task already?'.format(task_id))
        else:
            task = self.dbm.delete_task(task)
            if(task):
                print('Task with ID {} successfully deleted.'.format(task_id))

    def clear(self):
        print("Not impletmented yet")
