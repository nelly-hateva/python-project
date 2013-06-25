import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from projects.models import Project


def create_project(title, days, lead, kind):
    return Project.objects.create(title=title,
        start_date=timezone.now() + datetime.timedelta(days=days),
        lead=lead, kind=kind)


class ProjectsViewTests(TestCase):
    def test_index_view_with_no_projects(self):
        response = self.client.get(reverse('projects:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects available yet.")
        self.assertQuerysetEqual(response.context['projects_list'], [])

    def test_index_view_with_one_project(self):
        create_project(title="Blank project", days=-1,
                       lead="Nelly Hateva", kind="BP")
        response = self.client.get(reverse('projects:index'))
        self.assertQuerysetEqual(
            response.context['projects_list'],
            ['<Project: Blank project>']
        )

    def test_index_view_with_more_projects(self):
        create_project(title="Agile Kanban project", days=-5,
                       lead="Ivan Ivanov", kind="AK")
        create_project(title="Blank project", days=-2,
                       lead="Nelly Hateva", kind="BP")
        create_project(title="Agile Scrum project", days=-1,
                       lead="Georgi Ivanov", kind="AS")
        response = self.client.get(reverse('projects:index'))
        self.assertQuerysetEqual(
            response.context['projects_list'],
            ['<Project: Agile Scrum project>', '<Project: Blank project>',
             '<Project: Agile Kanban project>']
        )
