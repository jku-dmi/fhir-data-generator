import concurrent.futures
import requests
from fhirclient.models import bundle
from fhirclient.models.fhirabstractbase import FHIRValidationError

from generator.organization import generate_orga
from helpers.fhir_client import getClient


def generate_organization(n: int):
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

    print(b)

    smart = getClient()  # Assuming getClient() is defined elsewhere
    try:
        res = requests.post(smart.server.base_uri, json=b.as_json(),
                            headers={'Content-Type': 'application/fhir+json'})
        print(f"Response: {res}")
    except FHIRValidationError as e:
        print(f"FHIR Validation Error: {e}")


def generate_patient_data_set(n: int):
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

    print(b)

    smart = getClient()  # Assuming getClient() is defined elsewhere
    try:
        res = requests.post(smart.server.base_uri, json=b.as_json(),
                            headers={'Content-Type': 'application/fhir+json'})
        print(f"Response: {res}")
    except FHIRValidationError as e:
        print(f"FHIR Validation Error: {e}")
