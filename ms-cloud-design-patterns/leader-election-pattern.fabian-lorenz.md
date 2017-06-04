# Leader Election Pattern

Das Leader Election Pattern hat zum Ziel, die Aktionen mehrerer verteilter Komponenten, die an einer gemeinsamen Aufgabe arbeiten, zu koordinieren. Dafür wird aus allen Komponenten eine Komponente ausgewählt, die nun die Arbeit der anderen Komponenten managt. Somit wird verhindert, dass sich die Komponenten in ihrer Arbeit gegenseitig behindern, beispielsweise wenn versucht wird auf dieselbe Ressource zur gleichen Zeit zuzugreifen.  

## Problemhintergrund

Typischerweise ist es bei verteilten- oder Cloud-Anwendungen so, dass es mehrere Komponenten/Instanzen gibt, die beispielsweise denselben Programmcode beinhalten und auf gemeinsame Ressourcen zugreifen müssen. Dies kann bei skalierbaren Anwendungen der Fall sein, wenn beispielsweise jede Komponente für genau einen Benutzer zuständig ist, aber auf gemeinsame Ressourcen zugegriffen werden muss. Damit beim Zugriff auf diese gemeinsamen Ressourcen nicht unter anderem die Änderungen von einer Ressource von einer anderen stumpf überschrieben werden, muss dieser Zugriff koordiniert werden.  
Auch ist es möglich, dass jede Komponente nur einen kleinen Teil einer großen Aufgabe bearbeitet und am Ende alle Teilergebnisse zusammengeführt werden müssen.  
Da in beiden Fällen jede Komponente gleichgestellt ist (Peer), gibt es keine direkte Komponente die speziell für die Koordination zuständig ist.

## Lösung  
Um dieses Problem nun zu lösen, muss eine Instanz aus allen Instanzen gewählt werden, die nun die Leitung der anderen übernimmt. Da alle Instanzen dieselbe Code-Basis aufweisen, ist es somit möglich, dass jede beliebige Instanz zum Leiter ernannt wird. Der Prozess zur Wahl des Leiters muss also genau koordiniert werden, damit es nicht zu Fehlern kommt und es beispielsweise zwei oder mehr Instanzen gibt, die die Leitung übernehmen.
Des Weiteren muss darauf geachtet werden, dass im Fehlerfall, beispielsweise bei einem Netzwerkausfall, ein neuer Leiter ernannt wird, wenn der alte seine Aufgabe nicht mehr absolvieren kann. Häufig wird dies so gelöst, dass jede Instanz den Leiter überwacht, beispielsweise durch einen Herzschlag-Mechanismus oder einfachem Abfragen des Leiters. Tritt dabei ein Fehler auf, wählen die verbleibenden Instanzen unter sich einen neuen Leiter aus.
Die Wahl eines Leiters kann dabei beispielsweise folgendermaßen ablaufen:

* Es wird die Instanz mit der niedrigsten Prozess ID gewählt.
* Es existiert ein Mutex, der von allen versucht wird zu erreichen. Die Instanz die den Mutex zuerst bekommt wird zum Leiter. Dabei muss allerdings sichergestellt werden, dass der Mutex freigestellt wird, wenn der Leiter beispielsweise durch einen Fehler vom Netzwerk getrennt wird.
* Implementierung verschiedenster Leader Election Algorithmen, beispielsweise Bully- oder Ring-Algorithmus. Diese setzen voraus, dass jede Instanz eine eigene einzigartige ID besitzt und das die Instanzen untereinander kommunizieren können.  

## Probleme und Überlegungen

Folgende Punkte müssen bei der Anwendung dieses Patterns beachtet werden:

* Der Prozess zum Wahl eines Leiters muss Fehlerresistent sein.
* Es muss möglich sein den Ausfall eines Leiters festzustellen und entsprechend zu handeln, beispielsweise indem ein neuer Leiter gewählt wird.
* In skalierbaren Systemen ist es möglich, dass die Instanz die zum Leiter gewählt wurde beendet wird, wenn weniger Ressourcen benötigt werden und das System runter skaliert.
* Wird ein Mutex zur Wahl eines Leiters genutzt, ist der gesamte Prozess auch abhängig davon. Fällt der Zugriff zu dieser Mutex-Ressource aus, so kann auch kein neuer Leiter gewählt werden und das gesamte Peer System kann zusammenbrechen.
* Die manuelle Implementierung von einem der vorhandenen Leader Election Algorithmen bietet die größte Flexibilität und Anpassbarkeit.  

## Wann sollte es genutzt werden

Dieses Pattern sollte genutzt werden, wenn es in einem Verteilten (Cloud) System mehrere gleichgestellte Instanzen/Komponenten gibt, deren Zusammenarbeit sorgfältig koordiniert werden muss und es keinen direkten eigenständigen Leiter gibt.
Der gewählte Leiter sollte dabei nur die Koordination der Arbeit der anderen Instanzen übernehmen und nicht noch selbst diese Arbeit ausführen, um zu verhindern, dass die Kommunikation verlangsamt wird.  
Dieses Pattern sollte nicht verwendet werden wenn:

* Es einen speziellen Prozess gibt, der die Aufgabe der Koordination übernimmt und somit immer als Leiter fungiert. Dies könnte beispielsweise durch ein Singleton Prozess umgesetzt werden, welcher im Fehlerfall neugestartet werden kann.
* Die Koordination durch deutlich einfachere Verfahren abgewickelt werden kann. Beispielsweise kann im Fall, dass mehrere Instanzen den Zugriff auf eine gemeinsame Ressource benötigen ein optimistischer oder pessimistischer Kontrollzugriff (Locking) realisiert werden.
* Es entsprechende Drittanbieter Lösungen/Frameworks gibt, die diese Koordination der einzelnen Prozesse übernehmen können.
