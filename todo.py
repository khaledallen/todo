import argparse
import os.path
import json
from datetime import date, timedelta
from enum import Enum
from task import Task
from priority import Priority
from taskmanager import TaskManager

def parse_commands (parser, namespace):
  namespaces = []
  commands = namespace.commands
  while commands:
    n = parser.parse_args(commands)
    commands = n.commands
    namespaces.append(n)

  return namespaces

def main():
    local_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(local_path, 'config.json')
    if not os.path.exists(config_path):
        print('Please create a config.json file')
        #This is where the install function will go
        return

    f = open(config_path)
    config = json.load(f)

    os.chdir(os.path.expanduser(config['tasksDirectory']))
    task_manager = TaskManager(config['dbName'])

    ## This function takes the 'extra' attribute from global namespace and re-parses it to create separate namespaces for all other chained commands.

    argparser=argparse.ArgumentParser()

    # This may break updates.
    argparser._positionals.title = 'Commands'

    subparsers = argparser.add_subparsers(dest='subparser_name')

    parser_add = subparsers.add_parser('add', help = 'add a task')
    parser_add.add_argument('task', nargs='?', help="The name of the task you want to add. If you omit this, todo will explicitly ask for a name.", default=None)
    parser_add.add_argument('-q', '--quick', action='store_true', help='Suppress asking for task details. Todo will prompt for a task name if one wasn\'t provided.')
    parser_add.add_argument('-d', '--due-date', metavar='<date>', action='store', help='Set due date. You can also say "today" or "tomorrow"')
    parser_add.add_argument('-p', '--priority', metavar='<[H]igh, [M]edium, [L]ow>', action='store', help='Set priority', choices=['H', 'h', 'M', 'm', 'L', 'l', 'High', 'Medium', 'Low', 'high', 'medium', 'low', 'HIGH', 'MEDIUM', 'LOW'])
    parser_add.add_argument('-D', '--details', metavar='<details text>', action='store', help='Set details')
    parser_add.add_argument('-l', '--list', metavar='<list name>', action='store', help='Set which list the task belongs to')
    parser_add.add_argument('-a', '--action', metavar='<shell command>', action='store', help='Set a terminal command to execute when you DO the task')

    parser_list = subparsers.add_parser('list', help = "List tasks")
    parser_list.add_argument('list', nargs='?', default=None, help='Which list you want to show. Passing "list" here will list all lists (eg, todo list list)')
    parser_list.add_argument('-p', '--priority', action='store_true', help='Sort by priority')
    parser_list.add_argument('-d', '--due_date', action='store_true', help='Sort by due date. This takes priority over sorting by priority, so if you select both, tasks will be sorted by date first, then priority')

    parser_complete = subparsers.add_parser('complete', help = "Mark a task completed")
    parser_complete.add_argument('id', default=None, help='Id of the task to mark completed')
    parser_complete.add_argument('-u', '--uncomplete', action='store_true', help='Mark a task uncompleted')
    
    parser_details= subparsers.add_parser('details', help = "View details for a task")
    parser_details.add_argument('id', default=None, help = 'Id of the task whose details you want to see')

    parser_do= subparsers.add_parser('do', help = "Perform the action for a task")
    parser_do.add_argument('id', default=None, help = 'Id of the task whose action to execute')

    parser_delete = subparsers.add_parser('delete', help="Delete a task")
    parser_delete.add_argument('id', default=None, help='Id of the task to delete')
    parser_delete.add_argument('-f', '--force', action='store_true', help='Don\'t prompt for confirmation.')

    parser_clear = subparsers.add_parser('clear', help="Delete all completed tasks")
    parser_clear.add_argument('-f', '--force', action='store_true', help='Don\'t prompt for confirmation.')

    parser_search = subparsers.add_parser('search', help='Search your tasks and generate a list of matches')
    parser_search.add_argument('query', metavar='<search term>', action='store', help='The text to match. Words are split and search will return anything that matches all words provided, not necessarily in the order given')
    ## Add nargs="*" for zero or more other commands
    argparser.add_argument('commands', metavar='<command>', nargs = "*", help = argparse.SUPPRESS) 

    args = argparser.parse_args()
    commands = parse_commands(argparser, args)

    if args.subparser_name == 'add':
        task_manager.add(
                task_name = args.task,
                task_due_date = args.due_date,
                task_priority = args.priority,
                task_details = args.details,
                task_list = args.list,
                task_action = args.action,
                quick_input = args.quick)
    elif args.subparser_name == 'list':
        task_manager.list(args.list, args.priority, args.due_date)
    elif args.subparser_name == 'complete':
        task_manager.complete(args.id, args.uncomplete)
    elif args.subparser_name == 'details':
        task_manager.details(args.id)
    elif args.subparser_name == 'do':
        task_manager.do(args.id)
    elif args.subparser_name == 'delete':
        task_manager.delete(args.id, args.force)
    elif args.subparser_name == 'clear':
        task_manager.clear(args.force)
    elif args.subparser_name == 'search':
        task_manager.search(args.query)

if __name__ == "__main__":
    main()
