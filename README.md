# FHIR-Testdaten Generator
Dieses Projekt ist ein Python-Skript welches mit Hilfe von Python Faker und SMART on fhir client zufällige Daten in Form von FHIR Resourcen generiert.

## Voraussetzungen
- Python Version 3.11.0 installiert
- Python Package fhirclient installiert
- Python Package Faker (26.2.0) ínstalliert

## Aufsetzen der Umgebung
- Falls noch nicht installiert: Installation von Python 3.11 (https://www.python.org/downloads/release/python-3110/)
- Klonen des Source-Codes von https://github.com/jku-dmi/fhir-data-generator.git
```
git clone https://github.com/jku-dmi/fhir-data-generator.git
```
- Installieren der Pakete fhirclient & Faker. In PyCharm funktioniert das über den Package Manager. 
  - Faker: https://faker.readthedocs.io/en/master/
  - fhirclient: https://github.com/smart-on-fhir/client-py?tab=readme-ov-file
- Installation von Docker (Desktop) (https://www.docker.com/)
- Installieren vom HAPI FHIR Server zur Datenvalidierung in Docker -> https://github.com/hapifhir/hapi-fhir-jpaserver-starter
  - Hierbei die Standard Ports und Einstellungen bestehen lassen, dann muss im Skript keine Anpassung vorgenommen werden.
    - Die Einstellungen für die Verbindung können unter [fhir_client.py](helpers/coding/fhir_client.py) angepasst werden.
- 