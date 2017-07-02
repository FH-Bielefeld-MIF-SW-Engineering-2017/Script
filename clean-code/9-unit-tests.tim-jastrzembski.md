#  9 Unit-Tests

Unit-Tests finden heutzutage vor allem im Test Driven Development und agilen Softwareentwicklungsprozessen sehr viel Verwendung, was vor rund 20 Jahren (1997) noch ganz anders aussah: Viele konnten mit dem Begriff "Unit-Test" nichts anfangen, da es prinzipiell nur Wegwerfcode war, welcher nur bestätigt hat, dass ihr Programm "läuft". Zwar werden viele automatisierte Unit-Tests geschrieben, jedoch vergessen die meisten den wahren Sinn dieser Tests.

## Die 3 Gesetze des TDD

Test Driven Development setzt voraus, dass vor dem Verfassen des eigentlichen Quellcodes die dazugehörigen Tests geschrieben werden. Darüber hinaus gibt es diese drei Gesetze, welche die wesentliche Struktur der Test definieren: 

1. **Gesetz**: Schreibe zuerst den zum Quellcode passenden Test, bevor du den Quellcode selbst verfasst.
2. **Gesetz**: Schreibe nur so viele Unit-Tests wie nötig, damit ein Test fehlschlagen kann. Ein nicht kompilierbarer Test ist auch ein Fehlgeschlagener Test.
3. **Gesetz**: Schreibe nur so viel Code wie nötig, um den aktuell fehlgeschlagenen Test zu bestehen.

## Tests sauber halten

Viele Programmierer tendieren dazu, "Quick and Dirty" zu programmieren. Die resultieren Konsequenzen werden dabei mit der Zeit immer größer: Je schlampiger die Tests geschrieben werden und je größer der Quellcode wird. desto schwieriger kann er später geändert werden. Im schlimmsten Fall kann sich das Problem wie ein Rattenschwanz sowohl durch den Quellcode als auch durch die dazu geschriebenen Tests ziehen, sodass man im Endeffekt nun die doppelte Arbeitszeit in die Wartung der Tests und des Quellcodes investieren muss. Das kann zur Folge haben, dass die ganze Testsuite verworfen wird, was dann im Laufe der Zeit zu mehr Inkonsistenzen im Quellcode führt. Letztlich beginnt der Quellcode zu verfaulen.
Die Tests halten den Quellcode dementsprechend flexibel, wartbar und wiederverwertbar.

## Saubere Tests

Lesbarkeit ist der Schlüssel zu sauberen Tests. Die Tests sind lesbar, sofern diese klar und simpel formuliert sind. Das `BUILD-OPERATE-CHECK`-Pattern bietet eine simple und klare Struktur zum Aufbauen von Tests:
1. **BUILD**: In der ersten Phase werden Daten zum Testen vorbereitet.
2. **OPERATE**: In der zweiten Phase werden die Daten von der zu testenden Funktion genutzt.
3. **CHECK**: In der dritten Phase wird überprüft, ob die Funktion die Daten wie erwartet verarbeitet hat.

Zudem sollte man in Erwägung ziehen nur ein Assert und ein einzelnes Konzept pro Test zu verwenden. Somit bleibt der Test übersichtlich und ist für den Leser besser nachzuvollziehen.

### Domain-spezifische Testsprache

Es gibt Domain-spezifische Sprachen, welche Funktionen und Tools zum Testen von Quellcode bieten. Mithilfe dieser Sprachen ist das Erstellen und Lesen von Tests wesentlich einfacher.

## F.I.R.S.T.

Saubere Tests folgen auch folgenden fünf Regeln, welche unter dem Akronym FIRST bekannt sind. 

* **Fast**(Schnell): Tests müssen schnell sein, damit sie frequenziell getestet werden können. Sind sie zu langsam, wird zu weniger Teststarts tendiert, was dazu führen kann, das bestehende Probleme nicht schnell genug gefunden werden. Das wiederum führt dazu, dass man hinterher den Code aufräumen muss, was zusätzliche Zeit und Arbeit kostet.
* **Independent**(Unabhängig): Tests müssen unabhängig voneinander sein. Man muss alle separat starten können. Wenn Tests voneinander abhängig, verkompliziert sich die Fehleranalyse, da nicht direkt bekannt ist, welche der getesteten Funktion fehlerhaft ist. 
* **Repeatable**(Wiederholbar): Tests sollten in jeder Umgebung wiederholbar sein.  
* **Self-Validating**(Selbstvalidierung): Man kann Tests entweder bestehen oder bei diesen durchfallen. Entsprechend sollen Tests nur einen `boolean` zurückgeben können.  
* **Timeley**(Zeitig): Die Tests sollten direkt vor dem eigentlichen Quellcode entwickelt werden. Wenn der Quellcode davor entwickelt wird, könnte die Testentwicklung zu schwer erscheinen und wird letzten Endes vielleicht nicht umgesetzt. 



