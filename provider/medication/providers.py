from faker.providers import DynamicProvider

SnowmedCodeProvider = DynamicProvider(
    provider_name="medication_snowmed_code",
    elements=[
        ('372687004', 'Acetaminophen 500mg tablet'),
        ('108761000', 'Amoxicillin 500mg capsule'),
        ('197480005', 'Ibuprofen 200mg tablet'),
        ('421568003', 'Metformin 500mg tablet'),
        ('11151000146106', 'Simvastatin 20mg tablet'),
        ('387461000', 'Lisinopril 10mg tablet'),
        ('399719003', 'Levothyroxine sodium 50mcg tablet'),
        ('764146007', 'Omeprazole 20mg capsule'),
        ('417475005', 'Amlodipine 5mg tablet'),
        ('429679003', 'Metoprolol tartrate 50mg tablet'),
        ('764089005', 'Atorvastatin 40mg tablet'),
        ('419568007', 'Hydrochlorothiazide 25mg tablet'),
        ('766939001', 'Furosemide 40mg tablet'),
        ('764073002', 'Albuterol 90mcg inhaler'),
        ('415006007', 'Warfarin 5mg tablet'),
        ('421570002', 'Losartan 50mg tablet'),
        ('111355001', 'Clopidogrel 75mg tablet'),
        ('387471000', 'Cetirizine 10mg tablet'),
        ('764085004', 'Doxycycline 100mg capsule'),
        ('408782007', 'Glipizide 5mg tablet')
    ],
)

MedicationStatusProvider = DynamicProvider(
    provider_name="medication_status",
    elements=[
        "active",
        "inactive",
        "entered-in-error"
    ],
)

MedicationFormProvider = DynamicProvider(
    provider_name="medication_form",
    elements=[
        ('66076007', 'Chewable tablet'),
        ('385018001', 'Oral drops'),
        ('385041009', 'Oral powder'),
        ('385124005', 'Eye drops'),
        ('385157007', 'Nasal spray'),
        ('1231713000', 'Oral pure liquid'),
        ('764788008', 'Oropharyngeal solution'),
        ('385121002', 'Eye cream'),
        ('385118004', 'Cutaneous stick'),
        ('385088008', 'Dental gel'),
        ("385063000", "Oral gum")
    ],
)

MedicationAmountProvider = DynamicProvider(
    provider_name="medication_amount",
    elements=[
        "1",
        "10",
        "50"
    ],
)

QuantityValueProvider = DynamicProvider(
    provider_name="quantity_value",
    elements=[
        1,
        5,
        10,
        50,
        100,
        400,
        800
    ],
)