import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
from helpers.fhir_client import get_client
from helpers.faker_instance import getFaker

smart = get_client()
fake = getFaker()




def get_icd10_as_cc():
    codeableconcept = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = "http://fhir.de/CodeSystem/bfarm/icd-10-gm"
    coding.version = "2024"
    coding.code = fake.icd_10_code()
    codeableconcept.coding = [coding]
    return codeableconcept

