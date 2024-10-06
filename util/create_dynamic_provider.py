import json
from typing import List
from faker.providers import DynamicProvider
from util.faker_instance import add_provider


def create_dynamic_provider(provider_name, elements):
    # Create a new dynamic provider with the given name and elements
    try:
        provider = DynamicProvider(
            provider_name=provider_name,
            elements=elements,
        )
        add_provider(provider)
    except Exception as e:
        print(f"Error creating dynamic provider - Error: {e}")


def bundle_response_list_to_provider(response: List, provider_name: str):

    ids = []
    try:
        for e in response:
            bundle = json.loads(e)
            for entry in bundle['entry']:
                location = entry['response']['location']
                res_id = location.split('/')[1]
                ids.append(res_id)
    except Exception as e:
        print(f"Error creating dynamic provider from response: List - Error: {e}")
    create_dynamic_provider(provider_name, ids)
