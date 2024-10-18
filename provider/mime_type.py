from faker.providers import DynamicProvider

# Possible file MIME types
MimeTypeProvider = DynamicProvider(
     provider_name="mime_type",
     elements=["pdf", "xml", "json", "png", "jpeg", "xlsx"],

)
