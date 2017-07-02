#  12 Emergenz

Kents Becks regeln des "Simple Design"s

Nach Kent Beck ist ei Desing einfach ("simple") wenn es den folgenden Regeln folgt:

1. Es besteht alle (geschriebenen) Tests
2. Es enthält keinen doppelten Code
3. Es drückt die Absicht des Programmierers aus
4. Es hat so wenig wie möglich Klassen und Methoden

Die Regeln sind ihrer Wichtigkeit nach aufsteigend Nummeriert. 

## Regel 1 - Es besteht alle Tests

Ein System das nicht Testbar ist kann nicht verfiziert werden. Ein System das nicht verifiziert werden kann sollte nich eingesetzt werden.

Ein System zu erstellen das testbar ist bringt Anforderungen an die Architektur und den Quelltext mit sich. Um die einzelnen Teile des Systems testbar zu machen müssen die Anforderungen aus den vorhergehenden Kapiteln befolgt werden. Software Testbar zu machen führt zu niedriger Koppelung sowie hohe Kohäsion.

## Regel 2-4 - Refactoring

Die erste Regel ermöglicht es festzustellen ob vorherige Funktionen durch spätere Änderungen verändert werden. Die Regeln 2-4 können nun durch Refactoring erreicht werden. Eine nicht-saubere Code-Base kann Schritt für Schritt in eine saubere überführt werden.

Dabei sind vorallem folgende Regeln einzuhalten:

* Kein doppelter Code: Doppelter Code macht es schwer die funktionfähigkeit eines System aufrecht zu erhalten. 
* Ausdruck der Absicht: Die Absicht des Programmiers sollte im Code, auch ohne Kommentare, ersichtlich sein. Code wird öfter gelesen als geschrieben, hierüber sollte man sich beim Schreiben von Code klar sein.
* so wenig wie möglich Klasse und Methoden: Die richtige Anzahl an Klassen und Methoden zu finden ist schwer, gerade wenn das System dem SRP folgen soll. Man sollte jedoch versuchen die Anforderungen mit so wenig wie möglich Klassen zu erreichen.

