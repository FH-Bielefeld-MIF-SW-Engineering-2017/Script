# Fazit

Ein direkter Vergleich der vorgestellten Kommunikationsmethoden ist aufgrund ihrer Heterogenität nur schwer möglich. Es wurden eine Basistechnik, ein Netzwerkprotokoll, ein Architekturstil sowie eine Abfragesprache vorgestellt, welche zwar im Allgemeinen dem Informationstausch dienen, diesen jedoch auf verschiedenen Ebenen unterstützen. Welche Methode Anwendung finden sollte, hängt immer von der jeweiligen Problemstellung ab und ist nicht generell vorherzusagen. Die nachfolgende Gegenüberstellung soll die jeweiligen Anwendungsgebiete trotzdem grob verdeutlichen und somit Klarheit bezüglich der Verwendung schaffen \(siehe Tab. 5\).

| Kommunikationsmethode / Eignung: | Geeignet für: | Ungeeignet für: |
| :--- | :--- | :--- |
| **RPC** | Auslagerung von Methodenlogik | Datenlastige Nachrichtenaustausche |
| **WebSocket** | Echtzeitanwendungen | Statische bzw. unkritische Daten |
| **REST** | Öffentliche Dienste mit standardisierter Schnittstelle, Austausch von einheitlichen Datenobjekten | Methodenaufrufe, kontinuierlich angepasste Datentypen |
| **GraphQL** | Austausch von kontinuierlich angepassten Datentypen / -objekten | Methodenaufrufe |

Tabelle 5: Gegenüberstellung Kommunikationsmethoden

