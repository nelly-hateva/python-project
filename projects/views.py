from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from projects.models import Project, Issue
from projects.forms import CreateProjectForm


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.order_by('-start_date')


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_queryset(self):
        return Project.objects.all()


class CreateProjectView(generic.FormView):
    template_name = 'projects/create_project.html'
    form_class = CreateProjectForm


class AddProjectView(generic.RedirectView):
    def post(self, request, *args, **kwargs):
        try:
            title = request.POST['title']
        except KeyError:
            # Redisplay the project create form.
            return render(request, 'projects/create_project.html', {
                'error_message': "All fields are required.",
            })
        try:
            kind = request.POST['kind']
        except KeyError:
            # Redisplay the project create form.
            return render(request, 'projects/create_project.html', {
                'error_message': "All fields are required.",
            })
        else:
            Project.objects.create(title=title,
                                   start_date=timezone.now(),
                                   lead="Nelly Hateva", kind=kind)
            return HttpResponseRedirect(reverse('projects:index'))


class CreateIssueView(generic.CreateView):
    model = Issue


class AddIssueView(generic.View):
    pass
