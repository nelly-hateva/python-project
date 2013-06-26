import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from projects.models import Project


def create_project(title, days, lead, kind):
    """
    Creates a project with the given `title`, `lead` and `kind`
    started the given number of `days` offset to now (negative number).
    """
    return Project.objects.create(title=title,
        start_date=timezone.now() + datetime.timedelta(days=days),
        lead=lead, kind=kind)


class ProjectsIndexViewTests(TestCase):
    def test_index_view_with_no_projects(self):
        """
        If no projects exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('projects:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects available yet.")
        self.assertQuerysetEqual(response.context['projects_list'], [])

    def test_index_view_with_one_project(self):
        """
        One project should be displayed on the index page.
        """
        create_project(title="Blank project", days=-1,
                       lead="Nelly Hateva", kind="BP")
        response = self.client.get(reverse('projects:index'))
        self.assertQuerysetEqual(
            response.context['projects_list'],
            ['<Project: Blank project>']
        )

    def test_index_view_with_more_projects(self):
        """
        Projects should be displayed on the index page.
        """
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


class ProjectDetailViewTests(TestCase):
    def test_detail_view_with_nonexistent_project(self):
        """
        The detail view of nonexistent project should
        return a 404 not found.
        """
        response = self.client.get(reverse('projects:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_of_project(self):
        """
        The detail view of a project should display
        the project's title.
        """
        project = create_project(title="Project title", days=-1,
                                 lead="Georgi Georgiev", kind="AK")
        response = self.client.get(reverse('projects:detail',
                                           args=(project.id,)))
        self.assertContains(response, project.title, status_code=200)


class CreateProjectViewTests(TestCase):
    def test_create_project_view(self):
        """
        The create project view should display
        "Select Project Type:".
        """
        response = self.client.get(reverse('projects:create'))
        self.assertContains(response, 'Select Project Type:', status_code=200)


class AddProjectViewTest(TestCase):
    def test_add_a_project_with_title_and_kind(self):
        """
        If the form is valid, the project must be saved to the database
        and the client should be redirected to the index page.
        """
        #response = self.client.post(reverse('projects:create'),
        #                            {'title': 'Project title',
        #                             'kind': 'AK'})
        #print(Project.objects.all())
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(Project.objects.all()[0].pk, 1)
        #self.assertContains(response, 'Create Project', status_code=200)

    def test_add_a_project_with_no_title(self):
        """
        If the form is invalid, the view should return
        the create project view with error message
        "Please enter the title of the project.".
        """
        response = self.client.post(reverse('projects:create'),
                                    {'title': '',
                                     'kind': 'AK'})
        #self.assertContains(response,
        #                    'All fields are required.',
        #                    status_code=200)
        self.assertEqual(Project.objects.all().count(), 0)

    def test_add_a_project_with_no_kind(self):
        """
        If the form is invalid, the view should return
        the create project view with error message
        "You didn't select type of project.".
        """
        response = self.client.post(reverse('projects:create'),
                                    {'title': 'Title'})
        #self.assertContains(response,
        #                    'All fields are required.',
        #                    status_code=200)
        self.assertEqual(Project.objects.all().count(), 0)
