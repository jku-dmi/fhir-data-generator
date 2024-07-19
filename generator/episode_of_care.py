import fhirclient.models.identifier as i
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.episodeofcare as eoc
import fhirclient.models.fhirreference as fr
from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()


def generate_episode_of_care(patient, organization):
    episode_of_care = eoc.EpisodeOfCare()
    patient_referenz = fr.FHIRReference()
    patient_referenz.reference = "Patient/{}".format(patient)
    episode_of_care.patient = patient_referenz

    identifier = i.Identifier()
    identifier.system = 'http://hospital.smarthealthit.org'
    identifier.value = '12345'
    identifier.use = 'usual'

    episode_of_care.identifier = [identifier]
    episode_of_care.status = fake.eoc_status()

    mo = fr.FHIRReference()
    mo.reference = 'Organization/' + organization
    episode_of_care.managingOrganization = mo

    type = cc.CodeableConcept()
    coding = cod.Coding()

    coding.system = 'http://hl7.org/fhir/ValueSet/episodeofcare-type'
    coding.code = fake.eoc_type()
    type.coding = [coding]
    episode_of_care.type = [type]




    res = episode_of_care.create(smart.server)
    return res['id']



def set_contition(episode_of_care, condition):

    con_ref = fr.FHIRReference()
    con_ref.reference = "Condition/{}".format(condition)
    episode_of_care.diagnosis.condition = con_ref