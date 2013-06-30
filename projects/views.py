from django.views import generic
from django.utils import timezone
from django.http import HttpResponse,  HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext, loader

from projects.models import Project, Issue
from projects.forms import ProjectForm, IssueForm


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


class CreateProjectView(generic.CreateView):
    model = Project
    form_class = ProjectForm


class AddProjectView(generic.RedirectView):
    def post(self, request, *args, **kwargs):
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            return super(AddProjectView, self).post(request, *args, **kwargs)
        else:
            # Redisplay the create project form.
            return render(request, 'projects/project_form.html', {
                'form': ProjectForm,
                #'error_message': project_form.errors,
                'error_message': 'All the fields are required.',
            })


class CreateIssueView(generic.CreateView):
    model = Issue
    form_class = IssueForm

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['pk'])
        template = loader.get_template('projects/issue_form.html')
        context = RequestContext(request, {
            'project_id': project.id,
            'form': IssueForm,
        })
        return HttpResponse(template.render(context))


class AddIssueView(generic.RedirectView):
    def post(self, request, *args, **kwargs):
        issue_form = IssueForm(request.POST)
        if issue_form.is_valid():
            issue = issue_form.save(commit=False)
            issue.project = Project.objects.all().get(pk=int(kwargs['pk']))
            issue_form.save()
            return render(request, 'projects/detail.html', {
                'project': issue.project
            })
        else:
            # Redisplay the create issue form
            return render(request, 'projects/issue_form.html', {
                'form': IssueForm,
                'error_message': 'All the fields are required',
            })


class DetailIssueView(generic.DetailView):
    model = Issue
    template_name = 'projects/issue.html'


class StartIssueView(generic.View):
    def post(self, request, *args, **kwargs):
        issue = Issue.objects.all().get(pk=kwargs['pk'])
        print(issue.status)
        if issue.status == 'OPEN' or issue.status == 'RESOLVED':
            issue.status = 'IN_PROGRESS'
        issue.save()
        return HttpResponseRedirect('/projects/' + str(issue.project.id))


class StopIssueView(generic.View):
    def post(self, request, *args, **kwargs):
        issue = Issue.objects.all().get(pk=kwargs['pk'])
        if issue.status == 'IN_PROGRESS' or 'REOPENED':
            issue.status = 'RESOLVED'
        issue.save()
        return HttpResponseRedirect('/projects/' + str(issue.project.id))

class CloseIssueView(generic.View):
    def post(self, request, *args, **kwargs):
        issue = Issue.objects.all().get(pk=kwargs['pk'])
        issue.status = 'CLOSED'
        issue.save()
        return HttpResponseRedirect('/projects/' + str(issue.project.id))
