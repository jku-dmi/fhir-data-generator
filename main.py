from generator.data_set import generate_data_set_references

def main():
    #res = requests.get("http://localhost:8080/fhir/Patient?_summary=count", headers={'Content-Type': 'application/fhir+json'})
    #print(f"number of patients: {res.json().get('total')}")
    #print("Starting the data generation")
    # generate_data_random_references(patient_count=10000, medication_count=1500, organization_count=1500, encounter_count=20000, episode_of_care_count=20000, procedure_count=25000, document_reference_count=20000, medication_statement_count=15000, condition_count=10000)

    generate_data_set_references(patient_count=10000, medication_count=10000, organization_count=10000, encounter_count=10000, episode_of_care_count=10000, procedure_count=10000, document_reference_count=10000, medication_statement_count=10000, condition_count=10000, write_to_file=True, bundle_size=1000)
    print("VERSUS\n")

    #generate_data(count=1234, resource="Patient", generator=generate_patient, provider_name="get_patient_id")
    #res = requests.get("http://localhost:8080/fhir/Patient?_summary=count", headers={'Content-Type': 'application/fhir+json'})
    #print(f"number of patients: {res.json().get('total')}")


if __name__ == "__main__":
    main()
