from django import forms

from projects.models import Project


class CreateProjectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField(max_length=50,
                                               label='Project Title',
                                               required=True)
        self.fields['choice'] = forms.ChoiceField(label='Select Project Type',
                                   widget=forms.RadioSelect,
                                   choices=Project.TYPE_OF_PROJECTS_CHOICES,
                                   required=True)
