from django.test import TestCase

from django.core.urlresolvers import reverse


class ProjectsViewTests(TestCase):
    def test_index_view_with_no_projects(self):
        """
        If no projects exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('projects:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects available yet.")
        self.assertQuerysetEqual(response.context['projects_list'], [])
