from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

class DocIdProvider(BaseProvider):
     def doc_id(self) -> str:
          return fake.numerify(text='%.%.%%%.#.#.#.#.###.#.#.#############.####.#############')
