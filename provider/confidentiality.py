from faker.providers import DynamicProvider


# List of possible confidentiality values
ConfidentialityProvider = DynamicProvider(
     provider_name="confidentiality",
     elements=["L", "M", "N", "R", "U", "V"],
)
