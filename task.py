from datetime import date
from datetime import timedelta
from priority import Priority
from utils import Text

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
        return (Text.BOLD + 'Name:' + Text.END + ' {name:30}' + Text.BOLD + 'Complete:' + Text.END +' {complete}\n'+
                Text.BOLD + 'Due Date:' + Text.END + ' {due_date}\n'+
                Text.BOLD + 'Priority:' + Text.END + ' {priority}\n'+
                Text.BOLD + 'List:' + Text.END + ' {list}\n'+
                Text.BOLD + 'Action:' + Text.END + ' {action}\n'+
                Text.BOLD + 'Details:' + Text.END + ' {details}\n').format( name=self.name, complete=bool(self.complete), due_date=self.due_date, priority=self.priority.name, list=self.list, action=self.action, details=self.details)

    def print_abbrv(self):
        completed = u'\033[1m\u2713\033[0m' if self.complete else ' '
        if self.priority is Priority.HIGH:
            priority_sym = u'\u21A5'
        elif self.priority is Priority.MEDIUM:
            priority_sym = u'\u21A6'
        elif self.priority is Priority.LOW:
            priority_sym = u'\u21A7'
        elif self.priority is Priority.NONE:
            priority_sym = ' '
        if self.due_date != None:
            due_date = self.due_date.strftime('%D')
        else:
            due_date = ''

        return '({0:04}) \033[1m{1:1}\033[0m [{2:1}] - {3:30}{4:>9}'.format(self.id, priority_sym, completed, self.name, due_date, align='right')


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

