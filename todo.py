import argparse
from datetime import date, timedelta
import os.path
from enum import Enum
from task import Task
from priority import Priority
from taskmanager import TaskManager

FILENAME = os.path.join('todolist.txt')

def main():
    task_manager = TaskManager(FILENAME)
    parser = argparse.ArgumentParser(description='Manage your todo list.')
    parser.add_argument('action', action='store', choices=['add', 'list', 'complete'])
    parser.add_argument('-t', action='store')
    parser.add_argument('-d', action='store')
    parser.add_argument('-p', action='store')
    parser.add_argument('-e', action='store')
    parser.add_argument('-l', action='store')

    args = parser.parse_args();
    if args.action == 'add':
        add(args.t, args.d, args.p, args.e)
    elif args.action == 'list':
        list()

if __name__ == "__main__":
    main()
