from fhirclient import client

settings = {
    'app_id': 'fhir_server',
    'api_base': 'http://localhost:8080/fhir/'
}


def getClient():
    return client.FHIRClient(settings=settings)
