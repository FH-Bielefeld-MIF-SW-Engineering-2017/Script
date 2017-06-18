# Unterstützende Workflows
## DevOps
## CI
## CD
## CD
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
