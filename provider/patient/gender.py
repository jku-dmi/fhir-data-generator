# create new provider class
from faker.providers import DynamicProvider

GenderProvider = DynamicProvider(
     provider_name="gender",
     elements=["female", "male", "other", "unknown"],
)
