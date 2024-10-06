import random

import fhirclient.models.documentreference as dr
import fhirclient.models.identifier as i
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr
import fhirclient.models.attachment as att
import fhirclient.models.codeableconcept as cc
import fhirclient.models.patient as p
import fhirclient.models.encounter as e

from util.fhir_client import get_client
from util.faker_instance import get_faker

smart = get_client()
fake = get_faker()


def generate_document_reference(patient: p.Patient | None, encounter: e.Encounter | None) -> dr.DocumentReference:
    document_reference = dr.DocumentReference()
    if patient is None:
        patient = fake.get_patient_id()
    if encounter is None:
        encounter = fake.get_encounter_id()

    identifier = i.Identifier()
    ident_id = fake.doc_id()

    coding2 = cod.Coding()
    coding2.system = 'http://id-berlin.de/fhir/externalDocumentId'
    coding2.value = ident_id

    coding3 = cod.Coding()
    coding3.system = 'http://dmi.de/fhir/sid/document/9998'
    coding3.value = ident_id

    identifier.coding = [coding2, coding3]
    document_reference.identifier = [identifier]

    document_reference.active = True
    document_reference.status = fake.doc_ref_status()
    #TODO: Check why local fhir server doenst accept defined values (https://build.fhir.org/documentreference.html)
    #document_reference.docStatus = fake.doc_ref_doc_status()
    document_reference.editTime = fake.timestamp()

    doc_type = fake.doc_ref_type()

    coding_type = cod.Coding()
    coding_type.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    coding_type.value = doc_type[0]
    coding_type.display = doc_type[2]

    coding_type2 = cod.Coding()
    coding_type2.system = "http://loinc.org"
    coding_type2.value = doc_type[1]
    coding_type2.display = doc_type[2]

    coco_type = cc.CodeableConcept()
    coco_type.coding = [coding_type, coding_type2]
    document_reference.type = coco_type

    #TODO: Check if logic is correct or nah
    coding_category = cod.Coding()
    coding_category.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    coding_category.value = doc_type[0]
    coding_category.display = doc_type[2]
    coding_category2 = cod.Coding()
    coding_category2.system = "http://loinc.org"
    coding_category2.value = doc_type[1]
    coding_category2.display = doc_type[2]
    coco_category = cc.CodeableConcept()
    coco_category.coding = [coding_category, coding_category2]
    document_reference.category = [coco_category]

    sub_ref = fr.FHIRReference()
    sub_ref.reference = "Patient/{}".format(patient)
    document_reference.subject = sub_ref

    context_ref = fr.FHIRReference()
    context = dr.DocumentReferenceContext()

    context_ref.reference = "Encounter/{}".format(encounter)
    context.encounter = [context_ref]

    document_reference.context = context

    attachment = att.Attachment()
    attachment.contentType = fake.att_content_type()
    url = fake.att_url()
    attachment.url = url[0] + fake.numerify(text='####') + url[1]

    if (random.choice([True, False])):
        title = fake.numerify(text="#######.###.xml")
    else:
        title = fake.numerify(text="########.###.pdf")

    attachment.title = title

    content1 = dr.DocumentReferenceContent()
    content1.attachment = attachment
    codingFormat = cod.Coding()
    codingFormat.display = url[1][1:]
    content1.format = codingFormat

    document_reference.content = [content1]

    #res = document_reference.create(smart.server)

    #return res['id']
    return document_reference

def generate_document_reference_with_set_reference(patient: p.Patient | None, encounter: e.Encounter | None) -> dr.DocumentReference:
    document_reference = dr.DocumentReference()
    if patient is None:
        patient = fake.get_patient_id()
    if encounter is None:
        encounter = fake.get_encounter_id()

    identifier = i.Identifier()
    ident_id = fake.doc_id()

    coding2 = cod.Coding()
    coding2.system = 'http://id-berlin.de/fhir/externalDocumentId'
    coding2.value = ident_id

    coding3 = cod.Coding()
    coding3.system = 'http://dmi.de/fhir/sid/document/9998'
    coding3.value = ident_id

    identifier.coding = [coding2, coding3]
    document_reference.identifier = [identifier]

    document_reference.active = True
    document_reference.status = fake.doc_ref_status()
    #TODO: Check why local fhir server doenst accept defined values (https://build.fhir.org/documentreference.html)
    #document_reference.docStatus = fake.doc_ref_doc_status()
    document_reference.editTime = fake.timestamp()

    doc_type = fake.doc_ref_type()

    coding_type = cod.Coding()
    coding_type.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    coding_type.value = doc_type[0]
    coding_type.display = doc_type[2]

    coding_type2 = cod.Coding()
    coding_type2.system = "http://loinc.org"
    coding_type2.value = doc_type[1]
    coding_type2.display = doc_type[2]

    coco_type = cc.CodeableConcept()
    coco_type.coding = [coding_type, coding_type2]
    document_reference.type = coco_type

    #TODO: Check if logic is correct or nah
    coding_category = cod.Coding()
    coding_category.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    coding_category.value = doc_type[0]
    coding_category.display = doc_type[2]
    coding_category2 = cod.Coding()
    coding_category2.system = "http://loinc.org"
    coding_category2.value = doc_type[1]
    coding_category2.display = doc_type[2]
    coco_category = cc.CodeableConcept()
    coco_category.coding = [coding_category, coding_category2]
    document_reference.category = [coco_category]

    sub_ref = fr.FHIRReference()
    sub_ref.reference = "Patient/{}".format(patient)
    document_reference.subject = sub_ref

    context_ref = fr.FHIRReference()
    context = dr.DocumentReferenceContext()

    context_ref.reference = "Encounter/{}".format(encounter)
    context.encounter = [context_ref]

    document_reference.context = context

    attachment = att.Attachment()
    attachment.contentType = fake.att_content_type()
    url = fake.att_url()
    attachment.url = url[0] + fake.numerify(text='####') + url[1]

    if (random.choice([True, False])):
        title = fake.numerify(text="#######.###.xml")
    else:
        title = fake.numerify(text="########.###.pdf")

    attachment.title = title

    content1 = dr.DocumentReferenceContent()
    content1.attachment = attachment
    codingFormat = cod.Coding()
    codingFormat.display = url[1][1:]
    content1.format = codingFormat

    document_reference.content = [content1]

    #res = document_reference.create(smart.server)

    #return res['id']
    return document_reference


def generate_document_reference() -> dr.DocumentReference:
    document_reference = dr.DocumentReference()
    patient = fake.get_patient_id()
    encounter = fake.get_encounter_id()

    identifier = i.Identifier()
    ident_id = fake.doc_id()

    coding2 = cod.Coding()
    coding2.system = 'http://id-berlin.de/fhir/externalDocumentId'
    coding2.value = ident_id

    coding3 = cod.Coding()
    coding3.system = 'http://dmi.de/fhir/sid/document/9998'
    coding3.value = ident_id

    identifier.coding = [coding2, coding3]
    document_reference.identifier = [identifier]

    document_reference.active = True
    document_reference.status = fake.doc_ref_status()
    document_reference.editTime = fake.timestamp()

    doc_type = fake.doc_ref_type()

    coding_type = cod.Coding()
    coding_type.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    coding_type.code = doc_type[0]
    coding_type.display = doc_type[2]

    coding_type2 = cod.Coding()
    coding_type2.system = "http://loinc.org"
    coding_type2.code = doc_type[1]
    coding_type2.display = doc_type[2]

    coco_type = cc.CodeableConcept()
    coco_type.coding = [coding_type, coding_type2]
    document_reference.type = coco_type

    coding_category = cod.Coding()
    coding_category.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    coding_category.code = doc_type[0]
    coding_category.display = doc_type[2]
    coding_category2 = cod.Coding()
    coding_category2.system = "http://loinc.org"
    coding_category2.code = doc_type[1]
    coding_category2.display = doc_type[2]
    coco_category = cc.CodeableConcept()
    coco_category.coding = [coding_category, coding_category2]
    document_reference.category = [coco_category]

    sub_ref = fr.FHIRReference()
    sub_ref.reference = "Patient/{}".format(patient)
    document_reference.subject = sub_ref

    context_ref = fr.FHIRReference()
    context = dr.DocumentReferenceContext()

    context_ref.reference = "Encounter/{}".format(encounter)
    context.encounter = [context_ref]

    document_reference.context = context

    attachment = att.Attachment()
    attachment.contentType = fake.att_content_type()
    url = fake.att_url()
    attachment.url = url[0] + fake.numerify(text='####') + url[1]

    if (random.choice([True, False])):
        title = fake.numerify(text="#######.###.xml")
    else:
        title = fake.numerify(text="########.###.pdf")

    attachment.title = title

    content1 = dr.DocumentReferenceContent()
    content1.attachment = attachment
    codingFormat = cod.Coding()
    codingFormat.display = url[1][1:]
    content1.format = codingFormat

    document_reference.content = [content1]

    #res = document_reference.create(smart.server)

    #return res['id']
    return document_reference
