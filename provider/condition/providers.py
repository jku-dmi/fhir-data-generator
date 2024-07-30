# create new provider class
from faker.providers import DynamicProvider

ClinicalStatusProvider = DynamicProvider(
     provider_name="clinical_status",
     elements=["active", "recurrence", "relapse", "inactive", "remission", "resolved"],
)
