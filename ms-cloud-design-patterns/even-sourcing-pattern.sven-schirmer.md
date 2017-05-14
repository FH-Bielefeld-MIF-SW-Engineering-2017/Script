# Event Sourcing Pattern
Bei dem Event Sourcing Pattern werden alle Veränderungen des Zustands eines Systems oder der Daten als Sequenz von Events gespeichert. 

## Problematik
Das herkömmliche [create, read, update, and delete (CRUD)](https://de.wikipedia.org/wiki/CRUD)  Model birgt einige Nachteile: <br /> 
Zunächst werden bei einem Update die alten Werte mit neuen Werten überschrieben. Das konventionelle Update impliziert demnach eine Löschung (Delete) der alten Daten, sofern kein Logfile existiert, welches alle Änderungen aufzeichnet. Bei einem Updatevorgang werden die Daten meißt gesperrt, wodurch andere Benutzer und Anwendungen keine Änderungen an den Daten machen können. Des Weiteren werden bei einem CRUD System die Operationen direkt auf dem Data Store durchgeführt. Hieraus relsultierte eine schlechtere Performance und Reaktion, sowie Skalierbarkeit des Systems.

## Lösung
Die Anwendung beschreibt die Änderungen der Daten als Events. Auch das Löschen der Daten ist ein Event. Diese Events werden asynchron an den Event Store verschickt und dort persistent abgelegt. Eine Löschung der Events im Event Store ist nicht vorgesehen, die Events sind immutable. Der Event Store published die Events an einen Topic, sodass alle Consumer die den Topic abonniert haben, die Events bekommen und verabeiten können. Typische Abbonnenten sind z.B. Controller für die Materialized View, die daraufhin die View aktualisieren. 
Für die Vereinfachung der Präsentationsschicht wird meißt für jede Entität der derzeitige Datenstand als materialized View gespeichert. 

Das Event Sourcing Pattern wird meißt zusammen mit dem [CQRS-Pattern]( Script/ms-cloud-design-patterns/command-and-query-responsibility-segregation-cqrs-pattern.tolga-aydemir.md)  eingesetzt. 

### Vorteile
Der Prozess, der die Events verarbeitet, kann von dem Prozess, welcher das Event erstellt hat, entkoppelt werden, sodass die Verarbeitung später erfolgen kann. Außerdem enstehen durch die Entkopplerung neue Skalierungsmöglichkeiten.
Der gesamte Systemänderungsverlauf bzw. die Datenhistorie kann durch eine erneute Betrachtung der Events erfolgen. Dies ist hilfreich z.B. für das Debugging und Testen der Systeme.
Zudem kann hier auch die Business Logik einer Historisierung der Entittäten erfolgen. Generell hat der Event Log einen hohen Business Value.

## Berücksichtigungen
Durch eine fehlende Allokation der Daten, kann es zu misständen kommen. Besondern wenn mehrere verschiedene Anwendungen oder auch Instanzzen Events publishen wollen. Die korrekte Reihenfolge kann so auch nicht immer gewährleistet werden.
Ein Timestamp der Events oder eine autoinkrementelle ID-Nummer kann hier für eine ACID-Fähigkeit Abhilfe schaffen.
Außerdem ist immer eine Verzögerung der zwei entkoppelten Prozesse zu bemerken, wenn das Event gepuplished wurde wartet es noch auf seine Verarbeitung.

Der aktuelle Datenstand  wird durch die Verarbeitung aller Events bestimmt. Bei einer Vielzahl an Events empfiehlt es sich Snapshots zu machen, um eine Verarbeitung aller Events zu umgehen, sodass nur die Events ab dem Snapshot verarbeitet werden müssen. 

## Empfehlungen für die Benutzung des Patterns
Die Vorteile des Event Sourcing Patterns überwiegen, wenn 

- die beiden Prozesse (Datenveränderung, Datenverarbeitung) entkoppelt werden sollen, Flexibilität des Systems
- Datenzustandverläufe von Interesse sind.
- eine hohe Skalierbarkeit erwartet wird.
- schnelle und einfache Anpassung an neue Business Logik gefordert wird.

Eine Verwendung des Patterns ist nicht empfehlenswert, wenn

- die traditionellen CRUD Mechanismen ausreichend sind, Historisierung der Daten nicht benötigt wird.
- ACID Fähigkeit vorhanden sein muss. 
- Echtzeitupdates der Views gefordert werden.
- Veränderungen der Datenbestände nicht erfolgen.
