from django import forms

from projects.models import Project, Issue


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('start_date')


class IssueForm(forms.ModelForm):
    project_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Issue
        exclude = ('project', 'status', 'comment')
