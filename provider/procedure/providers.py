from faker.providers import DynamicProvider

ProcedureStatusProvider = DynamicProvider(
    provider_name="proc_status",
    elements=[
        "preparation",
        "in-progress",
        "not-done",
        "on-hold",
        "stopped",
        "completed",
        "entered-in-error",
        "unknown"
    ]
)


ProcedureSnomedProvider = DynamicProvider(
    provider_name="proc_snomed",
    elements=[
        ('1157017005', 'Endoscopy of upper gastrointestinal tract (procedure)'),
        ('103001000119102', 'Cholecystectomy (procedure)'),
        ('90721000119102', 'Laparoscopic cholecystectomy (procedure)'),
        ('324121000000109', 'Electrocardiogram (procedure)'),
        ('115160002', 'Intraocular lens implantation (procedure)'),
        ('2724002', 'Appendectomy (procedure)'),
        ('96361000119102', 'Arthroscopic surgery of knee joint (procedure)'),
        ('68810003', 'Cystoscopy (procedure)'),
        ('167690002', 'Tracheostomy (procedure)'),
        ('119332001', 'Thoracotomy (procedure)'),
        ('70711000119100', 'Electroconvulsive therapy (procedure)'),
        ('72346002', 'Peritoneal dialysis (procedure)'),
        ('2821000179102', 'Laparoscopic hernia repair (procedure)'),
        ('69851000119101', 'Cardiac catheterization (procedure)'),
        ('40873000119106', 'Skin biopsy (procedure)'),
        ('69721000119101', 'Angioplasty (procedure)'),
        ('90151000119104', 'Lung biopsy (procedure)'),
        ('80321000119104', 'Hip replacement (procedure)'),
        ('3867004', 'Colonoscopy (procedure)'),
        ('71521000119100', 'Gastric bypass surgery (procedure)')
    ]
)

