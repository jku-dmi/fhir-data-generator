from faker.providers import DynamicProvider


# Source: https://simplifier.net/packages/hl7.fhir.r4.core/4.0.1/files/78822
MedStatusProvider = DynamicProvider(
    provider_name="med_status",
    elements=["active", "completed", "entered-in-error", "intended", "intended", "on-hold", "unknown", "not-taken"],
)

# Source: https://build.fhir.org/valueset-medicationrequest-admin-location.html#expansion
MedCategoryProvider = DynamicProvider(
    provider_name="med_category",
    elements=["inpatient", "outpatient", "community"],
)