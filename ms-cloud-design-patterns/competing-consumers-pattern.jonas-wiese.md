# Competing Consumers Pattern
Falls eine Cloud basierte Anwendung viele Anfragen bearbeiten muss, die Anzahl der Anfragen aber stark schwankt, kann es sinnvoll sein, eine „Message Queue“ zu verwenden. Mit Hilfe dieser Queue kann die Anwendung (Producer) die Nachrichten zu anderen Anwendungen (Consumer Services) umleiten. Diese Consumer Services können die Nachrichten dann Asynchron und frei Skalierbar abarbeiten. 
## Vorteile
Da die Anzahl der Consumer Services variierbar ist, ermöglicht dieses Pattern eine inhärente Last Verteilung. Falls viele Anfragen eintreffen können weitere Instanzen des Consumer Service gestartet werden. Diese können, wenn die Anzahl der Anfragen abnimmt, abgeschaltet werden. Da die Message Queue als Buffer dient, ist eine Synchronisierung zwischen Producer und Consumer nicht nötig. Die Queue führt außerdem dazu, dass jede Anfrage mindestens einmal bearbeitet wird. 
Falls ein Consumer während der Bearbeitung einer Anfrage abstürzt, kann die Queue so konfiguriert werden, dass eine andere Instanz die Anfrage erneut bearbeitet. 
## Nachteile
Durch die Verwendung einer Message Queue ist nicht garantiert, dass die Nachrichten in der gleichen Reihenfolge, wie sie eingetroffen sind bearbeitet werden.
Da die Queue nur dafür sorgt, dass jede Nachricht mindestens einmalig bearbeitet wird, kann es vorkommen, dass eine Nachricht mehrfach abgebarbeitet wird. 
Da durch die Queue keine direkte Kommunikation zwischen Producer und Consumer erflogt, sie also füllig entkoppelt sind, ist es schwierig die Ergebnisse des Consumers zurück an den Producer zu liefern.  
Auch die Message Queue kann bei zu vielen Nachrichten zu Flaschenhals werden. 
## Fazit
Das Pattern sollte verwendet werden, wenn die Anzahl der Anfragen stark variiert und die Aufgaben der Anwendung gut Asynchron zu verarbeiten sind. Außerdem müssen die Aufgaben unabhängig voneinander sein und parallel verarbeitet werden können. 
Falls die Aufgaben nicht gut voneinander getrennt werden können oder die Reihenfolge der Aufgaben wichtig ist, ist das Pattern nicht sinnvoll zu Verwenden. 
