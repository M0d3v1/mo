# mo
# Task Manager

Task Manager is a Python application that allows users to create, update, and delete tasks.

## Features

- Create tasks: Users can create new tasks and add them to the task list.
- Update tasks: Users can update the details of existing tasks.
- Delete tasks: Users can delete tasks from the task list.

## Installation

1. Clone the repository:

git clone https://github.com/your-username/task-manager.git
2. Navigate to the project directory: cd task-manager 

3. Run the unit tests: python -m unittest test_task_manager.py


The tests should execute, and you should see the test results.

## Usage

1. Import the `TaskManager` class from the `task_manager` module:

```python
from task_manager import TaskManager


Create a new instance of the TaskManager class:
task_manager = TaskManager()

Use the available methods to interact with the task manager:
# Create a new task
task_manager.create_task("Task 1")

# Update an existing task
task_manager.update_task(0, "Updated Task 1")

# Delete a task
task_manager.delete_task(0)
