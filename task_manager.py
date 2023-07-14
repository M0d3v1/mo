class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, new_task):
        self.tasks[task_id] = new_task

    def delete_task(self, task_id):
        del self.tasks[task_id]
