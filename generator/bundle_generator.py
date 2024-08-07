import fhirclient.models.bundle as bundle

import time
import concurrent.futures

from generator.organization import generate_organizations
from generator.patient import generate_patient
from helpers.create_dynamic_provider import create_dynamic_provider
from helpers.faker_instance import getFaker
from helpers.fhir_client import get_client


def generate_bundle(n: int, max_parallel: int):
    """
    :param n: Number of bundles to generate
    :param batch_size: Size of a batch to send to the server
    :param max_parallel: Maximum number of threads
    """
    fake = getFaker()
    print("Starting the data generation")

    # define how many organizations should be generated
    orga_count = 10
    orga_ids = generate_organizations(orga_count)
    create_dynamic_provider("organization_id", orga_ids)

    for i in orga_ids:
        print(i)

    o = fake.organization_id()
    print(o)

    b = bundle.Bundle()
    b.type = "transaction"


    smart = get_client()

    print(f"Start generating bundle")
    start = time.time()
    patients = []

    # Thread pool for generating patient data
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_patient) for _ in range(n)]
        for future in concurrent.futures.as_completed(futures):
            patients.append(future.result())

    # Thread pool for sending POST requests with max 20 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as executor:
        futures = []
        for patient in patients:
            futures.append(executor.submit(post_request, "Patient", patient))
        concurrent.futures.wait(futures)

    total = time.time() - start
    print(f"Task completed in {total} seconds")






    # patient = generate_patient()
    # print(patient)
    # organization = generate_orga()
    # print(organization)

    # episode_of_care = generate_episode_of_care(patient, organization)
    # print(episode_of_care)

    # encounter = generate_encounter(patient, episode_of_care, organization)
    # print(encounter)

    # condition = generate_condition(patient, encounter)
    # print(condition)
    # add_condition(encounter, condition)

