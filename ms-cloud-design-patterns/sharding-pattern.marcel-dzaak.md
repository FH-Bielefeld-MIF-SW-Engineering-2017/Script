# Sharding Pattern
Die Idee ist es große Datenmengen in mehrere horizontale "Splitter"(Shards) aufzuteilen, um die Skalierbarkeit zu verbessern.

## When to use
Wenn die Daten die Ressourcen einer einzelnen Datenbank übersteigen werden.
Um die Performance zu steigern, indem die Zugriffskonflikte minimiert werden.

## Problemstellung
Eine Datenbank auf einem einzigen Server wird sich früher oder später mit den Folgenden Themen befassen müssen:
Speicherplatz
Rechenleistung
Netzwerkbandbreite
Datenverteilung

Diese Punkte durch "aufrüsten" auszubauen, verschiebt lediglich das Problem in die Zukunft.

## Sharding als Lösung
Die Datenbank wird in mehrere Splitter aufgeteilt. Jeder Splitter verfügt über das gleiche Schema, enthält jedoch nur eine individuelle Menge der Gesamten Datenmenge.

Für das Aufteilen von Daten auf die einzelnen Splitter werden "shard keys" oder "partition keys" verwendet. Dieser Schlüssel muss statisch sein.

Sharding organisiert die Daten, die Logic sorgt bei einem Zugriff der Applikation dafür, das die angeforderten Daten aufgefunden werden.

## Vorteile
Jederzeit erweiterbar, durch das Hinzufügen von weiteren Splittern.
Zugriffskonflikte können reduziert und Performance gesteigert werden, durch ein Ausbalancieren des Workloads der einzelnen Splitter.
In einer Cloudlösung können die Splitter "nah" am User platziert werden.

## Nachteile
Daten der Splitter müssen ausgeglichen werden, um für eine hohe Performance zu sorgen.

## Sharding Strategies
Für die Vergabe von "shard keys" und das Verteilen der Daten, gibt es 3 gängige Strategien, welche im Folgenden skizziert werden.

### The Lookup strategy
Hier liegen alle benötigten Daten (für einen Teil einer Abfrage) auf einem einzigen Shard.
Vorteile: Mehr Kontrolle über die Konfigurationen der Shards.
Nachteile: Overhead durch das aufsuchen mehrere Speicherorte(Shards)

### The Range strategy
Häufig zusammen abgefragte Daten, bspw. in einem Query, werden zusammen in einem Splitter gespeichert.
Vorteile: Einfach zu implementieren. Einfaches Datenmanagement
Nachteile: Keine optimale Balance zwischen den Shards. Rebalancing ist schwer.

### The Hash strategy
Aus mehreren Attributen werden Hashes gebildet, welche abgefragt werden können. Durch diese Strategie soll ein Balance der Zugriffe unter den Shards erreicht werden. Dies ist vor allem sinnvoll in Umgebungen, mit sehr vielen Zugriffen.
Vorteile: Hashermittlung kann Overhead erzeugen. Rebalancing ist schwer.






