from fhirclient import client
from urllib3.exceptions import NewConnectionError, MaxRetryError
from dotenv import load_dotenv, dotenv_values

from exceptions.fhir_connection_error import FhirConnection

def get_client():
    try:
        if load_dotenv():
            api = dotenv_values(".env")
            settings = {
                'app_id': api["APP_ID"],
                'api_base': api["API_BASE"],
            }
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
        raise FhirConnection(f"Something unexpected happend - log:  {e}", e)

    return connection
