from django.contrib import admin
from .models import *

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class ReportResource(resources.ModelResource):

    member = fields.Field(
        column_name='member',
        attribute='member',
        widget=ForeignKeyWidget(Member, 'name'))
    
    class Meta:
        model = Report
        fields = ('member__id', 'member', 'time_spent', 'date_created')

class ExportReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource

class EventResource(resources.ModelResource):

    member = fields.Field(
        column_name='member',
        attribute='member',
        widget=ForeignKeyWidget(Member, 'name'))
    
    class Meta:
        model = Event
        fields = ('member__id', 'member', 'time', 'name')

class EventExportAdmin(ImportExportModelAdmin):
    resource_class = EventResource

admin.site.register(Member)

@admin.register(Report)
class ReportAdmin(ExportReportAdmin, admin.ModelAdmin):
    list_display = ['member', 'time_spent', 'date_created']
    list_filter = ['member']
    search_fields = ['member__name', 'time_spent']

@admin.register(Event)
class EventAdmin(EventExportAdmin, admin.ModelAdmin):
    list_display = ["id", 'member', 'name', 'time']
    list_filter = ['member__name']
