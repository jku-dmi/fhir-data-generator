import fhirclient.models.patient as p
import fhirclient.models.fhirdate as fd
import fhirclient.models.meta as m
import fhirclient.models.identifier as i
import fhirclient.models.humanname as h
import fhirclient.models.address as a
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()

def generate_patient() -> int:
    patient = p.Patient()
    identifier = i.Identifier()

    identifier.system = 'http://hospital.smarthealthit.org'
    identifier.value = fake.numerify('############')
    identifier.use = 'usual'
    patient.identifier = [identifier]

    patient.meta = m.Meta()
    patient.meta.versionId = '1'
    patient.meta.lastUpdated = fd.FHIRDate(fake.timestamp())

    humanname = h.HumanName()
    humanname.use = fake.human_name_use()
    humanname.family = fake.last_name()
    humanname.given = [fake.first_name()]
    patient.name = [humanname]

    patient.active = True

    address = a.Address()
    address.type = fake.address_type()
    address.line = [fake.street_address()]
    address.city = fake.city()
    address.postalCode = fake.postcode()
    address.country = fake.country()
    patient.address = [address]

    patient.birthDate = fd.FHIRDate(fake.timestamp())
    patient.gender = fake.gender()

    marital_status = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = 'http://hl7.org/fhir/ValueSet/marital-status'
    coding.code = fake.marital_status()
    marital_status.coding = [coding]
    patient.maritalStatus = marital_status

    # Save the Patient resource to the FHIR server
    res = patient.create(smart.server)
    return res['id']
