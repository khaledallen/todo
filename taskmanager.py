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
        existinglist = self.dbm.get_list_by_name(task_obj.list)
        if existinglist == None:
            self.dbm.add_list(task_obj.list)

    def list(self, list=None, priority_sort=False, due_date_sort=False, task_list=None):
        if task_list != None:
            tasks = task_list
        elif list == 'list':
            lists = self.dbm.get_all_lists()
            for list in lists:
                print(list[1])
            return
        elif list != None:
            tasks = self.dbm.get_by_list(list)
        else:
            tasks = self.dbm.get_all()

        tasks.sort(key=lambda t: t.complete)
        if priority_sort and due_date_sort:
            tasks.sort(key=lambda t: (t.due_date if t.due_date else date.max, t.priority.value))
        elif priority_sort:
            tasks.sort(key=lambda t: t.priority.value)
        elif due_date_sort:
            tasks.sort(key=lambda t: t.due_date if t.due_date else date.max)

        print('{:<6} {:<8}{:<50}{:>9}'.format('Id', 'Status', 'Name', 'Due Date'))
        print('-' * 80)
        for task in tasks:
            print(task.print_abbrv())
        print('_' * 80)    
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
            self.list()

    def delete(self, task_id, force = False):
        try:
            task = self.dbm.get_task(int(task_id))
        except TypeError:
            print('Error: Can\'t find task with ID {}. Did you mistype the ID or delete the task already?'.format(task_id))
        else:
            if not force:
                confirm = input('Are you sure you want to delete task {}? (y/n)'.format(task.id))
            if force or confirm.lower() is 'y':
                task = self.dbm.delete_task(task)
                if(task):
                    print('Task with ID {} successfully deleted.'.format(task_id))
                else:
                    print('There was an error.')
            else:
                print('Cancelled')
            self.list()

    def clear(self, force):
        if not force:
            confirm = input('Are you sure you want to delete your completed tasks? (y/n)')
        if force or confirm.lower() == 'y':
            self.dbm.delete_completed()
        else:
            print('Cancelled')
        self.list()

    def search(self, query):
        tasks = self.dbm.get_all()

        results = []
        query_arr = query.split(' ')

        for task in tasks:
            include = True
            for query_snip in query_arr:
                if task.name.find(query_snip) == -1:
                    include = False
            if include:
                results.append(task)
                    
        return self.list(task_list=results)
            
