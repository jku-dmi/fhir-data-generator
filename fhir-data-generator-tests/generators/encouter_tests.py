import unittest
from fhirclient.models import encounter as enc
from generator.encounter import generate_encounter


class TestGenerateEncounter(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.encounter = generate_encounter()

    def test_encounter_object_creation(self):
        """Tests whether an object of type Encounter is created."""
        self.assertIsInstance(self.encounter, enc.Encounter, "The created object is not an Encounter")

    def test_encounter_fields_populated(self):
        """Tests whether important fields in the Encounter object are populated."""
        # Test subject (patient reference)
        self.assertIsNotNone(self.encounter.subject, "Encounter subject is missing")
        self.assertTrue(self.encounter.subject.reference.startswith("Patient/"), "Encounter subject reference is not a valid Patient reference")

        # Test episodeOfCare reference
        self.assertTrue(self.encounter.episodeOfCare, "Encounter episodeOfCare is missing")
        for eoc_ref in self.encounter.episodeOfCare:
            self.assertTrue(eoc_ref.reference.startswith("EpisodeOfCare/"), "Encounter episodeOfCare reference is not a valid EpisodeOfCare reference")

        # Test identifier
        self.assertTrue(self.encounter.identifier, "Encounter has no identifier")
        for identifier in self.encounter.identifier:
            self.assertTrue(identifier.coding, "Identifier has no coding")
            for coding in identifier.coding:
                self.assertIsNotNone(coding.system, "Identifier coding system is missing")
                self.assertIn(coding.system, ['http://terminology.hl7.org/CodeSystem/v2-0203', 'http://www.krankenhaus-oberstadt.de/sid/fallnr'], "Coding system does not match expected value")
                self.assertIsNotNone(coding.code, "Identifier coding code is missing")
            self.assertIsNotNone(identifier.value, "Identifier value is missing")

        # Test class_fhir
        self.assertIsNotNone(self.encounter.class_fhir, "Encounter class is missing")
        self.assertEqual(self.encounter.class_fhir.system, "http://fhir.de/ValueSet/EncounterClassDE", "Encounter class system does not match expected value")
        self.assertIsNotNone(self.encounter.class_fhir.value, "Encounter class value is missing")

        # Test status
        self.assertIsNotNone(self.encounter.status, "Encounter status is missing")

        # Test period
        self.assertIsNotNone(self.encounter.period, "Encounter period is missing")
        self.assertIsNotNone(self.encounter.period.start, "Encounter period start is missing")
        self.assertIsNotNone(self.encounter.period.start.date, "Encounter period start date is missing")
        self.assertIsNotNone(self.encounter.period.end, "Encounter period end is missing")
        self.assertIsNotNone(self.encounter.period.end.date, "Encounter period end date is missing")

        # Test serviceProvider (organization reference)
        self.assertIsNotNone(self.encounter.serviceProvider, "Encounter serviceProvider is missing")
        self.assertTrue(self.encounter.serviceProvider.reference.startswith("Organization/"), "Encounter serviceProvider reference is not a valid Organization reference")


if __name__ == '__main__':
    unittest.main()
