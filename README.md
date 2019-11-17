Run with `python3 todo.py` + various commands (eg `python3 todo.py add -t [TASKNAME]` or `python3 todo.py add`).
Test with the `unittest` modules. Eg, `python3 task_class_test.py` will run the tests in that module.

# Dev Process

1. First, create the method/class you want to build, but have it return empty.
2. Then add a test case that checks to see if the method does what you want it to do. If you're expanding an existing class, add a test case to the relevant unit test. If you're making a new class, add a dedicated class.
3. Edit your method so that it passes the test. Do this in the simplest, most straightforward way possible.
4. Optimize your method
5. Repeat with additional functionality for the method or each new method.

# Requirements

- [ ] Create and maintain a todo list
- [ ] Create and maintain arbitrary lists in various categories
- [ ] Set priority for tasks
- [ ] Display tasks by category and/or by priority
- [ ] Set details for tasks
- [ ] Set due dates for tasks and call up tasks by due date

# Tasks
- [x] Basic add a task to a list
- [x] Add a task with description, date, due date, priority
    - [x] Create a prompt
    - [ ] Create a CLI one line command for this
- [ ] Load the tasklist into memory in a meaningful way
- [x] List existing tasks
- [ ] List existing tasks by some sorting

    
    
    
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
    
