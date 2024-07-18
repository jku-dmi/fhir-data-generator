import fhirclient
import fhirclient.models.patient as p
import fhirclient.models.composition as c
import fhirclient.models.fhirdate as fd
import fhirclient.models.meta as m
import fhirclient.models.identifier as i
import fhirclient.models.humanname as h
import fhirclient.models.address as a
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod

from faker import Faker


from fhirclient import client

from providers.address import AddressTypeProvider
from providers.gender import GenderProvider
from providers.human_name import HumanNameUseProvider
from providers.marital_status import MaritalStatusProvider
from providers.timestamp import TimeStampProvider

settings = {
    'app_id': 'fhir_server',
    'api_base': 'http://localhost:8080/fhir/'
}

smart = client.FHIRClient(settings=settings)

fake = Faker(['de'], use_weighting=False)

fake.add_provider(AddressTypeProvider)
fake.add_provider(GenderProvider)
fake.add_provider(MaritalStatusProvider)
fake.add_provider(TimeStampProvider)
fake.add_provider(HumanNameUseProvider)



# Create a new Patient resource
patient = p.Patient()
identifier = i.Identifier()
identifier.system = 'http://hospital.smarthealthit.org'
identifier.value = '12345'
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


#address = a.Address()
#address.type = fake.address_type()
#address.line = fake.street_address()
#address.city = fake.city()
#address.postalCode = fake.postcode()
#address.country = fake.country()
#patient.address = address


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
patient_id = res['id']

print(f'Patient created with ID: {patient_id}')

# Create a new Composition (Document) resource
composition = c.Composition()
composition.id = 'example-composition'
composition.meta = m.Meta()
composition.meta.versionId = '1'
composition.meta.lastUpdated = fd.FHIRDate('2024-07-18T12:00:00Z')
composition.text = c.Narrative({'status': 'generated', 'div': '<div>A human-readable rendering of the document</div>'})
composition.status = 'final'
composition.type = c.CodeableConcept({'coding': [{'system': 'http://loinc.org', 'code': '34133-9', 'display': 'Summarization of Episode Note'}]})
composition.subject = {'reference': f'Patient/{patient.id}'}
composition.date = fd.FHIRDate('2024-07-18T12:00:00Z')
composition.title = 'Example Document'

# Save the Composition resource to the FHIR server
composition.create(smart.server)
print(f'Document created with ID: {composition.id}')