from faker.providers import DynamicProvider

EpisodeOfCareStatusProvider = DynamicProvider(
     provider_name="eoc_status",
     elements=["planned", "waitlist", "active", "onhold", "finished", "cancelled", "entered-in-error"],
)

EpisodeOfCareType = DynamicProvider(
     provider_name="eoc_type",
     elements=["hacc", "pac", "diab", "da", "cacp"],
)