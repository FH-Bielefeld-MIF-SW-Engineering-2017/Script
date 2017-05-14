# 

# Health Endpoint Monitoring Pattern

Ziel des Patterns ist es funktionale Checks innerhalb einer Anwendung auszuführen, deren Resultate von externen Applikationen über entsprechende Zugangspunkte in bestimmten Intervalen abgerufen werden können. Das Pattern hilft somit die korrekte Ausführung verschiedener Applikationen und Services zu gewährleisten.

#### Problematik

Es ist üblich bzw. in vielen Fällen eine feste Voraussetzung, dass Webapplikationen oder Services auf ihre korrekte Ausführung überprüft werden. Bei einem Service in der Cloud kommen jedoch neue Abhängigkeiten und potenzielle Problemquellen dazu. Der eigene Service hängt von anderen Services des Plattformanbieters ab, über dessen Service und Hostingumgebung man keine volle Kontrolle hat.

Auch hängt die Performance und Verfügbarkeit letzten Endes von der Hardware und der Netzwerkstärke des Clouddienstleisters ab. Es ist also zwingend notwendig in regulären Abstände die Verfügbarkeit der eigenen Services in der Cloud zu überprüfen.

#### Das Pattern

Das Pattern besteht aus 2 wesentlichen Vorgängen bzw. Element. Zum einen aus dem Kontroll-Tool das die Kontrollanfrage an einen frei konfigurierbaren Endpunkt einer Cloud Applikation stellt und zum anderen die Cloud Applikation die auf Anfrage ihre jeweiligen Checks durchführt. Diese können Kontrollen von weiteren genutzten Services inkludieren, sowie Kontrollen der Datenbankanbindungen und des Cloudspeichers. Ein entsprechender Response Code wird an das Kontroll-Tool zurück gesendet, der die Ergebnisse der Kontrollen ausdrückt \(siehe Abbildung 1\).

![](/assets/health_monitoring_1.jpg)\(Abbildung 1: Übersicht des Patterns\)

Das Kontroll-Tool analysiert anschließend des gesendet Response Code gegen seit Set von frei konfigurierbaren Regeln, die festlegen wie welche Ergebnisse zu bewerten sind.

Zusätzlich können weitere Checks durchgeführt werden.

* Detaillierte Analyse über den Inhalt der Antwort abseits des Codes, der weitere Information über potenziell teilweise fehlgeschlagene Tests geben könnnte, selbst wenn der Resonse Code 200\(OK\) war
* Das Messen der Antwortzeit zur Überprüfung der Performance der Applikation und der Netzwerkgeschwindigkeit
* Auslaufende SSL Zertifikate abfragen
* Messen eines DNS Lookups auf die URL der Applikation, sowie Kontrolle der zurückgegebene URL des DNS Lookups auf ihre Korrektheit 

Es ist empfehlenswert die Tests von verschiedenen Kontroll-Tools von der verschiedenen Standorten abfragen zu lassen um evtl. Unterschiede ausfindig zu machen. Die Tests sollten auch gegen Service-Instanzen von Kunden laufen, wenn also ein Kunde seinen Cloudspeicher auf mehre Standorte verteilt hat müssen alle Standorte kontrolliert werden.

#### Ausführung: Was mach beachten sollte

* Wie genau sollten die Antwort der Cloud Applikation aussehen? Der minimalste Ansatz, ein simpler HTML Repsonse Code, könnte potenziell nicht genug Informationen vermitteln. Dies wird jedoch bei den meisten Implementationen genutzt.
* Mehrere Endpunkte für unterschiedliche Services innerhalb der Applikation konfigurieren, so sollte jeder Check \(Datenbank, Storage..\) einzeln angesprochen werden können oder über einen weiteren Endpunkt übergreifend

* Den gleichen Endpunkt benutzen, der auch für den generellen Zugriff genutzt wird um über spezifische Pfade auch direkt Funktionale Tests auszuführen \(z.B. einen User anlegen\)

* Sollten zuviele Ressourcen der Cloud Applikation für die Checks verwendet werden, könnte dies die Usererfahrung beeinflussen. In der Regel können Logs über Fehler und Performance Counter bereits genug aussagen und machen ausgiebige Performance Checks daher unnötig.

* Sicherheit der Endpunkte: Zugriff nur mit Authentifikation / 'versteckte' Endpunkte über unübliche Ports & verschiedene IP Adressen / Endpunkte so konfigurieren das sie bestimmte Informationen über die gewünschten Tests benötigen, andernfalls werden Anfragen abgewiesen

  * Zugriff auf gesicherte Endpunkte: Nicht alle Tools Unterstützen in ihre eingebauten health-verification Features auch Authentifizierung. Drittpartyanbieter wie Pingdom, Panopta, NewRelic oder Statuscake helfen hier.

* Auch die Kontrolltools müssen getestet werden, z.B. indem eine Cloud Applikationen ein festen OK Response auf einem Endpoint sendet, den das Kontrolltool auslesen sollte.





