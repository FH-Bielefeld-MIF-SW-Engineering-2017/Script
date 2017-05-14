# 

# Health Endpoint Monitoring Pattern

Ziel des Patterns ist es funktionale Checks innerhalb einer Anwendung auszuführen, deren Resultate von externen Applikationen über entsprechende Zugangspunkte in bestimmten Intervalen abgerufen werden können. Das Pattern hilft somit die korrekte Ausführung verschiedener Applikationen und Services zu gewährleisten.

#### Problematik

Es ist üblich bzw. in vielen Fällen eine feste Voraussetzung, dass Webapplikationen oder Services auf ihre korrekte Ausführung überprüft werden. Bei einem Service in der Cloud kommen jedoch neue Abhängigkeiten und potenzielle Problemquellen dazu. Der eigene Service hängt von anderen Services des Plattformanbieters ab, über dessen Service und Hostingumgebung man keine volle Kontrolle hat.

Auch hängt die Performance und Verfügbarkeit letzten Endes von der Hardware und der Netzwerkstärke des Clouddienstleisters ab. Es ist also zwingend notwendig in regulären Abstände die Verfügbarkeit der eigenen Services in der Cloud zu überprüfen.

#### Lösung

Das Pattern besteht aus 2 wesentlichen Vorgängen bzw. Element. Zum einen aus dem Kontroll-Tool das die Kontrollanfrage an einen frei konfigurierbaren Endpunkt einer Cloud Applikation stellt und zum anderen die Cloud Applikation die auf Anfrage ihre jeweiligen Checks durchführt. Diese können Kontrollen von weiteren genutzten Services inkludieren, sowie Kontrollen der Datenbankanbindungen und des Cloudspeichers. Ein entsprechender Response Code wird an das Kontroll-Tool zurück gesendet, der die Ergebnisse der Kontrollen ausdrückt \(siehe Abbilung 1\).

![](/assets/health_monitoring_1.jpg)\(Abbildung 1: Übersicht des Patterns\)









