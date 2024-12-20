from fhirclient import client
from urllib3.exceptions import NewConnectionError, MaxRetryError
from dotenv import load_dotenv, dotenv_values
from exceptions.fhir_connection_error import FhirConnection

global settings


# Create a FHIR Client using the parameters from the .env file
def get_client():
    global settings
    try:
        if load_dotenv():
            env = dotenv_values(".env")
            settings = {
                'app_id': env["APP_ID"],
                'api_base': env["API_BASE"],
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
    except ConnectionError as ce:
        raise FhirConnection(f"An error occurred while connecting", ce)
    except Exception as e:
        raise FhirConnection(f"Something unexpected happened - log:  {e}", e)

    return connection
