from fhirclient import client
from urllib3.exceptions import NewConnectionError, MaxRetryError

from exceptions.fhir_connection_error import FhirConnection

settings = {
    'app_id': 'fhir_server',
    'api_base': 'http://localhost:8080/fhir/'
}


def get_client():
    try:
        connection = client.FHIRClient(settings=settings)
    except ConnectionRefusedError as cre:
        raise FhirConnection(f"Connection refused - please check the connection settings: {settings}", cre)
    except NewConnectionError as nce:
        raise FhirConnection(
            f"new connection failed - please check: {settings}", nce)
    except MaxRetryError as mre:
        raise FhirConnection(
            f"unable to connect - max retries for connection {settings} reached", mre)
    except ConnectionError as conerr:
        raise FhirConnection(f"An error occured while connecting", conerr)
    except Exception as e:
        raise FhirConnection(f"Something unexpected happend", e)

    return connection
