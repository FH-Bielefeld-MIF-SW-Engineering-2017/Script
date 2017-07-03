# Unterstützende Workflows
## DevOps
Wichtig für das Verständnis ist, dass DevOps kein Framework, Tool oder Technologie ist.
Bei DevOps geht es um die Kultur eines Unternehmens und um das Vorgehen, wie die Menschen in einem Unternehmen arbeiten.
Unterstützende Faktoren sind definierte Prozesse und angepasste Tools um durch automatisierte Abläufe eine erhöhte Effektivität zu erreichen.

Durch die Anpassungen und Veränderungen in den Bereichen Kultur, Prozesse und Technologie soll die Kommunikation, sowie die Zusammenarbeit der Entwicklung (development) und "IT operations" verbessert werden [20](../quellen.md).

![](/assets/DevOps.png)

Dies hat Auswirkungen auf die Effektivität des "application life cycles".
Durch diese Auswirkungen sind die Vorteile, welche durch den Einsatz von DevOps erzielt werden können, sehr vielseitig.

![](/assets/Benefits.png)

Die Kultur DevOps kann als innovatives Bündel gesehen werden um "Dev" und "Ops" Teams effektiv zu integrieren.
Dies beinhaltet Themen wie continuous build integration, continuous testing, continuous delivery, continuous improvement, etc., mit dem Ziel die Auslieferung von Software zu beschleunigen.

Die Schwierigkeit liegt darin, dass DevOps häufig nicht verstanden wird.
Hier geht es nicht um einzelne Bereiche, wie bereits aufgezählt bspw. continuous integration.
Es geht um die Kultur! Und eine Kultur zu wandeln, dauert sehr lange.
Ein Beispiel soll das Missverständnis rund um DevOps verdeutlichen. Hier geht es um fünf blinde Männer und einen Elephanten.
Jeder der Männer berührt einen spezifischen Teil des Elefanten und jeder nimmt an das dies der Elephant sei [20](../quellen.md).

Selbstverständlich bezieht sich der Kulturwandel nicht nur auf das "development" und "operations" Team. An diesem Wandeln müssen sich alle Teams (testing team, cloud team, etc.) anschließen.

Für ein tieferes Verständnis werden wir im Folgenden auf zwei Fragestellungen eingehen:
1) Warum DevOps?
2) Wie kann eine DevOps Kultur entstehen?

### Warum DevOps?
Veränderung ist eine essentieller Bestandteil des Lebens und auch von Organisationen.
Schaut man lediglich auf bestehende Methodiken, Kulturen und Praktiken wird man zukünftige "best practices" nie erreichen.
Vorallem in der sich schnell ändernden IT-Welt hat die Veränderung eine enorme Bedeutung.

Progress is impossible without change, and those who cannot change their minds cannot change anything. [20](../quellen.md)

Jede Änderung muss abgewogen werden nach dem Nutzen und den durch die Änderung entstehenden Schwierigkeiten.


### Wie kann eine DevOps Kultur entstehen?
Häufig führen Probleme und Ineffizienz zu Veränderungen. Hierdurch hat sich aus einem Wasserfallmodell die Agile Methodik entwickelt.
Eine Kultur zu verändern geht nicht über Nacht und benötigt sehr viel Zeit. Hieraus resultiert, dass DevOps als Kultur schrittweise eingeführt und akzeptiert werden muss.
Jeder Schritt ist unabhängig von einander zu implementieren und sollte keine Abhängigkeiten zu anderen Schritten haben [20](../quellen.md).

![](/assets/DevOps_Stages.png)

Bspw. kann "Continuous Testing" ohne jede andere DevOps Praktik implementiert werden. Hierdurch entsteht bereits ein Mehrwert,
welcher dazu beiträgt Akzeptanz zu schaffen und die Kultur der Menschen zu verändern [20](../quellen.md).

## Continuous Integration
Traditionell wird bei der Softwareentwicklung die Integration am Ende eines Projektes stattfinden. Je nach Projektgröße und Komplexität liegt die Dauer der Integrationsphase im Bereich Wochen oder Monate.

Continuous Integration (CI) bedeutet, dass zwei Entwickler unabhängig von einander Software schreiben können, jedoch für das selbe Produkt. Dies geschieht durch ständige und regelmäßige Integration in ein "source repository". 

In dem "source repository" werden die einzelnen Incremente mehrere Entwickler zusammengeführt und können durch einen CI Server integriert werden. Grundvoraussetzung hierfür, ist das jeder Entwickler neben seinem Produktiv-Code auch Tests entwickelt. Diese Tests werden durch den CI Server ausgeführt um sicher zu stellen, dass die einzelnen Incremente funktionsfähig bleiben. Das Ergebnis des CI Servers wird an die jeweiligen Entwickler zurück gegeben. Hierdurch können Fehler sofort behoben werden.

Das folgende Bild veranschaulicht den geschilderten Prozess.
![](/assets/CI.png)

Der integrierte Code, ist durch Continuous Integration nicht bereit in Produktion zu gehen, da zwar die Komponenten mit einander funktionieren, allerdings das Produkt (die Software) noch nicht in einer "production-like environment" getestet und verifiziert wurde.

Der Vorteil von CI ist, dass die Integration zum täglichen Geschäft wird. Eine "Big-Bang" Integration am Ende einer Entwicklung wird vermieden.

CI ist zwingend notwendig um Continuous Delivery durchführen zu können [4](../quellen.md).

## Continuous Delivery
Unter Continuous Delivery versteht man, neben allen beschriebenen Schritten von Continuous Integration, das der integrierte Quelltext automatisiert auf verschiedenen  Umgebungen getestet wird. Typischerweise sind diese Umgebungen sehr ähnlich zu einer potentiellen Produktiv-Umgebung.

In diesem Zusammenhang wird das deployen und testen auf den verschiedenen Umgebungen als "deployment pipeline" bezeichnet. Je nach Projekt, Team oder Organisation können unterschiedlich viele Umgebungen existieren. Das folgende Bild veranschaulicht diesen Prozess:

![](/assets/CDelivery.png)

In diesem Beispiel gibt es drei Umgebungen (Development, Test, Staging), welche durchlaufen werden, bevor es in die Produktiv-Umgebung geht. 

In jeder Umgebung wird der Quelltext unterschiedlich getestet. Es ergibt sich der Vorteil, dass mit jeder erfolgreich durchlaufenen Umgebung die Wahrscheinlichkeit wächst, dass der Quelltext auch in der Produktiv-Umgebung lauffähig sein wird [4](../quellen.md).

## Continuous Deployment
Continuous Deployment geht noch einen Schritt weiter und automatisiert ebenfalls die Übergabe in die Produktion.

![](/assets/CDvsCD.png)
[5](../quellen.md)

Jeder einzelne Commit eines Entwickler kann potentiell automatisiert in der Produktion ankommen. Voraussetzung hierfür ist der erfolgreiche Durchlauf aller bisher aufgeführten Schritte aus den Kapiteln Continuous Integration und Delivery. Zusammengefasst muss der Commit, bzw. der Mehrwert oder das Increment erfolgreich integriert worden sein und alle Tests auf allen implementierten Umgebungen bestehen. Anschließend muss nicht mehr entschieden werden, ob der Mehrwert in der Produktion verwendet werden kann. Dies geschieht mit Continuous Deployment ebenfalls automatisiert [4](../quellen.md).

## TDD, BDD, ATDD
Bei dem Test-driven development (TDD) werden bestehenden Anforderungen zu Beginn in diverse Testfälle gegossen. Anschließend wird die bestehende Software angepasst, sodass die bestehenden Testfälle erfüllt werden. Durch ein solches Vorgehen soll die Implementierung von überflüssigem Quelltext reduziert werden.

Im Kontext des Test-driven developments wird häufig von sehr kurzen Zyklen gesprochen. Diese bestehen aus dem Hinzufügen von Tests, der Prüfung ob die neuen Tests fehlschlagen, dem Implementieren, der erneuten Testausführung und einer abschließenden Phase der Quelltextrestrukturierung.

Grundlegende Prinzipien, welche sich der Entwickler gewahr sein sollte sind bspw. „keep it simple, stupid“ (KISS) oder „You aren’t gonna need it“ (YAGNI). Unter Beachtung solcher Prinzipien entsteht überschaubarer, “sauberer” Quelltext. 

Nachteile sind unter anderen das zeitintensive Testen und die Tatsache, dass in der Regel die Tests und der Quelltext von demselben Entwickler verfasst werden. Da dieses Verfahren nur so gut ist wie die Qualität der erstellten Tests, liegt hierin das größte Gefahrenpotential. Darüber hinaus stoßen test-first Tests dort an ihre Grenzen, wo bspw. komplette Funktionstests implementiert werden müssen (User Interfaces). Diese können nicht implementiert werden bevor die Funktion fertig gestellt wurde [1](../quellen.md).

Acceptance test-driven development (ATDD) beruht auf demselben Prinzip, wie das Test-driven development. Ein entscheidender Unterschied ist, dass bei diesem Verfahren ebenfalls nach dem test-first Prinzip Akzeptanztests geschrieben werden. Diese Art von Tests sollen die drei Gruppen Entwickler, Tester und den nicht/weniger technischen Part (Kunde, Produktmanager, o.ä.) näher zusammenbringen. 

Der Anlass hierfür sind die, sehr häufig drastisch, verschiedenen Verständnisse einer Sachlage und die daraus resultierenden Fehlentwicklungen, zusätzlichen Kosten, etc. Es wird hierbei versucht eine Sprache zu sprechen, indem niedergeschriebene Anforderungen in Akzeptanztests umgewandelt werden. Diese werden anschließend implementiert und nur diese Testfälle im Quelltext implementiert und behoben. Akzeptanztests, welche anschließend hinzugefügt werden, sind neue Anforderungen.

Solche Tests können/sollten von allen Beteiligten gelesen/verstanden werden können. Dies ist beim TDD nicht gegeben [2](../quellen.md).

Eine Erweiterung des Test-driven developments ist das Behavior-driven development. Die Methode verwendet eine eigene Sprache (domain-specific scripting language = DSL) um Testfälle zu beschreiben. Die verwendete Sprache ist in der Regel strukturiert aufgebaut und sollte auch für „Nicht-Programmierer“ verständlich sein. Hierdurch soll ein noch stärkerer Bezug zu den Akzeptanzkriterien hergestellt werden.


![](/assets/BDD_Example.png)

Eine Unit wird durch ihr Verhalten beschrieben. Dieses Verhalten sind die Akzeptanzkriterien, aus welchen durch test-first Tests erstellt werden. Diese Tests gehen direkt aus den gegebenen User Stories hervor und dessen Akzeptanzkriterien. Die obige Abbildung zeigt ein Beispiel für einen solchen Behavior-Test [3](../quellen.md).
