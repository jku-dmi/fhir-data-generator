import unittest

from fhirclient.models import patient as p
from generator.patient import generate_patient


class TestGeneratePatient(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.patient = generate_patient()

    def test_patient_object_creation(self):
        """Tests whether an object of type Patient is created."""
        self.assertIsInstance(self.patient, p.Patient, "The created object is not a Patient")

    def test_patient_fields_populated(self):
        """Tests whether important fields in the Patient object are populated."""
        # Test identifier
        self.assertTrue(self.patient.identifier, "Patient has no identifier")
        for identifier in self.patient.identifier:
            self.assertIsNotNone(identifier.system, "Identifier system is missing")
            self.assertIsNotNone(identifier.value, "Identifier value is missing")
            self.assertIsNotNone(identifier.use, "Identifier use is missing")

        # Test meta information
        self.assertIsNotNone(self.patient.meta, "Meta data is missing")
        self.assertIsNotNone(self.patient.meta.versionId, "Meta version ID is missing")
        self.assertIsNotNone(self.patient.meta.lastUpdated, "Meta last updated is missing")

        # Test name
        self.assertTrue(self.patient.name, "Patient has no name")
        for name in self.patient.name:
            self.assertIsNotNone(name.use, "Name use is missing")
            self.assertIsNotNone(name.family, "Name family is missing")
            self.assertTrue(name.given, "Name given is missing")

        # Test active
        self.assertIsNotNone(self.patient.active, "Patient active status is missing")

        # Test address
        self.assertTrue(self.patient.address, "Patient has no address")
        for address in self.patient.address:
            self.assertTrue(address.line, "Address line is missing")
            self.assertIsNotNone(address.city, "Address city is missing")
            self.assertIsNotNone(address.postalCode, "Address postal code is missing")
            self.assertIsNotNone(address.country, "Address country is missing")

        # Test birth date
        self.assertIsNotNone(self.patient.birthDate, "Patient birth date is missing")
        self.assertIsNotNone(self.patient.gender, "Patient gender is missing")

        # Test marital status
        self.assertIsNotNone(self.patient.maritalStatus, "Patient marital status is missing")
        self.assertTrue(self.patient.maritalStatus.coding, "Marital status coding is missing")
        for coding in self.patient.maritalStatus.coding:
            self.assertIsNotNone(coding.system, "Marital status coding system is missing")
            self.assertIsNotNone(coding.code, "Marital status coding code is missing")


if __name__ == '__main__':
    unittest.main()
