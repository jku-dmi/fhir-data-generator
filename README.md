# FHIR-Testdaten Generator
Dieses Projekt ist ein Python-Skript welches mithilfe von Python Faker und SMART on fhir client zufällige Daten in Form von FHIR Ressourcen generiert.

## Voraussetzungen
- Python Version 3.11.0 installiert
- Python Package fhirclient installiert
- Python Package requests installiert
- Python Package Faker (26.2.0) ínstalliert

## Aufsetzen der Umgebung
- Falls noch nicht installiert: Installation von [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- Klonen des Source-Codes von [github](https://github.com/jku-dmi/fhir-data-generator.git)
```
git clone https://github.com/jku-dmi/fhir-data-generator.git
```
- Einstellen des Python Interpreter (In Pycharm unten rechts)
- Installieren der Pakete fhirclient & Faker. In PyCharm funktioniert das über den Package Manager. 
  - [Faker](https://faker.readthedocs.io/en/master/)
  - [fhirclient](https://github.com/smart-on-fhir/client-py?tab=readme-ov-file)
  - [requests](https://pypi.org/project/requests/)
- Installation von [Docker (Desktop)](https://www.docker.com/)
- Installieren vom [HAPI FHIR Server](https://github.com/hapifhir/hapi-fhir-jpaserver-starter) in Docker 
  - Hierbei die Standard Ports und Einstellungen bestehen lassen, dann muss im Skript keine Anpassung vorgenommen werden.
    - Die Einstellungen für die Verbindung können unter [fhir_client.py](util/fhir_client.py) angepasst werden.
 

## Ausführen der Datengenerierung
In der Datei [main.py](main.py) ist die Methode zur Datengenerierung bereits aufgerufen. 

Dort müssen nur noch die Anzahl der zu generierenden Ressourcen als Parameter übergeben werden. Der letzte Parameter gibt die Größe eines Bundles an, welches dann an den Server gesendet wird.

## Ausführen der Abfragen
Der Code zur Ausführung der einzelnen Abfragen befindet sich ebenfalls in der [main.py](main.py). Dieser ist jedoch auskommentiert.

Dieser kann benutzt werden um die einzelnen Abfragen über die entsprechende Methode (abfrage1() - abfrage4()) durchzuführen.
Dafür muss nur der Methodenaufruf durch den gewünschten ersetzt werden.