from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.forms import (WorkerForm, TaskForm, TaskNameSearchForm,
                        WorkerUsernameSearchForm)
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


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 5
    queryset = Worker.objects.all().order_by("username")

    def get_queryset(self):
        form = WorkerUsernameSearchForm(self.request.GET)

        if form.is_valid():
            return Worker.objects.filter(
                username__icontains=form.cleaned_data["username"]
            )

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = WorkerUsernameSearchForm(
            initial={"username": username}
        )
        return context


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.select_related("position")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task:worker-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.all().order_by("deadline")

    def get_queryset(self):
        form = TaskNameSearchForm(self.request.GET)

        if form.is_valid():
            return Task.objects.filter(
                name__icontains=form.cleaned_data["name"]
            )

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(TaskListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = TaskNameSearchForm(
            initial={"name": name}
        )
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related("assignees__position")

    def post(self, request, *args, **kwargs) -> HttpResponseRedirect:
        task = self.get_object()
        if "assign" in request.POST:
            task.assignees.add(self.request.user)
        elif "remove" in request.POST:
            task.assignees.remove(self.request.user)
        task.save()
        return HttpResponseRedirect(
            reverse_lazy(
                "task:task-detail",
                kwargs={"pk": task.id}
            )
        )


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task/task_type_list.html"
    context_object_name = "task_type_list"
    queryset = TaskType.objects.all().order_by("name")


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task:task-type-list")
    template_name = "task/task_type_form.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task:task-type-list")
    template_name = "task/task_type_confirm_delete.html"
