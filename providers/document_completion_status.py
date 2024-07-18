# create new provider class
from faker.providers import DynamicProvider

DocumentCompletionStatusProvider = DynamicProvider(
     provider_name="completion_status",
     elements=["AU", "DI", "DO", "IN", "IP", "LA", "NU", "PA", "UC"],
)
