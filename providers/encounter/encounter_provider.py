# create new provider class
from faker.providers import DynamicProvider

EncounterClassProvider = DynamicProvider(
     provider_name="encounter_class",
     elements=["AMB", "IMP", "PRENC", "VR", "SS", "HH"],
)

EncounterStatusProvider = DynamicProvider(
     provider_name="encounter_status",
     elements=["planned", "in-progress", "onleave", "finished", "cancelled"],

)
EncounterDiagnosisUseTypeProvider = DynamicProvider(
     provider_name="diagnose_use_type",
     elements=["referral-diagnosis", "treatment-diagnosis"],
)
