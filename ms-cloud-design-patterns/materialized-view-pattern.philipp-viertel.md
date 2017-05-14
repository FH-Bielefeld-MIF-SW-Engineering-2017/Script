# Materialized View Pattern

## Context und Problem

Die Speicherung von Daten geschieht oft unter der Perspektive der reinen Datenspeicherung und berücksichtigt dabei nicht die Frage, wie die Daten gelesen werden sollen. Die Daten werden gemäß ihrer Typen gespeichert (z.B. Zahlen, Strings, usw.) und nach dem Schema des Datenmodells wie z.B. NoSQL oder relational.

Bei einer Datenabfrage ("Query"), welche nur eine Teilmenge der Daten benötigt, die jedoch über verschiedene Entitäten hinweg gespeichert wurden, müssen all diese Entitäten ausgelesen werden, um die gewollte Information zu erlangen.

## Lösung

Das Materialized View Pattern beschreibt die Erzeugung von im Voraus erzeugten vorgefüllten Views. So eine View "materialisiert" die Daten in einer Form, welche am besten geeignet ist für das Ergebnis der Datenabfrage.

Eine materialisierte View ("materialized View") enthält nur die relevanten Daten für die entsprechende Datenanfrage, was einen schnelleren und einfacheren Informationsgewinn bedeutet. Sie können auch aktuelle, berechnete Werte enthalten, welche in der Abfrage definiert sind. Diese Views und die Daten die sie enthalten, können jederzeit auf Basis der Quelldaten wieder neu erstellt werden. Sie wird daher in keinem Fall direkt von einer Applikation aktualisiert, sondern eher als Cache behandelt. Wenn sich die Quelldaten ändern, muss die View jedoch aktualisiert werden, was entweder vom System automatisiert durchgeführt wird oder manuell.

## Probleme und Überlegungen

Folgendes muss bei der Implementierung dieses Pattern beachtet werden:

* Wann und wie wird die View aktualisiert? (z.B. reagieren auf Veränderungen)
* Manche Systeme benötigen Materialized View Patterns. (z.B. bei Event Sourcing Patterns)
* Die Konsistenz der Daten bei Generierung und Aktualisierung der View
* Wo soll die View gespeichert werden? Sie muss nicht am selben Ort wie die eigentlichen Daten liegen
* Ist die View nur zur Leistungsverbesserung da, kann sie z.B. im Cache gespeichert werden
* Materialized Views sollten ausgereizt werden (Berechnungen in die Datenabfrage einbinden)
* Wenn es möglich ist, Indexierung der View vornehmen um die Leistung zu steigern in relationalen Datenbanken

## Wann wird dieses Pattern verwendet?

* Wenn Datenabfragen sehr komplex sind oder eine direkte Abfrage zu schwierig ist (z.B. unstrukturierte Daten, keine oder wenig Struktur vorhanden)
* Temporäre Views um die Leistung zu verbessern
* Lokal verfügbare Views, falls die Verbindung zu den Daten nicht besteht
* Vereinfachte Datenabfragen und Daten-Views zum experimentieren
* Sicherheit: Nur bestimmte Daten bestimmten Nutzern zur Verfügung stellen
* Als Brücke bei der Nutzung unterschiedlicher Datenspeichermethoden (z.B. eine Cloud zum Schreiben und eine relationale Datenbank für schnelle Datenabfragen)

Nicht zu verwenden unter folgenden Bedingungen:

* Die Daten sind einfach abzufragen
* Die Quelldaten ändern sich sehr oft
* Konistenz ist ein wichtiger Faktor

## Beispiel

Im folgenden Beispiel wird mittels anspruchsvollen Datenabfragen eine "materialized View" erstellt. Über verschiedene Entitäten wird eine View erstellt, die die gesamten Verkaufszahlen elektronischer Produkte enthält, zusammen mit der Anzahl der Kunden. Nutzer können mit Hilfe dieser View einfach bestimmte Resultate abfragen oder in andere Datenabfragen miteinbeziehen.

![](/assets/materialized-view-summary-diagram.png)\(Abbildung 1: Beispielhafte Anwendung um eine Zusammenfassung der Verkäufe darzustellen. Quelle: https://docs.microsoft.com/en-us/azure/architecture/patterns/materialized-view)

## Ähnliche Patterns und Richtlinien

Folgende Patterns und Richtlinien könnten auch von Interesse sein:

* Data Consistency Primer
* Command and Query Responsibility Segregation (CQRS) Pattern
* Event Sourcing Pattern
* Index Table Pattern
