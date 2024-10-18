from faker.providers import DynamicProvider

# Allowed document completion status
DocumentCompletionStatusProvider = DynamicProvider(
     provider_name="completion_status",
     elements=["AU", "DI", "DO", "IN", "IP", "LA", "NU", "PA", "UC"],
)
