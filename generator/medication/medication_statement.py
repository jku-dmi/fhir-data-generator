import fhirclient.models.medicationstatement as ms

import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr
import fhirclient.models.meta as m
import fhirclient.models.fhirdatetime as fdt
import fhirclient.models.patient as p
import fhirclient.models.encounter as e
import fhirclient.models.medication as med

from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_medication_statement() -> ms.MedicationStatement:
    medication_statement = ms.MedicationStatement()
    patient = fake.get_patient_id()
    encounter = fake.get_encounter_id()
    medication = fake.get_medication_id()

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

    effective_date_time = fdt.FHIRDateTime()
    effective_date_time.dateTime = fake.date_time()
    medication_statement.effectiveDateTime = effective_date_time

    #res = medication_statement.create(smart.server)
    #return res['id']
    return medication_statement


def generate_medication_statement_with_set_references(patient: p.Patient | None, encounter: e.Encounter | None,
                                  medication: med.Medication | None) -> ms.MedicationStatement:
    medication_statement = ms.MedicationStatement()
    if patient is None:
        patient = fake.get_patient_id()
    if encounter is None:
        encounter = fake.get_encounter_id()
    if medication is None:
        medication = fake.get_medication_id()

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

    effective_date_time = fdt.FHIRDateTime()
    effective_date_time.dateTime = fake.date_time()
    medication_statement.effectiveDateTime = effective_date_time

    #res = medication_statement.create(smart.server)
    #return res['id']
    return medication_statement
