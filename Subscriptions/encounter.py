import requests


def subscribe_to_encounter(url: str):
    request = {
        "resourceType": "Subscription",
        "identifier": [{
            "system": "http://hl7.org/fhir/StructureDefinition/subscription",
            "identifier": "0001",
        }],
        "status": "active",
        "name": "ClickhouseSubscription",
        "criteria": "Encounter?",
        "contact": [{
            "system": "email",
            "value": "jonaskuzia@gmail.com"
        }],
        "reason": "Loading Data into Clickhouse for optimized analytics",
        "filterBy": [{
            "resourceType": "http://hl7.org/fhir/StructureDefinition/Encounter",
        }],
        "channel": {
            "type": "rest-hook",
            "endpoint": "localhost:8000/api/data/encounter",
            "payload": "application/fhir+json"
        },

        "heartbeatPeriod": "30",
        "content": "full-resource"
    }

    response = requests.request("POST", url, json=request)
    print(response)
    print(response.text)
    return response
