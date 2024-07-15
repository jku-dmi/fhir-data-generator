import traceback

import requests
import json

from fhirclient.models.bundle import Bundle

from fhir_tool.exceptions.resource_not_available import ResourceNotAvailable
from fhir_tool.exceptions.resource_not_found import ResourceNotFound
from fhir_tool.fhir_client.fhir_client import smart

base_url: str = 'http://localhost:8080/fhir'
headers: dict[str, str] = {"Content-Type": "application/fhir+json; charset=utf-8"}

dataCI = {
    "resourceType": "ClinicalImpression",
    "id": "example",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: ClinicalImpression</b><a name=\"example\"> </a><a name=\"hcexample\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource ClinicalImpression &quot;example&quot; </p></div><p><b>identifier</b>: 12345</p><p><b>status</b>: completed</p><p><b>description</b>: This 26 yo male patient is brought into ER by ambulance after being involved in a motor vehicle accident</p><p><b>subject</b>: <a href=\"patient-example.html\">Patient/example</a> &quot;Peter CHALMERS&quot;</p><p><b>encounter</b>: <a href=\"encounter-example.html\">Encounter/example</a></p><p><b>effective</b>: 2014-12-06T20:00:00+11:00 --&gt; 2014-12-06T22:33:00+11:00</p><p><b>date</b>: 2014-12-06T22:33:00+11:00</p><p><b>performer</b>: <a href=\"practitioner-example.html\">Practitioner/example</a> &quot;Adam CAREFUL&quot;</p><p><b>problem</b>: <span>: MVA</span></p><p><b>summary</b>: <span title=\" \n   &lt;investigation&gt;\n    &lt;code&gt;\n      &lt;text value=&quot;Initial Examination&quot;/&gt;\n    &lt;/code&gt;\n    &lt;item&gt;\n      &lt;display value=&quot;deep laceration of the scalp (left temporo-occipital)&quot;/&gt;\n    &lt;/item&gt;\n    &lt;item&gt;\n      &lt;display value=&quot;decreased level of consciousness&quot;/&gt;\n    &lt;/item&gt;\n    &lt;item&gt;\n      &lt;display value=&quot;disoriented to time and place&quot;/&gt;\n    &lt;/item&gt;\n    &lt;item&gt;\n      &lt;display value=&quot;restless&quot;/&gt;\n    &lt;/item&gt;\n  &lt;/investigation&gt;\n   \">provisional diagnoses of laceration of head and traumatic brain injury (TBI)</span></p><blockquote><p><b>finding</b></p><h3>Items</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>Concept</b></td></tr><tr><td style=\"display: none\">*</td><td>850.0 <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (ICD-9#850.0)</span></td></tr></table></blockquote></div>"
    },
    "identifier": [{
        "value": "12345"
    }],
    "status": "completed",
    "description": "This 26 yo male patient is brought into ER by ambulance after being involved in a motor vehicle accident",
    "subject": {
        "reference": "Patient/example"
    },
    "encounter": {
        "reference": "Encounter/example"
    },
    "effectivePeriod": {
        "start": "2014-12-06T20:00:00+11:00",
        "end": "2014-12-06T22:33:00+11:00"
    },
    "date": "2014-12-06T22:33:00+11:00",
    "performer": {
        "reference": "Practitioner/example"
    },
    "problem": [{
        "display": "MVA"
    }],
    "summary": "provisional diagnoses of laceration of head and traumatic brain injury (TBI)",
    "finding": [{
        "item": {
            "concept": {
                "coding": [{
                    "system": "http://hl7.org/fhir/sid/icd-9",
                    "code": "850.0"
                }]
            }
        }
    }]
}

dataPatient = {
    "resourceType": "Patient",
    "id": "example",
    "text": {
        "status": "generated",
        "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p style=\"border: 1px #661aff solid; background-color: #e6e6ff; padding: 10px;\"><b>Jim </b> male, DoB: 1974-12-25 ( Medical record number/12345\u00a0(use:\u00a0USUAL,\u00a0period:\u00a02001-05-06 --&gt; (ongoing)))</p><hr/><table class=\"grid\"><tr><td style=\"background-color: #f3f5da\" title=\"Record is active\">Active:</td><td>true</td><td style=\"background-color: #f3f5da\" title=\"Known status of Patient\">Deceased:</td><td colspan=\"3\">false</td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Alternate names (see the one above)\">Alt Names:</td><td colspan=\"3\"><ul><li>Peter James Chalmers (OFFICIAL)</li><li>Peter James Windsor (MAIDEN)</li></ul></td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Ways to contact the Patient\">Contact Details:</td><td colspan=\"3\"><ul><li>-unknown-(HOME)</li><li>ph: (03) 5555 6473(WORK)</li><li>ph: (03) 3410 5613(MOBILE)</li><li>ph: (03) 5555 8834(OLD)</li><li>534 Erewhon St PeasantVille, Rainbow, Vic  3999(HOME)</li></ul></td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Nominated Contact: Next-of-Kin\">Next-of-Kin:</td><td colspan=\"3\"><ul><li>Bénédicte du Marché  (female)</li><li>534 Erewhon St PleasantVille Vic 3999 (HOME)</li><li><a href=\"tel:+33(237)998327\">+33 (237) 998327</a></li><li>Valid Period: 2012 --&gt; (ongoing)</li></ul></td></tr><tr><td style=\"background-color: #f3f5da\" title=\"Patient Links\">Links:</td><td colspan=\"3\"><ul><li>Managing Organization: <a href=\"organization-example-gastro.html\">Organization/1</a> &quot;Gastroenterology&quot;</li></ul></td></tr></table></div>"
    },
    "identifier": [{
        "use": "usual",
        "type": {
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                "code": "MR"
            }]
        },
        "system": "urn:oid:1.2.36.146.595.217.0.1",
        "value": "12345",
        "period": {
            "start": "2001-05-06"
        },
        "assigner": {
            "display": "Acme Healthcare"
        }
    }],
    "active": "true",
    "name": [{
        "use": "official",
        "family": "Chalmers",
        "given": ["Peter",
                  "James"]
    },
        {
            "use": "usual",
            "given": ["Jim"]
        },
        {
            "use": "maiden",
            "family": "Windsor",
            "given": ["Peter",
                      "James"],
            "period": {
                "end": "2002"
            }
        }],
    "telecom": [{
        "use": "home"
    },
        {
            "system": "phone",
            "value": "(03) 5555 6473",
            "use": "work",
            "rank": 1
        },
        {
            "system": "phone",
            "value": "(03) 3410 5613",
            "use": "mobile",
            "rank": 2
        },
        {
            "system": "phone",
            "value": "(03) 5555 8834",
            "use": "old",
            "period": {
                "end": "2014"
            }
        }],
    "gender": "male",
    "birthDate": "1974-12-25",
    "_birthDate": {
        "extension": [{
            "url": "http://hl7.org/fhir/StructureDefinition/patient-birthTime",
            "valueDateTime": "1974-12-25T14:35:45-05:00"
        }]
    },
    "deceasedBoolean": "false",
    "address": [{
        "use": "home",
        "type": "both",
        "text": "534 Erewhon St PeasantVille, Rainbow, Vic  3999",
        "line": ["534 Erewhon St"],
        "city": "PleasantVille",
        "district": "Rainbow",
        "state": "Vic",
        "postalCode": "3999",
        "period": {
            "start": "1974-12-25"
        }
    }],
    "contact": [{
        "relationship": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/v2-0131",
                "code": "N"
            }]
        }],
        "name": {
            "family": "du Marché",
            "_family": {
                "extension": [{
                    "url": "http://hl7.org/fhir/StructureDefinition/humanname-own-prefix",
                    "valueString": "VV"
                }]
            },
            "given": ["Bénédicte"]
        },
        "telecom": [{
            "system": "phone",
            "value": "+33 (237) 998327"
        }],
        "address": {
            "use": "home",
            "type": "both",
            "line": ["534 Erewhon St"],
            "city": "PleasantVille",
            "district": "Rainbow",
            "state": "Vic",
            "postalCode": "3999",
            "period": {
                "start": "1974-12-25"
            }
        },
        "gender": "female",
        "period": {
            "start": "2012"
        }
    }],
}


def get_metadata():
    url = base_url + "/metadata"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except Exception as e:
        print("Error loading server metadata fromm url: " + base_url)


def check_resource(res):
    metadata = get_metadata()
    resources = []
    if 'rest' in metadata:
        for rest in metadata['rest']:
            if 'resource' in rest:
                for resource in rest['resource']:
                    # print(f"Resource: {resource['type']}")
                    resources.append(resource['type'])

    if res in resources:
        return 1
    else:
        return 0


def get_by_resource(res_type: str) -> dict:
    """
    :type res_type: str
    """
    res_type.strip()
    url = f"{base_url}/{res_type}"
    try:
        if check_resource(res_type):
            response = requests.get(url)
            return response.json()
        else:
            raise ResourceNotAvailable("Resource not available.", errors=["Resource not available."])
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("requesting " + url + " went wrong.")


def get_by_id(res_type: str, res_id: str) -> dict:
    """
    :type res_type: str
    :type res_id: str
    """
    res_type.strip()
    url = f"{base_url}/{res_type}/{res_id}"
    try:
        if check_resource(res_type):
            response = requests.get(url)
            if response.status_code in (200, 201):
                return response.json()
            else:
                response.raise_for_status()
                raise ResourceNotFound("Resource not found.", errors=["Resource not found."])
        else:
            raise ResourceNotAvailable("Resource not available.", errors=["Resource not available."])
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("requesting " + url + " went wrong.")


def post_request(res_type: str, data: dict) -> dict:
    """
    :type res_type: Resource type
    :type data: data to store in the resource
    """
    res_type.strip()
    url = f"{base_url}/{res_type}"
    try:
        if check_resource(res_type):
            response = requests.post(url, headers=headers, json=data)
            print(response.json())
            return response.json()
        else:
            raise ResourceNotAvailable("Resource not available.", errors=["Resource not available."])
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("post request to " + url + " went wrong.")
        print(traceback.format_exc())


def update_request(res_type: str, res_id: str, updated_data: dict) -> dict:
    """
    :type res_type: basestring
    :type updated_data: dict
    :type res_id: str
    """
    res_type.strip()
    url = f"{base_url}/{res_type}/{res_id}"

    try:

        if check_resource(res_type):
            response = requests.put(url, headers=headers, data=json.dumps(updated_data))
            return response.json()
        else:
            raise ResourceNotAvailable("Resource not available.", errors=["Resource not available."])
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("put request to " + url + " went wrong.")


def delete_by_id(res_type: str, res_id: str) -> dict:
    """
    :type res_type: str
    :type res_id: str
    """
    res_type.strip()
    url = f"{base_url}/{res_type}/{res_id}"
    try:
        if check_resource(res_type):
            response = requests.delete(url)
            if response.status_code in (200, 201):
                return response.json()
            else:
                response.raise_for_status()
                raise ResourceNotFound("Resource not found.", errors=["Resource not found."])
        else:
            raise ResourceNotAvailable("Resource not available.", errors=["Resource not available."])
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("requesting " + url + " went wrong.")


def delete_by_params(params: dict, res_type: str = "") -> dict:
    """
    :type params: dict
    :type res_type: str
    """
    if(res_type != ""):
        res_type.strip()
        url = f"{base_url}/{res_type}/{params}"
    else:
        url = f"{base_url}/{params}"

    try:
        if check_resource(res_type):
            response = requests.delete(url)
            if response.status_code in (200, 201):
                return response.json()
            else:
                response.raise_for_status()
                raise ResourceNotFound("Resource not found.", errors=["Resource not found."])
        else:
            raise ResourceNotAvailable("Resource not available.", errors=["Resource not available."])
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("requesting " + url + " went wrong.")


def get_resource_count(res_type: str) -> int:
    """
    :param res_type: Resource type
    :return:
    """
    url = f"{base_url}/{res_type}?_summary=count"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the total count of patients
            total = data['total']
            print(f"Total number of patients: {total}")
            return total
    except ResourceNotAvailable as e:
        print(e.message)
    except Exception as e:
        print("requesting " + url + " went wrong.")


def post_request_batch(bundle: Bundle):
    try:
        print(bundle)
        response = requests.post(base_url, data=bundle, headers=headers)
        print(response.json())
        if response.status_code in [200, 201]:
            print("Successfully sent the bundle to the FHIR server.")
            print(response.json())
        else:
            raise Exception("Error sending bundle to the FHIR server.")
            print(f"Failed to send the bundle: {response.status_code}, {response.text}")
    except Exception as e:
        print("Sending the bundle to the server went wrong " + e.message)


def request_bundle(bundle: Bundle):
    try:
        response = smart.batch(bundle)
        print(response)
        if response.status_code in [200, 201]:
            print("Successfully sent the bundle to the FHIR server.")
            print(response.json())
        else:
            raise Exception("Error sending bundle to the FHIR server.")
            print(f"Failed to send the bundle: {response.status_code}, {response.text}")
    except Exception as e:
        print("Sending the bundle to the server went wrong " + e.message)