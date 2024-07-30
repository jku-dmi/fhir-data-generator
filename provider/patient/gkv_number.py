from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

class GKVProvider(BaseProvider):
     def gkv_number(self) -> str:
          return fake.numerify(text='%%%%%%%%%%')



