import fhirclient.models.identifier as i
import fhirclient.models.address as a
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.organization as o
from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_organization() -> o.Organization:
    organization = o.Organization()

    identifier = i.Identifier()
    identifier.system = 'https://gematik.de/fhir/sid/telematik-id'
    identifier.value = fake.numerify('############')
    organization.identifier = [identifier]

    organization.active = True

    organization_type = cc.CodeableConcept()
    coding = cod.Coding()
    coding.system = 'http://terminology.hl7.org/CodeSystem/organization-type'
    coding.code = fake.organisation_type()
    organization_type.coding = [coding]
    organization.type = [organization_type]

    organization.name = fake.company()

    address = a.Address()
    address.type = fake.address_type()
    address.line = [fake.street_address()]
    address.city = fake.city()
    address.postalCode = fake.postcode()
    address.country = fake.country()
    organization.address = [address]

    return organization
