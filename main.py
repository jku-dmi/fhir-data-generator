import json
import sys

import requests
from fhirclient.models import bundle

from generator import generate_patient, generate_episode_of_care, generate_encounter, generate_document_reference, \
    generate_condition, generate_procedure
from generator.data_set import send_bundle, generate_patients, \
    generate_organizations, generate_medications, generate_resources, generate_data_random_references, generate_data
from generator.medication.medication_statement import generate_medication_statement
from helpers.create_dynamic_provider import create_dynamic_provider, bundle_response_to_provider
from helpers.faker_instance import add_provider, getFaker
import time

from helpers.fhir_client import get_client
from helpers.util import split


def main():
    #res = requests.get("http://localhost:8080/fhir/Patient?_summary=count", headers={'Content-Type': 'application/fhir+json'})
    #print(f"number of patients: {res.json().get('total')}")
    #print("Starting the data generation")
    # generate_data_random_references(patient_count=10000, medication_count=1500, organization_count=1500, encounter_count=20000, episode_of_care_count=20000, procedure_count=25000, document_reference_count=20000, medication_statement_count=15000, condition_count=10000)
    start_time = time.time()
    patient_count = 1234
    bundle_size = 1000
    reps, rest = divmod(patient_count, bundle_size)
    result = []

    if reps > 0:
        for i in range(reps):
            result.append(generate_resources(generate_patient, "Patient", bundle_size))
    # regerate rest
    result.append(generate_resources(generate_patient, "Patient", rest))
    create_dynamic_provider("get_patient_id", result)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Patient with generate resource - bundle_size = {bundle_size} ; {elapsed_time:.2f} Sekunden.")

    print("VERSUS\n")

    generate_data(count=1234, resource="Patient", generator=generate_patient, provider_name="get_patient_id")
    #res = requests.get("http://localhost:8080/fhir/Patient?_summary=count", headers={'Content-Type': 'application/fhir+json'})
    #print(f"number of patients: {res.json().get('total')}")
    """
    patient = generate_patient()
    print(patient)
    organization = '8852'  # generate_orga()
    print(organization)
    episode_of_care = generate_episode_of_care(patient, organization)
    print(episode_of_care)
    encounter = generate_encounter(patient, episode_of_care, organization)
    print(encounter)
    document_reference = generate_document_reference(patient, encounter)
    print(document_reference)
    procedure = generate_procedure(patient, encounter)
    print(procedure)
    
    organization = '8852'
    medication = generate_medication(organization)
    print(medication)

    patient = '2'
    encounter = '9006'
    med_ref = generate_medication_statement(patient, encounter, medication)
    print(med_ref)
    """
    #condition = generate_condition(patient, encounter)
    #print(condition)
    #add_condition(encounter, condition)

    '''
    anzahl_orgas = 10
    res = []
    for n in range(anzahl_orgas):
        res.append(generate_orga())

    bundle_entries = []
    for o in res:
        entry = bundle.BundleEntry()
        entry.resource = o
        request = bundle.BundleEntryRequest()
        request.method = "POST"
        request.url = "Organization"
        entry.request = request
        bundle_entries.append(entry)

    b = bundle.Bundle()
    b.type = "transaction"
    b.entry = bundle_entries

    print(bundle)

    smart = getClient()
    try:
        # res = b.create(smart.server)
        res = requests.post(smart.server.base_uri, json=b.as_json(), headers={'Content-Type': 'application/fhir+json'})
        print(f"Response: {res}")
    except FHIRValidationError as e:
        print(f"FHIR Validation Error: {e}")

    '''

    #for i in orga_ids:
    #    print(i)

    #fake = getFaker()
    #o = fake.organization_id()

    #print(o)
    """
    start_time = time.time()
    result = generate_organizations(100)
    if result is not None:
        bundle_response_to_provider(result, "get_organization_id")
    else:
        raise Exception("Es konnten keine Organisationen zum FHIR-Server gesendet werden. Bitte überprüfe die "
                        "Verbindung und starte das Skript erneut.")
        sys.exit(0)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Organization - bundle_size = 100 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    medication_result = generate_medications(500)
    if medication_result is not None:
        bundle_response_to_provider(medication_result, "get_medication_id")
    else:
        print(
            "Es konnten keine Medikamente zum FHIR-Server gesendet werden. Bitte überprüfe die Verbindung und starte "
            "das Skript erneut.")
        sys.exit(0)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Medication - bundle_size = 500 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    patient_result = generate_patients(1000)
    bundle_response_to_provider(patient_result, "get_patient_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Patient - bundle_size = 1000 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    patient_result1 = generate_resources(generate_patient, "Patient", 1000)
    bundle_response_to_provider(patient_result1, "get_patient_id1")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Patient with generate resource - bundle_size = 1000 {elapsed_time:.2f} Sekunden.")
"""

    """
    start_time = time.time()
    episode_of_care_result = generate_resources(generate_episode_of_care, "EpisodeOfCare", 1000)
    bundle_response_to_provider(episode_of_care_result, "get_episode_of_care_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Episode of care - bundle_size = 100 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    encounter_result = generate_resources(generate_encounter, "EpisodeOfCare", 1000)
    bundle_response_to_provider(encounter_result, "get_encounter_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Provider - bundle_size = 50 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    document_reference_result = generate_resources(generate_document_reference, "DocumentReference", 1000)
    bundle_response_to_provider(document_reference_result, "get_document_reference_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Document Reference- bundle_size = 25 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    condition_result = generate_resources(generate_condition, "Condition", 1000)
    bundle_response_to_provider(condition_result, "get_condition_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Provider - bundle_size = 200 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    procedure_result = generate_resources(generate_procedure, "Procedure", 1000)
    bundle_response_to_provider(procedure_result, "get_procedure_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Procedure- bundle_size = 150 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    medication_statement_result = generate_resources(generate_medication_statement, "MedicationStatement", 1000)
    bundle_response_to_provider(medication_statement_result, "get_medication_statement_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Medication Statement- bundle_size = 75 {elapsed_time:.2f} Sekunden.")

    """


if __name__ == "__main__":
    main()
