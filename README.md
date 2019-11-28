Run with `python3 todo.py` + various commands (eg `python3 todo.py add -t [TASKNAME]` or `python3 todo.py add`).
Test with the `unittest` modules. Eg, `python3 task_class_test.py` will run the tests in that module.

# Dev Process

1. First, create the method/class you want to build, but have it return empty.
2. Then add a test case that checks to see if the method does what you want it to do. If you're expanding an existing class, add a test case to the relevant unit test. If you're making a new class, add a dedicated class.
3. Edit your method so that it passes the test. Do this in the simplest, most straightforward way possible.
4. Optimize your method
5. Repeat with additional functionality for the method or each new method.

# Features

- [ ] User can search for task by keywords
- [ ] Todolist can check if a task is similar to an existing one and let the user know it's already on the list or allow bumping it     
- [ ] User can display tasks by various attributes (priority, due date, category)
- [ ] User can clear completed tasks to an archive
- [x] User can add a task
- [x] User can add a task with due date, priority, details, and title
- [x] User can quick add a task with default values from the command line directly
- [x] User can set an action that `todo do` will execute in the shell    
- [x] Create and maintain arbitrary lists in various categories

# Tasks
- [ ] Display tasks by due date
- [ ] Display tasks by priority
- [ ] Search by...name
- [ ] Create archive in the DB for clearing tasks
- [ ] Create config file for defaults
    - [ ] Show/hide completed tasks by default
    - [ ] Set default sorting
    - [ ] Set location of db
    - [ ] Auto-archive tasks when completed
- [x] Basic add a task to a list
- [x] Add a task with description, date, due date, priority
    - [x] Create a prompt
    - [x] Create a CLI one line command for this
- [x] Implement category/lists
- [x] Load the tasklist into memory in a meaningful way
- [x] List existing tasks
- [x] List existing tasks by some sorting
- [x] Set priority for tasks
- [x] Set due dates for tasks
- [x] Set details for tasks
- [x] Display tasks by category

# Implementation Ideas

We can start with something simple in Python that uses a text file, and then if we want to grow it later, we can.

The app could use a text file to store todos, which would be the simplest and most portable solution -> just move the text file and load the software and you're golden
Or it could use a database, either SQL or Neo4j, or some combination, where it uses  textfile as a backup but mainly interacts with a database that it sets up

I would like it to be a CLI, so I can manage todos from the keyboard.

I would at some point like to have it accessible remotely. So that there is a CLI app, but it also connects to a remote location as well. That might just be a matter of giving it a Git repo, and having it maintain synchronization with Github, which actually would be very tidy.

## Language Options

- C/C++/C#
- Python

## Storage Options

- SQLite
- Combination of text and database
    
    
