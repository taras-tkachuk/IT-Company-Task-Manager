from django.urls import path

from task.views import index, WorkerListView, TaskListView, TaskTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks-types/", TaskTypeListView.as_view(), name="task-type-list"),
]

app_name = "task"
