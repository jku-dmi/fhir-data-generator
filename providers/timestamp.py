from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

class TimeStampProvider(BaseProvider):
    def timestamp(self) -> str:
        return fake.date() + "T" + fake.time()



