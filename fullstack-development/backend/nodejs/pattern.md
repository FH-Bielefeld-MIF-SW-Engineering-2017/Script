# Patterns

## Standard Callback Pattern
Das Standard Callback Pattern beschreibt die Verwendung von Callback Funktionen als Funktionsparameter, um einen Asynchronen Programmfuss zu ermöglichen. Dies wird auch als Continuation-Passing Style bezeichnet. [2](../quellen.md)

## Event Emitter Pattern
Eher ungeeignet ist das Standard Callback Pattern, wenn bei einem Funktionsaufruf mehrere Events auftreten können. In einem solchen Fall bietet sich das Event Emitter Pattern an. Das Objekt, in dem Events auftreten können, implementiert hier eine Methode „on“ oder „addListener“, mit der Callback-Funktionen an bestimmte Events registriert werden können. Es sind auch mehrere Registrierungen zum gleichen Event möglich. Sollte nun ein Event auftreten, so werden die registrierten Funktionen zu dem zugehörigen Event aufgerufen. [2](../quellen.md)

## Promise Pattern
Eine weitere Alternative zum Callback Pattern ist das Verwenden von Promises. Ein Promise ist das Ergebniss einer Asynchronen Operation und kann einen von drei verschiedenen Zuständen haben. Diese sind pending (der initiale Zustand), fulfilled (die ausgeführte Operation war erfolgreich) oder rejected (die ausgeführte Operation schlug fehl). [7](../quellen.md)  
Beim Promise Pattern hat die Funktion keinen Callback Parameter, sondern es wird ein Promise Objekt zurückgeben.

Autor: Niklas Harting
