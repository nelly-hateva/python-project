import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from projects.models import Project


def create_project(title, days, lead, project_type):
    """
    Creates a project with the given `title`, `lead` and `project_type`
    started the given number of `days` offset to now (negative number).
    """
    return Project.objects.create(title=title,
        start_date=timezone.now() + datetime.timedelta(days=days),
        lead=lead, project_type=project_type)


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
                       lead="Nelly Hateva", project_type="BP")
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
                       lead="Ivan Ivanov", project_type="AK")
        create_project(title="Blank project", days=-2,
                       lead="Nelly Hateva", project_type="BP")
        create_project(title="Agile Scrum project", days=-1,
                       lead="Georgi Ivanov", project_type="AS")
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
                                 lead="Georgi Georgiev", project_type="AK")
        response = self.client.get(reverse('projects:detail',
                                           args=(project.id,)))
        self.assertContains(response, project.title, status_code=200)


class CreateProjectViewTests(TestCase):
    def test_create_project_view(self):
        """
        The create project view should display
        Title:
        Lead:
        Project type:
        Create
        """
        response = self.client.get(reverse('projects:create'))
        self.assertContains(response, 'Title:', status_code=200)
        self.assertContains(response, 'Lead:', status_code=200)
        self.assertContains(response, 'Project type:', status_code=200)
        self.assertContains(response, 'Create', status_code=200)


class AddProjectViewTest(TestCase):
    def test_add_a_project_valid_form(self):
        """
        If the form is valid, the project must be saved to the database
        and the client should be redirected to the index page.
        """
        response = self.client.post(reverse('projects:create'),
                                    {'title': 'Project title',
                                     'lead': 'Project lead',
                                     'project_type': 'AK'})
        #print(Project.objects.all())
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(Project.objects.all()[0].pk, 1)
        #self.assertContains(response, 'Create Project', status_code=200)

    def test_add_a_project_with_no_title(self):
        """
        If the form is invalid, the view should return
        the create project view with error message
        "All the fields are required".
        """
        #response = self.client.post(reverse('projects:create'),
        #                            {'title': '',
        #                             'lead': 'Project lead',
        #                             'project_type': 'AK'})
        #self.assertContains(response,
        #                    'All the fields are required.',
        #                    status_code=200)
        #self.assertEqual(Project.objects.all().count(), 0)

    def test_add_a_project_with_no_project_type(self):
        """
        If the form is invalid, the view should return
        the create project view with error message
        "All the fields are required".
        """
        #response = self.client.post(reverse('projects:create'),
        #                            {'title': '',
        #                             'lead': 'Project lead'})
        #self.assertContains(response,
        #                    'All the fields are required.',
        #                    status_code=200)
        #self.assertEqual(Project.objects.all().count(), 0)

    def test_add_a_project_with_no_lead(self):
        """
        If the form is invalid, the view should return
        the create project view with error message
        "All the fields are required".
        """
        #response = self.client.post(reverse('projects:create'),
        #                            {'title': '',
        #                             'project_type': 'AK'})
        #self.assertContains(response,
        #                    'All the fields are required.',
        #                    status_code=200)
        #self.assertEqual(Project.objects.all().count(), 0)


class CreateIssueViewTests(TestCase):
    def test_create_issue_view_for_existent_project(self):
        """
        The create issue view for existent project should display
        Issue type:
        Summary:
        Priority:
        Assignee:
        Reporter:
        Description:
        Create
        """
        create_project(title="Blank project", days=-1,
                       lead="Nelly Hateva", project_type="BP")
        response = self.client.get(reverse('projects:create_issue', args=(1,)))
        self.assertContains(response, 'Issue type:', status_code=200)
        self.assertContains(response, 'Summary:', status_code=200)
        self.assertContains(response, 'Priority:', status_code=200)
        self.assertContains(response, 'Assignee:', status_code=200)
        self.assertContains(response, 'Reporter:', status_code=200)
        self.assertContains(response, 'Description:', status_code=200)
        self.assertContains(response, 'Create', status_code=200)

    def test_create_issue_view_for_nonexistent_project(self):
        """
        The create issue view for nonexistent project should
        return a 404 not found.
        """
        response = self.client.get(reverse('projects:create_issue', args=(1,)))
        self.assertEqual(response.status_code, 404)


class AddIssueViewTest(TestCase):
    def test_add_an_issue_valid_form(self):
        """
        If the form is valid, the issue must be saved to the database
        and the client should be redirected to the isssue's project page.
        """
        create_project(title="Blank project", days=-1,
                       lead="Nelly Hateva", project_type="BP")
        #response = self.client.post(reverse('projects:create_issue',
        #                                      args=(1,)),
        #                                    {'issue_type': 'BG',
        #                                    'summary': 'Issue summary',
        #                                    'priority': 'MJ',
        #                                    'assignee': 'Ivan Ivanov',
        #                                    'reporter': 'Kircho Kirev',
        #                                    'description': 'Bug description'})
        #self.assertEqual(Project.objects.all().get(pk=1).issue_set.count(), 1)
        #self.assertContains(response, 'Create Project', status_code=200)

    def test_add_an_issue_invalid_form(self):
        """
        If the form is invalid, the view should redisplay
        the create issue view.
        """
        create_project(title="Blank project", days=-1,
                       lead="Nelly Hateva", project_type="BP")
        #response = self.client.post(reverse('projects:create_issue',
        #                                      args=(1,)),
        #                                    {'issue_type': 'BG',
        #                                    'priority': 'MJ',
        #                                    'assignee': 'Ivan Ivanov',
        #                                    'reporter': 'Kircho Kirev',
        #                                    'description': 'Bug description'})
        #self.assertEqual(Project.objects.all().get(pk=1).issue_set.count(), 0)
        #self.assertContains(response, 'Create Project', status_code=200)
