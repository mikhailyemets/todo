from django import forms
from .models import Task, Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "owner","tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "is_done", "deadline"]

    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)
        self.fields["deadline"].help_text = (
            "Enter the deadline for the task (Format: YYYY-MM-DD HH:MM:SS)"
        )
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "content",
            "is_done",
            "deadline",
            Submit("update", "Update Task", css_class="btn-primary"),
        )


class SearchForm(forms.Form):
    tag_search = forms.CharField(max_length=100, required=False)
