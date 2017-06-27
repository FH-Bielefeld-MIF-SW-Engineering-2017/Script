# Grundlagen

## Was ist Node.js?
Node.js ist eine Open-Source JavaScript Laufzeitumgebung auf Basis von Google Chrome’s V8 JavaScript Engine, die in C/C++ entwickelt wurde. Node.js wird hauptsächlich für die serverseitige Ausführung von JavaScript verwendet. Mit Node.js lassen sich sehr performante und skalierbare Anwendungen entwickeln. Vor dem Ausführen von JavaScript wird dieser von Node.js in nativen Maschinencode kompiliert. [3](../quellen.md) [4](../quellen.md)  
Node.js ist aber noch mehr, es enthält auch eine Reihe von Standardbibliotheken (Module) und Funktionen, die das Entwickeln von Serveranwendungen stark vereinfachen. Eines der bekanntesten Standardmodule ist das Express.js Modul, welches einem Entwickler die Möglichkeit gibt, mit sehr wenig Code einen kompletten Webserver zu erstellen. [4](../quellen.md)

## Module
Im Node.js Umfeld bezeichnen Module Softwarebibliotheken, die eine Anwendung um bereits vorgefertigte Funktionalitäten erweitern können.  
Module können einzelne .js-Dateien oder ein komplettes Verzeichnis mit mehreren .js-Dateien sein. Die Möglichkeit auch ein ganzes Verzeichnis als Modul anzubieten ermöglichte es, komplexeren Modulen in logische Moduleinheiten und in verschiedene Dateien zu untergliedern. [6](../quellen.md)

## Der Node Package Manager

### Was ist der Node Package Manager?
Ein wichtiges Tool bei der Entwicklung von Anwendungen mit Node.js ist der ”Node Package Manager (npm)“. Mit diesem Paketmanager lassen sich Module bequem von der Kommandozeile verwalten und installieren. Den Node Package Manager kann man sich ähnlich wie die Paketmanager unter den verschiedenen Linux Distributionen vorstellen. Im Wesentlichen lassen sich neue Module und deren Abhängigkeiten installieren, aktualisieren und löschen. [6](../quellen.md) [8](../quellen.md)  

### Module verwalten
Grundsätzlich lassen sich neue Module global oder lokal installieren, updaten und löschen. Lokal bedeutet in diesem Zusammenhang, dass das Modul nur in der aktuellen Anwendung zur Verfügung steht, während eine globale Installation von Modulen diese systemweit zur Verfügung stellt. Im Nachfolgenden wird ein Überblick über die wichtigsten Funktionen des Node Package Manager gegeben [2](../quellen.md):
```javascript
$ npm install <Modul>
$ npm install -g <Modul>
$ npm update
$ npm update −g
$ npm uninstall <Modul>
$ npm uninstall -g <Modul>
```  
Der Parameter ”-g“ veranlasst npm, die Operation auf den globalen Kontext anzuwenden. Ist kein Parameter angegeben, geht npm vom lokalen Kontext aus. Wichtig ist auch, dass bei der Verwendung eines dieser Kommandos im lokalen Kontext das aktuelle Arbeitsverzeichnis dem Root-Verzeichnis der betroffenen Anwendung entsprechen muss. [8](../quellen.md)  

Autor: Niklas Harting