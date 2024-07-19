from generator.encounter import generate_encounter, add_condition
from generator.episode_of_care import generate_episode_of_care
from generator.organization import generate_organizations, generate_orga
from generator.patient import generate_patient
from helpers.create_dynamic_provider import create_dynamic_provider
from generator.condition import generate_condition
from helpers.fhir_client import getClient


import fhirclient.models.encounter as enc


def main():
    print("Starting FHIR Tool")

    patient = generate_patient()
    print(patient)
    organization = generate_orga()
    print(organization)


    episode_of_care = generate_episode_of_care(patient, organization)
    print(episode_of_care)


    encounter = generate_encounter(patient, episode_of_care, organization)
    print(encounter)

    condition = generate_condition(patient, encounter)
    print(condition)
    add_condition(encounter, condition)




    #anzahl_orgas = 10
    #orga_ids = generate_organizations(anzahl_orgas)

    #create_dynamic_provider("organization_ids", orga_ids)

    #for i in orga_ids:
    #    print(i)


if __name__ == "__main__":
    main()
