from datetime import date
from datetime import timedelta
from priority import Priority
from termcolor import colored, cprint

class Task:
    def __init__(self,
            id = None,
            name = None,
            due_date = None,
            priority = None,
            details = None,
            list = None,
            complete = False,
            action = None):
        self.id = id  #this is always set by the database
        self.name = name
        self.due_date = self.process_due_date(due_date)
        self.priority = self.process_priority(priority)
        self.details = details
        self.list = list
        self.complete = complete
        self.action = action

    def __str__(self):
        return '{} Due: {}, {}, Details: {}, List: {}, Complete: {}'.format(self.name, self.due_date, self.priority, self.details, self.list, self.complete)

    def print_detail(self):
        return ('Name: {name:30}Complete: {complete}\n'+
                'Due Date: {due_date}\n'+
                'Priority: {priority}\n'+
                'List: {list}\n'+
                'Action: {action}\n'+
                'Details: {details}\n').format( name=self.name, complete=bool(self.complete), due_date=self.due_date, priority=self.priority.name, list=self.list, action=self.action, details=self.details)

    def print_abbrv(self):
        completed = colored('\u2713', attrs=['bold']) if self.complete else ' '
        action = u'\u25B6' if self.action else ' '
        if self.priority is Priority.HIGH:
            priority_sym = colored('H', attrs=['bold'])
        elif self.priority is Priority.MEDIUM:
            priority_sym = colored('M', attrs=['bold'])
        elif self.priority is Priority.LOW:
            priority_sym = colored('L', attrs=['bold'])
        elif self.priority is Priority.NONE:
            priority_sym = ' '
        if self.due_date != None:
            if self.due_date < date.today():
                due_date = colored(self.due_date.strftime('%D'), 'red')
            else:
                due_date = self.due_date.strftime('%D')
        else:
            due_date = ''

        return "{0:04} {1:1} {2:2}[{3:1}] {4:50}{5:>9}".format(self.id, priority_sym, action, completed, self.name, due_date, align='right')


    def process_due_date(self, due_date_string = None):
        if type(due_date_string) == date:
            return due_date_string
        if due_date_string == 'today':
            return date.today()
        elif due_date_string == 'tomorrow':
            return date.today() + timedelta(1)
        elif due_date_string != None and due_date_string != '' and due_date_string != 'None':
            date_array = due_date_string.split('/')
            if len(date_array) > 1:
                month = int(date_array[0])
                day = int(date_array[1])
                if len(date_array) == 3:
                    if len(date_array[2]) == 4:
                        year = int(date_array[2])
                    elif len(date_array[2]) == 2:
                        year = 2000 + int(date_array[2])
                else:
                    year = date.today().year
            else:
                date_array = due_date_string.split('-')
                year = int(date_array[0])
                month = int(date_array[1])
                day = int(date_array[2])
            return date(year, month, day)
        return 

    def process_priority(self, priority_input = None):
        if type(priority_input) == Priority:
            return priority_input
        if type(priority_input) == int:
            return Priority(priority_input)
        if priority_input == None or priority_input == '' or priority_input == 'None':
            return Priority.NONE
        if priority_input[0].lower() == 'h':
            return Priority.HIGH
        if priority_input[0].lower() == 'm':
            return Priority.MEDIUM
        if priority_input[0].lower() == 'l':
            return Priority.LOW

