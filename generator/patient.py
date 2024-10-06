import fhirclient
import fhirclient.models.patient as p
import fhirclient.models.fhirdate as fd
import fhirclient.models.meta as m
import fhirclient.models.identifier as i
import fhirclient.models.humanname as h
import fhirclient.models.address as a
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.fhirinstant as fi

from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_patient() -> p.Patient:
    patient = p.Patient()
    identifier = i.Identifier()

    identifier.system = 'http://hospital.smarthealthit.org'
    identifier.value = fake.numerify('############')
    identifier.use = 'usual'
    patient.identifier = [identifier]

    patient.meta = m.Meta()
    patient.meta.versionId = '1'
    fhir_instant = fi.FHIRInstant()
    fhir_instant.datetime = fake.date_time()
    patient.meta.lastUpdated = fhir_instant

    humanname = h.HumanName()
    humanname.use = fake.human_name_use()
    humanname.family = fake.last_name()
    humanname.given = [fake.first_name()]
    humanname.text = [humanname.given[0] + " " + humanname.family]
    patient.name = [humanname]

    patient.active = True

    address = a.Address()
    address.type = fake.address_type()
    address.line = [fake.street_address()]
    address.city = fake.city()
    address.postalCode = fake.postcode()
    address.country = fake.country()
    patient.address = [address]

    bd = fd.FHIRDate()
    bd.date = fake.date_time()
    patient.birthDate = bd
    patient.gender = fake.gender()

    marital_status = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = 'http://hl7.org/fhir/ValueSet/marital-status'
    coding.code = fake.marital_status()
    marital_status.coding = [coding]
    patient.maritalStatus = marital_status

    return patient
