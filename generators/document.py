import concurrent.futures
import json
import time
import threading
from typing import Union

from providers.confidentiality import ConfidentialityProvider
from providers.document_completion_status import DocumentCompletionStatusProvider
from providers.gkv_number import GKVProvider
from providers.human_name import HumanNameUseProvider
from providers.contact_point import ContactPointSystemProvider, ContactPointUseProvider
from providers.address import AddressTypeProvider, AddressUseProvider
from providers.gender import GenderProvider
from providers.marital_status import MaritalProvider
from providers.mime_type import MimeTypeProvider
from providers.oid import OidProvider
from providers.timestamp import TimeStampProvider
from faker import Faker


from resources.http_requests import post_request

fake = Faker(['de'], use_weighting=False)

fake.add_provider(HumanNameUseProvider)
fake.add_provider(ContactPointSystemProvider)
fake.add_provider(ContactPointUseProvider)
fake.add_provider(AddressUseProvider)
fake.add_provider(AddressTypeProvider)
fake.add_provider(GenderProvider)
fake.add_provider(MaritalProvider)
fake.add_provider(GKVProvider)
fake.add_provider(OidProvider)
fake.add_provider(TimeStampProvider)
fake.add_provider(DocumentCompletionStatusProvider)
fake.add_provider(ConfidentialityProvider)
fake.add_provider(MimeTypeProvider)


def generate_document_data() -> Union[dict, None]:
    address = fake.address()
    address_dict = parse_address(address)

    data = {
        "resourceType": "Document",
        "id":"b4de5b28-7e0d-49d5-883e-af0188033313",
        "active":"true",
        "identifier":[
            {
                "type":{
                    "code":"RI",
                    "system":"http://terminology.hl7.org/CodeSystem/v2-0203"
                },
                "value": fake.oid(),
                "formatType":"other",
                "issuer":{
                    "oid": fake.oid(),
                    "display":"DMS",
                    "system":"http://www.krankenhaus-oberstadt.de/sid/docid"
                }
            }
        ],
        "editTime": fake.timestamp(),
        "completionStatus":{
            "value": fake.document_completion_status(),
            "system":"http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion"
        },
        "confidentiality":{
            "value": fake.confidentiality(),
            "system":"https://terminology.hl7.org/5.2.0/CodeSystem-v3-Confidentiality.html"
        },
        "subject":"6f633d04-ef57-451b-856f-2e1232ee57e3",
        "encounter":"22035706-35e6-4375-bc49-a5ba34f7e773",
        "documentType":"212152",
        "department":[
            {
                "identifier":{
                    "value":"CHIR",
                    "system":"http://www.krankenhaus-oberstadt.de/sid/department"
                },
                "display":"Fachabteilung CHIR"
            }
        ],
        "mimeType":"application/" + fake.mime_type(),
        "objectType":"default",
        "fileContentURI": fake.numerify('#######'),
        "hash":[
            {
                "value":"1347ae6292960abf3c0ab6d6a8ded6d7772362310a13339fec0ddbb770b9b09855f2f5445a1ee3f8dd2f5d0ffa8054c2ed2611baea5f3915adbc081c5667eca6",
                "algorithm":"SHA-512"
            }
        ]
    }
    print(f"Generated document data: {json.dumps(data)}")
    return data


def post_request_batch(batch_data):
    for data in batch_data:
        post_request("Document", data)


def generate_patients(n: int, batch_size: int = 10):
    """
    :type n: Number of documents to generate
    :type batch_size: Size of a batch to send to the server
    """
    print(f"Start generating {n} patients")
    start = time.time()

    patients = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_patient_data) for _ in range(n)]
        for future in concurrent.futures.as_completed(futures):
            patients.append(future.result())

    # Batch processing
    for i in range(0, len(patients), batch_size):
        batch = patients[i:i + batch_size]
        post_request_batch(batch)
        # print(f"Batch {i // batch_size + 1} of {len(patients) // batch_size + 1} processed")

    total = time.time() - start
    print(f"Task completed in {total} seconds")


def generate_patients_threads(n: int, max_parallel: int = 20):
    """
    :param n: Number of patients to generate
    :param batch_size: Size of a batch to send to the server
    :param max_parallel: Maximum number of threads
    """
    print(f"Start generating {n} patients")
    start = time.time()
    patients = []
    print(f"Start generating {n} patients")
    # Thread pool for generating patient data
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(generate_patient_data) for _ in range(n)]
        for future in concurrent.futures.as_completed(futures):
            patients.append(future.result())

    # Thread pool for sending POST requests with max 20 threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as executor:
        futures = []
        for patient in patients:
            futures.append(executor.submit(post_request, "Patient", patient))
        concurrent.futures.wait(futures)

    total = time.time() - start
    print(f"Task completed in {total} seconds")


"""
def generate_patient1(n: int):
    print("Start generating " + str(n) + " patients")
    start = time.time()
    count: int = 0
    for _ in range(n):
        address = fake.address()
        address_dict = parse_address(address)

        data = {
            "resourceType": "Patient",
            "active": True,
            "name": [
                {
                    "use": fake.human_name_use(),
                    "family": fake.last_name(),
                    "given": [fake.first_name()],
                }
            ],
            "gender": fake.gender(),
            "birthDate": fake.date_of_birth().isoformat(),
            "telecom": [{
                "use": fake.contact_point_use()
            },
                {
                    "system": "phone",
                    "value": fake.phone_number(),
                    "use": fake.contact_point_use(),
                    "rank": 1
                },
                {
                    "system": "email",
                    "value": fake.safe_email(),
                    "use": fake.contact_point_use(),
                    "rank": 2
                },
                {
                    "system": "email",
                    "value": fake.safe_email(),
                    "use": fake.contact_point_use(),
                    "period": {
                        "end": fake.year()
                    }
                }],
            "address": [{
                "use": fake.address_use(),
                "type": fake.address_type(),
                "text": address,
                "line": [address_dict['street']],
                "city": address_dict['city'],
                "state": address_dict['state'],
                "postalCode": address_dict['zip_code'],
                "period": {

                    "start": fake.date()
                }
            }],
        }

        post_request("Patient", data)
        count += 1
        print("Patient nr. " + str(count) + " created")

    total = time.time() - start
    print("Task completed in " + str(total) + " seconds")
"""


def parse_address(address: str) -> dict[str, str]:
    """
    Split Address: street, city, country und zip

    :param address: Randomly generated address with fake.address() method
    :return: dict with street, city, country and zip
    """
    lines = address.split('\n')
    if len(lines) != 2:
        raise ValueError("Address format is incorrect.")

    street = lines[0].strip()
    city_state_zip = lines[1].strip()

    if ',' in city_state_zip:
        city, state_zip = city_state_zip.rsplit(',', 1)
        city = city.strip()
        state_zip = state_zip.strip()
    else:
        city = ""
        state_zip = city_state_zip

    state_zip_parts = state_zip.split()
    if len(state_zip_parts) < 2:
        raise ValueError("State and ZIP code format is incorrect.")

    state = " ".join(state_zip_parts[:-1])
    zip_code = state_zip_parts[-1]

    state = state.strip()
    zip_code = zip_code.strip()

    return {
        'street': street,
        'city': city,
        'state': state,
        'zip_code': zip_code
    }
