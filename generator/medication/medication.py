import fhirclient.models.medicationstatement as ms

import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr
import fhirclient.models.medication as m
import fhirclient.models.identifier as i
import fhirclient.models.ratio as r
import fhirclient.models.quantity as q

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()


def generate_medication():
    medication = m.Medication()

    identifier = i.Identifier()
    identifier.value = fake.uuid4()
    medication.identifier = [identifier]

    code = cc.CodeableConcept()
    snowmed = cod.Coding()
    snowmed.system = "http://snomed.info/sct"
    snowmedcode = fake.medication_snowmed_code()
    snowmed.code = snowmedcode[0]
    snowmed.display = snowmedcode[1]
    code.coding = [snowmed]
    medication.code = code

    medication.status = fake.medication_status()
    organization = fake.get_organization_id()

    manufacurer = fr.FHIRReference()
    manufacurer.reference = "Organization/{}".format(organization)
    medication.manufacturer = manufacurer

    form = cc.CodeableConcept()
    form_code = cod.Coding()
    form_code.system = "http://snomed.info/sct"
    form_code_value = fake.medication_form()
    form_code.code = form_code_value[0]
    form_code.display = form_code_value[1]

    medication.form = form

    ratio = r.Ratio()
    numerator = q.Quantity()
    numerator.code = "mg"
    numerator.unit = "mg"
    numerator.system = "http://unitsofmeasure.org"
    numerator.value = fake.quantity_value()
    denominator = q.Quantity()
    denominator.value = fake.quantity_value()
    denominator.unit = "mg"
    denominator.system = "http://unitsofmeasure.org"
    denominator.code = "mg"
    ratio.numerator = numerator
    ratio.denominator = denominator

    medication.amount = ratio

    #res = medication.create(smart.server)
    #return res['id']
    return medication


