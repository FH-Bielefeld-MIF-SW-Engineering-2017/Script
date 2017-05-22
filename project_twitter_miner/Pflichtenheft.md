# Pflichtenheft

## Vorwort

Das Projekt trägt den Namen "Twitter Miner" und befasst sich mit der Klassifikation von Tweets. Ergebnis der Klassifikation ist eine Sentiment Analyse, dass heißt es wird bestimmt, ob ein Tweet eine positive oder eine negative Meinung enthält. Das Ziel des Projektes ist, anhand der Sentiment Analyse das Stimmungsbild zu einem bestimmten Hashtag zu bestimmen und dem Anwender in geeigneter Form darzustellen. Die Klassifikation der Tweets soll mit drei verschiedenen Algorithmen durchgeführt werden, um ein  möglichst umfassendes Stimmungsbild zu präsentieren. Durchgeführt wird das Projekt im Rahmen des Modules "Spezielle Gebiete zum Software Engineering" des Informatik Masterstudiengang während des Sommersemesters 2017. Projektmitglieder sind Yannick Kloss, Sven Schirmer und Daniel Beneker. 

## Funktionsumfang

[Hier Anfordeurngen nach Rupp Schablone (Das System kann soll muss....)]
**Funktional:**
* Die Anwendung muss als Webanwendung, bestehend aus Client und Server relisiert werden
* Der Client muss eine, im Browser geöffnete, Webseite sein
* Der Client muss Suchanfragen in Form eines Hachtags (z.B. "#landtagswahl") in einer Textbox annehmen
* Der Client muss Suchanfragen mit der Betätigung eines Buttons an den Server schicken
* Der Client sollte die Antworten auf Suchanfragen in einer informativen Art und Weise anzeigen
* Die Client muss bei wiederholten Suchanfragen die Antworten von alten Suchanfragen von der Anzeige löschen
* Der Server muss die Webseite an anfragende Clients ausliefern
* Der Server muss gleichzeitige Client-Anfragen parallel bearbeiten
* Der Server muss eine Verbindung zur Twitter-API herstellen und die Suchanfragen von Clients an die Twitter-API schicken
* Der Server muss Algorithmen der folgenden Klassifizierungsverfahren realisieren: SVM, Bayes und Decision Trees
* Der Server muss die validen Antworten der Twitter-API von den Klassifizierungsverfahren hinsichtlich der Stimmungslage (Sentiment Analyse) klassifizieren
* Der Server sollte ungültige Anfragen von Clients mit einer Fehlermeldung beantworten
* Der Server sollte unerwartete Antworten der Twitter-API mit einer Fehlermeldung an anfragende CLients beantworten
* Der Server muss Suchanfragen mit den neusten 15 gefunden Tweets und den Ergebnissen der Klassifizierung beantworten


**Nicht-Funktional:**
* Der Server muss Client-Anfragen in Echtzeit beantworten
* Der Server sollte als Docker-Container realisiert werden


## Systemarchitektur

[Bild Systemarchitektur einbinden]

## Gui Mock Ups

Yannick

## Use Case Diagramm

alle Nachdecken + Feritgstellung am 22.5

## User Stories

* Als Administrator möchte ich einen Bayes Klassifikator mit Trainigsdaten trainieren lassen.
* Als Administrator möchte ich eine Support Vector Machine mit Trainigsdaten trainieren lassen.
* Als Administrator möchte ich einen Decision Tree mit Trainigsdaten trainieren lassen.
* Als Anwedner möchte ich in der Weboberfläche einen Hastag eingeben, um Tweets zu diesem Hashtag zu klassifizieren.


## Daten Modell

Schnittstellen ? -> 22.5

## Projektplan

Sven MS Projekt, Zusammen

## Verantwortlichkeiten

Die Komponenten der Systemarchitektur teilen sich wie folgt auf die Projektmitglieder auf.
* Twitter-Connector -> Sven Schirmer
* Client            -> Yannick Kloss
* Frontend Server   -> Daniel Beneker

Nachfolgend sind die Verantwortlichkeiten für die Algorithmen aufgelistet.
* Decision Tree     -> Yannick Kloss
* Bayes             -> Sven Schirmer
* SVM 			    -> Daniel Beneker
