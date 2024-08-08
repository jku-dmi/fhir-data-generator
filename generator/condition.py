import fhirclient.models.condition as c
import fhirclient.models.fhirdatetime as fdt
import fhirclient.models.fhirinstant as fi
import fhirclient.models.meta as m
import fhirclient.models.identifier as i
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr

from util.fhir_client import get_client
from util.faker_instance import get_faker
from util.coding.icd10 import get_icd10_as_cc

smart = get_client()
fake = get_faker()


def generate_condition() -> c.Condition:
    condition = c.Condition()
    patient = fake.get_patient_id()
    encounter = fake.get_encounter_id()

    identifier = i.Identifier()

    identifier.system = 'http://hospital.smarthealthit.org'
    identifier.value = fake.numerify('############')
    identifier.use = 'usual'
    condition.identifier = [identifier]

    meta = m.Meta()
    meta.profile = ["http://dmi.de/fhir/StructureDefinition/DaWiMedCondition"]
    last_updated = fi.FHIRInstant()
    last_updated.datetime = fake.date_time()
    meta.lastUpdated = last_updated
    condition.meta = meta

    clinical_status = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = "http://terminology.hl7.org/CodeSystem/condition-clinical"
    coding.code = fake.clinical_status()
    clinical_status.coding = [coding]
    condition.clinicalStatus = clinical_status

    code = get_icd10_as_cc()
    condition.code = code

    sub_ref = fr.FHIRReference()
    sub_ref.reference = "Patient/{}".format(patient)
    condition.subject = sub_ref

    enc_ref = fr.FHIRReference()
    enc_ref.reference = "Encounter/{}".format(encounter)
    condition.encounter = enc_ref

    recorded_date = fdt.FHIRDateTime()
    recorded_date.date = fake.date_time()
    condition.recordedDate = recorded_date

    #res = condition.create(smart.server)
    #return res['id']
    return condition
