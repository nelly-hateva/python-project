from django.views.generic import ListView, DetailView, FormView, RedirectView
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from projects.models import Project
from projects.forms import CreateProjectForm


class IndexView(ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.order_by('-start_date')


class DetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'

    def get_queryset(self):
        return Project.objects.all()


class CreateProjectView(FormView):
    template_name = 'projects/create_project.html'
    form_class = CreateProjectForm


class AddProjectView(RedirectView):
    def post(self, request, *args, **kwargs):
        try:
            kind = request.POST['choice']
        except KeyError:
            # Redisplay the project create form.
            return render(request, 'projects/create_project.html', {
                'error_message': "You didn't select type of project.",
            })
        else:
            try:
                title = request.POST['title']
            except KeyError:
                # Redisplay the project create form.
                return render(request, 'projects/create_project.html', {
                    'error_message': "Please enter the title of the project.",
                })
            else:
                Project.objects.create(title=title,
                                       start_date=timezone.now(),
                                       lead="Nelly Hateva", kind=kind)
                return HttpResponseRedirect(reverse('projects:index'))
