import fhirclient.models.encounter as enc
import fhirclient.models.fhirdatetime as fdt
import fhirclient.models.identifier as i
import fhirclient.models.period as per
import fhirclient.models.coding as cod
import fhirclient.models.codeableconcept as cc
import fhirclient.models.fhirreference as fr
import fhirclient.models.patient as p
import fhirclient.models.organization as o
import fhirclient.models.episodeofcare as eoc

from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_encounter() -> enc.Encounter:
    encounter = enc.Encounter()
    patient = fake.get_patient_id()
    episode_of_care = fake.get_episode_of_care_id()
    organization = fake.get_organization_id()

    encounter.active = True

    sub_ref = fr.FHIRReference()
    sub_ref.reference = "Patient/{}".format(patient)
    encounter.subject = sub_ref

    eoc_ref = fr.FHIRReference()
    eoc_ref.reference = "EpisodeOfCare/{}".format(episode_of_care)
    encounter.episodeOfCare = [eoc_ref]

    identifier = i.Identifier()

    coding = cod.Coding()
    coding.system = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    coding.code = 'VN'

    issuer = cod.Coding()
    issuer.system = "http://www.krankenhaus-oberstadt.de/sid/fallnr"
    issuer.code = "VN"

    identifier.coding = [coding, issuer]
    identifier.value = fake.numerify('###########')  #IsiK Aufnahmenummer
    encounter.identifier = [identifier]

    enc_class = cod.Coding()

    enc_class.system = "http://fhir.de/ValueSet/EncounterClassDE"
    enc_class.value = fake.encounter_class()

    encounter.class_fhir = enc_class

    encounter.status = fake.encounter_status()

    p = per.Period()

    start = fdt.FHIRDateTime()
    start.date = fake.date_time()
    end = fdt.FHIRDateTime()
    end.date = fake.date_time()
    p.start = start
    p.end = end
    encounter.period = p

    organization_ref = fr.FHIRReference()
    organization_ref.reference = "Organization/{}".format(organization)
    encounter.serviceProvider = organization_ref

    #res = encounter.create(smart.server)
    #return res['id']
    return encounter

def generate_encounter_with_set_references(patient: p.Patient | None, episode_of_care: eoc.EpisodeOfCare | None,
                       organization: o.Organization | None) -> enc.Encounter:
    encounter = enc.Encounter()
    if patient is None:
        patient = fake.get_patient_id()
    if episode_of_care is None:
        episode_of_care = fake.get_episode_of_care_id()
    if organization is None:
        organization = fake.get_organization_id()

    encounter.active = True

    sub_ref = fr.FHIRReference()
    sub_ref.reference = "Patient/{}".format(patient)
    encounter.subject = sub_ref

    eoc_ref = fr.FHIRReference()
    eoc_ref.reference = "EpisodeOfCare/{}".format(episode_of_care)
    encounter.episodeOfCare = [eoc_ref]

    identifier = i.Identifier()

    coding = cod.Coding()
    coding.system = 'http://terminology.hl7.org/CodeSystem/v2-0203'
    coding.code = 'VN'

    issuer = cod.Coding()
    issuer.system = "http://www.krankenhaus-oberstadt.de/sid/fallnr"
    issuer.code = "VN"

    identifier.coding = [coding, issuer]
    identifier.value = fake.numerify('###########')  #IsiK Aufnahmenummer
    encounter.identifier = [identifier]

    enc_class = cod.Coding()

    enc_class.system = "http://fhir.de/ValueSet/EncounterClassDE"
    enc_class.value = fake.encounter_class()

    encounter.class_fhir = enc_class

    encounter.status = fake.encounter_status()

    p = per.Period()

    start = fdt.FHIRDateTime()
    start.date = fake.date_time()
    end = fdt.FHIRDateTime()
    end.date = fake.date_time()
    p.start = start
    p.end = end
    encounter.period = p

    organization_ref = fr.FHIRReference()
    organization_ref.reference = "Organization/{}".format(organization)
    encounter.serviceProvider = organization_ref

    #res = encounter.create(smart.server)
    #return res['id']
    return encounter


def add_condition_encounter(encounter, condition):
    e = enc.Encounter.read(encounter, smart.server)
    encounter_diagnosis = enc.EncounterDiagnosis()

    use_coding = cod.Coding()
    use_coding.system = "http://fhir.de/ValueSet/DiagnoseTyp"
    use_coding.code = fake.diagnose_use_type()
    dia_cc = cc.CodeableConcept()
    dia_cc.coding = [use_coding]
    encounter_diagnosis.use = dia_cc

    condition_ref = fr.FHIRReference()
    condition_ref.reference = "Condition/{}".format(condition)
    encounter_diagnosis.condition = condition_ref
    e.diagnosis = [encounter_diagnosis]
    e.update(smart.server)
