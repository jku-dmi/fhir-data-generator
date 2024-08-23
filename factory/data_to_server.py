import concurrent.futures
import datetime
import json
import time
from typing import Callable, List
from fhirclient.models import bundle as bundle_model
from generator import generate_condition, generate_procedure
from generator.document_reference import generate_document_reference
from generator.encounter import generate_encounter
from generator.episode_of_care import generate_episode_of_care
from generator.medication.medication_statement import generate_medication_statement
from generator.organization import generate_organization
from generator.patient import generate_patient
from generator.medication.medication import generate_medication
from util.create_dynamic_provider import bundle_response_list_to_provider
from util.util import send_bundle


def generate_resources_to_server(function: Callable, resource_type: str, n: int) -> json:
    """
    Generate any number of fhir resources.
    :param function: Function who generates and returns one resource.
    :param resource_type: Resource name to put it as request url.
    :param n: Number of resources to generate.
    :return: JSON response of server.
    """

    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_resource = {executor.submit(function): i for i in range(n)}
        for future in concurrent.futures.as_completed(future_to_resource):
            try:
                resource = future.result()
                res.append(resource)
            except Exception as e:
                print(f"Resource generation failed with exception: {e}")

        bundle_entries = []
        for e in res:
            entry = bundle_model.BundleEntry()
            entry.resource = e
            request = bundle_model.BundleEntryRequest()
            request.method = "POST"
            request.url = resource_type
            entry.request = request
            bundle_entries.append(entry)

        b = bundle_model.Bundle()
        b.type = "transaction"
        b.entry = bundle_entries

        return send_bundle(b)


def generate_data_to_server(count: int, resource_type: str, generator: Callable, provider_name: str,
                            bundle_size: int = 1000) -> List[int] | None:
    """
    generate fhir data
    :param count: number of resources to generate
    :param resource_type: resource type
    :param generator: Callable(method) that generates the data
    :param bundle_size: maximum number of resources to put into a bundle (default = 1000)
    :return: None
    """
    print(f"Start generation of {count} {resource_type} resources")
    start_time = time.time()
    reps, rest = divmod(count, bundle_size)
    result = []
    if reps > 0:
        for i in range(reps):
            result.append(generate_resources_to_server(generator, resource_type, bundle_size))
            print(f"Bundle {i} of {reps} generated; type = {resource_type}; current time =   {datetime.datetime.now()}")
    # generate rest
    if rest != 0:
        result.append(generate_resources_to_server(generator, resource_type, rest))

    end_time = time.time()
    elapsed_time = end_time - start_time
    bundle_response_list_to_provider(result, provider_name)
    print(f"{resource_type}s generated - elapsed time: {elapsed_time:.2f} seconds.")
    return result


def generate_data_random_references_to_server(patient_count: int, medication_count: int, organization_count: int,
                                              encounter_count: int,
                                              episode_of_care_count: int, condition_count: int,
                                              document_reference_count: int,
                                              procedure_count: int,
                                              medication_statement_count: int, bundle_size: int = 1000):
    generate_data_to_server(organization_count, "Organization", generate_organization,
                            "get_organization_id", bundle_size)
    generate_data_to_server(medication_count, "Medication", generate_medication, "get_medication_id",
                            bundle_size)
    generate_data_to_server(patient_count, "Patient", generate_patient, "get_patient_id",
                            bundle_size)
    generate_data_to_server(episode_of_care_count, "EpisodeOfCare", generate_episode_of_care,
                            "get_episode_of_care_id", bundle_size)
    generate_data_to_server(encounter_count, "Encounter", generate_encounter, "get_encounter_id",
                            bundle_size)
    generate_data_to_server(document_reference_count, "DocumentReference", generate_document_reference,
                            "get_document_reference_id", bundle_size)
    generate_data_to_server(condition_count, "Condition", generate_condition, "get_condition_id",
                            bundle_size)
    generate_data_to_server(procedure_count, "Procedure", generate_procedure, "get_procedure_id",
                            bundle_size)
    generate_data_to_server(medication_statement_count, "MedicationStatement", generate_medication_statement,
                            "get_medication_statement_id", bundle_size)


def generate_medications(n: int):
    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_resource = {executor.submit(generate_medication): i for i in range(n)}
        for future in concurrent.futures.as_completed(future_to_resource):
            try:
                resource = future.result()
                res.append(resource)
            except Exception as e:
                print(f"Resource generation failed with exception: {e}")

        bundle_entries = []
        for e in res:
            entry = bundle_model.BundleEntry()
            entry.resource = e
            request = bundle_model.BundleEntryRequest()
            request.method = "POST"
            request.url = "Medication"
            entry.request = request
            bundle_entries.append(entry)

        b = bundle_model.Bundle()
        b.type = "transaction"
        b.entry = bundle_entries

        return send_bundle(b)