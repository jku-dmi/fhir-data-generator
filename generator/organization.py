import fhirclient.models.identifier as i
import fhirclient.models.address as a
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.organization as organization

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()


def generate_organizations(anzahl: int) -> []:
    ids = []

    for i in range(anzahl):
        ids.append(generate_orga())

    return ids


def generate_orga():
    orga = organization.Organization()

    identifier = i.Identifier()
    identifier.system = 'https://gematik.de/fhir/sid/telematik-id'
    identifier.value = fake.numerify('############')
    orga.identifier = [identifier]

    orga.active = True

    type = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = 'http://terminology.hl7.org/CodeSystem/organization-type'
    coding.code = fake.organisation_type()
    type.coding = [coding]
    orga.type = [type]

    orga.name = fake.company()

    orga.telecom = []

    address = a.Address()
    address.type = fake.address_type()
    address.line = [fake.street_address()]
    address.city = fake.city()
    address.postalCode = fake.postcode()
    address.country = fake.country()
    orga.address = [address]

    #res = orga.create(smart.server)
    #return res['id']
    return  orga
