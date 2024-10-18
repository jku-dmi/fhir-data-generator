from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

# Generate a random visitor number
class VisitorNumberProvider(BaseProvider):
     def visitor_number(self) -> str:
          return fake.numerify(text='##########')



