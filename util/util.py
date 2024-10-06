import json
import requests
from fhirclient.models import bundle as bundle_model
from fhirclient.models.fhirabstractbase import FHIRValidationError
from util.faker_instance import get_faker
from util.fhir_client import get_client

fake = get_faker()
smart = get_client()

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
