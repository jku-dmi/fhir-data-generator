import unittest
from fhirclient.models import organization as o
from generator.organization import generate_organization

class TestGenerateOrganization(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.organization = generate_organization()

    def test_organization_object_creation(self):
        """Tests whether an object of type Organization is created."""
        self.assertIsInstance(self.organization, o.Organization, "The created object is not an Organization")

    def test_organization_fields_populated(self):
        """Tests whether important fields in the Organization object are populated."""
        # Test identifier
        self.assertTrue(self.organization.identifier, "Organization has no identifier")
        for identifier in self.organization.identifier:
            self.assertIsNotNone(identifier.system, "Identifier system is missing")
            self.assertEqual(identifier.system, 'https://gematik.de/fhir/sid/telematik-id', "Identifier system does not match expected value")
            self.assertIsNotNone(identifier.value, "Identifier value is missing")

        # Test active status
        self.assertIsNotNone(self.organization.active, "Organization active status is missing")

        # Test type (CodeableConcept)
        self.assertTrue(self.organization.type, "Organization type is missing")
        for org_type in self.organization.type:
            self.assertTrue(org_type.coding, "Organization type has no coding")
            for coding in org_type.coding:
                self.assertIsNotNone(coding.system, "Organization type coding system is missing")
                self.assertEqual(coding.system, 'http://terminology.hl7.org/CodeSystem/organization-type', "Organization type coding system does not match expected value")
                self.assertIsNotNone(coding.code, "Organization type coding code is missing")

        # Test name
        self.assertIsNotNone(self.organization.name, "Organization name is missing")

        # Test address
        self.assertTrue(self.organization.address, "Organization has no address")
        for address in self.organization.address:
            self.assertTrue(address.line, "Address line is missing")
            self.assertIsNotNone(address.city, "Address city is missing")
            self.assertIsNotNone(address.postalCode, "Address postal code is missing")
            self.assertIsNotNone(address.country, "Address country is missing")


if __name__ == '__main__':
    unittest.main()
