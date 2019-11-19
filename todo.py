import argparse
from datetime import date, timedelta
import os.path
from enum import Enum
from task import Task
from priority import Priority

# Maybe this can be set by the user
FILENAME = os.path.join('todolist.txt')

def add(task_name = None, task_due_date = None, task_priority = None, task_details = None):
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
    parser.add_argument('-d', action='store')
    parser.add_argument('-p', action='store')
    parser.add_argument('-e', action='store')

    args = parser.parse_args();
    if args.action == 'add':
        add(args.t, args.d, args.p, args.e)
    elif args.action == 'list':
        list()

if __name__ == "__main__":
    main()
