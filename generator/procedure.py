import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.procedure as proc
import fhirclient.models.fhirreference as fr
import fhirclient.models.fhirdatetime as fdt
import fhirclient.models.meta as m
import fhirclient.models.patient as p
import fhirclient.models.encounter as e

from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_procedure() -> proc.Procedure:
    procedure = proc.Procedure()
    patient = fake.get_patient_id()
    encounter = fake.get_encounter_id()

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

    performed_date_time = fdt.FHIRDateTime()
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

    #res = procedure.create(smart.server)
    #return res['id']
    return procedure

def generate_procedure_with_set_references(patient: p.Patient | None, encounter: e.Encounter | None) -> proc.Procedure:
    procedure = proc.Procedure()
    if patient is None:
        patient = fake.get_patient_id()
    if encounter is None:
        encounter = fake.get_encounter_id()

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

    performed_date_time = fdt.FHIRDateTime()
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

    #res = procedure.create(smart.server)
    #return res['id']
    return procedure