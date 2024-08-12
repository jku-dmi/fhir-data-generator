import json

import requests
from fhirclient.models import bundle as bundle_model
from fhirclient.models.fhirabstractbase import FHIRValidationError

from util.create_dynamic_provider import bundle_response_to_provider, bundle_response_list_to_provider
from util.faker_instance import get_faker
from util.fhir_client import get_client

fake = get_faker()
smart = get_client()


def save_bundle(bundle_: bundle_model.Bundle(), file_name) -> str:
    try:
        data = bundle_.as_json()
        with open(file_name, 'a', encoding='utf-8') as f:  # a = append, w = write
            json.dump(data, f, ensure_ascii=False, indent=4)
        return file_name
    except IOError as e:
        print(f"IO Error while writing {file_name} - log: {e}")
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def send_bundle(bundle_: bundle_model.Bundle()) -> json:
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
        print(f"Unexpected error while sending a request - log: {e}")


def send_json_to_sever(path: str, provider_name: str):
    try:
        f = open(path, 'r')
        data = json.load(f)
        response_list = []

        for bundle in data:
            res = requests.post(smart.server.base_uri, json=bundle,
                                headers={'Content-Type': 'application/fhir+json'})
            print(res.content)
            response_list.append(res)

        bundle_response_list_to_provider(response_list, provider_name)
        # bundle_response_list_to_provider(res.json(), provider_name)
        f.close()
        return response_list

    except FileNotFoundError as fnfe:
        print(f"Could not find file: {path} - log {fnfe}")
    except FHIRValidationError as e:
        print(f"FHIR Validation failed: {e}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")
