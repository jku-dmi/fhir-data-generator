from faker.providers import DynamicProvider

# List of possible ICD 10 codes in the generated resources.
ICD10Provider = DynamicProvider(
     provider_name="icd_10_code",
     elements=["F32.0", "M33.2", "F91.0", "F32.1", "F34.4", "I11.00", "I27", "J00", "J03", "J68.0", "J68.4", "K26.2"],
)
