import time

from Subscriptions.encounter import subscribe_to_encounter
from factory.data_to_server import generate_data_random_references_to_server
from util.abfragen import abfrage1, abfrage2, abfrage4, abfrage5, abfrage7, abfrage8, abfrage9, abfrage10, abfrage3


def main():
    #res = requests.get("http://localhost:8080/fhir/Patient?_summary=count", headers={'Content-Type': 'application/fhir+json'})
    #print(f"number of patients: {res.json().get('total')}")
    #print("Starting the data generation")
    # generate_data_random_references(patient_count=10000, medication_count=1500, organization_count=1500, encounter_count=20000, episode_of_care_count=20000, procedure_count=25000, document_reference_count=20000, medication_statement_count=15000, condition_count=10000)

    start_time = time.time()
    print(abfrage10())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"elapsed_time: {elapsed_time}")
    # send_json_to_sever("./patient.json", "get_patient_id")
    """print("Now send to files the server\n")
    send_json_to_sever("./organization.json", "get_organization_id")
    send_json_to_sever("./patient.json", "get_patient_id")
    send_json_to_sever("./medication.json", "get_medication_id")
    send_json_to_sever("./episode_of_care.json", "get_episode_of_care_id")
    send_json_to_sever("./encounter.json", "get_encounter_id")
    send_json_to_sever("./document_reference.json", "get_document_reference_id")
    send_json_to_sever("./condition.json", "get_condition_id")
    send_json_to_sever("./procedure.json", "get_procedure_id")
    send_json_to_sever("./medication_statement.json", "get_medication_statement_id")
"""
    #subscribe_to_encounter("http://localhost:8080/fhir/Subscription")
    #generate_data_random_references_to_server(10, 10, 10, 100,
    #                                          100, 100,
    #                                          50000,
    #                                          100,
    #                                          1000,
    #                                          100)
    #response = generate_medication()
    #print(response)

    #generate_data(count=1234, resource="Patient", generator=generate_patient, provider_name="get_patient_id")
    #res = requests.get("http://localhost:8080/fhir/Patient?_summary=count", headers={'Content-Type': 'application/fhir+json'})
    #print(f"number of patients: {res.json().get('total')}")


if __name__ == "__main__":
    main()
