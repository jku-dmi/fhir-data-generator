from faker.providers import BaseProvider
from faker import Faker

fake = Faker()


# Defining the structure of a Oid and providing a function to generate a random Oid
class OidProvider(BaseProvider):
    def oid(self) -> str:
        return fake.numerify(text='#.#.###.#.##.#.#.#####.####.#############.#')
