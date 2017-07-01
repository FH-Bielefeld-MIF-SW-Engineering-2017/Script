# Agile Vorgehensmodelle
Agile Vorgehensmodelle sind eine Methode des Projekt Managements.
Sie zeichnen sich üblicherweise durch iteratives Vorgehen
und kurze Feedback-Zyklen aus.
Sie sollen nach häufiger Auffassung schwergewichtige Vorgehensmodelle
ablösen, die mit viel Management-Aufwand verbunden sind, ablösen.

Robert Martin beschreibt hingegen, dass in den Anfangszeiten der
Software-Entwicklung in den 60er Jahren bereits agil gearbeitet wurde.
Er begründet das damit, dass damals hauptsächlich disziplinierte,
professionelle Mathematiker und Fachanwender als Softwareentwickler
tätig waren. Erst das auftauchen großer Mengen junger,
undisziplinierter Entwickler machte es nötig, ihnen feste Strukturen
vorzugeben. (vgl. [6], ab ca. 48m)

Bekannte, aktuelle Vertreter agiler Vorgehensmodelle sind Scrum,
Kanban und Extreme Programming (XP).
Die ersteren Beiden sollen nachfolgend kurz erläutwert werden.

## Scrum
Das zur Zeit bekannteste agile Modell ist Scrum,
es soll hier nur in seinen Grundzügen erläutert werden.
Er stammt zwar aus der Softwareentwicklung, ist aber prinzipiell
unabhängig davon.

Einer der Hauptaspekte von Scrum ist die Einteilung der
Projektlaufzeit in sogeannte Sprints. Diese dauern üblicherweise
2-4 Wochen und am Ende jees Sprints sollte eine lauffähige,
inkrementell verbesserte Software bereit stehen.
Während eines Sprints werden einzelne Aufgaben in Form von Backlog-Items
abgearbeitet. Die abzuarbeitenden Items werden jeweils vor Beginn
eines Sprints festgelegt und dem Product-Backlog entnommen.
Die Backlog-Items, die während eines Sprints abgearbeitet werden sollen,
werden im Sprint-Backlog abgelegt.

Der Product-Backlog beinhaltet alle noch zu erledigenden Backlog-Items und wird
vom Product-Owner befüllt. Das geschieht initial beim Projektbeginn, sowie
während der Projektlaufzeit (z.B. Änderungswünsche nach einem Sprint).

Neben dem Product Owner gibt es außerdem noch das Entwicklerteam als beteiligte,
welche die eigentliche Entwicklungsarbeit erledigen.
Außerdem gibt es den Scrum Master, der die Durchführung überwacht.
Er stellt eine "dienende Führungskraft" dar, gibt also keine Arbeitsanweisungen,
sondern steht beratend zur Seite.

## Kanban
Kanban is ein weiteres agiles Vorgehensmodell, sein zentraler Punkt ist das sogenannte
Kanban-Board.
Der Begriff "Kanban" stammt aus dem japanischen und bedeutet "Signalkarte",
dort wurde es als Produktionsprozess ursprünglich von Toyota entwickelt.
In der IT wurde es zuerst 2007 von David J. Anderson vorgestellt.

### Pull-Prinzip
Kanban arbeitet nach dem sogenanten Pull-Prinzip. Das bedeutet, dass keine Arbeit
auf Vorrat erledigt wird, sondern immer erst dann ausgeführt wird, wenn sie wirklich
benötigt wird. Das führt in der Anwendung in Produktionsumgebungen zu deutlich
geringeren Lagerkapazitäten und einer Reduktion von Abfall, falls auf Vorrat produziertes
am Ende nicht mehr gebraucht werden kann.
In der Software-Entwicklung ist Lagergröße zwar kein entscheidender Faktor,
aber die Reduktion von Abfall, also Code der am Ende nicht gebraucht wird,
ist mindestens genau so wichtig, wenn nicht wichtiger, da die Arbeitszeit
der Entwickler die hauptsächlich begrenzende Ressource ist.

### Kanban-Board
Im Kanban-Board werden alle einzelnen Aufgaben in Form von Zetteln aufgeklebt.
Dabei gibt es eine Unterteilung in Spalten, die jeweils mit dem Zustand der
darin enthaltenen Karten beschriftet sind (z.B. "To Do", "In Arbeit", "Testing", "Erledigt").

![Beispiel Kanban Board](https://upload.wikimedia.org/wikipedia/commons/d/d3/Simple-kanban-board-.jpg)
Abbildung: Beispielhaftes Kanbanboard, Quelle: [Wikipedia, Jeff.lasovski](https://de.wikipedia.org/wiki/Datei:Simple-kanban-board-.jpg)

Das Board darf natürlich nicht nach belieben mit Aufgaben versehen werden.
Es unterliegt einigen Regeln und Gesetzmäßigkeiten, diese werden in den
sechs Kernpraktiken genauer beschrieben.

### Kernpraktiken

Die sechs Kernpraktiken von Kanban lauten im einzelnen:

1. **Visualisiere den Fluss der Arbeit**  
  Auf dem Kanban Board finden sich alle Aufgaben, die noch ausstehen, gerade erledigt werden,
  oder schon abgeschlossen sind. Das bringt eine gute Übersicht über den aktuellen Status
  einzelner Arbeitseinheiten sowie den Fortschritt des Projekts.

1. **Begrenze die Menge angefangener Arbeit**  
  Es darf jeweils nur eine begrenzte Menge an Karten in den Spalten vorhanden sein.
  Es kann allerdings sinnvoll sein, nicht für jede Spalte ein Limit zu setzen.
  So kann zum Beispiel eine Spalte "Fertig" alle bereits erledigten Karten
  enthalten. Diese zu beschränken würde schlussendlich dazu führen, dass keine Arbeit
  mehr verrichtet werden darf.
  Dadurch wird effektiv die angefangene Arbeit auf die Anzahl der Karten limitiert.
  Das Ziel ist es dabei, dass einzelne Aufgaben schneller erledigt werden, wenn nicht
  zwischendurch andere angefangen werden. Dabei wird die benötigte Zeit für die einzelnen
  Aufgaben zwar nicht signifigant gesenkt (höchstens durch weniger Wechsel zwischen Aufgaben),
  aber der Fortschritt ist schneller sichtbar. Außerdem können eventuell abhängige Aufgaben
  so eher von anderen Entwicklern begonnen werden.

1. **Miss und steuere den Fluss**  
  Typische Werte, die in einem Kanbanprozess gemessen werden, sind die Wartezeit, Zykluszeit
  und der Durchsatz. Diese erlauben es, Rückschlüsse auf die Organisation der Arbeit
  zu ziehen und sie zu verbessern.

1. **Mache die Regeln für den Prozess explizit**  
  Um unnötige Unsicherheiten und Ablaufprobleme zu vermeiden, sollen alle Beteiligten
  die genauen Regeln des Prozesses kennen. Dazu gehören unter anderem die exakte Beteutung
  der Kanban-Board-Spalten, was genau fertig heißt (Definition of Done),
  und der genaue Ablauf, wer wann welche Karten auf dem Kanban-Board verschiebt.

1. **Implementiere Feedback-Mechanismen**  
  Um den Prozess kontinuierlich zu verbessern, ist es wichtig, Schwächen aufzudecken
  und Verbesserungsmöglichkeiten für diese zu finden.
  Damit diese kontinuierliche Verbesserung funktioniert,
  muss sie auf allen Ebenen der Organisation stattfinden.
  Dazu gehört, dass auch Entwickler konkrete Verbesserungsvorschläge einbringen. 
  Darüber hinaus kann aber auch Feedback von Außenstehenden wertvoll sein,
  da es neue Blickwinkel ermöglicht.
  Nützliche Mittel, um regelmäßiges Feedback zu ermöglichen, sind Daily-Standups
  und insbesondere (z.B. monatliche) Retrospektiven.

1. **Führe Verbesserungen auf Basis von Modellen durch**  
  Schon lange gibt es wissenschaftliche Modelle, die sich mit Engpässen und Problemen
  in Betriebsabläufen beschäftigen. Es ist sinnvoll, diese für die Verbesserung
  des Prozesses einzusetzen. Die Auswahl der Modelle ist nicht weiter eingeschränkt,
  damit die Modelle verwendet werden können, die für den konkreten Einzelfall am
  geeignestens sind.

### Kanban und andere Vorgehensmodelle
Da Kanban im Gegensatz zu anderen Vorgehensmodellen einige Dinge nicht festlegt,
ist es prinzipiell Möglich, Kanban gleichzeitig mit anderen Modellen einzusetzen.
So ist zum Beispiel keine zeitliche Einteilung in Sprints gegeben, wie es in Scrum
der Fall ist. Außerdem gibt es keine feste Rollenbeschreibung der Beteiligten.
Kanban und Scrum können so zum Beispiel in einer Kombination durchgeführt werden.
So können die Vorteile des Kanban-Boards und dessen Regeln mit den Rollen- und Zeiteinteilung
von Scrum vereint werden.

Es ist auch möglich, Kanban mit nicht agilen Vorgehensmodellen zusammen zu benutzen.
Fall es in irgendeiner Art Kollisionen gibt, ist auch ein "Kanban-Light" vorstellbar,
dass je nach Anwendungsfall eine oder mehrere Kernpraktiken ändert oder auslässt.
In jedem Fall kann dabei der Vorteil des Kanban-Boards und dessen dokumentierender
bzw. visualisierender Funktion genutzt werden.
