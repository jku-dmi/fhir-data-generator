import fhirclient.models.medicationstatement as ms

import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr
import fhirclient.models.meta as m
import fhirclient.models.fhirdate as fd

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()


def generate_medication_statement(patient, encounter, medication):
    medication_statement = ms.MedicationStatement()

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

    effectiveDateTime = fd.FHIRDate()
    effectiveDateTime.dateTime = fake.date_time()
    medication_statement.effectiveDateTime = effectiveDateTime

    res = medication_statement.create(smart.server)
    return res['id']


