## 3.5 Mocking Frameworks
Im Allgemeinen werden Mocking Frameworks verwendet, um die Interaktion mit Abhängigkeiten zu überprüfen. Dabei kann getestet werden, wie sich das externe Modul verhält und was bestimmte vorgegebene Rückgabewerte im weiteren Verlauf auslösen. Ebenso kann verhindert werden, dass die externen Module überhaupt ausgeführt werden und stattdessen ein gemocktes Modul ausführen. Dies ist notwendig, da es Anwendungsfälle gibt, bei denen nicht direkt getestet werden kann oder sollte, wie zum Beispiel Datenbankzugriffe, bei denen eine Testdatenbank mit Testdaten erforderlich ist. [13](../Quellen.md) [14](../Quellen.md)
### 3.5.1 Sinon.js
Sinon bietet Funktionalitäten an, um diese Anforderungen vereinfacht durchzuführen. Zum Analysieren der Funktionsaufrufe bietet Sinon Spies an. Damit kann überprüft werden, wie oft eine Funktion aufgerufen wurde und welche Parameter übergeben wurden. [13](../Quellen.md) [14](../Quellen.md)

```javascript
it('should call save once', function() {
  var test = sinon.spy(ModuleName, 'testFunction');
  functionWhichIncludesTestFunction();
  sinon.assert.calledOnce(test);
});
```
Anhand des Beispiels kann ein solcher Aufruf dargestellt werden. Der Spy wird auf eine bestimmte Funktion in einem Modul initialisiert. Danach kann eine Funktion aufgerufen werden, welche die Testfunktion beinhaltet. Nun können Aussagen getroffen werden, ob die untersuchte Funktion tatsächlich aufgerufen wird oder nicht.

Spies sind lediglich Beobachter und nehmen keinen Einfluss auf Funktionen. Wird dies benötigt, kann auf Stubs gesetzt werden. Ein Beispiel dazu wäre der Test einer Funktion, welche Daten aus einer Datenbank ausließt. Ist die Datenbank leer oder keine Testdatenbank vorhanden, können solche Tests schlecht ausgeführt werden. Das Einrichten würde nun viel Zeit kosten. Stattdessen kann der Code durch ein Stub so manipuliert werden, dass das Testen auch ohne spezielle Einrichtungen stattfinden kann. [13](../Quellen.md)
```javascript
var stub = sinon.stub(modelService, 'getModel')
                .returns(new Model('Example Model'));
```
Bei diesem Beispiel wird deutlich, dass die Methode des modelService, 'getModel' immer ein neu erzeugtes Model zurückliefert. Diese Methode könnte ohne den Stub versuchen, das Model aus der Datenbank zu laden. Durch diese Deklarierung wird die ursprüngliche Methode überschrieben und Tests könnten mit diesem Model-Objekt weiterarbeiten. [13](../Quellen.md)

Ebenfalls kann mit Stubs geprüft werden, ob im Fehlerfall wirklich bestimmte, im Test vorher festgelegte, Fehlermeldungen auftreten. Es können auch asynchrone Funktionen getestet werden, indem ein erwartetes Callback mitgegeben wird und der Test synchron ausgeführt wird. [14](../Quellen.md)

Sinon bietet dazukommend noch die Möglichkeit Mocks zu erzeugen. Mocks werden dann interessant, wenn mehrere, bestimmte Verhaltensweisen geprüft werden sollen. Darum werden die Annahmen auch vorher definiert und erst dann wird die Funktion ausgeführt. Die verschiedenen Annahmen können so in einem Statement deklariert werden. Mit Stubs können solche Tests ebenfalls ausgeführt werden, jedoch müssten dann auch mehrere Annahmen unabhängig voneinander geschrieben werden, was zu großen Codeblöcken führen kann. Bei Mocks sollte darauf geachtet werden, nicht zu viele Annahmen auf einmal zu überprüfen, da sonst kleine Änderungen im Code, welche keine dramatischen Auswirkungen haben, zu Fehlerfällen führen. [14](../Quellen.md)
