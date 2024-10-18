import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


# Function to get the full CodeableConcept for the icd10 Code for the condition resource
def get_icd10_as_cc():
    codeable_concept = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = "http://fhir.de/CodeSystem/bfarm/icd-10-gm"
    coding.version = "2024"
    coding.code = fake.icd_10_code()
    codeable_concept.coding = [coding]
    return codeable_concept
