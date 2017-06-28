## Vergleich und Fazit
|  | MQTT | REST | CoAP | AMQP | XMPP |
| ------------- | ------------- | ------------- |  ------------- | ------------- | ------------- |
| Protokoll | TCP | TCP | UDP | TCP | TCP |
| Push Nachrichten | Ja | Nein | Ja | Ja| Ja |
| Online Status \*\*\*| Ja | Nein | Nein |  Nein | Ja |
| IoT Optimiert | Ja | Nein | Ja | Ja | mit Extension |
| QoS | Ja | Nein | Ja | Ja | Nein |
| Many2Many | Ja | Nein | Nein | Ja | Ja |
| Arduino Library | Ja | Ja | Ja | Nein | Ja |
| Minimal Header | 2 Byte * [27](Quellen.md) | 26 Byte* [25](Quellen.md) | 4 Byte ** [27](Quellen.md) | 8 Byte* [26](Quellen.md) | 83 Byte* [24](Quellen.md) | 

\* Zusätzlich 64 Byte für darunterliegende Protokolle
\** Zusätzlich 52 Byte für darunterliegende Protokolle

\*\*\* Kommunikationspartner merkt, wenn Problem vorliegt (Online Status / LastWill)





Grundsätzlich lassen sich alle Protokolle mittels Kryptographie so verschlüsseln, dass es dritten nahezu unmöglich ist, die gesendeten Nachrichten mitzulesen. Aber alle vorgestellten Protokolle haben ihre Vor- und Nachteile, sodass bei der Auswahl eines Protokolls immer auf den genauen Anwendungsfall geschaut werden muss. Grade die Kombination der Protokolle kann es Verteilten Systemen ermöglichen äußerst vielseitig eingesetzt zu werden. Hier fällt besonders die Kombination REST / CoAP auf, da CoAP zu diesem Anwendungsfall konstruiert wurde. Aber auch andere Protokoll Kombinationen sind denkbar.
