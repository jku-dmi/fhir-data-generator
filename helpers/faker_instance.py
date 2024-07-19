from faker import Faker

from providers.address import AddressTypeProvider
from providers.condition.clinical_status import ClinicalStatusProvider
from providers.encounter.encounter_provider import EncounterClassProvider, EncounterStatusProvider, \
    EncounterDiagnosisUseTypeProvider
from providers.eoc_status import EpisodeOfCareStatusProvider
from providers.episode_of_care_type import EpisodeOfCareType
from providers.gender import GenderProvider
from providers.human_name import HumanNameUseProvider
from providers.location.location_provider import LocationPhysicalTypeProvider
from providers.marital_status import MaritalStatusProvider
from providers.orga_type import OrganisationTypProvider
from providers.timestamp import TimeStampProvider
from providers.coding.icd10 import ICD10Provider

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

def add_provider(provider):
    fake.add_provider(provider)
    return fake

def getFaker() -> Faker:
    return fake