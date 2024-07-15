# create new provider class
from faker.providers import DynamicProvider

ContactPointSystemProvider = DynamicProvider(
     provider_name="contact_point_system",
     elements=["phone", "fax", "email", "pager", "url", "sms", "other"],
)

ContactPointUseProvider = DynamicProvider(
     provider_name="contact_point_use",
     elements=["home", "work", "temp", "old", "mobile"],
)
