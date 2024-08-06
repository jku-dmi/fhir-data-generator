from fhirclient import client
from urllib3.exceptions import NewConnectionError, MaxRetryError

settings = {
    'app_id': 'fhir_server',
    'api_base': 'http://localhost:8080/fhir/'
}


def getClient():
    global connection
    try:
        connection = client.FHIRClient(settings=settings)
    except ConnectionRefusedError:
        print(f"Die Verbindung wurde verweigert. Bitte überprüfe die Verbindung: {settings}")
    except NewConnectionError:
        print(
            f"Es konnte keine Verbindung zum FHIR-Server hergestellt werden. Bitte überprüfe die Verbindung: {settings}")
    except MaxRetryError:
        print(
            f"Es konnte keine Verbindung zum FHIR-Server hergestellt werden. Bitte überprüfe die Verbindung: {settings}")
    except ConnectionError as conerr:
        print(f"Es gab einen Fehler bei der Verbindung: {conerr}")
    except Exception as e:
        print(f"Es ist ein Fehler beim Herstellen der Verbindung aufgetreten: {e}")

    return connection
