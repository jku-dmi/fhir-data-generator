from faker import Faker

from provider.address import AddressTypeProvider
from provider.condition.providers import ClinicalStatusProvider
from provider.document_reference.providers import StatusProvider, DocStatusProvider, DocTypeProvider, \
    AttachmentContentTypeProvider, AttachmentUrlProvider
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
from provider.timestamp import TimeStampProvider, TwoTimeStampsProvider
from provider.coding.icd10 import ICD10Provider

fake = Faker(['de'], use_weighting=False)

fake.add_provider(AddressTypeProvider)
fake.add_provider(GenderProvider)
fake.add_provider(MaritalStatusProvider)
fake.add_provider(TimeStampProvider)
fake.add_provider(OrganisationTypProvider)
fake.add_provider(EpisodeOfCareStatusProvider)
fake.add_provider(MaritalStatusProvider)
fake.add_provider(HumanNameUseProvider)
fake.add_provider(EpisodeOfCareType)
fake.add_provider(ClinicalStatusProvider)
fake.add_provider(ICD10Provider)
fake.add_provider(EncounterClassProvider)
fake.add_provider(EncounterStatusProvider)
fake.add_provider(LocationPhysicalTypeProvider)
fake.add_provider(EncounterDiagnosisUseTypeProvider)
fake.add_provider(StatusProvider)
fake.add_provider(DocStatusProvider)
fake.add_provider(DocTypeProvider)
fake.add_provider(DocIdProvider)
fake.add_provider(TwoTimeStampsProvider)
fake.add_provider(OidProvider)
fake.add_provider(AttachmentContentTypeProvider)
fake.add_provider(AttachmentUrlProvider)
fake.add_provider(ProcedureStatusProvider)
fake.add_provider(ProcedureSnomedProvider)
fake.add_provider(MedStatusProvider)
fake.add_provider(MedCategoryProvider)
fake.add_provider(SnowmedCodeProvider)
fake.add_provider(MedicationStatusProvider)
fake.add_provider(MedicationFormProvider)
fake.add_provider(QuantityValueProvider)



def add_provider(provider):
    fake.add_provider(provider)
    return fake

def getFaker() -> Faker:
    return fake