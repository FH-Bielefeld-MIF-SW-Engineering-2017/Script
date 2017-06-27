# Kombinieren anderer Methoden und Standards mit ArchiMate

ArchiMate soll herkömmliche Methoden der Modellierung nicht ersetzen, sondern eine Schnittstelle zwischen den Methoden bieten. Dabei werden einzelne Methoden der Modellierung in Kombination mit ArchiMate verwendet. Domänen-spezifische Sprachen, wie bspw. UML für Software oder BPMN für Business-Prozesse, können durch ArchiMate in Relation zueinander gesetzt werden. Somit bietet ArchiMate eine für Laien verständliche abstrakte Sicht auf eine Vielzahl von Domänen und deren Relationen zueinander, während die herkömmlichen Methoden innerhalb der Domänen eine weitere Detailtiefe für Experten zulassen (siehe Abbildung 6.1).

[vgl. S. 123]

![](/assets/ArchiMateScope.png)

*Abbildung 6.1: ArchiMate als Schnittstelle zu herkömmlichen Sprachen der Modellierung*

## Business Motivation Model

Das Business Motivation Model (BMM) beschreibt eine detailliertere Sicht für eine Business Motivation und steht in Relation zu der zuvor erwähnten Schicht "Motivation" des ArchiMate Frameworks. Tabelle 6.1 stellt die Elemente von BMM den Elementen von ArchiMate (AM)gegenüber.

[vgl. S. 125]

![](/assets/ArchiMateBMM.png)

*Tabelle 6.1: Gegenüberstellung BMM zu AM*

## Business Process Model and Notation
Business Process Model and Notation (BPMN) gilt als Standard in der Modellierung von Business Prozessen. ArchiMate dient zur Modellierung von "High-Level-Prozessen" und deren Relation zum Kontext des Unternehmens. BPMN bietet hier eine detaillierte Sicht auf den kompletten Informationsfluss innerhalb eines Prozesses, welcher vom Kontext des Unternehmens gekapselt ist. Tabelle 6.2 stellt die Elemente der BPMN denen von ArchiMate gegenüber.

[vgl. S. 133-134]

![](/assets/ArchiMateBPMN.png)

*Tabelle 6.2: Gegenüberstellung BPMN zu AM*

## Unified Modeling Language
Unified Modeling Language (UML) ist ein Standard in der Modellierung von Software und ist die Inspiration einiger Konzepte von ArchiMate. Die Schicht der "Applikation" ist mit UML streng gekoppelt und bietet daher sehr ähnliche Elemente. Jedoch gibt es feine  Unterschiede zwischen UML und ArchiMate. In ArchiMate ist bspw. die Richtung der Relationen häufig umgekehrt. Auf Ebene der Architektur liegt der Fokus auf dem allgemeinen Verständnis, ob ein Dienst (Service) nun bereitgestellt oder aktiv von einem Benutzer abgerufen wird ist in ArchiMate irrelevant, während der Richtung von Funktionsaufrufen innerhalb einer Software eine wichtige Bedeutung beigemessen wird. Ein weiterer wichtiger Unterschied ist, dass ArchiMate zwischen Dienst (Service) und Schnittstelle (Interface) für diesen Dienst unterscheidet, während in der UML nur die Schnittstelle als solche vorhanden ist. Die Unterscheidung zwischen Dienst (Service) und Schnittstelle (Interface) ist in ArchiMate von Bedeutung um für Laien verständlich darstellen zu können, dass mehrere Schnittstellen dafür zuständig sein können den gleichen Dienst zu unterstützen. Tabelle 6.3 stellt eine Gegenüberstellung der Elemente aus UML zu ArchiMate dar.

[vgl. S. 135-138]

![](/assets/ArchiMateUML.png)

*Tabelle 6.3: Gegenüberstellung UML zu AM*

## Entity Relationship Diagram
Das Entity Relationship Diagram (ERD) dient zur Modellierung von Daten und ist aus Sicht einer Architektur zu spezifisch, bspw. sind Fremdschlüssel oder Kardinalitäten aus dem ERD ungeeignet um Informationsflüsse von Daten innerhalb einer Architektur darzustellen. Somit kann das ERD verwendet werden, um technisch relevante Detailtiefen für Experten der Datenmodellierung darzustellen. Dennoch sind die Konzepte eines ERD geeignet, um passive Strukturen in ArchiMate zu modellieren. Eine Gegenüberstellung der Elemente ist in Tabelle 6.4 dargestellt.

[vgl. S. 139]

![](/assets/ArchiMateUML.png)

*Tabelle 6.4: Gegenüberstellung ERD zu AM*
