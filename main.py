import json

from fhirclient.models import bundle

from generator import generate_patient, generate_episode_of_care, generate_encounter, generate_document_reference, \
    generate_condition, generate_procedure
from generator.data_set import send_bundle, generate_patients, \
    generate_organizations, generate_medications, generate_resources
from generator.medication.medication_statement import generate_medication_statement
from helpers.create_dynamic_provider import create_dynamic_provider, bundle_response_to_provider
from helpers.faker_instance import add_provider, getFaker
import time


def main():
    print("Starting the data generation")
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
    start_time = time.time()
    result = generate_organizations(100)
    bundle_response_to_provider(result, "get_organization_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Organization - bundle_size = 100 {elapsed_time:.2f} Sekunden.")

    start_time = time.time()
    medication_result = generate_medications(500)
    bundle_response_to_provider(medication_result, "get_medication_id")
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
