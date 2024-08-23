import json
from typing import List

import requests
from fhirclient.models.bundle import Bundle
from fhirclient.models.fhirabstractbase import FHIRValidationError
from fhirclient.models.patient import Patient

from util.fhir_client import get_client

smart = get_client()


# Abfragen von allen Patienten die das Medikament '197480005', 'Ibuprofen 200mg tablet' innerhalb der letzten 2 Jahre verschrieben bekommen habe
def abfrage1():
    try:
        medication_ids = []
        med_state_ids = []
        res = requests.get(smart.server.base_uri + "/Medication", params={"_content": "Ibuprofen 200mg"})
        medications = res.json()
        for entry in medications['entry']:
            med_id = entry['resource']['id']
            medication_ids.append(med_id)

        # build string to fine all medication statements
        med_statement_string = ""
        for med_id in medication_ids:
            med_statement_string = med_statement_string + str(med_id) + ","

        med_statement_string = med_statement_string + "630603,"
        med_statement_string = med_statement_string[:-1]

        url = smart.server.base_uri + "/MedicationStatement?_content:contains=630603, 630604"
        print(med_statement_string)
        #res = requests.get(url)
        res = requests.get(smart.server.base_uri + "/MedicationStatement",
                           params={"_content:contains": med_statement_string})
        medication_statements = res.json()

        print(medication_statements)

        return med_state_ids
    except FHIRValidationError as fve:
        print(f"FHIR Validation failed: {fve}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


def abfrage2():
    try:
        patients = []
        encounter_ids = []
        res = requests.get(smart.server.base_uri + "/Encounter", params={"_content": "630061"})
        encounter = res.json()
        print(encounter)
        for entry in encounter['entry']:
            e_id = entry['resource']['id']
            encounter_ids.append(e_id)
            p_id = entry['resource']['subject']['reference']
            p_id = p_id.split('/')[1]
            patients.append(p_id)

        return patients
    except FHIRValidationError as fve:
        print(f"FHIR Validation failed: {fve}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e.with_traceback()}")
