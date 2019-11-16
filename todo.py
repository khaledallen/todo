import argparse
from datetime import date, timedelta
import os.path
from enum import Enum

class Priority(Enum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2
    NONE = 3

# Maybe this can be set by the user
FILENAME = os.path.join('todolist.txt')

class Task:
    def __init__(self, name = None, due_date = None, priority = None, details = None):
        self.name = name
        self.due_date = self.process_due_date(due_date)
        self.priority = self.process_priority(priority)
        self.details = details

    def process_due_date(self, due_date_string = None):
        if due_date_string == 'today':
            return date.today()
        elif due_date_string == 'tomorrow':
            return date.today() + timedelta(1)
        elif due_date_string != None:
            month = int(due_date_string[:2])
            day = int(due_date_string[3:5])
            if len(due_date_string) == 10:
                year = int(due_date_string[-4:])
            elif len(due_date_string) == 8:
                year = 2000 + int(due_date_string[-2:])
            elif len(due_date_string) == 5:
                year = date.today().year
            return date(year, month, day)
        return 

    def process_priority(self, priority_string = None):
        if priority_string == None:
            return Priority.NONE
        if priority_string[0].lower() == 'h':
            return Priority.HIGH
        if priority_string[0].lower() == 'm':
            return Priority.MEDIUM
        if priority_string[0].lower() == 'l':
            return Priority.LOW

    def to_entry_string(self):
        return '{name}:{due_date}:{priority}:{details}'.format(
                    name = self.name,
                    due_date = self.due_date,
                    priority = self.priority,
                    details = self.details
                )

def add(quick_task_name = None):
    if quick_task_name == None:
        task_name = input('Task name: ')
        task_due_date = input('Due date: ')
        task_priority = input('Priority ([H]i, [M]edium, [L]ow): ')
        task_details = input('Details (optional): ')

        task_obj = Task(task_name, task_due_date, task_priority, task_details)
    else:
        task_obj = Task(quick_task_name)

    os.chdir(os.path.expanduser('~'))
    file = open(FILENAME, 'a+')

    print('the task received was', task_obj.to_entry_string())
    task_file_entry = task_obj.to_entry_string()

    file.write(task_file_entry + '\n')
    file.close();

def list():
    os.chdir(os.path.expanduser('~'))
    file = open(FILENAME, 'r')
    tasks = file.readlines()
    for task in tasks:
        print(task)
    

def main():
    parser = argparse.ArgumentParser(description='Manage your todo list.')
    parser.add_argument('action', action='store', choices=['add', 'list', 'complete'])
    parser.add_argument('-t', action='store')

    args = parser.parse_args();
    if args.action == 'add':
        add(args.t)
    elif args.action == 'list':
        list()

if __name__ == "__main__":
    main()
