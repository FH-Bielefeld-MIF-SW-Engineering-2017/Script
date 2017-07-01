# Systems Modeling Language

Die Systems Modeling Language (SysML) ist eine allgemeine grafische Modellierungssprache um komplexe Systeme zu spezifizieren, analysieren, designen und verifizieren. Die erste Version von SysML wurde von der Object Management Group 2007 angekündigt und liegt bis dato in der Version 1.5 vor. Komplexe Systeme umfassen in der Regel Hardware, Software, Informationen, Personal, Abläufe und technische Hilfsmittel. Die SysML liefert eine grafische Repräsentation mit einer Semantik um Systemanforderungen, Verhalten, Struktur und Zusicherungen eines Systems zu modellieren. Sie enthält eine Teilmenge der UML-Elemente und zusätzlich Erweiterungen, um den Anforderungen des System Engineering gerecht zu werden (s. Abbildung 2).

![](/assets/schnittmenge_uml_sysml.jpg)

**SysMLDiagramme **

Die SysML umfasst insgesamtneun Diagramme. Das Use Case-, Sequence-, State Machine- und Package Diagramm wurden von der UML übernommen. Das Activity-, Block Definition- und Internal Block Diagramm wurden auch von der UML übernommen, enthalten jedoch Modifikationen. Das Requirement Diagramm und Paramteric Diagramm sind neu in der SysML. Die nachfolgende Abbildung zeigt die Hierarchie der Diagramme.

![](/assets/sysml_diagramme.jpg)

**Requirement Diagramm**

Das Requirement Diagramm wird zur Visualisierung von text-basierten Anforderungen und deren Beziehung zu anderen Modelelementen verwendet. Es können Beziehungen zwischen den Elementen hergestellt werden, um z.B. zu zeigen, dass eine Anforderung durch ein anderesElement (z.B. ein Systemelement) erfüllt wird oder das ein Testfall eine Anforderung verifiziert. Zusätzlich können Anforderungshierarchien oder Anforderungsableitungen dargestellt werden. [OMG17](Quellen.md)

**Block Definition Diagramm**

Das Block Definition Diagramm wird verwendet um Systemhierarchien zu definieren. Das Basiselement ist der Block, welcher als Repräsentant von Hardware, Software, Hilfsmittel, Personal oder anderen Systemelementen dient.[OMG17](Quellen.md)

**Internal Block Diagramm**

Das Internal Block Diagramm beschreibt die interne Struktur eines Blocks mit seinen Teilen (parts), Schnittstellen(ports) und den Verbindungen (connectors) in einem bestimmten Kontext.[OMG17](Quellen.md)

**Package Diagramm**

Das Package Diagramm dient zur Darstellung der Organisation / Struktur eines Models. Es eignet sich sehr gut, um eine Navigation durch das Modell herzustellen.[OMG17](Quellen.md)

**Parametric Diagramm**

Das Parametric Diagramm beschreibt die Beschränkungen (engl. constraints) der Systemeigenschaften wie z.B. Performanz, Zuverlässigkeit oder zulässige Eigenschaften und ist ein Hilfsmittel für die Analyse eines Systems.[OMG17](Quellen.md)

**Use Case Diagramm**

Das Use-Case Diagramm liefert eine High-Level Beschreibung der Funktionalität, die das System seiner Umwelt bereitstellt.[OMG17](Quellen.md)

**Activity Diagramm**

Das Activity Diagramm zeigt den Daten- und Kontrollfluss von verschiedenen Abläufen im System.[OMG17](Quellen.md)

**Sequence Diagramm**

Das Sequence Diagramm zeigt die Interaktion zwischen dem System und seiner Umwelt oder zwischen verschiedenen Systemelementen.[OMG17](Quellen.md)

**State Machine Diagram**

Das State Machine Diagramm beschreibt Zustandsübergänge und Aktionen, die ein System oder Systemelement ein Antwort auf Events durchführt. [OMG17](Quellen.md)

**Cross-cutting**

Im Bereich des Systems Engineering wird oft der Begriff „Allokation“ verwendet. Dieser meint die Zuweisung von Funktion zu Komponenten, logische zu physikalische Komponenten oder Software zu Hardware. Die SysML stellt dafür eine spezielle Relationship „allocate“ bereit. [OMG17](Quellen.md)