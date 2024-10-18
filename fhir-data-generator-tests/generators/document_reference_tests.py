import unittest
from fhirclient.models import documentreference as dr
from generator.document_reference import generate_document_reference


class TestGenerateDocumentReference(unittest.TestCase):

    def setUp(self):
        """Executed before each test."""
        self.document_reference = generate_document_reference()

    def test_document_reference_object_creation(self):
        """Tests whether an object of type DocumentReference is created."""
        self.assertIsInstance(self.document_reference, dr.DocumentReference, "The created object is not a DocumentReference")

    def test_document_reference_fields_populated(self):
        """Tests whether important fields in the DocumentReference object are populated."""
        # Test identifier
        self.assertTrue(self.document_reference.identifier, "DocumentReference has no identifier")
        for identifier in self.document_reference.identifier:
            self.assertTrue(identifier.coding, "Identifier has no coding")
            for coding in identifier.coding:
                self.assertIsNotNone(coding.system, "Identifier coding system is missing")
                self.assertIn(coding.system, ['http://id-berlin.de/fhir/externalDocumentId', 'http://dmi.de/fhir/sid/document/9998'], "Coding system does not match expected value")
                self.assertIsNotNone(coding.value, "Identifier coding value is missing")

        # Test status and docStatus
        self.assertIsNotNone(self.document_reference.status, "DocumentReference status is missing")
        self.assertIsNotNone(self.document_reference.docStatus, "DocumentReference docStatus is missing")

        # Test editTime
        self.assertIsNotNone(self.document_reference.editTime, "DocumentReference editTime is missing")

        # Test type (CodeableConcept)
        self.assertIsNotNone(self.document_reference.type, "DocumentReference type is missing")
        for coding in self.document_reference.type.coding:
            self.assertIsNotNone(coding.system, "DocumentReference type coding system is missing")
            self.assertIn(coding.system, ["http://dvmd.de/fhir/CodeSystem/kdl", "http://loinc.org"], "DocumentReference type coding system does not match expected value")
            self.assertIsNotNone(coding.value, "DocumentReference type coding value is missing")
            self.assertIsNotNone(coding.display, "DocumentReference type coding display is missing")

        # Test category (CodeableConcept)
        self.assertTrue(self.document_reference.category, "DocumentReference category is missing")
        for category in self.document_reference.category:
            for coding in category.coding:
                self.assertIsNotNone(coding.system, "Category coding system is missing")
                self.assertIn(coding.system, ["http://dvmd.de/fhir/CodeSystem/kdl", "http://loinc.org"], "Category coding system does not match expected value")
                self.assertIsNotNone(coding.value, "Category coding value is missing")
                self.assertIsNotNone(coding.display, "Category coding display is missing")

        # Test subject (patient reference)
        self.assertIsNotNone(self.document_reference.subject, "DocumentReference subject is missing")
        self.assertTrue(self.document_reference.subject.reference.startswith("Patient/"), "DocumentReference subject reference is not a valid Patient reference")

        # Test context (encounter reference)
        self.assertIsNotNone(self.document_reference.context, "DocumentReference context is missing")
        self.assertTrue(self.document_reference.context.encounter, "DocumentReference context encounter is missing")
        for encounter_ref in self.document_reference.context.encounter:
            self.assertTrue(encounter_ref.reference.startswith("Encounter/"), "DocumentReference context encounter reference is not a valid Encounter reference")

        # Test content (Attachment)
        self.assertTrue(self.document_reference.content, "DocumentReference content is missing")
        for content in self.document_reference.content:
            self.assertIsNotNone(content.attachment, "DocumentReference attachment is missing")
            self.assertIsNotNone(content.attachment.contentType, "Attachment contentType is missing")
            self.assertIsNotNone(content.attachment.url, "Attachment URL is missing")
            self.assertIsNotNone(content.attachment.title, "Attachment title is missing")
            self.assertIsNotNone(content.format, "DocumentReference format is missing")
            self.assertIsNotNone(content.format.display, "DocumentReference format display is missing")


if __name__ == '__main__':
    unittest.main()
