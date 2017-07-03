## CoAP
### Protokollübersicht
Das “constrained application protocol” (CoAP) basiert auf dem REST Architekturmodell. Es wurde 2014 von der Internet Engineering Task Force (IETF) als RFC eingereicht und ist als Protokoll zur Machine to Machine (M2M) Kommunikation im Internet of Things (IoT) gedacht. Es eignet sich besonders für diese Art der Kommunikation, da es nicht wie das normale Rest Modell auf http und damit TCP setzt, sondern die Daten über UDP ausgetauscht werden. Damit kann der durch das Protokoll entstehende Overhead deutlich reduziert werden. Deshalb ist diese Art der Datenübertragung für das Umfeld von Low Power Geräten besser geeignet. 
CoAP wurde zusätzlich so gestaltet, dass eine Nachricht ohne großen Aufwand auf eine normale REST Schnittstelle umgeleitet werden kann. So wurden die vier Grundfunktionen von REST (Get, Post, Put, Delete) als Aktionen in CoAP übernommen. Auch werden Ressourcen grundsätzlich mit einer URI identifiziert [13](Quellen.md).    
 Zusätzlich wurden aber weitere Funktionen, die grade im IoT Umfeld nützlich sind, hinzugefügt. 
### Observe
Anders als bei REST, können die vier Standardoperationen auch zu einer langanhaltenden, zustandsbehafteten Kommunikation genutzt werden. Wird das Observe Flag im Header einer CoAP Nachricht gesetzt, wird zuerst die gewünschte Ressource übertragen. Anschließend kann der Server aber bei Änderungen der Ressource diese sofort wieder an den Client übertragen, ohne dass dieser erneut danach fragt. Beide Kommunikationspartner können gleichermaßen die „Beobachtung“ beenden [6](Quellen.md).    
### Resource Discovery
Server stellen an einem bestimmten Pfad („/.well-known/core“) eine Liste der verfügbaren Ressourcen zur Verfügung. Diese Liste kann von Clients genutzt werden, um nach Ressourcen zu suchen [14](Quellen.md). 
### Confirmable und Non-Confirmable Nachrichten
Bei REST wird durch das TCP Protokoll jede Nachricht zu nahezu 100% zugestellt. Hierzu werden die Nachrichten durch ein „ACK“ von Empfänger bestätigt. Obwohl CoAP auf UDP setzt, eine solche Funktion also nicht im darunterliegenden Protokoll verfügbar ist, können wichtige Nachrichten als solche gekennzeichnet werden, sodass eine Empfangsbestätigung vom Empfänger gesendet werden muss. Allerdings lässt sich dieses Feature für jede Nachricht getrennt definieren, sodass es auch, für „unwichtige“ Daten den Nachrichtentyp „Non-Confirmable“ gibt – „fire'n'forget“ [9](Quellen.md).  

![alt text]("/assets/coap.png/" "CoAP Confirmable und Non-Confirmable")

### Sicherheit
Da CoAP nicht auf TCP basiert, sind SSL und TLS nicht einfach zu nutzen. Um trotzdem eine Verschlüsselung zu bieten nutzt CoAP „Datagram Transport Layer Security“ (DTLS) [15](Quellen.md). Dieses basiert weitestgehend auf TLS und bietet den Clients eine RSA oder AES Verschlüsslung [16](Quellen.md).      

### IoT Verwendung
Das Proktokoll eignet sich sehr gut für den Einsatz im IoT. Besonders die gute Kombination mit REST fallen positiv auf.
