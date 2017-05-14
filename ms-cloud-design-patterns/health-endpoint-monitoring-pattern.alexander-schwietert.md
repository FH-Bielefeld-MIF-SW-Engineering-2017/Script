# 

# Health Endpoint Monitoring Pattern

Ziel des Patterns ist es funktionale Checks innerhalb einer Anwendung auszuführen, deren Resultate von externen Applikationen über entsprechende Zugangspunkte in bestimmten Intervalen abgerufen werden können. Das Pattern hilft somit die korrekte Ausführung verschiedener Applikationen und Services zu gewährleisten.

#### Problematik

Es ist üblich bzw. in vielen Fällen eine feste Voraussetzung, dass Webapplikationen oder Services auf ihre korrekte Ausführung überprüft werden. Bei einem Service in der Cloud kommen jedoch neue Abhängigkeiten und potenzielle Problemquellen dazu. Der eigene Service hängt von anderen Services des Plattformanbieters ab, über dessen Service und Hostingumgebung man keine volle Kontrolle hat.

Auch hängt die Performance und Verfügbarkeit letzten Endes von der Hardware und der Netzwerkstärke des Clouddienstleisters ab. Es ist also zwingend notwendig in regulären Abstände die Verfügbarkeit der eigenen Services in der Cloud zu überprüfen.

#### Lösung

Das Pattern besteht aus 2 wesentlichen Vorgängen bzw. Element. Zum einen aus dem Kontroll-Tool das die Kontrollanfrage an einen frei konfigurierbaren Endpunkt einer Cloud Applikation stellt und zum anderen die Cloud Applikation die auf Anfrage ihre jeweiligen Checks durchführt. Diese können Kontrollen von weiteren genutzten Services inkludieren, sowie Kontrollen der Datenbankanbindungen und des Cloudspeichers. Ein entsprechender Response Code wird an das Kontroll-Tool zurück gesendet, der die Ergebnisse der Kontrollen ausdrückt \(siehe Abbilung 1\).

![](/assets/health_monitoring_1.jpg)\(Abbildung 1: Übersicht des Patterns\)

Das Kontroll-Tool analysiert anschließend des gesendet Response Code gegen seit Set von frei konfigurierbaren Regeln, die festlegen wie welche Ergebnisse zu bewerten sind.

Zusätzlich können weitere Checks durchgeführt werden.

* Detaillierte Analyse über den Inhalt der Antwort abseits des Codes, der weitere Information über potenziell teilweise fehlgeschlagene Tests geben könnnte, selbst wenn der Resonse Code 200\(OK\) war
* Das Messen der Antwortzeit zur Überprüfung der Performance der Applikation und der Netzwerkgeschwindigkeit
* Auslaufende SSL Zertifikate abfragen
* Messen eines DNS Lookups auf die URL der Applikation, sowie Kontrolle der zurückgegebene URL des DNS Lookups auf ihre Korrektheit 

Es ist empfehlenswert die Tests von verschiedenen Kontroll-Tools von der verschiedenen Standorten abfragen zu lassen um evtl. Unterschiede ausfindig zu machen. Die Tests sollten auch gegen Service-Instanzen von Kunden laufen, wenn also ein Kunde seinen Cloudspeicher auf mehre Standorte verteilt hat müssen alle Standorte kontrolliert werden.





