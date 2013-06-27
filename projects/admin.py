from django.contrib import admin
from projects.models import Project, Issue


class IssueInline(admin.TabularInline):
    model = Issue
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['lead']}),
        (None,               {'fields': ['project_type']}),
    ]
    inlines = [IssueInline]

    list_display = ('title', 'start_date', 'lead', 'project_type')
    list_filter = ['start_date', 'project_type', 'lead']
    search_fields = ['title', 'lead']
    date_hierarchy = 'start_date'

admin.site.register(Project, ProjectAdmin)
