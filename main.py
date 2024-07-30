from generator.data_set import generate_organization
from generator.medication.medication import generate_medication
from generator.medication.medication_statement import generate_medication_statement


def main():
    print("Starting the data generation")
    """
    patient = generate_patient()
    print(patient)
    organization = '8852'  # generate_orga()
    print(organization)
    episode_of_care = generate_episode_of_care(patient, organization)
    print(episode_of_care)
    encounter = generate_encounter(patient, episode_of_care, organization)
    print(encounter)
    document_reference = generate_document_reference(patient, encounter)
    print(document_reference)
    procedure = generate_procedure(patient, encounter)
    print(procedure)
    
    organization = '8852'
    medication = generate_medication(organization)
    print(medication)

    patient = '2'
    encounter = '9006'
    med_ref = generate_medication_statement(patient, encounter, medication)
    print(med_ref)
    """
    #condition = generate_condition(patient, encounter)
    #print(condition)
    #add_condition(encounter, condition)

    '''
    anzahl_orgas = 10
    res = []
    for n in range(anzahl_orgas):
        res.append(generate_orga())

    bundle_entries = []
    for o in res:
        entry = bundle.BundleEntry()
        entry.resource = o
        request = bundle.BundleEntryRequest()
        request.method = "POST"
        request.url = "Organization"
        entry.request = request
        bundle_entries.append(entry)

    b = bundle.Bundle()
    b.type = "transaction"
    b.entry = bundle_entries

    print(bundle)

    smart = getClient()
    try:
        # res = b.create(smart.server)
        res = requests.post(smart.server.base_uri, json=b.as_json(), headers={'Content-Type': 'application/fhir+json'})
        print(f"Response: {res}")
    except FHIRValidationError as e:
        print(f"FHIR Validation Error: {e}")

    '''
    #create_dynamic_provider("organization_id", orga_ids)

    #for i in orga_ids:
    #    print(i)

    #fake = getFaker()
    #o = fake.organization_id()

    #print(o)

    generate_organization(10)


if __name__ == "__main__":
    main()
