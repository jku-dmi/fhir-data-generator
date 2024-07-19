from faker.providers import DynamicProvider

from helpers.faker_instance import add_provider


def create_dynamic_provider(provider_name, elements):
    # Create a new dynamic provider with the given name and elements
    provider = DynamicProvider(
        provider_name=provider_name,
        elements=elements,
    )
    add_provider(provider)
