from faker.providers import DynamicProvider

codeSystemIdentifierTypeDeBasis = DynamicProvider(
     provider_name="code_system_identifier_type_de_basis",
     elements=["PKV", "GKV", "ZANR", "KZVA", "KVZ10"],
)

