import random

import fhirclient.models.documentreference as dr
import fhirclient.models.identifier as i
import fhirclient.models.coding as cod
import fhirclient.models.fhirreference as fr
import fhirclient.models.attachment as att
import fhirclient.models.codeableconcept as cc

from helpers.fhir_client import getClient
from helpers.faker_instance import getFaker

smart = getClient()
fake = getFaker()
def generate_document_reference() -> dr.DocumentReference:
    document_reference = dr.DocumentReference()
    patient = fake.get_patient_id()
    encounter = fake.get_encounter_id()

    identifier = i.Identifier()
    identId = fake.doc_id()

    coding2 = cod.Coding()
    coding2.system = 'http://id-berlin.de/fhir/externalDocumentId'
    coding2.value = identId

    coding3 = cod.Coding()
    coding3.system = 'http://dmi.de/fhir/sid/document/9998'
    coding3.value = identId


    identifier.coding = [coding2, coding3]
    document_reference.identifier = [identifier]

    document_reference.active = True
    document_reference.status = fake.doc_ref_status()
    #TODO: Check why local fhir server doenst accept defined values (https://build.fhir.org/documentreference.html)
    #document_reference.docStatus = fake.doc_ref_doc_status()
    document_reference.editTime = fake.timestamp()

    docType = fake.doc_ref_type()

    codingType = cod.Coding()
    codingType.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    codingType.value = docType[0]
    codingType.display = docType[2]

    codingType2 = cod.Coding()
    codingType2.system = "http://loinc.org"
    codingType2.value = docType[1]
    codingType2.display = docType[2]

    cocoType = cc.CodeableConcept()
    cocoType.coding = [codingType, codingType2]
    document_reference.type = cocoType

    codingCategory = cod.Coding()
    codingCategory.system = "http://dvmd.de/fhir/CodeSystem/kdl"
    codingCategory.value = docType[0]
    codingCategory.display = docType[2]
    codingCategory2 = cod.Coding()
    codingCategory2.system = "http://loinc.org"
    codingCategory2.value = docType[1]
    codingCategory2.display = docType[2]
    cocoCategory = cc.CodeableConcept()
    cocoCategory.coding = [codingCategory, codingCategory2]
    document_reference.category = [cocoCategory]

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


    if(random.choice([True, False])):
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
