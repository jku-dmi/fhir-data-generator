from fhirclient import client
from urllib3.exceptions import NewConnectionError, MaxRetryError

from exceptions.FHIRConnection import FHIRConnectionException

settings = {
    'app_id': 'fhir_server',
    'api_base': 'http://localhost:8080/fhir/'
}


def get_client():
    try:
        connection = client.FHIRClient(settings=settings)
    except ConnectionRefusedError as cre:
        raise FHIRConnectionException(f"Connection refused - please check the connection settings: {settings}", cre)
    except NewConnectionError as nce:
        raise FHIRConnectionException(
            f"new connection failed - please check: {settings}", nce)
    except MaxRetryError as mre:
        raise FHIRConnectionException(
            f"unable to connect - max retries for connection {settings} reached", mre)
    except ConnectionError as conerr:
        raise FHIRConnectionException(f"An error occured while connecting", conerr)
    except Exception as e:
        raise FHIRConnectionException(f"Something unexpected happend", e)

    return connection
