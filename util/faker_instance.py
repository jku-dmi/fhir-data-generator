from faker import Faker
from provider.address import AddressTypeProvider
from provider.condition.providers import ClinicalStatusProvider
from provider.document_reference.providers import DocStatusProvider, DocTypeProvider, \
    AttachmentContentTypeProvider, AttachmentUrlProvider, DocRefStatusProvider
from provider.encounter.providers import EncounterClassProvider, EncounterStatusProvider, \
    EncounterDiagnosisUseTypeProvider
from provider.episode_of_care.providers import EpisodeOfCareStatusProvider, EpisodeOfCareType
from provider.id_provider.document_id import DocIdProvider
from provider.medication.providers import SnowmedCodeProvider, MedicationStatusProvider, MedicationFormProvider, \
    QuantityValueProvider
from provider.medication_statement.providers import MedStatusProvider, MedCategoryProvider
from provider.oid import OidProvider
from provider.patient.gender import GenderProvider
from provider.patient.human_name import HumanNameUseProvider
from provider.location.providers import LocationPhysicalTypeProvider
from provider.patient.marital_status import MaritalStatusProvider
from provider.orga_type import OrganisationTypProvider
from provider.procedure.providers import ProcedureStatusProvider, ProcedureSnomedProvider
from provider.coding.icd10 import ICD10Provider
from provider.code_system_identfier_type_de_basis import codeSystemIdentifierTypeDeBasis

# Creating a faker instance
fake = Faker(['de'], use_weighting=False)

# Adding all the providers to the Fake instance to use them
providers = [
    AddressTypeProvider,
    GenderProvider,
    MaritalStatusProvider,
    OrganisationTypProvider,
    EpisodeOfCareStatusProvider,
    HumanNameUseProvider,
    EpisodeOfCareType,
    ClinicalStatusProvider,
    ICD10Provider,
    EncounterClassProvider,
    EncounterStatusProvider,
    LocationPhysicalTypeProvider,
    EncounterDiagnosisUseTypeProvider,
    DocRefStatusProvider,
    DocStatusProvider,
    DocTypeProvider,
    DocIdProvider,
    OidProvider,
    AttachmentContentTypeProvider,
    AttachmentUrlProvider,
    ProcedureStatusProvider,
    ProcedureSnomedProvider,
    MedStatusProvider,
    MedCategoryProvider,
    SnowmedCodeProvider,
    MedicationStatusProvider,
    MedicationFormProvider,
    QuantityValueProvider,
    codeSystemIdentifierTypeDeBasis
]

for p in providers:
    fake.add_provider(p)


# Function to add a dynamic provider from create_dynamic_provider to the Faker instance while the programm is running
def add_provider(provider):
    fake.add_provider(provider)
    return fake


# Function to get the Faker instance anywhere in the Programm
def get_faker() -> Faker:
    return fake
