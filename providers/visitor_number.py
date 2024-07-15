from faker.providers import BaseProvider
from faker import Faker
fake = Faker()

class VisitorNumberProvider(BaseProvider):
     def visitor_number(self) -> str:
          return fake.numerify(text='##########')



