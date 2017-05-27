#  4 Kommentare

Kommentare in Quelltexten sind meistens ein "notwendiges Übel", welche verwendet werden müssen, da Programmiersprachen nicht
aussagekräftig genug sind. Kommentare würden nicht benötigt werden, wenn Programmiersprachen die Absichten der Programmierer
besser ausdrücken würden. Deswegen werden Kommentare eingesetzt, um zu erklären, warum ein bestimmter Ansatz gewählt wurde.

Das Einsetzen von Kommentaren ist in der Regel schlecht, da es bedeutet, dass eine Absicht nicht durch den Quelltext ausgedrückt
werden kann und der Code nicht aussagekräftig genug ist. Wenn man dabei ist, einen Kommentar zu schreiben, sollte man scih überlegen,
ob man den Quelltext nicht so umschreiben kann, dass er aussagekräftiger ist und somit kein Kommentar benötigt wird.
Häufige Probleme mit Kommentaren sind zum Beispiel Kommentare, die irreführend sidn oder Falschinformationen liefern. Desweiteren
werden viele Kommentare nicht angepasst, wenn der Code umgebaut wird.

## Gute Kommentare
Es gibt einige Arten von Kommentaren, die gut sind und deren richtiger Einsatz meist erwünscht ist. Trotzdem sollten Kommentare
nur sparsam eingesetzt werden. So sind zum Beispiel
rechtliche Kommentare erwünscht, die Copyright-Informationen angeben und beschreiben, unter welcher Lizenz der Quelltext
steht. Diese Kommentare sind notwendig, sollte aber so kurz wie möglich gehalten werden. Es ist besser, auf ein
externes Dokument zu verweisen, welches Informationen zu der Quelltext-Lizenz enthält, als den gesamten Lizenz-Text als Kommentar
einzufügen.

Weiterhin sind informative Kommentare erwünscht, die zum Beispiel angeben, welches Muster ein regulärer Ausdruck als gültig
erkennt. Neben dieser Art von Kommentaren zählen Kommentare, die beschreiben, warum eine bestimmte Lösung gewählt wurde,
zu den guten Kommentaren. Sie erklären, warum ausgerechnet die Lösung, die implementiert wurde, gewählt wurde.

Ein großes Problem sind nichtsaussagende Rückgabewerte, die meist Integerwerte sind. Ein gutes Beispiel sind die Rückgabewerte
der compareTo()-Methode. Die beste Lösung für dieses Problem wäre eigentlich, dass der Code so geändert wird, dass die
Rückgabewerte aussagekräftig sind. Dies lässt sich aber nicht immer durchführen, da man nicht jeden Quelltext ändern kann
(die Standard-Bibliothek zum Beispiel). In diesem Fall ist es dann angebracht, Kommentare zu verwenden, die die Bedeutung des
Rückgabewertes beschreiben. Ein Risiko besteht darin, dass die Kommentare falsch sind, wenn der Code geändert wurde,
die Kommentare aber nicht angepasst wurden.

Desweiteren sind Kommentare erwünscht, die vor Gefahren warnen. Zum Beispiel, wenn eine bestimmte Methode nicht threadsafe ist.

TODO-Kommentare sind meist nützlich, um sich schnell Aufgaben für bestimmten Code-Teilen zu notieren. Auch, wenn Aufgaben
an andere abgegeben werden sollen, sind TODO-Kommentare nützlich. Zu beachten ist, dass sie wieder schnell aus dem Quelltext
entfernt werden.

Zusätzlich sind Kommentare, die die Wichtigkeit von Code hervorheben, angemessen, wenn der Code überflüssig erscheint, um
Probleme zu verhindern. Andere Entwickler könnten ansonsten Codeteile überarbeiten und wichtigen, aber überflüssig
erscheinenden Code entfernen.

Weitere wichtige Kommentare sind JavaDocs für öffentliche APIs. Ohne gute Dokumentation sind neue APIs nur schwer zu verwenden.

## Schlechte Kommentare
Die meisten Kommentare sind schlecht. Viele Kommentare sind meist ein Indikator für schlechten Code. So sollten zum Beispiel
redundante Kommentare, also Kommentare, die selbsterklärenden Code erklären vermieden werden. Außerdem werden manchmal Kommentare
geschrieben, die irreführend und nicht präzise genug sind. Sie können den Betrachter verwirren und letztendlich muss er sich
doch den Quelltext ansehen, um zu verstehen, was dort passiert. Eine weitere schlechte Art von Kommentare sind Kommentare,
die wegen Coding-Richtlinen geschrieben werden und eigentlich nicht nötig wären. Sie blähen den Quelltext nur unnötig auf und
hindern Betrachter daran, schnell durch den Quelltext durchzusteigen.

Desweiteren sollten Kommentare mit Änderungshinweisen vermieden werden. Dies sind Kommentare, die auflisten, wann wer welche
Änderung an der Datei durchgeführt hat. Heute gibt es dafür Versionierungssysteme, die diese Aufgabe übernehmen. Genauso sind
Kommentare überflüssig, die die Autoren von Codeblöcken angeben. Auch diese Aufgabe übernehmen Versionierungssysteme.
Außerdem sollten auch überflüssige Kommentare vermieden werden. Kommentare für Getter- und Setter-Methoden werden zum
Beispiel nicht benötigt. Sie sind redundant, da der Name der Methode schon aussagt, welchen Wert die Methoden zurückliefern
oder entgegennehmen.

Auch sollten Kommentare nicht verwendet werden, wenn sie durch die Benutzung von Variablen oder Funktionen überflüssig wären.
So sollten Codeblöcke in Methoden mit aussagekräftigen Namen ausgelagert werden, wenn sie Kommentare benötigen, die beschreiben,
was die Codeblöcke machen.

Positionsmarkierungen, also Kommentare, die Gruppen von Funktionen und Methoden markieren, sollten nur selten eingesetzt werden.
Werden Positionsmarkierungen zu häufig eingesetzt, werden sie ignoriert und blähen damit den Quelltext nur unnötig auf.

Ein Indikator für zu große Codeblöcke sind Kommentare, die angeben, zu welcher öffnenden Klammer eine schließende Klammer
gehört. Sind diese Art von Kommentaren notwendig, sind die Codeblöcke zu groß und müssen zum Beispiel durch Auslagerung
von Codeteilen in Methoden verkleinert werden.

Quelltext, der auskommentiert ist, sollte entfernt werden. Codeleichen machen den Quelltext unübersichtlich. Versionierungssysteme
helfen dabei, Code, der entfernt wurde, wiederzubeschaffen.

Kommentare, die HTML-Formatierungen beinhalten sollte außerdem nicht verwendet werden. Auch sie blähen den Quelltext unnötig auf
und machen die eigenltichen Kommentare im Quelltext schwer lesbar. Die Programme, die die Kommentare aus den Quelltexten
extrahieren, sollten die Formatierungen hinzufügen.

Auch Kommentare, die Informationen zum gesamten System enthalten oder Teile beschreiben, die nichts mit dem direkt anliegenden
Codeblock zu tun haben, sollten vermieden werden. Es besteht die Gefahr, dass der Kommentar nicht angepasst wird, wenn
etwas an anderer Stelle geändert wird. Wenn ein Kommentar geschrieben werden muss, sollte darauf geachtet werden, dass
er nur den direkt anliegenden Codeblock beschreibt. Außerdem sollten Kommentare immer kleingehalten werden und nicht einen
standardisierten Ablauf erklären. Diese Informationen können im Internet nachgelesen werden. Man sollte hierbei lieber
auf die entsprechenden Dokumente dazu verweisen.

Außerdem sollten JavaDoc-Kommentare in nichtöffentlichem Quelltext vermieden werden. Sie liefern keine nützlichen Informationen
und das Warten der JavaDoc-Kommentare ist umständlich.
