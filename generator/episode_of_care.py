import random
import fhirclient.models.identifier as i
import fhirclient.models.codeableconcept as cc
import fhirclient.models.coding as cod
import fhirclient.models.episodeofcare as eoc
import fhirclient.models.fhirreference as fr
import fhirclient.models.period as p
import fhirclient.models.fhirdatetime as fdt
from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_episode_of_care() -> eoc.EpisodeOfCare:
    episode_of_care = eoc.EpisodeOfCare()

    patient = fake.get_patient_id()
    organization = fake.get_organization_id()

    patient_referenz = fr.FHIRReference()
    patient_referenz.reference = "Patient/{}".format(patient)
    episode_of_care.patient = patient_referenz

    episode_of_care.status = fake.eoc_status()

    mo = fr.FHIRReference()
    mo.reference = 'Organization/{}'.format(organization)
    episode_of_care.managingOrganization = mo

    identifier = i.Identifier()
    coding = cod.Coding()
    coding.system = 'http://hl7.org/fhir/ValueSet/episodeofcare-type'
    coding.code = fake.eoc_type()

    issuer = cod.Coding()
    issuer.system = "http://www.krankenhaus-oberstadt.de/sid/fallnr"
    issuer.code = fake.oid()

    coco = cc.CodeableConcept()
    coco.coding = [coding, issuer]

    identifier.type = coco

    identifier.value = fake.numerify('##########')

    episode_of_care.identifier = [identifier]

    period = p.Period()
    timestamp_tuple = fake.timestamps_two()
    start = fdt.FHIRDateTime()
    start.date = timestamp_tuple[0]
    period.start = start
    end = fdt.FHIRDateTime()
    end.date = timestamp_tuple[1]

    if(random.choice([True, False])):
        period.end = end

    episode_of_care.period = period

    return episode_of_care


def add_condition_episode_of_care(episode_of_care, condition) -> int:
    con_ref = fr.FHIRReference()
    con_ref.reference = "Condition/{}".format(condition)
    episode_of_care.diagnosis.condition = con_ref
    res = episode_of_care.update(smart.server)
    return res['id']
