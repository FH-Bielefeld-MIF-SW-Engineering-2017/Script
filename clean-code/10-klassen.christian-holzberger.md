#  10 Klassen



Im 10. Kapitel wird beschrieben in welcher Art und Weise mit Klassen umgegeangen werden soll. 

Eine Klasse soll in folgender Reihenfolge die Definitionen ihrer Bestandteile enthalten:

1. Liste der Variablen
   1. public static Konstanten
   2. privat static Variablen
   3. private Variablen
   4. public Variablen - Es sollte so gut wie nie ein Grund vorliegen diese einzusetzen

Dazu werden 3 Prinzipien beschrieben

* Klassen sollen klein gehalten werden - Das "Single Responsibility Principle"
* Kohäsion - Sichbarkeit von Details
* Grupierung nach Änderungshäufigkeit - "Organizing for Change"

## Klassen sollen klein gehalten werden

Während man bei Funktionen die größe anhand der Zeilen von Code bestimmt ermittelt man die "Größe" einer Klasse anhand ihrer Zuständigkeiten. Eine Klasse sollte nach möglichkeit genau eine Zuständigkeit haben.

Werden innerhalb einer Klasse Methodennamen wie "Manger*", "Prozess", "Super benutzt" ist ein gutes Zeichen dafür, dass die Klasse zu viele Zuständigkeiten hat.

Die Zuständigkeit einer Funktion sollte mit 25 Wörtern beschrieben werden können. Sollte man in dieser Beschreibung die wöter "Wenn", "Und", "Oder" und "Aber" benutzen ist es ein gutes Zeichen dafür, dass die Klasse zu viele Zuständigkeiten hat.

### Single Responsibility Principle (SRP)

Weiterhin kann man überlegen welche Gründe für eine Änderung an der Klasse sprechen (Neue Version, Neue Währung, Anderer Server,…), wenn es mehr als einen Grund für eine Änderung gibt ist die Klasse vermutlich nicht klein genug. 

Das SRP legt fest, dass es für eine Klasse genau einen Grund geben darf sie zu verändern. Das führt dazu, dass eine Software die sonst aus eingen großen Klassen bestehen würde aus vielen kleinen Klassen besteht. Diese können dann wie ein Werkzeugkasten eingesetz werden.

## Kohäsion

Klassen sollten eine wenige Instanz-Variablen besitzen. Jede Methode der Klasse manipuliert eine oder mehrere dieser Variablen. Man spricht von geringer Kohäsion wenn eine Methode eine oder wenige Instanz-Variblen verändert. Verändert alle Methode alle Variablen einer Klasse spricht man von einer Klasse mit maximaler Kohäsion.

Maximale Kohäsion ist anzustereben da dies verdeutlicht, dass die Klasse eine logische Einheit bildet.

Um von einer Klasse mit geringer Kohäsion zu mehreren Klassen mit hoher Kohäsion zu kommen kann man sich dem Refactoring bedienen. 

## Organizing for Change

Durch sich ändernde Anforderungen wird auch Code im Laufe der Zeit geändert. Jede dieser Änderungen birgt die Gefahr neue Fehler ins System einzbauen. Die Funktion des Systems ist dann nicht mehr oder nur eingeschränkt gegeben. Durch die organisation von Code in Klassen kann das Risiko, neue Fehler einzbauen, veringert werden.

Durch den Einsatz von SRP und dem Ziel eine möglichst hohe Kohäsion zu erreichen werden Änderungen isoliert. Diese Änderungen können dann gezielt getestet werden. 

