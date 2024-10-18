from datetime import datetime
from typing import Tuple
from faker.providers import BaseProvider
from faker import Faker

fake = Faker()


class TimeStampProvider(BaseProvider):
    def timestamp(self) -> str:
        return fake.date() + "T" + fake.time()


class TwoTimeStampsProvider(BaseProvider):
    def timestamps_two(self) -> tuple[datetime, datetime]:
        sDateTime = fake.date_time()
        eDateTime = fake.date_time_between(start_date=sDateTime, end_date='+10y')

        return sDateTime, eDateTime
