# You are building a Task Management System.

# Each task:
# has an id
# has a title
# can have a next task (tasks are linked)

# Requirements:
# Design Task using OOP
# Store tasks using Linked List
# Print all tasks in order
class task:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.next = None


task1 = task(1, "develop UI")
task2 = task(2, "develop backend")
task3 = task(3, "write tests")

task1.next = task2
task2.next = task3

current = task1
while current is not None:
    print(current.title)
    current = current.next