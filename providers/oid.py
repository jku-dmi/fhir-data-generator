from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

class OidProvider(BaseProvider):
     def oid(self) -> str:
          return fake.numerify(text='#.#.###.###.###.#####.###.##')



