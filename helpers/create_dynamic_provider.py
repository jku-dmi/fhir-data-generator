import json

from faker.providers import DynamicProvider

from helpers.faker_instance import add_provider


def create_dynamic_provider(provider_name, elements):
    # Create a new dynamic provider with the given name and elements
    try:
        provider = DynamicProvider(
            provider_name=provider_name,
            elements=elements,
        )
        add_provider(provider)
    except Exception as e:
        print(f"Es ist ein Fehler beim Erstellen des Providers aufgetreten: {e}")


def bundle_response_to_provider(response: str, provider_name: str):
    try:
        bundle = json.loads(response)
        ids = []
        for entry in bundle['entry']:
            location = entry['response']['location']
            id = location.split('/')[1]
            ids.append(id)
        # print(ids)
        create_dynamic_provider(provider_name, ids)
    except Exception as e:
        print(f"Es ist ein Fehler beim Erstellen des Providers aus der Bundle-response aufgetreten: {e}")
