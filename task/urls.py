from django.urls import path

from task.views import (index, WorkerListView, TaskListView,
                        TaskTypeListView, WorkerDetailView,
                        TaskDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks-types/", TaskTypeListView.as_view(), name="task-type-list"),
]

app_name = "task"
