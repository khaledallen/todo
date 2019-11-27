import argparse
from datetime import date, timedelta
import os.path
from enum import Enum
from task import Task
from priority import Priority
from taskmanager import TaskManager

DBNAME = 'todo.db'

def main():
    os.chdir(os.path.expanduser('~/Coding/todo-app'))
    task_manager = TaskManager(DBNAME)
    parser = argparse.ArgumentParser(description='Manage your todo list.')
    parser.add_argument('action', action='store', choices=['add', 'list', 'complete', 'do', 'detail'])
    parser.add_argument('-t', action='store')
    parser.add_argument('-d', action='store')
    parser.add_argument('-p', action='store')
    parser.add_argument('-e', action='store')
    parser.add_argument('-l', action='store')

    args = parser.parse_args();
    if args.action == 'add':
        task_manager.add(args.t, args.d, args.p, args.e)
    elif args.action == 'list':
        task_manager.list()
    elif args.action == 'detail':
        task_manager.detail(int(args.t))
    elif args.action == 'complete':
        task_manager.complete(int(args.t))
    elif args.action == 'do':
        task_manager.do(int(args.t))

if __name__ == "__main__":
    main()
