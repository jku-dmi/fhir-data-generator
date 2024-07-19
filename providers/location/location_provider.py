from faker.providers import DynamicProvider

LocationPhysicalTypeProvider = DynamicProvider(
     provider_name="physical_type",
     elements=["si", "bu", "wi", "wa", "lvl", "co", "ro", "bd", "ve", "ho", "ca", "rd", "area", "jdn", "vi"],
)
