import os.path
from task import Task

class TaskManager:
    def __init__(self, task_file_path):
        self.tasks = dict()
        os.chdir(os.path.expanduser('~'))
        file = open(task_file_path, 'r')
        self.process_task_file(file)
        file.close()
        print(self.tasks)

    def process_task_file(self, task_file):
        for line in task_file.readlines():
            print(line)
            task_data = line.split(':')
            print(task_data)
            task = Task(task_data[0], task_data[1], task_data[2], task_data[3], task_data[4])
            list_category = task.list
            self.tasks[list_category] = task

    def add(self, task_name = None, task_due_date = None, task_priority = None, task_details = None):
        print(task_name, task_due_date, task_priority, task_details)
        if task_name == None:
            task_name = input('Task name: ')
            task_due_date = input('Due date: ')
            task_priority = input('Priority ([H]i, [M]edium, [L]ow): ')
            task_details = input('Details (optional): ')

            task_obj = Task(task_name, task_due_date, task_priority, task_details)
        else:
            task_obj = Task(task_name, task_due_date, task_priority, task_details)

        os.chdir(os.path.expanduser('~'))
        file = open(FILENAME, 'a+')

        print('Adding {} to your todo list'.format(task_obj.to_entry_string()))
        task_file_entry = task_obj.to_entry_string()

        file.write(task_file_entry + '\n')
        file.close();

    def list(self):
        tasks = _task_repository.get_all()
        for task in tasks:
            print(task)
