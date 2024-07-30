# create new provider class
from faker.providers import DynamicProvider

OrganisationTypProvider = DynamicProvider(
     provider_name="organisation_type",
     elements=["prov", "dept", "team", "govt", "ins", "pay", "edu", "reli", "crs", "cg", "bus", "other"],
)
