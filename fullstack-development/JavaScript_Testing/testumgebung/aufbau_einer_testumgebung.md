# 3 Aufbau einer Testumgebung
Das folgende Diagramm soll bei dem Verständnis helfen, wie eine Testumgebung aufgebaut ist und die einzelnen Frameworks und Libraries miteinander interagieren.
![Interaktion zwischen Testframeworks und Libraries](/assets/Testumgebung.png)
Auf die einzelnen Punkte des Diagramms wird im späteren Verlauf eingegangen. Die in Klammern aufgeführten Frameworks und Libraries geben ein Beispiel zu dem Oberpunkt an. Es gibt wesentlich mehr Möglichkeiten diese Struktur mit anderen Technologien aufzubauen.
## 3.1 Test Runner
Test Runner erfüllen das Ziel die entwickelten Tests automatisiert auszuführen und eine gut formatierte und ausdrucksstarke Ausgabe der Testergebnisse anzuzeigen. [10](../Quellen.md)
### 3.1.1 Karma
Karma ist ein Test Runner und wird verwendet um die entwickelten JavaScript Tests automatisiert ausführen zu lassen. Es wurde zuallererst unter dem Namen Testacular veröffentlicht. Google entwarf es bei der Entwicklung von AngularJS und stellte es kostenlos, quelloffen und öffentlich zur Verfügung. Ziel war es, eine effiziente und einfache Testumgebung zu entwerfen. Karma basiert auf Node.js und Socket.io. Es zeichnet sich besonders durch seine Einfachheit und gute Performance aus. Durch das automatisierte  Ausführen von Tests können Fehler während der Entwicklungsphase vermieden werden. Ebenfalls kann mittels Karmas Unterstützung sehr gut Test Driven Development (TDD) umgesetzt werden. [1](../Quellen.md)

Karma besitzt eine Konfigurationsdatei, in der verschiedene Herangehensweisen deklariert werden können. So kann durch das autowatch Attribut mitgeteilt werden, dass die Tests immer dann ausgeführt werden sollen, sobald sich eine Datei verändert. Es können auch Einstellungen bezüglich der Browserwahl, wie beispielsweise, dass die Tests in Chrome und Firefox laufen sollen, vorgenommen werden. Dazu werden die Source Dateien in ein IFrame geladen und die Tests werden ausgeführt. Die Ergebnisse werden dann zurück an den Server versandt. [4](../Quellen.md)

Es ist ebenfalls möglich mit Karma End-to-end Tests durchzuführen, jedoch ist Karmas Design auf low level unit testing ausgelegt. Für diesen Anwendungszweck sollte vorzugsweise auf high level unit testing zurückgegriffen werden, auf welche im späteren Verlauf eingegangen wird. Karma lässt sich zudem sehr einfach mit einem Continuous Integration System, wie beispielsweise Jenkins und mit IDE’s wie Webstrom oder dem Browser Google Chrome verknüpfen. [2](../Quellen.md) [3](../Quellen.md)

## 3.2 Browserify und Watchify
Browserify hilft dabei die externen Javascript Abhängigkeiten und die selbst entwickelten Module zu bündeln und im Webbrowser bereit zu stellen. Dazu wird für jede Browser Ansicht eine JavaScript Datei erstellt, welche die zu bündelnden Abhängigkeiten inkludiert. In dieser Datei können dann Funktionen aufgerufen werden, welche auf dem Browser ausgeführt werden sollen. Wird eine Abhängigkeit bzw. eine JavaScript Datei verändert oder neu hinzugefügt, muss ein einziger Befehl aufgerufen und die aktuelle Seite im Browser neu geladen werden, um die aktualisierten Module nutzen zu können. Um diesen Schritt noch weiter zu vereinfachen gibt es Watchify. Hiermit werden Veränderungen automatisch erkannt und das JavaScript Bündel automatisch neu erstellt. Ein einfaches Neuladen der Seite reicht hierbei aus. [24](../Quellen.md)
## 3.3 Test Frameworks
### 3.3.1 Mocha
Mocha wurde 2011 von Tj Holowaychuk, dem Gründer von ExpressJS und weiteren erfolgreichen NodeJS Projekten, entwickelt und ist eine der meistgenutzten Test Frameworks. Die erste Version wurde 2012 veröffentlicht. Es ist für das Behaviour Driven Development (BDD) geeignet und hat sowohl einen eigenen Test Runner als auch eine Browser Unterstützung integriert. Das Testen von asynchronen Funktionen wird durch die eigene done() Funktion unterstützt. Mocha bietet die Möglichkeit an vor dem Test Initalisierungsfunktionen und nach dem Test Aufräumfunktionen sowohl synchron als auch asynchron auszuführen. [6](../Quellen.md) [7](../Quellen.md) [12](Quelen.md) [19](../Quellen.md)
```javascript
var assert = require('chai').assert;
describe("Numbers",function(){
  it('should add two numbers',function(){
    assert.equal(5, 3 + 2, '5 equal 3 + 2');
  })
});
```
Mocha besitzt keine integrierte Assertion Library. In diesem Beispiel wurde Chai gewählt, welches im späteren Verlauf näher erläutert wird. Der Test erhält eine Überschrift, welche in der Test Ausgabe als erstes ersichtlich ist und die Unit Tests somit in der Ausgabe gruppiert. Danach wird die Funktion getestet, welche ebenfalls eine Beschreibung erhält. Über die Assertion Library Chai werden dann zwei Objekte auf Gleichheit geprüft und der Test abgeschlossen. Es können ebenfalls mit beforeEach und afterEach Vorbereitungen bzw. Aufräumarbeiten vor und nach den Tests ausgeführt werden. [6](../Quellen.md)
### 3.3.2 Tape
Tape’s Zielsetzung liegt darin, Tests so einfach und minimal wie möglich umzusetzen. Daher wird zum Ausführen von Tests nur das absolute Minimum an Tools benötigt. Ebenso gibt es keine Konfigurationsdateien. Es soll dem Entwickler die Möglichkeit bieten einfache, verständliche und modulare Tests zu schreiben. Tape besitzt standartmäßig einen Test Runner und eine Assertion Library. [10](../Quellen.md)
```javascript
var test = require('tape');
test('My first tape test', function(assert){
  assert.equal(1, 2, 'Numbers 1 and 2 are the same');
  assert.end();
});
```
Über node kann diese Test Datei einfach ausgeführt werden. Das Beispiel zeigt, dass wieder eine Beschreibung des Tests eingegeben werden kann, welcher in dem Testergebnis verzeichnet wird. Über den Funktionsparameter assert können Objekte getestet werden. In dem Beispiel werden zwei unterschiedliche Objekte auf Gleichheit geprüft. Da dies Fehlschlagen wird, wird in dem Fehlerbericht ebenfalls die Beschreibung des Tests ausgegeben. Durch assert.end() kann ausgesagt werden, dass der Test vorbei ist und keine Überprüfungen mehr stattfinden. Die standartmäßige Assertion Library von Tape bietet einen wesentlich eingeschränkteren Umfang als beispielsweise Chai. Es hilft jedoch dabei, sich schnell einarbeiten zu können und knappe und einfache Tests zu schreiben. Außerdem sollten die Funktionalitäten ausreichen, um alle möglichen Tests abbilden zu können. Tape besitzt zudem die Möglichkeiten mittels Browserify und testling, Tests im Browser auszuführen und Initalisierungs- sowie Aufräummethoden zu verwenden, jedoch müssen diese im Funktionsrumpf des Tests manuell aufgerufen werden. [10](../Quellen.md) [11](../Quellen.md)

### 3.3.3 Jest
Facebooks JavaScript testing Framework Jest kann mit dem vorher beschriebenen Framework Mocha verglichen werden. Es bietet jedoch viele Möglichkeiten, wie beispielsweise Mocking und Assertion ohne diese vorher installieren zu müssen. Eine einfache Installation von Jest reicht aus und es benötigt nur eine äußerst geringe Konfiguration. Ebenso ermöglicht Jest sehr vereinfacht Snapshot Tests mit dessen Hilfe überprüft werden kann ob sich die UI unerwartet verändert hat. [26](../Quellen.md) [27](../Quellen.md)

### 3.3.4 Vergleich von Javascript testing Frameworks
X | Mocha | Jest | Tape
------------ | ------------- | ------------- | -------------
Flexible Assertion Library Wahl | Ja | Nein | Nein
Installation | Komplizierter, da keine All-In-One Lösung | Einfach | Einfach
Performance | Schnell | Automocking verlangsamt | Schnell
CI-Unterstützung | Ja | Ja mit Einschränkungen | Ja
asynchrone Tests | Ja | Ja | Ja
snapshot testing | sehr schwer | sehr einfach | mit Snapshotter einfach
Mächtigkeit des Frameworks | mächtig | mächtig | nur das nötigste
Dokumentation | ausführlich | sehr gering | sehr gering

Bei der Wahl eines JavaScript testing Frameworks gibt es einige Punkte zu beachten. Es kommt meist auf den Anwendungsfall an und die Wahl sollte darauf abgestimmt sein. So bleibt dem Entwickler bei Mocha die freie Wahl, Reporting Tools, Test Runner und Assertion Libraries auszuwählen. Bei Jest und Tape sind diese bereits vorab vorhanden. Natürlich können auch hier Assertion Libraries hinzugefügt werden, jedoch eingeschränkter als bei Mocha. Die gewährte Flexibilität erschwert die Installation und Konfiguration. So haben Jest und Tape All-In-One Lösungen, welche hervorragend für einen schnellen Einsatz sind. Bei Mocha müssen erst die Libraries ausgewählt und hinzuinstalliert werden. Von der Performance sind alle Test Frameworks schnell, jedoch bietet Jest die Möglichkeit Abhängigkeiten automatisch zu mocken. Dies ist in der neuen Jest Version per default deaktiviert, kann jedoch im aktivierten Zustand zu Verlangsamungen führen. [21](../Quellen.md) [8](../Quellen.md)

Alle testing Frameworks besitzen eine Continuous Integration Unterstützung, jedoch kann es bei Jest beim snapshot testing auf einem CI System zu Fehlern kommen. Das automatische Erzeugen von Snapshots kann Möglicherweise fehlschlagen. Es wird hierbei empfohlen die Snapshots beim Test statisch in dem Projektordner zu speichern. [15](../Quellen.md) [22](../Quellen.md) [23](../Quellen.md)

Eine weitere Art des Testens, ist das Vergleichen von Snapshots, welche beispielsweise im JSON Format vorliegen können und somit das Herausfinden von unerwarteten Änderungen auf dem User Interface. Hierfür wird eine Datei, welche die aktuelle Ansicht darstellt, erstellt und beim Durchlaufen des Tests die veränderte Ansicht mit der gespeicherten verglichen. Jedes Framework besitzt die Möglichkeit, solche Tests durchzuführen. Bei Jest ist dies vorab schon vorhanden und sehr einfach umzusetzen. Bei den anderen beiden Frameworks müssen externe Libraries hinzugefügt werden, welche dies ermöglichen. [15](../Quellen.md) [16](../Quellen.md)

Da Tape's Grundprinzip lautet, sich nur auf das Wichtigste, nämlich das Testen, zu konzentrieren, ist der Umfang des Testframeworks wesentlich geringer als bei Mocha und Jest. Tape möchte mit möglichst wenig Einarbeitungszeit und nur den nötigsten Funktionen das Testen ermöglichen. Die Dokumentation ist bei Mocha im Gegensatz zu den anderen beiden Frameworks am ausführlichsten. [6](../Quellen.md)

## 3.4 Assertion Libaries
Assertion Libaries versuchen die Tests durch eigene Funktionen übersichtlicher, einfacher, aussagekräftiger und lesbarer zu machen. Teilweise können die Fehlermeldungen mit Beschreibungen verknüpft werden, welche vorher definiert wurden um direkt darauf hinzuweisen, an welcher Stelle der Fehler aufgetreten ist. Außerdem werden die Testfälle übersichtlich formatiert ausgegeben. Es werden meist auch zusätzliche Untersuchungsmöglichkeiten zur Verfügung gestellt. [10](../Quellen.md)
### 3.4.1 Chai
Chai bietet viele nützliche Erweiterungen. So kann mithilfe der Library getestet werden, ob Objekte ungleich null sind, größer oder kleiner sind und vieles mehr. Es besitzt drei verschiedene Assertion Arten. Eines davon ist die Assert Schreibweise. Dieses ähnelt der von nodeJS bereitgestellten Assert Schnittstelle und fügt weitere Testmöglichkeiten und Browserkompatibilität hinzu. [6](../Quellen.md) [9](../Quellen.md)
```javascript
var assert = require('chai').assert;
var foo = 'bar';
assert.typeOf(foo, 'string', 'foo is a string');
assert.equal(foo, 'bar', 'foo equal `bar`');
assert.lengthOf(foo, 3, 'foo`s value has a length of 3');
```
Anhand des Beispiels können Tests eingesehen werden, welche den Typen, die Gleichheit und die Länge von Objekten überprüfen kann. Optional kann als letzter Parameter eine Beschreibung mitgegeben werden, welche im Fehlerfall mit angegeben wird.
Die anderen beiden Assertion Arten befassen sich mit dem Behavior Driven Design (BDD). Hierbei werden verkette Konstrukte aufgestellt, um eine Annahme zu überprüfen. [9](../Quellen.md)

Eines dieser BDD Assertion Art ist Chai’s Expect.
```javascript
var expect = require('chai').expect;
var foo = 'bar';
expect(foo).to.be.a('string');
expect(foo, 'description: expect: [foo]').to.equal('bar');
expect(foo).to.have.lengthOf(3);
```
Dieses Beispiel zeigt das Testen mithilfe von Chai’s Expect. Es werden Verschachtelungen augebaut wie to.be.a (Typprüfung), to.equal (Vergleich mit anderem Objekt) und to.have.lengthOf (Größenprüfung). Der Anfang einer Verkettung beginnt immer mit der expect-Funktion. Das zu testende Objekt wird der expect-Funktion übergeben und kann optional noch eine Beschreibung als zweiten Parameter erhalten, welche im Fehlerfall zu mehr Verständnis verhelfen kann. [9](../Quellen.md)

Should besitzt eine starke Ähnlichkeit zu Expect und baut ebenfalls verkettete Konstrukte auf. Jede Assertion benötigt hierbei jedoch am Anfang der Verkettung ein should. Hierbei sollte immer auf Browser Kompatibilität geachtet werden, da einige Fehler verursacht werden können. [9](../Quellen.md)
```javascript
var should = require('chai').should();
var foo = 'bar';
foo.should.be.a('string');
foo.should.equal('bar');
foo.should.have.lengthOf(3);
```
Das Beispiel sieht dem Expect Beispiel sehr ähnlich, jedoch wird auf die Expect Funktion verzichtet und stattdessen auf das Should Objekt gesetzt.
