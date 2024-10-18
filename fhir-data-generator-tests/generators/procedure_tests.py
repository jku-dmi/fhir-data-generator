import unittest
from fhirclient.models import procedure as proc
from generator.procedure import generate_procedure


class TestGenerateProcedure(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.procedure = generate_procedure()

    def test_procedure_object_creation(self):
        """Tests whether an object of type Procedure is created."""
        self.assertIsInstance(self.procedure, proc.Procedure, "The created object is not a Procedure")

    def test_procedure_fields_populated(self):
        """Tests whether important fields in the Procedure object are populated."""
        # Test meta information
        self.assertIsNotNone(self.procedure.meta, "Meta data is missing")
        self.assertTrue(self.procedure.meta.profile, "Meta profile is missing")
        self.assertIn("http://dmi.de/fhir/StructureDefinition/DaWiMedProzedur", self.procedure.meta.profile, "Profile does not match expected value")

        # Test status
        self.assertIsNotNone(self.procedure.status, "Procedure status is missing")

        # Test subject (patient reference)
        self.assertIsNotNone(self.procedure.subject, "Procedure subject is missing")
        self.assertTrue(self.procedure.subject.reference.startswith("Patient/"), "Procedure subject reference is not a valid Patient reference")

        # Test encounter reference
        self.assertIsNotNone(self.procedure.encounter, "Procedure encounter is missing")
        self.assertTrue(self.procedure.encounter.reference.startswith("Encounter/"), "Procedure encounter reference is not a valid Encounter reference")

        # Test performedDateTime
        self.assertIsNotNone(self.procedure.performedDateTime, "Procedure performedDateTime is missing")
        self.assertIsNotNone(self.procedure.performedDateTime.date, "Procedure performedDateTime.date is missing")

        # Test code
        self.assertIsNotNone(self.procedure.code, "Procedure code is missing")
        self.assertTrue(self.procedure.code.coding, "Procedure code has no coding")
        for coding in self.procedure.code.coding:
            self.assertIsNotNone(coding.system, "Procedure coding system is missing")
            self.assertEqual(coding.system, "http://snomed.info/sct", "Procedure coding system does not match expected value")
            self.assertIsNotNone(coding.code, "Procedure coding code is missing")
            self.assertIsNotNone(coding.display, "Procedure coding display is missing")


if __name__ == '__main__':
    unittest.main()
