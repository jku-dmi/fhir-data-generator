import json
import time
from typing import List

import requests
from fhirclient.models.bundle import Bundle
from fhirclient.models.fhirabstractbase import FHIRValidationError
from fhirclient.models.patient import Patient

from util.fhir_client import get_client

smart = get_client()


# Alle Patienten die das Medikament '764073002', 'Omeprazole 20mg capsule' verschrieben bekommen haben.
def abfrage1():
    try:
        med_state_ids = []
        res = requests.get(smart.server.base_uri + "/Medication",
                           params={"code": "764073002", "_count": "1000000"})
        medications = res.json()

        medication_statements = []
        for entry in medications['entry']:
            med_id = entry['resource']['id']
            res = requests.get(smart.server.base_uri + "/MedicationStatement",
                               params={"medication": med_id})
            res_json = res.json()
            if res_json['total'] != 0:
                for e in res_json['entry']:
                    ms_id = e['resource']['id']
                    med_state_ids.append(ms_id)

        print(medication_statements)
        return med_state_ids
    except FHIRValidationError as fve:
        print(f"FHIR Validation failed: {fve}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


# Abfrage aller Patienten die in Kontakt mit der Organisation mit der ID 1005514 hatten
def abfrage2():
    try:
        patients = []
        encounter_ids = []
        res = requests.get(smart.server.base_uri + "/Encounter", params={"_content": "1005514"})
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
        print(f"Unexpected error while sending a request - log: {e}")


# Abfrage aller Patienten, welche eine Behandlung zwischen dem 01.01.2023 - 01.01.2024 hatten und deren Status aktiv ist.
def abfrage3():
    try:
        encounter_ids = []
        patient_ids = []
        res = requests.get(smart.server.base_uri + "/Encounter", params={"date": "ge2010-01-01",
                                                                         "date": "le2011-12-31"})
        encounter = res.json()
        for entry in encounter['entry']:
            e_id = entry['resource']['id']
            encounter_ids.append(e_id)
            p_id = entry['resource']['subject']['reference'].split('/')[1]
            res = requests.get(smart.server.base_uri + "/Patient",
                               params={"_id": p_id,
                                       "active": "true"})
            res_json = res.json()
            if res_json['total'] != 0:
                for e in res_json['entry']:
                    ms_id = e['resource']['id']
                    patient_ids.append(ms_id)

        return patient_ids
    except FHIRValidationError as fve:
        print(f"FHIR Validation failed: {fve}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")


# Abfrage aller MedicationStatements mit dem Medikament '111355001', 'Clopidogrel 75mg tablet', produziert von der Organisation mit der ID 1.
def abfrage4():
    try:
        medication_ids = []
        res = requests.get(smart.server.base_uri + "/Medication", params={"_content": "764146007",
                                                                          "manufacturer": " 1"})
        medications = res.json()
        print(medications)
        for entry in medications['entry']:
            e_id = entry['resource']['id']
            medication_ids.append(e_id)

        # build string to fine all medication statements
        med_statement_string = ""
        for med_id in medication_ids:
            med_statement_string = med_statement_string + str(med_id) + ","

        med_statement_string = med_statement_string[:-1]

        medication_statement_ids = []
        res = requests.get(smart.server.base_uri + "/MedicationStatement",
                           params={"_content:contains": med_statement_string})
        medication_statements = res.json()
        print(medication_statements)
        for entry in medication_statements['entry']:
            e_id = entry['resource']['id']
            medication_statement_ids.append(e_id)

        return medication_statement_ids
    except FHIRValidationError as fve:
        print(f"FHIR Validation failed: {fve}")
    except ConnectionError as ce:
        print(
            f"Error connecting to the FHIR Server - Please check: {smart.server.base_uri}", ce)
    except Exception as e:
        print(f"Unexpected error while sending a request - log: {e}")
