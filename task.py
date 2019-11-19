from datetime import date
from datetime import timedelta
from priority import Priority

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
        elif due_date_string != None and due_date_string != '':
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
        if priority_string == None or priority_string == '':
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

