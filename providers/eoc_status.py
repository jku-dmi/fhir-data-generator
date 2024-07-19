# create new provider class
from faker.providers import DynamicProvider

EpisodeOfCareStatusProvider = DynamicProvider(
     provider_name="eoc_status",
     elements=["planned", "waitlist", "active", "onhold", "finished", "cancelled", "entered-in-error"],
)
