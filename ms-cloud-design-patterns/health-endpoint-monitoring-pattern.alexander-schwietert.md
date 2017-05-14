# 

# Health Endpoint Monitoring Pattern

Ziel des Patterns ist es funktionale Checks innerhalb einer Applikation auszuführen. Diese werden von externen Kontroll-Tools über entsprechende Zugangspunkte angestoßen und in bestimmten Intervalen abgerufen. Das Pattern hilft somit die korrekte Ausführung verschiedener Applikationen und Services zu gewährleisten.

#### Einsatzgebiet

* Webseiten und Webapplikationen auf Verfügbarkeit und korrekte Funktionsweise überwachen
* Middle-tier oder geteilte Services überwachen, um Fehlerquellen zu isolieren, die andere Applikationen beeinflussen könnten
* Zum Erweitern von bereits vorhandenen Überwachungselementen wie dem Logging und protokollierte Performanzkennzahlen einer Applikation

#### Problematik

Es ist üblich bzw. in vielen Fällen eine feste Voraussetzung, dass Webapplikationen oder Services auf ihre korrekte Ausführung überprüft werden. Bei einem Service in der Cloud kommen jedoch neue Abhängigkeiten und potenzielle Problemquellen dazu. Der eigene Service hängt potenziell von weiteren Services des Plattformanbieters oder anderen ab und über die Hostingumgebung hat man keine volle Kontrolle.

Auch hängt die Performance und Verfügbarkeit letzten Endes von der Hardware und der Netzwerkverbindung des Clouddienstleisters ab. Es ist also zwingend notwendig in regulären Abständen die Verfügbarkeit der eigenen Services in der Cloud zu überprüfen.

#### Das Pattern

Das Pattern besteht aus 2 wesentlichen Vorgängen bzw. Elementen. Zum einen aus dem Kontroll-Tool, das die Kontrollanfrage an einen frei konfigurierbaren Endpunkt einer Cloud Applikation stellt. Zum anderen die Cloud Applikation, die auf Anfrage ihre jeweiligen Checks durchführt. Diese können Kontrollen von weiteren genutzten Services inkludieren, sowie Kontrollen der Datenbankanbindungen und des Cloudspeichers. Ein entsprechender Response Code wird an das Kontroll-Tool zurückgesendet \(siehe Abbildung 1\).

![](/assets/health_monitoring_1.jpg)\(Abbildung 1: Übersicht des Patterns\)

Das Kontroll-Tool analysiert anschließend den gesendeten Response Code gegen ein Set von frei konfigurierbaren Regeln, die festlegen wie welche Ergebnisse zu bewerten sind.

Zusätzlich können weitere Checks durchgeführt werden.

* Detaillierte Analyse des Inhalts der Antwort abseits des Codes, der z.B. weitere Information über teilweise fehlgeschlagene Tests geben könnte, selbst wenn der gegebene Response Code 200\(OK\) war
* Das Messen der Antwortzeit zur Überprüfung der Performance der Applikation und der Netzwerkgeschwindigkeit
* Auslaufende SSL Zertifikate abfragen
* Messen eines DNS Lookups auf die URL der Applikation, sowie Kontrolle der zurückgegebenen URL des DNS Lookups auf ihre Korrektheit 

Es ist empfehlenswert die Tests von verschiedenen Kontroll-Tools von verschiedenen Standorten abfragen zu lassen um evtl. Unterschiede in der Verbindung ausfindig zu machen. Dies kann potenziell auch die Wahl beeinflussen wo eine Applikation deployt wird. Die Tests sollten auch gegen die Service-Instanzen von Kunden laufen, um zu überprüfen ob die Applikation für alle Kunden korrekt funktioniert. Wenn also ein Kunde seinen Cloudspeicher auf mehre Standorte verteilt hat müssen alle Standorte kontrolliert werden.

#### Implementierung: Was man beachten sollte

* Wie genau sollten die **Antwort der Cloud Applikation** aussehen? Der minimalste Ansatz, ein simpler HTML Response Code, könnte potenziell nicht genug Informationen übermitteln.

* **Mehrere Endpunkte** für unterschiedliche Services innerhalb der Applikation konfigurieren, so sollte jeder Check \(Datenbank, Storage..\) einzeln angesprochen werden können oder über einen weiteren Endpunkt übergreifend. Für den jeweiligen Endpunkt können unterschiedliche Regeln \(z.B. erwartete Antwortzeiten\) definiert werden.

* Man kann den gleichen Endpunkt benutzen, der auch für den generellen Zugriff genutzt wird um über die jeweiligenPfade auch direkt** funktionale Tests** auszuführen \(z.B. einen User anlegen mit /applikation-url/create & /applikation-url/healthcheck/id für den regulären Check\)

* Sollten zu viele **Ressourcen der Cloud Applikation **für die Checks verwendet werden, könnte dies die Usererfahrung beeinflussen. In der Regel können Logs über Fehler und Performanzzähler bereits genug aussagen und machen ausgiebige Performance Checks daher unnötig.

* **Sicherheit **der Endpunkte: Zugriff nur mit Authentifikation / 'versteckte' Endpunkte über unübliche Ports & verschiedene IP Adressen / Endpunkte so konfigurieren das sie bestimmte Informationen über die gewünschten Tests benötigen, andernfalls werden Anfragen abgewiesen

  * Zugriff auf gesicherte Endpunkte: Nicht alle Tools Unterstützen in ihre eingebauten health-verification Features auch Authentifizierung. Drittparty Anbieter wie Pingdom, Panopta, NewRelic oder Statuscake helfen hier.

* Auch die **Kontrolltools müssen getestet werden**, z.B. indem eine Cloud Applikationen ein festen OK Response auf einem Endpunkt sendet, den das Kontrolltool auslesen korrekt auslesen sollte.

#### Microsoft Azure

Applikationen die auf einer Microsoft Azure Umgebung gehostet werden, können bereits eingebaute Services der Plattform nutzen.

Der **Azure Management Service** bietet dabei die Möglichkeit bis zu 10 Regeln festzulegen, die durch einen Grenzwert definiert werden. Dieser kann sich z.B. auf die CPU Auslastung oder die Fehler pro Sekunde bei Anfragen beziehen. Bei Überschreitung der festgelegten Werte wird Alarm gegeben und der Nutzer per Email informiert.

Welche Konditionen überwacht werden können hängt von der Applikation und der Hostumgebung ab, nutzen jedoch in jedem Fall vom Nutzer definierte Endpunkte um die Kontrollen abzufragen.

Für virtuelle Maschinen oder Webapplikationen kann ein sogenannter **Traffic Manager **zusätzlich HTML Request stellen, die z.B. die Verfügbarkeit von Webseiten checken.

