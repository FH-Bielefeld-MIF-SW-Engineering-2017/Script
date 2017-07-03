## 3.6 E2E-testing Libraries
Neben Unit Tests ist es ebenfalls sinnvoll GUI-Tests zu entwickeln, um eine hohe Qualität zu erzielen. Diese Tests werden meist mit realen Endgeräten und Browsern automatisiert ausgeführt. Bei Single Page Application kann das Testen zu Problemen führen. Hierbei können Inhalte ohne das Laden einer neuen Seite dargestellt werden, was beim Testen schwer zu realisieren ist, da keine eindeutige Aktion kommt, dass eine Anfrage abgeschlossen wurde. Protractor bietet hier eine Lösung. [17](../Quellen.md)

### 3.6.1 Protractor
Die von Google für AngularJS entwickelte E2E-testing Library Protractor bietet die Möglichkeit das Frontend zu testen. Es nutzt die WebDriver-API von Selenium und zusätzlich das BDD-Testframework Jasmine. Als BBD-Framework können auch andere Frameworks, wie beispielsweise Mocha oder Cucumber verwendet werden. Protractor kann eigenständig identifizieren, wenn eine Seite komplett fertig geladen ist und realisiert automatisch Veränderungen. Es bietet Möglichkeiten, vereinfacht Elemente der Oberfläche ausfindig zu machen. [17](../Quellen.md)

Nach der Installation und Konfiguration von Protractor wird ein Selenium Server gestartet.
```javascript
exports.config = {
  seleniumAddress: 'http://localhost:4444/test',
  specs: ['*.e2e.js'],
  multiCapabilities: [
    { browserName: 'firefox' },
    { browserName: 'chrome'  }
  ]
 }
 ```
Eine solche Konfigurationsdatei kann im Beispiel eingesehen werden. Es wird die Addresse des Testservers eingestellt und die Browser auf denen getestet werden soll. Mit dem "specs"-Attribut werden alle Datein (hier mit der Endung ".e2e.js") geladen, welche die auszuführenden Tests enthalten. [17](../Quellen.md)

```javascript
describe('Web Example', function() {
  it('should have a page title and submit button', function() {
    browser.get('https://testaddress/');
    expect(browser.getTitle()).toEqual('Test Page');
    expect(element(by.buttonText('Submit')).isDisplayed()).toBeTruthy();
  });
});
```
In diesem Beispiel lässt sich solch eine Testdatei erkennen. Es werden Beschreibungen angegeben, damit die Formatierung und Ausdrucksstärke in dem Testbericht vorhanden ist. Danach wird über die deklarierten Browser eine URL aufgerufen und das Ergebnis überprüft. Browser ist hierbei eine globale Variable, welche eine Webdriver Instanz darstellt. In diesem Test wird erst überprüft, ob der Titel der Seite tatsächlich "Test Page" lautet und ob auf der Oberfläche ein Button angezeigt wird, welcher den Text "Submit" beinhaltet. Mithilfe der globalen Variable "by" können HTML Elemente durch verschiedene Funktionen erleichtert gefunden werden. Durch "element" wird der Treffer zu einem Objekt, welches analysiert werden kann. [17](../Quellen.md)
