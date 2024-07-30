# create new provider class
from faker.providers import DynamicProvider

ConfidentialityProvider = DynamicProvider(
     provider_name="confidentiality",
     elements=["L", "M", "N", "R", "U", "V"],
)
