from django.contrib import admin


from import_export.admin import ImportExportModelAdmin
from deni_apps.models import CandidateDetails



# Register your models here.
@admin.register(CandidateDetails)
class CandidateDetailsAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/change_list.html'
    list_display = ['name', 'candiate_doj', 'candiate_email_id', 'hiring_manager', 'hiring_manager_email_id']
    search_fields = ('name', 'hiring_manager',)
