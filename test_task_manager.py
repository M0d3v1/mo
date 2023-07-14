import unittest
from task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_create_task(self):
        self.task_manager.create_task("Task 1")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_update_task(self):
        self.task_manager.create_task("Task 1")
        self.task_manager.update_task(0, "Updated Task 1")
        self.assertEqual(self.task_manager.tasks[0], "Updated Task 1")

    def test_delete_task(self):
        self.task_manager.create_task("Task 1")
        self.task_manager.delete_task(0)
        self.assertEqual(len(self.task_manager.tasks), 0)

if __name__ == "__main__":
    unittest.main()
