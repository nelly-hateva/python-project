from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    start_date = models.DateTimeField('date started')
    lead = models.CharField(max_length=50, blank=False)

    BUG_TRACKING = 'BT'
    PROJECT_MANAGEMENT = 'PM'
    AGILE_KANBAN = 'AK'
    SOTWARE_DEVELOPMENT = 'SD'
    AGILE_SCRUM = 'AS'
    BLANK_PROJECT = 'BP'
    DEMO_PROJECT = 'DP'
    TYPE_OF_PROJECTS = (
        (BUG_TRACKING, 'Bug Tracking'),
        (PROJECT_MANAGEMENT, 'Project Management'),
        (AGILE_KANBAN, 'Agile Kanban'),
        (SOTWARE_DEVELOPMENT, 'Software Development'),
        (AGILE_SCRUM, 'Agile Scrum'),
        (BLANK_PROJECT, 'Blank Project'),
        (DEMO_PROJECT, 'Demo Project'),
    )
    kind = models.CharField(max_length=2,
                            choices=TYPE_OF_PROJECTS,
                            default=BLANK_PROJECT)

    def __str__(self):
        return self.title


class Issue(models.Model):
    project = models.ForeignKey(Project)

    BUG = 'BG'
    NEW_FEATURE = 'NF'
    TASK = 'TS'
    IMPROVEMENT = 'IM'
    TYPE_OF_ISSUES = (
        (BUG, 'Bug'),
        (NEW_FEATURE, 'New feature'),
        (TASK, 'Task'),
        (IMPROVEMENT, 'Improvement'),
    )
    issue_type = models.CharField(max_length=2,
                                  choices=TYPE_OF_ISSUES,
                                  default=BUG)

    summary = models.CharField(max_length=100, blank=False)

    MAJOR = 'MJ'
    BLOCKER = 'BL'
    CRITICAL = 'CR'
    MINOR = 'MN'
    TRIVIAL = 'TR'
    PRIORITY_TYPES = (
        (MAJOR, 'Major'),
        (BLOCKER, 'Blocker'),
        (CRITICAL, 'Critical'),
        (MINOR, 'Minor'),
        (TRIVIAL, 'TR'),
    )
    priority = models.CharField(max_length=2,
                            choices=PRIORITY_TYPES,
                            default=MAJOR)

    assignee = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    due_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.summary
