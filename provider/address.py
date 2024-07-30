from faker.providers import DynamicProvider

AddressUseProvider = DynamicProvider(
    provider_name="address_use",
    elements=["home", "work", "temp", "old", "billing"],
)

AddressTypeProvider = DynamicProvider(
    provider_name="address_type",
    elements=["postal", "physical", "both"],
)


