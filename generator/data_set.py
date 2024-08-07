import concurrent.futures
import json
import time
from typing import Callable

import requests
from fhirclient.models import bundle as bundle_model
from fhirclient.models.fhirabstractbase import FHIRValidationError

from exceptions.FHIRConnection import FHIRConnectionException
from generator import generate_condition, generate_procedure
from generator.document_reference import generate_document_reference
from generator.encounter import generate_encounter, add_condition_encounter
from generator.episode_of_care import generate_episode_of_care, add_condition_eoc
from generator.medication.medication_statement import generate_medication_statement
from generator.organization import generate_organization
from generator.patient import generate_patient
from generator.medication.medication import generate_medication
from helpers.create_dynamic_provider import create_dynamic_provider, bundle_response_to_provider
from helpers.faker_instance import getFaker
from helpers.fhir_client import get_client

fake = getFaker()


def send_bundle(bundle_: bundle_model.Bundle()) -> json:
    smart = get_client()
    try:
        res = requests.post(smart.server.base_uri, json=bundle_.as_json(),
                            headers={'Content-Type': 'application/fhir+json'})
        return json.dumps(res.json())
    except FHIRValidationError as e:
        print(f"FHIR Validation failed: {e}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - error: {e}")


def generate_organizations(n: int) -> json:
    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_org = {executor.submit(generate_organization): i for i in range(n)}
        for future in concurrent.futures.as_completed(future_to_org):
            try:
                org = future.result()
                res.append(org)
            except Exception as e:
                print(f"Organization generation failed with exception: {e}")

    bundle_entries = []
    for o in res:
        entry = bundle_model.BundleEntry()
        entry.resource = o
        request = bundle_model.BundleEntryRequest()
        request.method = "POST"
        request.url = "Organization"
        entry.request = request
        bundle_entries.append(entry)

    b = bundle_model.Bundle()
    b.type = "transaction"
    b.entry = bundle_entries

    res = send_bundle(b)
    return res


def generate_medications(n: int) -> json:
    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_org = {executor.submit(generate_medication): i for i in range(n)}
        for future in concurrent.futures.as_completed(future_to_org):
            try:
                org = future.result()
                res.append(org)
            except Exception as e:
                print(f"Medication generation failed with exception: {e}")

    bundle_entries = []
    for o in res:
        entry = bundle_model.BundleEntry()
        entry.resource = o
        request = bundle_model.BundleEntryRequest()
        request.method = "POST"
        request.url = "Medication"
        entry.request = request
        bundle_entries.append(entry)

    b = bundle_model.Bundle()
    b.type = "transaction"
    b.entry = bundle_entries

    return send_bundle(b)


def generate_patients(n: int) -> json:
    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_org = {executor.submit(generate_patient): i for i in range(n)}
        for future in concurrent.futures.as_completed(future_to_org):
            try:
                org = future.result()
                res.append(org)
            except Exception as e:
                print(f"Patient generation failed with exception: {e}")

    bundle_entries = []
    for o in res:
        entry = bundle_model.BundleEntry()
        entry.resource = o
        request = bundle_model.BundleEntryRequest()
        request.method = "POST"
        request.url = "Patient"
        entry.request = request
        bundle_entries.append(entry)

    b = bundle_model.Bundle()
    b.type = "transaction"
    b.entry = bundle_entries

    return send_bundle(b)


def generate_resources(function: Callable, resourceType: str, n: int) -> json:
    """
    Generate any number of fhir resources.
    :param function: Function who generates and returns one resource.
    :param resourceType: Resource name to put it as request url.
    :param n: Number of resources to generate.
    :return: Response of server.
    """

    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_org = {executor.submit(function): i for i in range(n)}
        for future in concurrent.futures.as_completed(future_to_org):
            try:
                org = future.result()
                res.append(org)
            except Exception as e:
                print(f"Resource generation failed with exception: {e}")

        bundle_entries = []
        for e in res:
            entry = bundle_model.BundleEntry()
            entry.resource = e
            request = bundle_model.BundleEntryRequest()
            request.method = "POST"
            request.url = resourceType
            entry.request = request
            bundle_entries.append(entry)

        b = bundle_model.Bundle()
        b.type = "transaction"
        b.entry = bundle_entries
    return send_bundle(b)


def generate_data_random_references(patient_count: int, medication_count: int, organization_count: int,
                                    encounter_count: int,
                                    episode_of_care_count: int, condition_count: int, document_reference_count: int,
                                    procedure_count: int,
                                    medication_statement_count: int, bundle_size: int = 1000) -> json:

    # generate Organizations
    print(f"Start generation of {organization_count} organizations")
    start_time = time.time()
    result = generate_resources(generate_organization, "Organization", organization_count)
    if result is not None:
        bundle_response_to_provider(result, "get_organization_id")
    else:
        raise FHIRConnectionException(
            "Resultset was None - check the response and the connection and restart the script.")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Organizations generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate medications
    print(f"Start generation of {medication_count} medications")
    start_time = time.time()
    medication_result = generate_resources(generate_medication, "Medication", medication_count)
    bundle_response_to_provider(medication_result, "get_medication_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Medications generated - elapsed time: {elapsed_time:.2f} seconds.")

    # Generate patients
    print(f"Start generation of {patient_count} patients")
    start_time = time.time()
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
    print(f"Patients generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate episode of cares
    print(f"Start generation of {episode_of_care_count} episode of cares")
    start_time = time.time()
    episode_of_care_result = generate_resources(generate_episode_of_care, "EpisodeOfCare", episode_of_care_count)
    bundle_response_to_provider(episode_of_care_result, "get_episode_of_care_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Episode of cares generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate encounter
    print(f"Start generation of {encounter_count} encouters")
    start_time = time.time()
    encounter_result = generate_resources(generate_encounter, "EpisodeOfCare", encounter_count)
    bundle_response_to_provider(encounter_result, "get_encounter_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Providers generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate provider
    print(f"Start generation of {document_reference_count} document references")
    start_time = time.time()
    document_reference_result = generate_resources(generate_document_reference, "DocumentReference",
                                                   document_reference_count)
    bundle_response_to_provider(document_reference_result, "get_document_reference_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Document references generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate condition
    print(f"Start generation of {condition_count} conditions")
    start_time = time.time()
    condition_result = generate_resources(generate_condition, "Condition", condition_count)
    bundle_response_to_provider(condition_result, "get_condition_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Providers generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate procedure
    print(f"Start generation of {procedure_count} procedures")
    start_time = time.time()
    procedure_result = generate_resources(generate_procedure, "Procedure", procedure_count)
    bundle_response_to_provider(procedure_result, "get_procedure_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Procedures generated - elapsed time: {elapsed_time:.2f} seconds.")

    # generate medication statements
    print(f"Start generation of {medication_statement_count} medication statements")
    start_time = time.time()
    medication_statement_result = generate_resources(generate_medication_statement, "MedicationStatement",
                                                     medication_statement_count)
    bundle_response_to_provider(medication_statement_result, "get_medication_statement_id")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Medication statements generated - elapsed time: {elapsed_time:.2f} seconds.")


def generate_data(count: int, resource: str, generator: Callable, provider_name: str, bundle_size: int = 1000):
    """
    generate fhir data
    :param count:
    :param resource:
    :param generator:
    :param provider_name:
    :param bundle_size:
    :return:
    """
    print(f"Start generation of {count} {resource} resources")
    start_time = time.time()
    reps, rest = divmod(count, bundle_size)
    result = []
    if reps > 0:
        for i in range(reps):
            result.append(generate_resources(generator, resource, bundle_size))
    # generate rest
    result.append(generate_resources(generate_patient, resource, rest))
    create_dynamic_provider(provider_name, result)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{resource}s generated - elapsed time: {elapsed_time:.2f} seconds.")


def generate_data_set_references(patient_count: int, medication_count: int, organization_count: int,
                                    encounter_count: int,
                                    episode_of_care_count: int, condition_count: int, document_reference_count: int,
                                    procedure_count: int,
                                    medication_statement_count: int, bundle_size: int = 1000):

    generate_data(organization_count, "Organization", generate_organization, "get_organization_id", bundle_size)
    generate_data(medication_count, "Medication", generate_medication, "get_medication_id", bundle_size)
    generate_data(patient_count, "Patient", generate_patient, "get_patient_id", bundle_size)
    generate_data(episode_of_care_count, "EpisodeOfCare", generate_episode_of_care, "get_episode_of_care_id", bundle_size)
    generate_data(encounter_count, "Encounter", generate_encounter, "get_encounter_id", bundle_size)
    generate_data(document_reference_count, "DocumentReference", generate_document_reference, "get_document_reference_id", bundle_size)
    generate_data(condition_count, "Condition", generate_condition, "get_condition_id", bundle_size)
    generate_data(procedure_count, "Procedure", generate_procedure, "get_procedure_id", bundle_size)
    generate_data(medication_statement_count, "MedicationStatement", generate_medication_statement, "get_medication_statement_id", bundle_size)
