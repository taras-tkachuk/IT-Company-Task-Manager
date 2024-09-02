from django.test import TestCase

from task.forms import WorkerForm, WorkerUsernameSearchForm, TaskTagSearchForm
from task.models import Position


class FormTests(TestCase):
    def test_worker_creation_form_is_valid(self) -> None:
        position = Position.objects.create(name="develop")
        form_data = {
            "username": "new_user",
            "first_name": "Test",
            "last_name": "Last",
            "password1": "worker123",
            "password2": "worker123",
            "position": position,
        }
        form = WorkerForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_worker_serch_form_with_valid_data(self):
        form = WorkerUsernameSearchForm(data={"username": "Test"})
        self.assertTrue(form.is_valid())

    def test_worker_serch_form_with_invalid_data(self):
        form = WorkerUsernameSearchForm()
        self.assertFalse(form.is_valid())

    def test_tag_serch_form_with_valid_data(self):
        form = TaskTagSearchForm(data={"tag": "@python-refactoring"})
        self.assertTrue(form.is_valid())

    def test_tag_serch_form_with_invalid_data(self):
        form = TaskTagSearchForm()
        self.assertFalse(form.is_valid())
