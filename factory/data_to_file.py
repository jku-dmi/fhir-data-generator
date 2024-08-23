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
from util.faker_instance import get_faker
from util.fhir_client import get_client
from util.util import save_bundle

fake = get_faker()
smart = get_client()


def generate_resources_to_file(function: Callable, resource_type: str, n: int, destination: str) -> json:
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
        save_bundle(b, destination)
    return b


def generate_data_to_file(count: int, resource_type: str, generator: Callable,
                          destination: str, bundle_size: int = 1000) -> List[int] | None:
    """
    generate fhir data
    :param count: number of resources to generate
    :param resource_type: resource type
    :param generator: Callable(method) that generates the data
    :param destination: None = send data to FHIR Server, "*" = save data in file with the given name
    :param bundle_size: maximum number of resources to put into a bundle (default = 1000)
    :return: None
    """
    print(f"Start generation of {count} {resource_type} resources")
    start_time = time.time()
    reps, rest = divmod(count, bundle_size)
    result = []
    with open(destination, 'w', encoding='utf-8') as f:  # a = append, w = write
        f.write("[")
    if reps > 0:
        for i in range(reps):
            result.append(generate_resources_to_file(generator, resource_type, bundle_size, destination))
            with open(destination, 'a', encoding='utf-8') as f:  # a = append, w = write
                f.write(",")
    # generate rest if needed
    if rest != 0:
        result.append(generate_resources_to_file(generator, resource_type, rest, destination))
    with open(destination, 'a', encoding='utf-8') as f:  # a = append, w = write
        f.write("]")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{resource_type}s generated - elapsed time: {elapsed_time:.2f} seconds.")
    return result


def generate_data_random_references_to_file(patient_count: int, medication_count: int, organization_count: int,
                                            encounter_count: int,
                                            episode_of_care_count: int, condition_count: int,
                                            document_reference_count: int,
                                            procedure_count: int,
                                            medication_statement_count: int, bundle_size: int = 1000):
    generate_data_to_file(organization_count, "Organization", generate_organization,
                          "organization.json", bundle_size)
    generate_data_to_file(medication_count, "Medication", generate_medication,
                          "medication.json", bundle_size)
    generate_data_to_file(patient_count, "Patient", generate_patient,
                          "patient.json", bundle_size)
    generate_data_to_file(episode_of_care_count, "EpisodeOfCare", generate_episode_of_care,
                          "episode_of_care.json", bundle_size)
    generate_data_to_file(encounter_count, "Encounter", generate_encounter,
                          "encounter.json", bundle_size)
    generate_data_to_file(document_reference_count, "DocumentReference", generate_document_reference,
                          "document_reference.json", bundle_size)
    generate_data_to_file(condition_count, "Condition", generate_condition,
                          "condition.json", bundle_size)
    generate_data_to_file(procedure_count, "Procedure", generate_procedure,
                          "procedure.json", bundle_size)
    generate_data_to_file(medication_statement_count, "MedicationStatement", generate_medication_statement,
                          "medication_statement.json", bundle_size)
