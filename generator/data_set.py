import concurrent.futures
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
from util.create_dynamic_provider import create_dynamic_provider
from util.faker_instance import get_faker
from util.fhir_client import get_client
from util.util import send_bundle, save_bundle

fake = get_faker()
smart = get_client()


def generate_resources(function: Callable, resource_type: str, n: int, destination: str | None) -> json:
    """
    Generate any number of fhir resources.
    :param destination: if set write to file, otherwise send resource directly to the server
    :param function: Function who generates and returns one resource.
    :param resource_type: Resource name to put it as request url.
    :param n: Number of resources to generate.
    :return: Response of server.
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

    if destination:
        return (
            save_bundle(b, destination))
    else:
        return send_bundle(b)


def generate_data(count: int, resource_type: str, generator: Callable, provider_name: str | None,
                  destination: str | None, bundle_size: int = 1000) -> List[int] | None:
    """
    generate fhir data
    :param count: number of resources to generate
    :param resource_type: resource type
    :param generator: Callable(method) that generates the data
    :param provider_name: If set - create a dynamic Faker provider to return the id of a random resource from the generated set
    :param destination: None = send data to FHIR Server, "*" = save data in file with the given name
    :param bundle_size: maximum number of resources to put into a bundle (default = 1000)
    :return: None
    """
    print(f"Start generation of {count} {resource_type} resources")
    start_time = time.time()
    reps, rest = divmod(count, bundle_size)
    result = []
    if destination is None:
        if reps > 0:
            for i in range(reps):
                result.append(generate_resources(generator, resource_type, bundle_size, destination))
        # generate rest
        if rest != 0:
            result.append(generate_resources(generate_patient, resource_type, rest, destination))

    if destination is not None:
        if reps > 0:
            for i in range(reps):
                result.append(generate_resources(generator, resource_type, bundle_size, destination))
        # generate rest if needed
        if rest != 0:
            result.append(generate_resources(generate_patient, resource_type, rest, destination))

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{resource_type}s generated - elapsed time: {elapsed_time:.2f} seconds.")
    if provider_name is not None and destination is not None:
        print(f"RESULT: {result}")
        create_dynamic_provider(provider_name, result)
        return None
    else:
        return result


def generate_data_random_references(patient_count: int, medication_count: int, organization_count: int,
                                    encounter_count: int,
                                    episode_of_care_count: int, condition_count: int, document_reference_count: int,
                                    procedure_count: int,
                                    medication_statement_count: int, write_to_file: bool, bundle_size: int = 1000):
    if write_to_file:
        generate_data(organization_count, "Organization", generate_organization,
                      "get_organization_id", "organization.json", bundle_size)
        generate_data(medication_count, "Medication", generate_medication, "get_medication_id",
                      "medication.json", bundle_size)
        generate_data(patient_count, "Patient", generate_patient, "get_patient_id",
                      "patient.json", bundle_size)
        generate_data(episode_of_care_count, "EpisodeOfCare", generate_episode_of_care,
                      "get_episode_of_care_id", "episode_of_care.json", bundle_size)
        generate_data(encounter_count, "Encounter", generate_encounter, "get_encounter_id",
                      "encounter.json", bundle_size)
        generate_data(document_reference_count, "DocumentReference", generate_document_reference,
                      "get_document_reference_id", "document_reference.json", bundle_size)
        generate_data(condition_count, "Condition", generate_condition, "get_condition_id",
                      "condition.json", bundle_size)
        generate_data(procedure_count, "Procedure", generate_procedure, "get_procedure_id",
                      "procedure.json", bundle_size)
        generate_data(medication_statement_count, "MedicationStatement", generate_medication_statement,
                      "get_medication_statement_id", "medication_statement.json", bundle_size)

    if not write_to_file:
        destination = None
        generate_data(organization_count, "Organization", generate_organization,
                      "get_organization_id", destination, bundle_size)
        generate_data(medication_count, "Medication", generate_medication, "get_medication_id",
                      destination, bundle_size)
        generate_data(patient_count, "Patient", generate_patient, "get_patient_id", destination,
                      bundle_size)
        generate_data(episode_of_care_count, "EpisodeOfCare", generate_episode_of_care,
                      "get_episode_of_care_id", destination, bundle_size)
        generate_data(encounter_count, "Encounter", generate_encounter, "get_encounter_id",
                      destination, bundle_size)
        generate_data(document_reference_count, "DocumentReference", generate_document_reference,
                      "get_document_reference_id", destination, bundle_size)
        generate_data(condition_count, "Condition", generate_condition, "get_condition_id",
                      destination, bundle_size)
        generate_data(procedure_count, "Procedure", generate_procedure, "get_procedure_id",
                      destination, bundle_size)
        generate_data(medication_statement_count, "MedicationStatement", generate_medication_statement,
                      "get_medication_statement_id", destination, bundle_size)


def generate_data_fix_references(patient_count: int, medication_count: int, organization_count: int, min_eoc: int, max_eoc: int,
                                 write_to_file: bool, bundle_size: int = 1000):
    if write_to_file:
        print(write_to_file)
        generate_data(organization_count, "Organization", generate_organization, None, "organization.json", bundle_size)
        generate_data(medication_count, "Medication", generate_medication, None,
                      "medication.json", bundle_size)
        generate_data(patient_count, "Patient", generate_patient, None,
                      "patient.json", bundle_size)
