from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from task.models import TaskType, Position, Task, Tag

from datetime import date


class WorkerTests(TestCase):
    username = "TestWorker"
    first_name = "Test"
    last_name = "Worker"
    password = "worker123"
    position = "QA"

    def setUp(self) -> None:
        self.position = Position.objects.create(name=self.position)
        self.worker = get_user_model().objects.create_user(
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            password=self.password,
            position=self.position,
        )

    def test_worker_creation(self) -> None:
        self.assertEqual(self.worker.username, self.username)
        self.assertEqual(self.worker.position, self.position)
        self.assertTrue(self.worker.check_password(self.password))

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            f"{self.username} - {self.last_name}"
        )


class PositionTests(TestCase):
    def test_position_str(self) -> None:

        position = Position.objects.create(name="develop")
        self.assertEqual(
            str(position),
            position.name
        )


class TaskTests(TestCase):
    def setUp(self) -> None:
        task_type = TaskType.objects.create(name="refactoring")
        self.task = Task.objects.create(
            name="TestTask",
            priority="urgent",
            deadline=date.today(),
            is_completed=False,
            task_type=task_type
        )

    def test_task_str(self) -> None:
        self.assertEqual(
            str(self.task),
            f"{self.task.name}, deadline: {self.task.deadline}"
        )

    def test_get_absolute_url(self) -> None:
        expected_url = reverse(
            "task:task-detail",
            kwargs={"pk": self.task.pk}
        )
        actual_url = self.task.get_absolute_url()
        self.assertEqual(expected_url, actual_url)


class TaskTypeTests(TestCase):

    def test_task_type_str(self):
        task_type = TaskType.objects.create(name="refactoring")
        self.assertEqual(str(task_type), task_type.name)


class TagTests(TestCase):

    def test_tag_str(self) -> None:
        tag = Tag.objects.create(name="@python-refactoring")
        self.assertEqual(str(tag), tag.name)
