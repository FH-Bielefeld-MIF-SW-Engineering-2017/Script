# Health Endpoint Monitoring Pattern

Ziel des Patterns ist es funktionale Checks innerhalb einer Anwendung auszuführen, deren Resultate von externen Applikationen über entsprechende Zugangspunkte in bestimmten Intervalen abgerufen werden können. Das Pattern hilft somit die korrekte Ausführung verschiedener Applikationen und Services zu gewährleisten.

#### Problematik

Es ist üblich bzw. in vielen Fällen eine feste Voraussetzung, dass Webapplikationen oder Services auf ihre korrekte Ausführung überprüft werden. Bei einem Service in der Cloud kommen jedoch neue Abhängigkeiten und potenzielle Problemquellen dazu. Der eigene Service hängt von anderen Services des Plattformanbieters ab, über dessen Service und Hostingumgebung man keine volle Kontrolle hat.

Auch hängt die Performance und Verfügbarkeit letzten Endes von der Hardware und der Netzwerkstärke des Clouddienstleisters ab. Es ist also zwingend notwendig in regulären Abstände die Verfügbarkeit der eigenen Services in der Cloud zu überprüfen.

#### Lösung





