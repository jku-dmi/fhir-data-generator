# create new provider class
from faker.providers import DynamicProvider

MimeTypeProvider = DynamicProvider(
     provider_name="mime_type",
     elements=["pdf", "xml", "json", "png", "jpeg", "xlsx"],

)
