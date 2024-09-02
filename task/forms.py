from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from task.models import Worker, Tag, Task


class WorkerForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position"
        )


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        ),
        required=True
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"


class TaskTagSearchForm(forms.Form):
    tag = forms.CharField(
        max_length=99,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by tag"
            }
        )
    )


class WorkerUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=99,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )
