import concurrent.futures
import json
import random
from typing import Callable

import requests
from fhirclient.models import bundle as bundle_model
from fhirclient.models.fhirabstractbase import FHIRValidationError

from generator import generate_condition, generate_procedure
from generator.document_reference import generate_document_reference
from generator.encounter import generate_encounter, add_condition_encounter
from generator.episode_of_care import generate_episode_of_care, add_condition_eoc
from generator.medication.medication_statement import generate_medication_statement
from generator.organization import generate_orga
from generator.patient import generate_patient
from generator.medication.medication import generate_medication
from helpers.create_dynamic_provider import create_dynamic_provider
from helpers.faker_instance import getFaker
from helpers.fhir_client import getClient

fake = getFaker()


def send_bundle(bundle_: bundle_model.Bundle()) -> json:
    smart = getClient()
    try:
        res = requests.post(smart.server.base_uri, json=bundle_.as_json(),
                            headers={'Content-Type': 'application/fhir+json'})
        return json.dumps(res.json())
    except FHIRValidationError as e:
        print(f"FHIR Validation Error: {e}")


def generate_organizations(n: int) -> json:
    res = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_org = {executor.submit(generate_orga): i for i in range(n)}
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


def generate_patient_data_set(n: int):
    id = 1
    res = []
    patient = generate_patient()
    organization = fake.get_organization()
    episode_of_care = generate_episode_of_care(patient, organization)

    encounter = generate_encounter(patient, episode_of_care, organization)

    document_reference = generate_document_reference(patient, encounter)

    condition = generate_condition(patient, encounter)

    add_condition_eoc(episode_of_care, condition)
    add_condition_encounter(encounter, condition)

    procedure = generate_procedure(patient, encounter)

    medication = fake.get_medication()

    medication_statement = generate_medication_statement(patient, encounter, medication)

    res.append([patient, organization, episode_of_care, encounter, document_reference, condition, procedure, medication,
                medication_statement])

    print(res)
