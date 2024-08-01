import json

from faker.providers import DynamicProvider

from helpers.faker_instance import add_provider


def create_dynamic_provider(provider_name, elements):
    # Create a new dynamic provider with the given name and elements
    provider = DynamicProvider(
        provider_name=provider_name,
        elements=elements,
    )
    add_provider(provider)


def bundle_response_to_provider(response: str, provider_name: str):
    bundle = json.loads(response)
    ids = []
    for entry in bundle['entry']:
        location = entry['response']['location']
        id = location.split('/')[1]
        ids.append(id)
    # print(ids)
    create_dynamic_provider(provider_name, ids)
