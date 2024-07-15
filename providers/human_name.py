# create new provider class
from faker.providers import DynamicProvider

HumanNameUseProvider = DynamicProvider(
     provider_name="human_name_use",
     elements=["usual", "official", "temp", "nickname", "anonymous", "old", "maiden"],
)
