from faker.providers import DynamicProvider

# Allowed contact points
ContactPointSystemProvider = DynamicProvider(
     provider_name="contact_point_system",
     elements=["phone", "fax", "email", "pager", "url", "sms", "other"],
)

# Allowed contact point use values
ContactPointUseProvider = DynamicProvider(
     provider_name="contact_point_use",
     elements=["home", "work", "temp", "old", "mobile"],
)
