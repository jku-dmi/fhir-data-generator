from faker.providers import DynamicProvider

MaritalProvider = DynamicProvider(
     provider_name="marital_status",
     elements=["A", "D", "I", "L", "M", "C", "P", "T", "U", "S", "W", "UNK"],
)
