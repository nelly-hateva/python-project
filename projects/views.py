from django.views.generic import ListView

from projects.models import Project


class IndexView(ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.order_by('-start_date')
