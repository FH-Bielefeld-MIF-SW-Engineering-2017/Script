Priority Queue Pattern
======================

 

Das Priority Queue Pattern arbeitet Abfragen mit einer höheren Priorität
schneller ab, als Abfragen mit eiener geringen Priorität.

 

Konzept und Problem
-------------------

 

Beispielsweise bei der Nutzung einer Cloud werden Abfragen an den Server über
eine Message-Queue verwaltet. Da einige Abfragen so zeitnah wie möglich
behandelt werden müssen, um dem Nutzer das Gefühl von “Echtzeit” zu vermitteln
müssen diese durch Priorisierung vorgeschaltet werden.

 

Lösung
------

 

Um das Konzept von First-in First-out zu modifizieren bekommt jede eingehende
Abfrage eine Priorität zugewiesen. Die neue Abfrage wird dann hinter das letzte
Element der gleichen Priorität gesetzt. Somit hat man mehrere First-in First-out
Queues innerhalb einer nach Prioritäten sortierten Queue.

Sollte ein System das Prinzip der Priority Queue nicht unterstützen, so kann
durch die Erstellung mehrer Queues für jede einzelne Priorität abhilfe
geschaffen werden.

Demnach werden erst alle Abfragen aus der Queue mit der höchsten Priorität
abgearbeitet. Ist diese leer, so wird auf die nächsthöhere Priorität
eingegangen.

Der hierbeschriebene single-pool-Ansatz führt dazu, dass eine Abfrage mit einer
niedrigen Priorität womöglich nie abgearbeitet wird, da neue Abfragen mit einer
höheren Priorität dazu kommen. Abhilfe soll hier der multi-pool-Ansatz sein,
welcher die niedriger priorisierten Abfragen in Abhängigkeit seiner verfügbaren
Resourcen aufjedenfall abarbeitet.

Die Nutzung der Priority Queue hat den Vorteil Buisseness-Anforderungen welche
die Priorisierung betreffen, wie beispielsweise die Bevorzugung von Pro-Kunden
gegenüber normalen Kunden durchsetzen zu können.

 

Probleme und Überlegungen
-------------------------

 

Die Prioritäten müssen in Abhängigkeit zur Lösung implementiert werden. Wenn
alle Abfragen die höchste Priorität haben, so muss unter Umständen auch hierbei
lange auf eine Antwort gewartet werden.

Bei einer hohen Auslastung der Queue muss für den single-pool-Ansatz eine Lösung
für die niedrig Priorisierten Abfragen gefunden werden.

Beim  multi-pool-Ansatz auf einer single-pool-Basis muss ein Algorithmus zum
Abrufen der korrekten Abfragen in den unterschiedlich priorisierten Queues
implementiert werden.

Die Raten der behandelten niedrig- und hochpriorisierten Abfragen müssen
überwacht und verglichen werden, um die Priorisierungen möglichst effizient
anzupassen.

 

Abschließend kann man sagen, dass die Priority Queue bei Abfragen mit
verschieden gewichteter Priorität oder bei Abfragen von Kunden mit verschieden
gewichteter Priorität zum Einsatz kommen sollte.
