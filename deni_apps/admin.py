from django.contrib import admin


from import_export.admin import ImportMixin
from deni_apps.models import CandidateDetails



# Register your models here.
@admin.register(CandidateDetails)
class CandidateDetailsAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ['name', 'email_sent_date', 'offer_accepted_date', 'candiate_doj', 'candiate_email_id', 'hiring_manager', 'hiring_manager_email_id', 'create_date', 'update_date']
    search_fields = ('name', 'hiring_manager',)
    # history_list_display = ['display_changes']

    # def display_changes(self, obj):
    #     changes = []
    #     for field in obj.history.latest().changes:
    #         old_value = field.old
    #         new_value = field.new
    #         if old_value == '' and new_value is None:
    #             # ignore empty string -> None changes
    #             continue
    #         changes.append(f"{field.field}: {old_value} -> {new_value}")
    #     return ', '.join(changes)

    # display_changes.short_description = 'Changes'

