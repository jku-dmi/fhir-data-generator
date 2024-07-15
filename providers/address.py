# create new provider class
from faker.providers import DynamicProvider


""" home | work | temp | old | billing - purpose of this address.
        Type `str`. """
AddressUseProvider = DynamicProvider(
    provider_name="address_use",
    elements=["home", "work", "temp", "old", "billing"],
)

AddressTypeProvider = DynamicProvider(
    provider_name="address_type",
    elements=["postal", "physical", "both"],
)


