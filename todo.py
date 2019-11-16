import argparse
import os.path

# Maybe this can be set by the user
FILENAME = os.path.join('todolist.txt')

class task:
    def __init__(self, name, due_date, priority, details):
        self.name = name
        self.due_date = Date(due_date)
        self.priority = priorityEnum.priority
        self.details = details

def add(task):
    if task == '':
        task_name = input('Task name: ')
        task_due_date = input('Due date: ')
        task_priority = input('Priority ([H]i, [M]edium, [L]ow): ')
        task_description = input('Details (optional)')

    os.chdir(os.path.expanduser('~'))
    file = open(FILENAME, 'a+')
    file.write(task + '\n')
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
