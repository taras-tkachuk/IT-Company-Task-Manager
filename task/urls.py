from django.urls import path

from task.views import (index, WorkerListView, TaskListView,
                        TaskTypeListView, WorkerDetailView,
                        TaskDetailView, TaskTypeCreateView,
                        TaskTypeUpdateView, TaskTypeDeleteView,
                        TaskCreateView, TaskUpdateView, TaskDeleteView,
                        WorkerCreateView, WorkerUpdateView, WorkerDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("tasks-types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),
    path("tasks-types/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task-type-update"),
    path("tasks-types/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
]

app_name = "task"
