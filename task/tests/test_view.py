from datetime import date
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task.models import Task, TaskType, Worker


HOME_PAGE = reverse("task:index")
WORKER_LIST = reverse("task:worker-list")
TASK_LIST = reverse("task:task-list")
TASK_TYPE_LIST = reverse("task:task-type-list")


class TestsForPublicRequired(TestCase):

    def test_workers_list(self) -> None:
        response = self.client.get(WORKER_LIST)
        self.assertNotEqual(response.status_code, 200)

    def test_tasks_list(self):
        response = self.client.get(TASK_LIST)
        self.assertNotEqual(response.status_code, 200)

    def test_positions_list(self):
        response = self.client.get(TASK_TYPE_LIST)
        self.assertNotEqual(response.status_code, 200)


class TestsForPrivateRequired(TestCase):

    def setUp(self) -> None:
        self.worker = get_user_model().objects.create_user(
            username="TestWorker",
            password="Test123"
        )
        self.client.force_login(self.worker)

    def test_login(self) -> None:
        response = self.client.get(HOME_PAGE)
        self.assertEqual(response.status_code, 200)

    def test_workers_list(self) -> None:
        response = self.client.get(WORKER_LIST)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            list(response.context["worker_list"]),
            list(Worker.objects.all())
        )


    def test_task_list_view(self):
        response = self.client.get(TASK_LIST)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "task/task_list.html")

    def test_task_type_list(self):
        response = self.client.get(TASK_TYPE_LIST)
        self.assertEqual(response.status_code, 200)
