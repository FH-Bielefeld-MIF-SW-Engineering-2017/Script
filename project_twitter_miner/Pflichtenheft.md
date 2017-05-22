# Pflichtenheft

## Vorwort

Das Projekt trägt den Namen "Twitter Miner" und befasst sich mit der Klassifikation von Tweets. Ergebnis der Klassifikation ist eine Sentiment Analyse, dass heißt es wird bestimmt, ob ein Tweet eine positive oder eine negative Meinung enthält. Das Ziel des Projektes ist, anhand der Sentiment Analyse das Stimmungsbild zu einem bestimmten Hashtag zu bestimmen und dem Anwender in geeigneter Form darzustellen. Die Klassifikation der Tweets soll mit drei verschiedenen Algorithmen durchgeführt werden, um ein  möglichst umfassendes Stimmungsbild zu präsentieren. Durchgeführt wird das Projekt im Rahmen des Modules "Spezielle Gebiete zum Software Engineering" des Informatik Masterstudiengang während des Sommersemesters 2017. Projektmitglieder sind Yannick Kloss, Sven Schirmer und Daniel Beneker. 

## Funktionsumfang

[Hier Anfordeurngen nach Rupp Schablone (Das System kann soll muss....)]

## Systemarchitektur

Das Projekt "Twitter Miner" wird entsprechend der Client-Server-Architektur entworfen. Der Client ist eine Webanwendung die im Browser des Anwenders läuft. Der Client öffnet eine Websocketverbindung zum Server, der sich um alle Aufgaben wie die Beschaffung der Daten und die Klassifikation kümmert. Der Server ist mit Python implementiert und teilt sich auf in fünf Komponenten. Auf die Kommnunikation zwischen den Komponenten, sowie zwischen dem Client und dem Server wird im Detail im Kapitel [Daten Modell](#datenmodell) beschrieben. Der Client kommuniziert mit der Komponente "Frontend Server". Dieser nutzt wiederum die Komponente "Twitter Connector" um Tweets mit Hilfe der Twitter-API zu einem bestimmten Hashtag zu laden. Die geladenen Tweets werden anschließend an die drei Algorithmus-Komponentten weitergegeben. Jede Komponente implementiert dabei einen bestimmten Klasifikationsalgorithmus. Die Ergebnisse der Klassifikation werden am Ende von der Frontend-Server-Komponente gesammelt und in geeigneter Form an den Client zurückgeliefert. Die Verantwortlichkeiten für die einzelnen Komponenten sind in Kapitel [Verantwortlichkeiten](#verantwortlichkeiten) aufgelistet.

![](/project_twitter_miner/img/Systemarchitektur.png)

## Gui Mock Ups

Yannick

## Use Case Diagramm

alle Nachdecken + Feritgstellung am 22.5

## User Stories

* Als Administrator möchte ich einen Bayes Klassifikator mit Trainigsdaten trainieren lassen.
* Als Administrator möchte ich eine Support Vector Machine mit Trainigsdaten trainieren lassen.
* Als Administrator möchte ich einen Decision Tree mit Trainigsdaten trainieren lassen.
* Als Anwedner möchte ich in der Weboberfläche einen Hastag eingeben, um Tweets zu diesem Hashtag zu klassifizieren.


## <a name="datenmodell"></a>Daten Modell

Schnittstellen ? -> 22.5

## Projektplan

Sven MS Projekt, Zusammen

## <a name="verantwortlichkeiten"></a>Verantwortlichkeiten

Die Komponenten der Systemarchitektur teilen sich wie folgt auf die Projektmitglieder auf.

| Komponente   |      Name      |
|:----------|:-------------|
| Twiter-Connector |  Sven Schirmer |
| Client |    Yannick Kloss   |
| Frontend Server | Daniel Beneker |


Nachfolgend sind die Verantwortlichkeiten für die Algorithmen aufgelistet.

| Komponente   |      Name      |
|:----------|:-------------|
| Bayes |  Sven Schirmer |
| Decision Tree |    Yannick Kloss   |
| SVM | Daniel Beneker |

