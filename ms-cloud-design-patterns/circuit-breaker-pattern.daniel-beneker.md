# Circuit Breaker Pattern

Mit diesem Pattern lässt sich auf Fehler, die unterschiedlich lange dauern,  angemessen reagieren. Die richtige Anwendung des Pattern kann die Stabilität und Elastizität eines Programms verbessern.

## Kontext und Problem

Es gibt zwei Arten von Fehlern: Kurzlebige Fehler, die sich oft nach kurzer Zeit auflösen, wie beispielsweise ein kurzeitig langsames Netzwerk und größere Fehler, die aus unerwarteten Ereignissen resultieren. Im letzteren Fall ist es sinnlos den ausgefallenen Service weiter anzusprechen. In diesem Fall sollte das Programm den Fehler schnell akzeptieren und entsprechend damit umgehen. 

## Lösung

Die Idee ist, das Programm davon abzuhalten Operationen, die sehr wahrscheinlich fehlschlagen, (erneut) auszuführen. In Abgrenzung dazu führt das „Retry Pattern“ Operationen erneut aus, wenn man davon ausgeht, dass sie funktionieren.
Das Circuit Breaker Pattern ist ein Proxy für Operationen die fehlschlagen können. Der Proxy misst die Anzahl vorheriger Fehler und entscheidet auf der Grundlage, ob weitere Operationen zugelassen werden oder nicht.

Implementieren lässt sich dieses verhalten als State Machine. Die folgende Abbildung stellt die State Machine mit den drei Zuständen Closed, Open und Half-Open dar.

![State Machine](https://github.com/FH-Bielefeld-MIF-SW-Engineering-2017/Script/blob/master/images/circuit-breaker-pattern.daniel-beneker.png „State Machine")
 
### Status: Closed

Dies ist der initiale Zustand. Alle Anfragen durchlaufen den Proxy und werden zugelassen. Kommt es bei einer Anfrage zu einem Fehler, wird er mit Hilfe eines Zählers registriert. Erreicht dieser Zähler einen Schwellwert, wird in den Status „Open“ gewechselt. Der Zähler sollte periodisch zurück gesetzt werden, damit gelegentliche Fehler nicht dazu führen, dass immer in den „Open“ Status gewechselt wird.

### Status: Open

Beim Wechsel in diesen Status wird ein Timeout-Timer gestartet. Der Proxy blockiert alle Anfragen und gibt entsprechende Exceptions zurück. Die Länge des Timeouts entscheidet darüber, wie lange alle Anfragen blockiert werden sollen. Ist der Timer abgelaufen, wird in den Status „Half-Open“ gewechselt.

### Status: Half-Open

In diesem Status wird ein Teil der Anfragen zugelassen. Mit diesem Status wird versucht zu erkennen, ob der entsprechende Service wieder erreichbar ist oder nicht. Es wird nur ein Teil der Anfragen zugelassen, um zu verhindern, dass ein Service, der wieder erreichbar ist, plötzlich mit so vielen Anfragen überflutet wird, dass er sofort wieder abstürzt. Alle erfolgreichen Anfragen werden gezählt. Schlägt eine Anfrage fehl, wird sofort wieder in den Status „Open“ zurück gewechselt. Wurde eine bestimmte Anzahl von Anfragen erfolgreich durchgeführt, ist davon auszugehen, dass der Fehler behoben ist. Es wird wieder in den Status „Closed“ gewechselt.

## Weitere Aspekte

* Exception Handling: Falls vom Circuit Breaker eine Exception geworfen wird, sollte der Empfänger entsprechend reagieren, wie beispielsweise dem Benutzer eine Meldung anzuzeigen, die Oberfläche für eine gewisse Zeit zu deaktivieren oder alternative Operationen anbieten.
* Verschiedene Arten von Exceptions: Circuit Breaker selbst kann verschiedenste Exception erhalten, wenn er eine Anfrage ausführt und diese fehlschlägt. Auf verschiedene Exceptions könnte unterschiedlich reagiert werden. So könnten beispielsweise mehr Timeout Fehler eintreten, bis in den „Open“ Status gewechselt wird, als bei einer allgemeinen Exception, die auf einen schwerwiegenderen Fehler hinweist.
* Logging: Fehlgeschlagene Anfragen sollten gespeichert werden. Außerdem sollte die State Machine an sich überwacht werden. Bei einem Wechsel in den Status „Open“ kann beispielsweise der Systemadministrator benachrichtigt werden.
* Fehlgeschlagene Operationen testen: Statt eines Timeout-Timers im „Open“ Status, kann der nicht erreichbare Service testweise angesprochen werden, um festzustellen, wann der Service wieder erreichbar ist. Dies kann mit einem einfachen Ping-Befehl oder über einen speziellen Health Endpoint realisiert werden.
* Manuelle Steuerung: Es sollte möglich sein, dass beispielsweise der Systemadministrator manuell einen bestimmten Status setzen kann.
* Overhead: Ein Circuit Breaker kann Ziel sehr vieler Anfragen werden und sollte daher nur einen kleinen Overhead erzeugen.
* Ressourcen differenzieren: Angenommen in einem Data-Store-Service ist eine Datei nicht mehr erreichbar, dann könnte es sein, dass der Circuit Breaker in den Status „Open“ wechselt und alle Anfragen blockiert, obwohl alle anderen Dateien des Data-Stores problemlos erreichbar sind.
* Fehlgeschlagene Anfragen erneut ausführen: Statt in einem Fehlerfall direkt eine Exception zu werfen, können auch alle Anfragen gesammelt werden und ausgeführt werden, sobald der Service wieder erreichbar ist.

---
**Quelle:**  
Cloud Design Patterns  
A. Homer, J Sharp, L. Brader, M. Narumoto, T. Swanson  
Microsoft 2015  
ISBN 979-1-62114-036-8 
Seite 14 bis 22 
