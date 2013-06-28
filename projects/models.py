from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    start_date = models.DateTimeField('date started',
                                      blank=False, auto_now_add=True)
    lead = models.CharField(max_length=50, blank=False)

    BUG_TRACKING = 'BUG_TRACKING'
    PROJECT_MANAGEMENT = 'PROJECT_MANAGEMENT'
    AGILE_KANBAN = 'AGILE_KANBAN'
    SOTWARE_DEVELOPMENT = 'SOTWARE_DEVELOPMENT'
    AGILE_SCRUM = 'AGILE_SCRUM'
    BLANK_PROJECT = 'BLANK_PROJECT'
    DEMO_PROJECT = 'DEMO_PROJECT'
    TYPE_OF_PROJECTS = (
        (BUG_TRACKING, 'Bug Tracking'),
        (PROJECT_MANAGEMENT, 'Project Management'),
        (AGILE_KANBAN, 'Agile Kanban'),
        (SOTWARE_DEVELOPMENT, 'Software Development'),
        (AGILE_SCRUM, 'Agile Scrum'),
        (BLANK_PROJECT, 'Blank Project'),
        (DEMO_PROJECT, 'Demo Project'),
    )
    project_type = models.CharField(max_length=19,
                            choices=TYPE_OF_PROJECTS,
                            default=BLANK_PROJECT)

    def __str__(self):
        return self.title


class Issue(models.Model):
    project = models.ForeignKey(Project)

    BUG = 'BUG'
    NEW_FEATURE = 'NEW_FEATURE'
    TASK = 'TASK'
    IMPROVEMENT = 'IMPROVEMENT'
    TYPE_OF_ISSUES = (
        (BUG, 'Bug'),
        (NEW_FEATURE, 'New feature'),
        (TASK, 'Task'),
        (IMPROVEMENT, 'Improvement'),
    )
    issue_type = models.CharField(max_length=11,
                                  choices=TYPE_OF_ISSUES,
                                  default=BUG)

    summary = models.CharField(max_length=100, blank=False)

    MAJOR = 'MAJOR'
    BLOCKER = 'BLOCKER'
    CRITICAL = 'CRITICAL'
    MINOR = 'MINOR'
    TRIVIAL = 'TRIVIAL'
    PRIORITY_TYPES = (
        (MAJOR, 'Major'),
        (BLOCKER, 'Blocker'),
        (CRITICAL, 'Critical'),
        (MINOR, 'Minor'),
        (TRIVIAL, 'Trivial'),
    )
    priority = models.CharField(max_length=8,
                            choices=PRIORITY_TYPES,
                            default=MAJOR)

    assignee = models.CharField(max_length=50, blank=False)
    reporter = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    due_date = models.DateField(auto_now_add=True)

    OPEN = 'OPEN'
    IN_PROGRESS = 'IN_PROGRESS'
    RESOLVED = 'RESOLVED'
    REOPENED = 'REOPENED'
    CLOSED = 'CLOSED'
    STATUS_TYPES = (
        (OPEN, 'Open'),
        (IN_PROGRESS, 'In progress'),
        (RESOLVED, 'Resolved'),
        (REOPENED, 'Reopened'),
        (CLOSED, 'Closed'),
    )
    status = models.CharField(max_length=11,
                              choices=STATUS_TYPES,
                              default=OPEN)
    comment = models.TextField()

    def __str__(self):
        return self.summary
