from faker.providers import DynamicProvider

codeSystemIdentfierTypeDeBasis = DynamicProvider(
     provider_name="code_system_identfier_type_de_basis",
     elements=["PKV", "GKV", "ZANR", "KZVA", "KVZ10"],
)

