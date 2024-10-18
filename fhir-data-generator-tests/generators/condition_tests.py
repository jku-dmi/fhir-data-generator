import unittest
from fhirclient.models import condition as c
from generator.condition import generate_condition


class TestGenerateCondition(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.condition = generate_condition()

    def test_condition_object_creation(self):
        """Tests whether an object of type Condition is created."""
        self.assertIsInstance(self.condition, c.Condition, "The created object is not a Condition")

    def test_condition_fields_populated(self):
        """Tests whether important fields in the Condition object are populated."""
        # Test identifier
        self.assertTrue(self.condition.identifier, "Condition has no identifier")
        for identifier in self.condition.identifier:
            self.assertIsNotNone(identifier.system, "Identifier system is missing")
            self.assertIsNotNone(identifier.value, "Identifier value is missing")
            self.assertEqual(identifier.use, 'usual', "Identifier use is not 'usual'")

        # Test meta
        self.assertIsNotNone(self.condition.meta, "Condition meta is missing")
        self.assertIn("http://dmi.de/fhir/StructureDefinition/DaWiMedCondition", self.condition.meta.profile, "Condition meta profile is missing or incorrect")
        self.assertIsNotNone(self.condition.meta.lastUpdated, "Condition meta lastUpdated is missing")

        # Test clinical status
        self.assertIsNotNone(self.condition.clinicalStatus, "Condition clinicalStatus is missing")
        self.assertTrue(self.condition.clinicalStatus.coding, "Condition clinicalStatus has no coding")
        for coding in self.condition.clinicalStatus.coding:
            self.assertIsNotNone(coding.system, "Clinical status coding system is missing")
            self.assertIsNotNone(coding.code, "Clinical status coding code is missing")

        # Test condition code
        self.assertIsNotNone(self.condition.code, "Condition code is missing")

        # Test subject (patient reference)
        self.assertIsNotNone(self.condition.subject, "Condition subject is missing")
        self.assertTrue(self.condition.subject.reference.startswith("Patient/"), "Condition subject reference is not a valid Patient reference")

        # Test encounter reference
        self.assertIsNotNone(self.condition.encounter, "Condition encounter is missing")
        self.assertTrue(self.condition.encounter.reference.startswith("Encounter/"), "Condition encounter reference is not a valid Encounter reference")

        # Test recorded date
        self.assertIsNotNone(self.condition.recordedDate, "Condition recordedDate is missing")
        self.assertIsNotNone(self.condition.recordedDate.date, "Condition recordedDate date is missing")

if __name__ == '__main__':
    unittest.main()
