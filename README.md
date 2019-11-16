# Requirements

- [ ] Create and maintain a todo list
- [ ] Create and maintain arbitrary lists in various categories
- [ ] Set priority for tasks
- [ ] Display tasks by category and/or by priority
- [ ] Set details for tasks
- [ ] Set due dates for tasks and call up tasks by due date

# Tasks
- [x] Basic add a task to a list
- [ ] Add a task with description, date, due date, priority
    - [ ] Create a prompt
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
    
