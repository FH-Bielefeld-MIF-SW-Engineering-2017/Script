# Index Table Pattern

Das Index Table Pattern dient zur Performance-Optimierung in Anwendungen,
die mit großen Mengen an persistierten Daten arbeiten.
Da insbesondere Abfragen anhand anderer Werte als des Primärschlüssels
besonders langsam werden können, bietet es die Möglichkeit,
weitere Schlüssel anlegen zu können.
In relationalen Datenbanken kann dieses Verhalten meist mittels
zusätzlicher Index-Spalten gelöst werden.
Das Index Table Pattern dient in anderen Fällen als eine Möglichkeit,
diese Funktionalität nachzubilden.

Bei der Umsetzung gibt es drei unterschliedliche Strategien:

- __Vollständige Duplizierung__  
  Sämtliche Daten pro zusätzlichem Schlüssel in einer zusätzlichen Tabelle
  abgelegt. Dabei findet eine _vollständige Denormalisierung_ statt.
  Problematisch bei häufigen Änderungen und im Bezug zur Speichermenge.
- __Normalisierte Index Tabellen__  
  Die neuen Tabellen enthalten jeweils nur den zusätzlichen Schlüssel
  und eine Referenz auf die ürsprüngliche Tabelle, den _Fact Table_.
  Problematisch, da in jedem Fall zwei Abfragen erfolgen müssen.
- __Teilnormalisierte Index Tabellen__  
  Ähnlich den normalisierten Tabellen, allerdings werden häufig
  verwendete Daten dupliziert und nur für die fehlenden eine
  Anfrage an den _Fact Table_ benötigt.
  Durch dieses Vorgehen erreicht man eine Balance zwischen den beiden
  anderen Fällen.

Darüber hinaus können auch Variationen umgesetzt werden,
wie ein Schlüssel, der aus mehreren Feldern des Fact Table besteht,
ein Ersatz für _Composite Keys_.
Ein Index Table kann auch verwendet werden, um den Zugriff auf Daten in
Shards zu optimieren. Dabei wird der für das Sharding gehashte
Primär Schlüssel als Referenz auf den geshardeten Fact Table verwendet.
Der Index Table bleibt dabei zusammenhängend.
