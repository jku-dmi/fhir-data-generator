import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.procedure as proc
import fhirclient.models.fhirreference as fr
import fhirclient.models.fhirdate as fd
import fhirclient.models.meta as m

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()


def generate_procedure(patient, encounter):
    procedure = proc.Procedure()

    meta = m.Meta()
    meta.profile = ["http://dmi.de/fhir/StructureDefinition/DaWiMedProzedur"]
    procedure.meta = meta

    procedure.status = fake.proc_status()

    patient_reference = fr.FHIRReference()
    patient_reference.reference = "Patient/{}".format(patient)
    procedure.subject = patient_reference


    encounter_reference = fr.FHIRReference()
    encounter_reference.reference = 'Encounter/{}'.format(encounter)
    procedure.encounter = encounter_reference

    performed_date_time = fd.FHIRDate()
    performed_date_time.date = fake.date_time()
    procedure.performedDateTime = performed_date_time


    code = cc.CodeableConcept()

    coding1 = cod.Coding()
    coding1.system = "http://snomed.info/sct"
    snomed = fake.proc_snomed()
    coding1.code = snomed[0]
    coding1.display = snomed[1]

    code.coding = [coding1]

    procedure.code = code

    res = procedure.create(smart.server)
    return res['id']
