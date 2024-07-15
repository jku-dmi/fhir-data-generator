import time

from fhir_tool.fhir_client.patient_generator import generate_patients_fhir_client
from fhir_tool.http_requests import get_by_resource, get_metadata, update_request, post_request, get_resource_count
from fhir_tool.json_file_reader import JsonFileReader
import json
from fhir_tool.data_generation.patient_generator import generate_patients, \
    generate_patients_threads

from fhir_tool.validation.validateResources import get_resources


def main():
    #print("Starting FHIR Tool")
    #r = get_by_resource("Patient")
    #try:
    #    print(json.dumps(r, indent=2))
    #except AttributeError as e:
    #    print("There was no response with an .json attribute ")
    #except Exception as e:
    #    print("An error occurred")

    # path = 'C:/Users/KuziaJ/PycharmProjects/fhir-tool/data/CI.json'

    # jfr = JsonFileReader(path)

    # jfr.show_content()

    # generate_patient_threading(1000, 10)
    get_resource_count("Patient")
    generate_patients_threads(1000, 20)
    generate_patients_fhir_client(1000)
    get_resource_count("Patient")



    # updated_data = {
    #     "resourceType": "Patient",
    #     "id": "1",
    #     "active": True,
    #     "name": [
    #         {
    #             "use": "official",
    #             "family": "Doe",
    #             "given": ["John"]
    #         }
    #     ],
    #     "gender": "male",
    #     "birthDate": "1980-01-01"
    # }

    #try:
    #    updated_resource = update_request("Patient", "1", updated_data)

    #    print(f"Updated Resource: {json.dumps(updated_resource, indent=2)}")
    #except requests.exceptions.RequestException as e:
    #    print(f"Request failed: {e}")


if __name__ == "__main__":
    main()
