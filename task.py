from datetime import date
from datetime import timedelta
from priority import Priority

class Task:
    def __init__(self,
            id = None,
            name = None,
            due_date = None,
            priority = None,
            details = None,
            list = None,
            complete = False):
        self.id = None  #this is always set by the database
        self.name = name
        self.due_date = self.process_due_date(due_date)
        self.priority = self.process_priority(priority)
        self.details = details
        self.list = list
        self.complete = complete

    def process_due_date(self, due_date_string = None):
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

