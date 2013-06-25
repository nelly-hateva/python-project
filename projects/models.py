from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField('date started')
    lead = models.CharField(max_length=50)

    BUG_TRACKING = 'BT'
    PROJECT_MANAGEMENT = 'PM'
    AGILE_KANBAN = 'AK'
    SOTWARE_DEVELOPMENT = 'SD'
    AGILE_SCRUM = 'AS'
    BLANK_PROJECT = 'BP'
    TYPE_OF_PROJECTS_CHOICES = (
        (BUG_TRACKING, 'Bug Tracking'),
        (PROJECT_MANAGEMENT, 'Project Management'),
        (AGILE_KANBAN, 'Agile Kanban'),
        (SOTWARE_DEVELOPMENT, 'Software Development'),
        (AGILE_SCRUM, 'Agile Scrum'),
        (BLANK_PROJECT, 'Blank Project'),
    )
    kind = models.CharField(max_length=2,
                             choices=TYPE_OF_PROJECTS_CHOICES,
                             default=BLANK_PROJECT)

    def __str__(self):
        return self.title
