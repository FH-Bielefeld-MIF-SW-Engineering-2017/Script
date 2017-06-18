# Unterstützende Workflows
## DevOps
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

In jeder Umgebung wird der Quelltext unterschiedlich getestet. Es ergibt sich der Vorteil, dass mit jeder erfolgreich durchlaufenen Umgebung die Wahrscheinlichkeit wächst, dass der Quelltext auch in der Produktiv-Umgebung lauffähig sein wird.

## Continuous Deployment
### TDD, BDD, ATDD
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
