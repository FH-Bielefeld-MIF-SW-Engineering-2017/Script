## XMPP
### Struktur & Nutzen
Das Extensible Messaging and Presence Protocol (XMPP, früher Jabber) wurde zur Nachrichten Übertragung zwischen Benutzern entwickelt. Unter anderem wird es daher zum Instant Messaging eingesetzt. Es wurde sowohl von Google als auch von Facebook für ihre jeweiligen Messanger benutzt. Es basiert auf dem TCP Protokoll und nutzt zur Nachrichtenübertragung den XML Standard. Das Protokoll ist qulloffen und die Entwicklung begann 1998.  Standardisiert wurde es 2004 von der IETF. Aber Schon 2003 wurde es von über 10.000.000 Menschen genutzt [21](Quellen.md). 
### Features
XMPP bietet Funktionen zum Nachrichtenaustausch zwischen zwei, aber auch mehreren Benutzern, kann den Onlinestatus übermitteln und Dateien und Zertifikate übertragen. Ähnlich wie alle anderen vorgestellten Protokolle nutzt XMPP einen Server um die Nachrichten der Nutzer zu verteilen. Jeder der Server kann mit anderen XMPP Servern kommunizieren, sodass die Kommunikation dezentraler wird.  Um Nutzer zu identifizieren hat jeder Nutzer eine ID (JID). Diese ist einer Email Adresse sehr ähnlich und besteht aus einem Namen und einem Server, bei welchem sich der Nutzer befindet. Zusammengesetzt werden beide Daten mit einem @, sodass eine JID die Form „alice@example.com“ hat [21](Quellen.md). 
Durch die Möglichkeit Server untereinander zu verbinden, können auch Gateways entstehen, sodass ein XMPP Nutzer mit einem Nutzer eines Anderen Protokolls kommunizieren kann.  

![alt text](/assets/xmpp.png/ "xmpp Ablauf")

XMPP kann durch verschiedene „Extensions“ erweitert werden, sodass es auch Implementierungen für Sprachnachrichten gibt. Diese Erweiterungen ermöglichen es aber auch XMPP im IoT Umfeld zu nutzen. Dieses hat den Vorteil, dass das Protokoll komplett quelloffen ist und durch die Server Kommunikation gut skalierbar ist [21](Quellen.md) [22](Quellen.md) [23](Quellen.md).  Gegen die Anwendung im IoT Umfeld spricht aber, dass das Protokoll durch die verwendeten XML Nachrichten sehr viel Overhead hat. Dadurch ist es grade auf Low Power Systemen schwierig zu nutzen 
### Sicherheit
Auch XMPP basiert auf dem TCP Protokoll, sodass TLS/SSL verwendet werden können. Um eine Ende zu Ende Verschlüsslung zu erzielen, können auch hier die Nutzdaten wiederrum verschlüsselt werden[21](Quellen.md).  

### IoT Verwendung
Tendenziell eignet sich XMPP gut für den Einsatz im IoT. Das Protokoll verfügt über viele Features (Many-to-Many, Online Status, Server-to-Server, [...]) die im IoT Umfeld sinvoll erscheinen.
Allerdings sind die Nachrichten durch das verwendete XML Format sehr lang,  sodass es zu einem erhelblichen Overhead kommt [24](Quellen.md). Dieses kann grade auf kleinen eingebetteten Geräten zu Problemen führen. 
