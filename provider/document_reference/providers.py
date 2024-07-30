from faker.providers import DynamicProvider

StatusProvider = DynamicProvider(
    provider_name="doc_ref_status",
    elements=["current", "superseded", "entered-in-error"],
)

DocStatusProvider = DynamicProvider(
    provider_name="doc_ref_doc_status",
    elements=["registered", "partial", "preliminary", "final", "amended", "corrected", "appended", "cancelled",
              "entered-in-error"],
)

DocTypeProvider = DynamicProvider(
    provider_name="doc_ref_type",
    elements=[
        ('UB9999', '77599-9', ''),
        ('AU050102', '11488-4', 'Überweisungsschein'),
        ('DG060111', '11524-6', 'EKG-Auswertung'),
        ('DG060203', '18725-2', 'Allergietest'),
        ('DG060202', '32451-7', 'Atemtest'),
        ('ED110108', '60591-5', 'eRezept'),
        ('OP150102', '68620-9', 'OP-Anmeldungsbogen'),
        ('OP150103', '34122-2', 'OP-Bericht'),
        ('OP150105', '64297-5', 'OP-Checkliste'),
        ('SD160102', '44650-9', 'Psychologischer Erhebungsbogen'),
        ('SD160104', '81223-5', 'Psychologisches Therapiegesprächsprotokoll'),
        ('SD160105', '64295-9', 'Psychologischer Verlaufsbogen'),
        ('SF060101', '55107-7', 'Forschungsbericht'),
        ('SF190102', '59284-0', 'Einwilligung Studie'),
        ('VL160105', '57133-1', 'Pflegebericht')
    ]
)


AttachmentContentTypeProvider = DynamicProvider(
    provider_name="att_content_type",
    elements=[
        "text/plain"
        "application/cda+xml"
        "application/pdf"
    ]
)

AttachmentUrlProvider = DynamicProvider(
    provider_name="att_url",
    elements=[
        ("Binary/", ""),
        ("Binary/", "/TXT"),
        ("Binary/", "/CDA"),
        ("Binary/", "/BRAT")
    ]
)
