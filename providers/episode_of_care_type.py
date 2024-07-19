# create new provider class
from faker.providers import DynamicProvider

EpisodeOfCareType = DynamicProvider(
     provider_name="eoc_type",
     elements=["hacc", "pac", "diab", "da", "cacp"],
)
