import fhirclient.models.medicationstatement as ms
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr
import fhirclient.models.meta as m
import fhirclient.models.fhirdatetime as fdt
from util.faker_instance import get_faker
from datetime import datetime, timezone

fake = get_faker()


def generate_medication_statement() -> ms.MedicationStatement:
    medication_statement = ms.MedicationStatement()

    try:
        patient = fake.get_patient_id()
    except AttributeError:
        patient = None

    try:
        encounter = fake.get_encounter_id()
    except AttributeError:
        encounter = None

    try:
        medication = fake.get_medication_id()
    except AttributeError:
        medication = None

    meta = m.Meta()
    meta.profile = ["http://dmi.de/fhir/StructureDefinition/DaWiMedMedicationStatement"]
    medication_statement.meta = meta

    medication_statement.status = fake.med_status()

    category = cc.CodeableConcept()
    category_coding = cod.Coding()
    category_coding.system = "http://terminology.hl7.org/CodeSystem/medicationrequest-admin-location"
    category_coding.code = fake.med_category()
    category.coding = [category_coding]
    medication_statement.category = category

    medication_ref = fr.FHIRReference()
    medication_ref.reference = 'Medication/{}'.format(medication)
    medication_statement.medicationReference = medication_ref

    subject = fr.FHIRReference()
    subject.reference = 'Patient/{}'.format(patient)
    medication_statement.subject = subject

    context = fr.FHIRReference()
    context.reference = 'Encounter/{}'.format(encounter)
    medication_statement.context = context

    medication_statement.effectiveDateTime = fdt.FHIRDateTime(datetime.now(timezone.utc).isoformat())

    bd = fdt.FHIRDateTime()
    bd.date = fake.date_time_between(start_date='now', end_date='+1y')
    medication_statement.effectiveDateTime = bd

    return medication_statement
