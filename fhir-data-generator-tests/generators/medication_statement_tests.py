import unittest
from fhirclient.models import medicationstatement as ms
from generator.medication.medication_statement import generate_medication_statement

class TestGenerateMedicationStatement(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.medication_statement = generate_medication_statement()

    def test_medication_statement_object_creation(self):
        """Tests whether an object of type MedicationStatement is created."""
        self.assertIsInstance(self.medication_statement, ms.MedicationStatement, "The created object is not a MedicationStatement")

    def test_medication_statement_fields_populated(self):
        """Tests whether important fields in the MedicationStatement object are populated."""
        # Test meta
        self.assertIsNotNone(self.medication_statement.meta, "MedicationStatement meta is missing")
        self.assertIn("http://dmi.de/fhir/StructureDefinition/DaWiMedMedicationStatement", self.medication_statement.meta.profile, "MedicationStatement meta profile is missing or incorrect")

        # Test status
        self.assertIsNotNone(self.medication_statement.status, "MedicationStatement status is missing")

        # Test category
        self.assertIsNotNone(self.medication_statement.category, "MedicationStatement category is missing")
        self.assertTrue(self.medication_statement.category.coding, "MedicationStatement category has no coding")
        for coding in self.medication_statement.category.coding:
            self.assertIsNotNone(coding.system, "Category coding system is missing")
            self.assertIsNotNone(coding.code, "Category coding code is missing")

        # Test medication reference
        self.assertIsNotNone(self.medication_statement.medicationReference, "MedicationStatement medicationReference is missing")
        self.assertTrue(self.medication_statement.medicationReference.reference.startswith("Medication/"), "MedicationStatement medicationReference is not a valid Medication reference")

        # Test subject (patient reference)
        self.assertIsNotNone(self.medication_statement.subject, "MedicationStatement subject is missing")
        self.assertTrue(self.medication_statement.subject.reference.startswith("Patient/"), "MedicationStatement subject reference is not a valid Patient reference")

        # Test context (encounter reference)
        self.assertIsNotNone(self.medication_statement.context, "MedicationStatement context is missing")
        self.assertTrue(self.medication_statement.context.reference.startswith("Encounter/"), "MedicationStatement context reference is not a valid Encounter reference")

        # Test effectiveDateTime
        self.assertIsNotNone(self.medication_statement.effectiveDateTime, "MedicationStatement effectiveDateTime is missing")
        self.assertIsNotNone(self.medication_statement.effectiveDateTime.date, "MedicationStatement effectiveDateTime date is missing")

if __name__ == '__main__':
    unittest.main()
