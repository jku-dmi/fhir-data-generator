import fhirclient.models.location as l
import fhirclient.models.fhirreference as fr
import fhirclient.models.identifier as i
import fhirclient.models.coding as c
import fhirclient.models.codeableconcept as cc

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()


def generate_location(organization) -> int:
    location = l.Location()
    identifier = i.Identifier()

    identifier.system = 'http://dmi.de/fhir/sid/station/9998'
    identifier.value = fake.numerify("####")  #id
    identifier.use = 'usual'
    location.identifier = [identifier]

    location.name = fake.sentence()

    pt = c.Coding()
    pt.system = "https://simplifier.net/medizininformatikinitiative-modulstrukturdaten/sd_mii_struktur_location"
    pt.code = fake.physical_type()
    ptcc = cc.CodeableConcept()
    ptcc.coding = [pt]
    location.physicalType = ptcc

    org_ref = fr.FHIRReference()
    org_ref.reference = "Organization/{}".format(organization)
    location.managingOrganization = org_ref

    res = location.create(smart.server)
    return res['id']
