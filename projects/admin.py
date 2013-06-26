from django.contrib import admin
from projects.models import Project, Issue


class IssueInline(admin.TabularInline):
    model = Issue
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['start_date'],
                                  'classes': ['collapse']}),
        (None,               {'fields': ['lead']}),
        (None,               {'fields': ['kind']}),
    ]
    inlines = [IssueInline]

    list_display = ('title', 'start_date', 'lead', 'kind')
    list_filter = ['start_date', 'kind', 'lead']
    search_fields = ['title', 'lead']
    date_hierarchy = 'start_date'

admin.site.register(Project, ProjectAdmin)
