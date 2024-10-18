import unittest
from fhirclient.models import medication as m
from fhirclient.models import ratio as r
from generator.medication.medication import generate_medication


class TestGenerateMedication(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.medication = generate_medication()

    def test_medication_object_creation(self):
        """Tests whether an object of type Medication is created."""
        self.assertIsInstance(self.medication, m.Medication, "The created object is not a Medication")

    def test_medication_fields_populated(self):
        """Tests whether important fields in the Medication object are populated."""
        # Test identifier
        self.assertTrue(self.medication.identifier, "Medication has no identifier")
        for identifier in self.medication.identifier:
            self.assertIsNotNone(identifier.value, "Identifier value is missing")

        # Test code
        self.assertIsNotNone(self.medication.code, "Medication code is missing")
        self.assertTrue(self.medication.code.coding, "Medication code has no coding")
        for coding in self.medication.code.coding:
            self.assertIsNotNone(coding.system, "Code coding system is missing")
            self.assertIsNotNone(coding.code, "Code coding code is missing")
            self.assertIsNotNone(coding.display, "Code coding display is missing")

        # Test status
        self.assertIsNotNone(self.medication.status, "Medication status is missing")

        # Test manufacturer
        self.assertIsNotNone(self.medication.manufacturer, "Medication manufacturer is missing")
        self.assertTrue(self.medication.manufacturer.reference.startswith("Organization/"), "Medication manufacturer reference is not a valid Organization reference")

        # Test form
        self.assertIsNotNone(self.medication.form, "Medication form is missing")
        self.assertTrue(self.medication.form.coding, "Medication form has no coding")
        for form_coding in self.medication.form.coding:
            self.assertIsNotNone(form_coding.system, "Form coding system is missing")
            self.assertIsNotNone(form_coding.code, "Form coding code is missing")
            self.assertIsNotNone(form_coding.display, "Form coding display is missing")

        # Test amount
        self.assertIsNotNone(self.medication.amount, "Medication amount is missing")
        self.assertIsInstance(self.medication.amount, r.Ratio, "Medication amount is not a Ratio")
        self.assertIsNotNone(self.medication.amount.numerator, "Medication amount numerator is missing")
        self.assertIsNotNone(self.medication.amount.denominator, "Medication amount denominator is missing")

        # Test numerator
        numerator = self.medication.amount.numerator
        self.assertIsNotNone(numerator.value, "Numerator value is missing")
        self.assertIsNotNone(numerator.unit, "Numerator unit is missing")
        self.assertIsNotNone(numerator.system, "Numerator system is missing")

        # Test denominator
        denominator = self.medication.amount.denominator
        self.assertIsNotNone(denominator.value, "Denominator value is missing")
        self.assertIsNotNone(denominator.unit, "Denominator unit is missing")
        self.assertIsNotNone(denominator.system, "Denominator system is missing")

if __name__ == '__main__':
    unittest.main()
