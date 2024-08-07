from fhirclient import client
from fhirclient.models.fhirabstractbase import FHIRAbstractBase

from helpers.fhir_client import get_client


class Document(FHIRAbstractBase):
    def __init__(self, jsondict=None, strict=True):
        super(Document, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        return [
            ("id", "id", str, False, None, False),
            ("active", "active", bool, False, None, False),
            ("identifier", "identifier", list, True, None, False),
            ("editTime", "editTime", str, False, None, False),
            ("completionStatus", "completionStatus", dict, False, None, False),
            ("confidentiality", "confidentiality", dict, False, None, False),
            ("subject", "subject", str, False, None, False),
            ("encounter", "encounter", str, False, None, False),
            ("documentType", "documentType", str, False, None, False),
            ("department", "department", list, True, None, False),
            ("mimeType", "mimeType", str, False, None, False),
            ("objectType", "objectType", str, False, None, False),
            ("fileContentURI", "fileContentURI", str, False, None, False),
            ("hash", "hash", list, True, None, False)
        ]


smart = get_client()

# Erstellen Sie eine Instanz der benutzerdefinierten Ressource als Blueprint
blueprint_document = {
    "resourceType": "CustomDocument",
    "document": [
        {
            "id": None,
            "active": None,
            "identifier": [
                {
                    "type": {
                        "code": None,
                        "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                    },
                    "value": None,
                    "formatType": None,
                    "issuer": {
                        "oid": None,
                        "display": None,
                        "system": "http://www.krankenhaus-oberstadt.de/sid/docid"
                    }
                }
            ],
            "editTime": None,
            "completionStatus": {
                "value": None,
                "system": "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion"
            },
            "confidentiality": {
                "value": None,
                "system": "https://terminology.hl7.org/5.2.0/CodeSystem-v3-Confidentiality.html"
            },
            "subject": None,
            "encounter": None,
            "documentType": None,
            "department": [
                {
                    "identifier": {
                        "value": None,
                        "system": "http://www.krankenhaus-oberstadt.de/sid/department"
                    },
                    "display": None
                }
            ],
            "mimeType": None,
            "objectType": None,
            "fileContentURI": None,
            "hash": [
                {
                    "value": None,
                    "algorithm": "SHA-512"
                }
            ]
        }
    ]
}

# Erstellen Sie eine Instanz der benutzerdefinierten Ressource
resource_blueprint = Document(blueprint_document)

# Zeigen Sie die Blueprint-Ressource als JSON an
print(resource_blueprint.as_json())
