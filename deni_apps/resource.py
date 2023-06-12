from import_export import resources
from deni_apps.models import CandidateDetails


class CandidateDetailsResource(resources.ModelResource):
    class Meta:
        model = CandidateDetails