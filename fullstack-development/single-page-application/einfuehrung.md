# Single Page Application

Eine Singe Page Application ist eine Web-Applikation, die lediglich aus einem einzigen HTML Dokument besteht und soll dadurch eine Nutzererfahrung ähnlich der einer Desktop-Applikation bieten. Der komplette Seiteninhalt \( HTML, Javascript und CSS\) wird dabei entweder beim initialen Laden der Seite übermittelt oder einzelne logische Seiten innerhalb der SPA dynamisch nachgeladen, in Abhängigkeit mit den Aktionen des Nutzers. Mit SPAs wird die Grundlage für eine Rich-Client bzw. Fat-Client-Architektur geboten, in der ein Großteil der Ausführung einer Webanwendung auf Clientseite geschieht und somit die Serverlast reduziert wird.

### Eigenschaften

* Der Sitzungszustand wird bei dem Client gespeichert, der Server stellt hingegen lediglich noch die Nutzdaten zur Verfügung. Ein erneutes LAden der SPA ist mit einem Neustart einer Anwendung gleichzusetzen.
* Serverseitige Funktionalitäten daher Zustandslos
* "offline-friendly", Nutzungsdaten können im local storage zwischengespeichert werden, die SPA kann so auch bei Verbindungsverlust weiter laufen

* WebClient fungieren als unabhängige Einheit mit verschiedenen Services und kann somit selbstständig auf Benutzerinteraktionen reagieren. Dadurch wird der Datenverkehrt zum Server verringert

* WebClient und Serverseite können separat entwickelt werden, lediglich die Schnittstellen für die Services müssen vorher definiert werden.



