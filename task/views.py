from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from task.models import Worker, Task, TaskType


def index(request: HttpRequest) -> HttpResponse:
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_task_types = TaskType.objects.count()
    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_task_types": num_task_types,
    }
    return render(request, "task/index.html", context=context)
