from django.contrib import admin


from import_export.admin import ImportMixin
from deni_apps.models import CandidateDetails



# Register your models here.
@admin.register(CandidateDetails)
class CandidateDetailsAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['name', 'candiate_doj', 'candiate_email_id', 'hiring_manager', 'hiring_manager_email_id']
    search_fields = ('name', 'hiring_manager',)
