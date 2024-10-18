import unittest

from dotenv import dotenv_values
from fhirclient.models import episodeofcare as eoc
from generator.episode_of_care import generate_episode_of_care


class TestGenerateEpisodeOfCare(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.episode_of_care = generate_episode_of_care()
        env = dotenv_values(".env")

    def test_episode_of_care_object_creation(self):
        """Tests whether an object of type EpisodeOfCare is created."""
        self.assertIsInstance(self.episode_of_care, eoc.EpisodeOfCare, "The created object is not an EpisodeOfCare")

    def test_episode_of_care_fields_populated(self):
        """Tests whether important fields in the EpisodeOfCare object are populated."""
        # Test patient reference
        self.assertIsNotNone(self.episode_of_care.patient, "EpisodeOfCare patient is missing")
        self.assertTrue(self.episode_of_care.patient.reference.startswith("Patient/"), "EpisodeOfCare patient reference is not a valid Patient reference")

        # Test status
        self.assertIsNotNone(self.episode_of_care.status, "EpisodeOfCare status is missing")

        # Test managing organization reference
        self.assertIsNotNone(self.episode_of_care.managingOrganization, "EpisodeOfCare managingOrganization is missing")
        self.assertTrue(self.episode_of_care.managingOrganization.reference.startswith("Organization/"), "EpisodeOfCare managingOrganization reference is not a valid Organization reference")

        # Test identifier
        self.assertTrue(self.episode_of_care.identifier, "EpisodeOfCare has no identifier")
        for identifier in self.episode_of_care.identifier:
            self.assertIsNotNone(identifier.type, "Identifier type is missing")
            self.assertTrue(identifier.type.coding, "Identifier type has no coding")
            for coding in identifier.type.coding:
                self.assertIsNotNone(coding.system, "Identifier type coding system is missing")
                self.assertIn(coding.system, ['http://hl7.org/fhir/ValueSet/episodeofcare-type', 'http://www.krankenhaus-oberstadt.de/sid/fallnr'], "Coding system does not match expected value")
                self.assertIsNotNone(coding.code, "Identifier type coding code is missing")
            self.assertIsNotNone(identifier.value, "Identifier value is missing")

        # Test period
        self.assertIsNotNone(self.episode_of_care.period, "EpisodeOfCare period is missing")
        self.assertIsNotNone(self.episode_of_care.period.start, "EpisodeOfCare period start is missing")
        self.assertIsNotNone(self.episode_of_care.period.start.date, "EpisodeOfCare period start date is missing")
        if self.episode_of_care.period.end:
            self.assertIsNotNone(self.episode_of_care.period.end.date, "EpisodeOfCare period end date is missing")

if __name__ == '__main__':
    unittest.main()
