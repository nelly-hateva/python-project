from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField('date started')
    lead = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title
