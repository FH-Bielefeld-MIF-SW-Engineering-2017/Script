# Systems Modeling Language

Die Systems Modeling Language (SysML) ist eine allgemeine grafische Modellierungssprache um komplexe Systeme zu spezifizieren, analysieren, designen und verifizieren. Die erste Version vonSysML wurde von der Object Management Group 2007 angekündigt und liegt bis dato in der Version 1.5 vor. Komplexe Systeme umfassen in der Regel Hardware, Software, Informationen, Personal, Abläufe und technische Hilfsmittel. Die SysML liefert eine grafische Repräsentation mit einer Semantik umSystemanforderungen, Verhalten, Struktur und Zusicherungen eines Systems zu modellieren. Sie enthält eine Teilmenge der UML-Elemente und zusätzlich Erweiterungen, um den Anforderungen des System Engineering gerecht zu werden (s. Abbildung 2).

![](..\assets\schnittmenge_uml_sysml.jpg)

**SysMLDiagramme **

Die SysML umfasst insgesamtneun Diagramme. Das Use Case-, Sequence-, State Machine- und Package Diagrammwurden von der UML übernommen. Das Activity-, Block Definition- und InternalBlock Diagramm wurden auch von der UML übernommen, enthalten jedoch Modifikationen.Das Requirement Diagramm und Paramteric Diagramm sind neu in der SysML. Die Abbildung 3zeigt die Hierarchie der Diagramme.

![](..\assets\sysml_diagramme.jpg)

**Requirement Diagramm**

Das Requirement Diagramm wirdzur Visualisierung von text-basierten Anforderungen und deren Beziehung zuanderen Modelelementen verwendet. Es können Beziehungen zwischen den Elementenhergestellt werden, um z.B. zu zeigen, dass eine Anforderung durch ein anderesElement (z.B. ein Systemelement) erfüllt wird oder das ein Testfall eineAnforderung verifiziert. Zusätzlich können Anforderungshierarchien oderAnforderungsableitungen dargestellt werden. 

**Block Definition Diagramm**

Das Block Definition Diagrammwird verwendet um Systemhierarchien zu definieren. Das Basiselement ist derBlock, welcher als Repräsentant von Hardware, Software, Hilfsmittel, Personaloder anderen Systemelementen dient.

**Internal Block Diagramm**

Das Internal Block Diagrammbeschreibt die interne Struktur eines Blocks mit seinen Teilen (parts), Schnittstellen(ports) und den Verbindungen (connectors) in einem bestimmten Kontext.

**Package Diagramm**

Das Package Diagramm dient zurDarstellung der Organisation / Struktur eines Models. Es eignet sich sehr gut,um eine Navigation durch das Modell herzustellen.

**Parametric Diagramm**

Das Parametric Diagrammbeschreibt die Beschränkungen (engl. constraints) der Systemeigenschaften wiez.B. Performanz, Zuverlässigkeit oder zulässige Eigenschaften und ist einHilfsmittel für die Analyse eines Systems.

**Use Case Diagramm**

Das Use-Case Diagramm lieferteine High-Level Beschreibung der Funktionalität, die das System seiner Umweltbereitstellt.

**Activity Diagramm**

Das Activity Diagramm zeigt denDaten- und Kontrollfluss von verschiedenen Abläufen im System.

**Sequence Diagramm**

Das Sequence Diagramm zeigt dieInteraktion zwischen dem System und seiner Umwelt oder zwischen verschiedenenSystemelementen.

**State Machine Diagram**

Das State Machine Diagrambeschreibt Zustandsübergänge und Aktionen, die ein System oder Systemelementein Antwort auf Events durchführt. 

**Cross-cutting**

Im Bereich des SystemsEngineering wird oft der Begriff „Allokation“ verwendet. Dieser meint dieZuweisung von Funktion zu Komponenten, logische zu physikalische Komponentenoder Software zu Hardware. Die SysML stellt dafür eine spezielle Relationship„allocate“ bereit. [OMG17]