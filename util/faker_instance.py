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

fake.add_provider(AddressTypeProvider,
                  GenderProvider,
                  MaritalStatusProvider,
                  TimeStampProvider,
                  OrganisationTypProvider,
                  EpisodeOfCareType,
                  ClinicalStatusProvider,
                  ICD10Provider,
                  EncounterClassProvider,
                  EpisodeOfCareStatusProvider,
                  HumanNameUseProvider,
                  ClinicalStatusProvider,
                  EncounterStatusProvider,
                  LocationPhysicalTypeProvider,
                  EncounterDiagnosisUseTypeProvider,
                  StatusProvider,
                  DocStatusProvider,
                  DocTypeProvider,
                  DocIdProvider,
                  TwoTimeStampsProvider,
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
                  QuantityValueProvider)


def add_provider(provider):
    fake.add_provider(provider)
    return fake


def get_faker() -> Faker:
    return fake
