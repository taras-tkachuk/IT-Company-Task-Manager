from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from task_manager import settings


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.username} - {self.last_name}"

    def get_absolute_url(self) -> object:
        return reverse("task:worker-detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    name = models.CharField(
        max_length=55,
        unique=True
    )

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("urgent", "Urgent"),
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=9, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        blank=True
    )
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)

    def __str__(self) -> str:
        return f"{self.name}, deadline: {self.deadline}"

    def get_absolute_url(self) -> object:
        return reverse("task:task-detail", kwargs={"pk": self.pk})
