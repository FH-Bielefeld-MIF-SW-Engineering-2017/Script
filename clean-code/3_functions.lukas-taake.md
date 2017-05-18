# 3 Functions
Funktionen sind der grundlegenste Bestandteil zur Strukturierung von
Sofware, sie stammen bereits aus Zeiten von Fortran und PL/1.
Ihre Struktur und Qualität macht einen wichtigen Bestandteil zur Lesbarkeit
von Quellcode aus.
Die wichtigsten Merkmale, um gute Funktionen zu schreiben, werden in diesem Kapitel erläutert.

*Anm. d. zusammenfassenden Autors: Das Buch enthält zahlreiche Codebeispiele zur Erläuterung.
Diese werden aus Gründen der Übersicht nicht übernommen.*

Gute Funktionen sollten **nicht besonders groß** sein. Als Richtwert wird eine Obergrenze von 20 Zeilen
gegeben. Das hat zur Folge, dass sie zu kurz sind um viele verschachtelte Kontrollstrukturen zu enthalten.
Große Blöcke innerhalb von Kontrollstrukturen sollten dann in separate Funktionen ausgelagert werden.
Das bietet zusätzliche Dokumentation in Form eines Funktionsnamens für diesen Block.

Eine Funktion sollte **genau eine Sache tun**. Diese dafür gut und ausschließlich.
Sie sollte, um ihren Zweck zu erfüllen, andere Funktionen der nächst niedrigeren
Abstarktioinsstufe aufrufen. Es ist ein gutes Indiz, dass eine Funktion mehr als eine Sache tut,
wenn eine weitere Funktion extrahiert werden kann, deren sinnvoller Name mehr als eine Neuformulierung
ihrer Implementierung ist. Ein weiteres Indiz ist die Unterteilung einer Funktion in Sektionen
mittels Kommentaren.

Es sollte nicht mehr als **ein Abstraktionslevel pro Funktion** aufgerufen werden.
Sie sollte nur ein Konzept auf nächst niedrigere Stufe hinunter brechen.
Andernfalls kann das einen Leser verwirren, der mit den niedriglevligen Details einer Anwendung nicht
vertraut ist. Essentielle Funktionen können so schnell zusammen mit Details vermischt werden.

**Switch Statements sollten vermieden werden**, denn sie tun per Definition immer mehr als eine Sache.
In Objektorientierten Spachen können sie durch Polymorphismus fast vermieden werden.
Sie müssen lediglich z.B. in einer *Abstract Factory* zur Erzeugung der entsprechenden Klassen
eingesetzt werden, können aber an sonsten aus dem Code ferngehalten werden.

Funktionen sollten **beschreibende Namen** tragen. Auch eine kurze Funktion sollte eher einen längeren,
aber guten, als einen kurzen, wenig aussagekräftigen Namen tragen. Außerdem sind beschreibende Namen
besser, als beschreibende Kommentare. Dazu sollte eine Namenskonvention verwendet, die es erlaubt,
leicht Namen aus mehreren Worte zu bilden. Wichtig ist, dass die Namensgebung konsistent ist
gleiche Sachverhalte immer gleich benennt. Darüber hinaus ist es nicht völlig untypisch,
dass die Suche nach einem guten Namen in der Restrukturierung des Codes endet.

Die **Anzahl der Parameter** sollte so niedrig sein, wie möglich.
Bevorzugt sind gar keine Parameter, ein oder zwei sind ebenfalls unproblematisch.
Drei Parameter sollten vermieden werden, wenn möglich, und mehr sollten auf keinen Fall verwendet werden.
Unter Umständen ist es sinnvoll, stattdessen Instanz-Variablen zu verwenden.
Return-Parameter sollten generell vermieden werden.
Viele Parameter führen neben mehr kognitivem Aufwand beim Lesen einer Funktion auch und vor allem
zu einem deutlich erhöhten Testaufwand. Während eine Parameterlose Funktion sehr einfach zu testen ist,
liegt der Aufwand bei drei oder mehr Parametern äußerst hoch, um alle Kombinationen zu prüfen.

Beispiele für Funktionen mit einem Parameter , der "monadische Form", sind etwa das Stellen einer Frage
`boolean fileExists("FileName")` oder das Umformen eines Parameters `InputStream fileOpen("FileName")`,
hier wird der String-Parameter in einen InputStream umgewandelt.
Auch die Behandlung von Events kann so gut umgesetzt werden.

