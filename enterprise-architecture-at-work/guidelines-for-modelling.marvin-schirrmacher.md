# Guidelines for Modelling

Es gibt nicht die eine einzig wahre und richtige Modellierung. Wichtig ist jedoch, dass jede Modellierungsart in sich konzeptionelle Integrität gewährt. Dabei soll die Grundidee eines Modells, unabhängig von dessen Komplexität, immer schnell und einfach verständlich sein. So sollen auch Personen ohne tieferes Wissen stets das Grundgerüst eines Modells nachvollziehen können.

## Der Modellierungsprozess

Im Kontext des Buchs ist in ein Modell immer ein abstraktes Abbild eines \(Teil-\)Aspekts der realen Welt. Die Modellierung ist dabei ein Transformationsprozess, bei dem reale Aspekte getreu übernommen und nicht verändert werden sollen, sondern nur gefiltert und konkretisiert werden \(vgl. Abbildung, der Informationsgehalt soll sich nicht ändern\). Das ermöglicht es reale Problemstellungen verständlich zu kommunizieren; entweder für Personen, die das Modell lesen sollen, und auch für die, die es kollaborativ erstellen.

![](/assets/EAAW - Knowledge goals and modelling guidelines.png)

Beim Modellieren werden typischerweise iterativ folgende Schritte durchlaufen:

* Erstellung und Definition des Zwecks einer Modellierung in Absprache mit den Stakeholdern
* Auswählen einer oder mehrerer Sichtweisen, was die zu berücksichtigenden Inhalte des Modells bestimmt
* Erstellung und Strukturierung des Modells, was stets in Kombination geschieht
  * Bei der Erstellung können zusätzliche Information durch weitere Gespräche mit den Stakeholdern eingeholt werden
  * Die Strukturierung dient der Aufteilung und Vereinfachung von komlexen Abbildern, sowie der Aufdeckung von sich wiederholenden Mustern aber auch Inkonsistenzen
* Visualisierung des Modells; dabei stets überlegen, welche Sichtweise in jedem konkreten Prozessabbild am sinnvollsten ist und wie diese am besten dargestellt werden kann \(textuell oder visuell\)
* Verwendung des Modells, durch Präsentation bei den Stakeholdern
  * Validierung durch das Einholen von Stakeholder-Feedback
  * Zusagen des Stakeholder einholen, ob der Entwurf übernommen werden soll
  * Weitere Stakeholder informieren
* Stetige Überarbeitung und Aktualisierung des Modells

Hilfreich bei der Modellierung ist die Definition allgemeingültiger Begriffe, sogenannte Modellierungsaktionen. Diese lassen sich aus den typischen Aufgaben ableiten. Die Aktionsbegriffe dienen als einfaches Vokabular. Der Modellierende selbst behält damit einen strukturierteren Überblick über seine Handlungen. Des Weiteren soll er damit sein eigenes Vorgehen stets objektiv und rational reflektieren können. Definieren lassen sich folgende Aktionen:

* Ein neues Element in einem Modell einführen, das relevant sein könnte
* Ein Element verfeinern
  * Klassifizieren nach bestehenden Kategorien oder eine neue Kategorie erstellen
  * Element beschreiben durch einen Text und/oder weitere Subelemente 
* Ein Element verwerfen; dabei aber festhalten, warum man es entfernt und was man ggf. positives mitnehmen kann
* Ein Konzept oder eine Beziehung abstrahieren; dabei können ggf. unwichtige Detailinformationen verwirftverworfen werden 
* Ein neues Element übersetzen bzw. ein passendes Element in einem anderen Modell identifizieren, dass das selbe aussagt, ggf.:
  * Zusätzliche Elemente für eine geeignete Übersetzung erstellen oder ersetzen
  * Diese Elemente mit den Element des anderen Modells verknüpfen
  * Eine vermittelnde Sprache zwischen den beiden Modellen modellieren
  * Übersetzungsregel definieren
  * Mögliche Missverständnisse festhalten
* Alle Aktionen sollten dokumentiert werden

## Richtlinien für's Modellieren

Für die verschiedenen Aspekte beim Modellieren lassen sich jeweils folgende Richtlinien forumulieren.

### Zielorientierte Modellierung

* Ein Modell soll Antworten auf Fragen liefern
* Man soll einen klaren Untereschied zwischen dem Modell und seiner Visualisierung machen
* Quantitätsmaxime: Ein Modell soll so informativ, wie nötig, aber nicht informativer, als nötig sein
* Qualitätsmaxime: Man soll nichts modellieren, was man für falsch hält oder für was man nicht genügend Belege hat
* Relevanzmaxime: Nur wirklich relevante Dinge modellieren
* Maxime der Art und Weise: Unklare Aussagen und Mehrdeutigkeiten vermeiden und sich kurz und prägnant formulieren
* Iterativ modellieren
* Dynamisch modellieren
* Ökonomisch im Model sein
* Ökonomisch in der Sichtweise sein
* Konzepte erkennbar machen
* Strukturen erkennbar machen
* Konsistenz innerhalb eines Modells bewahren
* Konsistenz zu referenzierten Modellen bewahren
* Modelle so korrekt und vollständig wie nötig machen
* Verschiedene Aspekte orthogonal betrachten

### Bevor man startet

* Gibt es klar definierte Stakeholder?
* Ist die Zielsetzung explizit beschrieben?
* Trägt eine Enterprise-Architektur zur Erreichung der Zielsetzung bei?
* Ist der Rahmen klar, von dem, was modelliert werden soll?
* Ist klar, ob die Ist- oder die Soll-Situation modelliert werden soll?
* Sind alle Informationen zur Erstellung des Modells verfügbar?
* Sind die realistischen Erwartungen an den Enterprise-Architekten klar?

### Inhalte

* Die Sichtweise wählen, die der Zeilsetzung genügen
* Stets den Fokus behalten
* Weniger wichtige Dinge und Ausnahmen vernachlässigen
* Sich nicht davor scheuen, bereits modellierte Elemente wieder zu verwerfen
* Konsistente Zwischenversionen mit den Stakeholdern besprechen
* Von einem Element ausgehend beginnen zu modellieren; dabei sind vier Richtungen möglich:
  * nach innen (hin zum inneren Aufbau eines Elements)
  * nach außen (hin zu den unterstützten Elementen)
  * nach unten (hin zu Realisierungen anderer Elemente)
  * seitwärts (hin zu kooperierenden Elementen)

![](/assets/EAAW - Metaphorical directions for viewpoints.png)

### Abstraktion

* Zuerst Schlüsselkonzepte und -beziehungen auf einem abstrakten Ebenen festhalten
* Nur eine begrenzte Zahl an vordefinierten Abstrkationebenen verwenden; die Ebenen sollten auf Basis der Modellierungsziele definiert werden
* Abstraktionsebenen konsistent halten

### Struktur und Visualisierung

* Ein Modell so selbsterklärend wie möglich machen
* Internes und externes Verhalten von einander trennen
* Layer verwenden

![](/assets/EAAW - Example of layered model.png)

* Nach Phasen gruppieren
* Nach Produkt oder Dienst gruppieren
* Nach verwendeten Informationen gruppieren
* Nach geographischen Standorten gruppieren
* Unabhängige Komponenten von einander trennen

### Konstruktiver Umgang mit Kommunikationsverlusten

Es kann immer vorkommen, dass ein Stakeholder ein Modell ab einem bestimmten Punkt nicht mehr versteht und es somit zu einem sogenannten Kommunikationsverlust kommt. Solche Zustände sind nicht gut, können aber produktiv genutzt werden, um wieder auf die Richtige Bahn zu kommen. Dazu muss das Modell hinsichtlich Lesbarkeit und Wirkung überprüft werden und je nachdme Korrekturen vorgenommen werden.

Bei der Lesbarkeit können folgende Probleme auftreten:

* Das Modell wird nicht verstanden, da unbekannte Begriffe und Konzepte verwendet werden. Lösung: Die dem Stakeholder bekannte Begriffe verwenden und das neue Vokabular vorstellen.
* Das Modell wird falsch verstanden, weshalb der Stakeholder falsche Schlussfolgerungen zieht. Lösung: Die dem Stakeholder bekannte Begriffe verwenden und das neue Vokabular vorstellen.
* Das Modell hat keine intuitive Struktur für den Empfänger. Lösung: Die Logik der Modelle des Stakeholders analysieren und dessen Struktur adaptieren.
* Das Modell hat eine unklare Struktur oder Notation und verursacht Fragen. Lösung: Strukturen (anhand von bekannten Beispielen) erklären.
* Die Visualisierung des Modells lenkt von der eigentlichen Nachricht ab. Lösung: Visuelle Ausschmückungen in Form von übertriebenen Diagrammen und Farben zugunsten der Inhaltsvermittlung weglassen.

Bei der Vermittlung und Wirkung können folgende Probleme auftreten:

* Die Statusberichte bleiben aus, da der Stakeholder nie Zeit hat. Lösung: Organisatorisches Problem, das nicht in diesem Buch behandelt wird.
* Das Modell hat eine zutreffende, aber ungewollte Nachricht. Lösung: Auf ein organisatorisches Problem, s.o.
* Das Modell ist irrelevant, ist also gut aber für die Problemstellung nicht von Bedeutung. Lösung: Vgl. 'Das Modell beinhaltet überflüssige Elemente'
* Das Modell ist überflüssig, da der Architekt zu viele irrelevante Aspekte betrachtet. Lösung: Problemstellung reflektieren und darauf fokoussieren.
* Das Modell ist zu komplex. Lösung: Mehr Abstraktionsebenen verwenden.
* Das Modell ist nicht konkret genug. Iterieren und Modell konkretisieren.
* Das Modell ist nicht umfassend genug, da nicht alle notwendigen Informationen abgebildet sind. Lösung: Weitere Aspekte des Stakeholders berücksichtigen ohne das Modell zu komplex zu machen.
* Das Modell ist nicht richtig und beinhaltet falsche Annahmen oder Begründungen. Lösung: Informationen neu sammeln und auf Richtigkeit prüfen.

## Lesbarkeit und Anwendbarkeit eines Modells

Die Lesbarkeit eines Modell hängt hauptsächlich von dessen Komplexität ab, weshalb diese möglichst gering gehalten werden muss. Dazu sollte die Anzahl der Elemente, der Elementtypen und der Beziehungen gering gehalten werden.

Zudem sollte die visuelle Komplexität reduziert werden, indem möglichst mehrere Sichtweisen verwendet werden, die Stakeholder-spezifische Teilaspekte ein- oder ausgeblenden. Des Weiteren hilft auch hier das Hinzufügen weitere (Zwischen-)Ebenen, die Bereiche voneinander trennen.

Berücksichtigt man zudem die Gestalt-Prinzipien (vgl. Abbildung), kann das Bild ohne Reduzierung von Elementen besser lesbar gemacht werden:

* Nähe (Proximity): Elemente, die näher beieinander stehen, werden intuitiv als zusammengehöhrend wahrgenommen
* Kontinuität (Continuity): Möglichst gerade Linien und nicht abknickende Linien verwenden
* Abschluss (Closure): Symmetrien und Stringenz werden besser wahrgenommen
* Gleichheit (Similarity): Objekte, die gleich aussehen, werden als zusammengehörend wahrgenommen und solche, die gleiche Größe haben, als von gleicher Priorität wahrgenommen.
* Drehung (Common fate): Wenn Objekte gleichen Aussehens unterschiedliche Orientierung haben, werden alle zusammen nicht mehr als eine Gruppe, sondern entsprechend der sich wiederholden Orientierungen, als mehrere einzelene Gruppen wahrgenommen.

![](/assets/EAAW - Examples of the Gestalt principles.png)

Darüber hinaus erhöhen die Repräsentationskonventionen die Lesbarkeit von Modellen. Es geht um die Optimierung und richtige Verwendung von Layout, Symbolen, Farben und Texten.

Das Layout ist das wichtigste Attribute bei der Gestaltung von verständlichen Modellen. Wichtige Punkte sind:
* freie, weiße Flächen verwenden, was Diagramme eleganter erscheinen lässt und Änderungen besser zulässt
* zwischen Normal- und Ausnahmefällen unterscheiden, indem man dem normalen Prozess eine eigenen Ebene lässt und Ausnahmebehandlungen paralle darunter oder darüber separat abbildet
* Symmetrien verwenden, um Ähnlichkeiten darzustellen
* Zeitabhängigkeiten von links nach rechts modellieren
* Sich überschneidende Linien vermeiden

![](/assets/EAAW - Example for symmetry and similarity.png)

![](/assets/EAAW - Example for time dependence from left to right.png)

Durch die Verwendung von realistischen und nachvollziehbaren Symbolen (Zylinde für Datenspeicher, Strichmenchen für Personen und Rollen) lassen sich Grundelemente ohne weitere Beschriftung erklären. Wichtige Punkte dabei sind:

* Ähnliche Zeichnungen für ähnliche Konzepte verwenden
* Die Liniendicke variieren, um wichtige Beziehungen zu unterstreichen

Mit Farben lassen sich Zugehörigkeiten, Gruppierungen sowie Prioriäten gut darstellen. Wichtige Punkte sind:

* Farben nutzen zur Betonung von Elementen
* Farben nutzen, um Zusammengehörigkeiten darzustellen
* Farben nutzen, um Emotionen zu erzeugen
* Nicht zu viele Farben nutzen

Zuleletzt ist auch die Wahl der richtigen Worte entscheidend, um Modelle schnell und leicht nachvollziehbar zu machen. Wichtige Punkte dabei sind:

* die Verwendung von Domänen-spezifischer Terminologie (die Sprache des Stakeholders)
* Namenkonventionen beachten (Verben für Aktionen, Nomen für Ressourcen)