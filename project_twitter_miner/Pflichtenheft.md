# Pflichtenheft

## Vorwort

Das Projekt trägt den Namen "Twitter Miner" und befasst sich mit der Klassifikation von Tweets. Ergebnis der Klassifikation ist eine Sentiment Analyse, dass heißt es wird bestimmt, ob ein Tweet eine positive oder eine negative Meinung enthält. Das Ziel des Projektes ist, anhand der Sentiment Analyse das Stimmungsbild zu einem bestimmten Hashtag zu bestimmen und dem Anwender in geeigneter Form darzustellen. Die Klassifikation der Tweets soll mit drei verschiedenen Algorithmen durchgeführt werden, um ein  möglichst umfassendes Stimmungsbild zu präsentieren. Durchgeführt wird das Projekt im Rahmen des Modules "Spezielle Gebiete zum Software Engineering" des Informatik Masterstudiengang während des Sommersemesters 2017. Projektmitglieder sind Yannick Kloss, Sven Schirmer und Daniel Beneker. 

## User Stories

* Als Administrator möchte ich einen Bayes Klassifikator mit Trainigsdaten trainieren lassen.
* Als Administrator möchte ich eine Support Vector Machine mit Trainigsdaten trainieren lassen.
* Als Administrator möchte ich einen Decision Tree mit Trainigsdaten trainieren lassen.
* Als Anwedner möchte ich in der Weboberfläche einen Hastag eingeben, um Tweets zu diesem Hashtag zu klassifizieren.

## Use Case Diagramm

Das nachfolgende Use-Case Diagramm verdeutlicht die Anwendungsfälle der Aktoren _Anwender_ und _Administrator_.

![](/project_twitter_miner/img/Use_Case_Diagramm.png)

## Funktionsumfang

Nachfolgend wurden die von dem Use-Case Diagramm und den User-Stories abgeleiteten funktionalen und nicht-funktionalen Anforderungen aufgelistet.

**Funktional:**
* Die Anwendung muss als Webanwendung, bestehend aus Client und Server relisiert werden.
* Der Client muss eine, im Browser geöffnete, Webseite sein.
* Der Client muss Suchanfragen in Form eines Hachtags (z.B. "#landtagswahl") in einer Textbox annehmen.
* Der Client muss Suchanfragen mit der Betätigung eines Buttons an den Server schicken.
* Der Client sollte die Antworten auf Suchanfragen in einer informativen Art und Weise anzeigen.
* Die Client muss bei wiederholten Suchanfragen die Antworten von alten Suchanfragen von der Anzeige löschen.
* Der Server muss die Webseite an anfragende Clients ausliefern.
* Der Server muss gleichzeitige Client-Anfragen parallel bearbeiten.
* Der Server muss eine Verbindung zur Twitter-API herstellen und die Suchanfragen von Clients an die Twitter-API schicken.
* Der Server muss Algorithmen der folgenden Klassifizierungsverfahren realisieren: SVM, Bayes und Decision Trees.
* Der Server muss die validen Antworten der Twitter-API von den Klassifizierungsverfahren hinsichtlich der Stimmungslage (Sentiment Analyse) klassifizieren.
* Der Server sollte ungültige Anfragen von Clients mit einer Fehlermeldung beantworten.
* Der Server sollte unerwartete Antworten der Twitter-API mit einer Fehlermeldung an anfragende CLients beantworten.
* Der Server muss Suchanfragen mit den neusten 15 gefunden Tweets und den Ergebnissen der Klassifizierung beantworten.


**Nicht-Funktional:**
* Der Server muss Client-Anfragen in Echtzeit beantworten.
* Der Server sollte als Docker-Container realisiert werden.

## Systemarchitektur

Das Projekt "Twitter Miner" wird entsprechend der Client-Server-Architektur entworfen. Der Client ist eine Webanwendung die im Browser des Anwenders läuft. Der Client öffnet eine Websocketverbindung zum Server, der sich um alle Aufgaben wie die Beschaffung der Daten und die Klassifikation kümmert. Der Server ist mit Python implementiert und teilt sich auf in fünf Komponenten. Auf die Kommnunikation zwischen den Komponenten, sowie zwischen dem Client und dem Server wird im Detail im Kapitel [Daten Modell](#datenmodell) beschrieben. Der Client kommuniziert mit der Komponente "Frontend Server". Dieser nutzt wiederum die Komponente "Twitter Connector" um Tweets mit Hilfe der Twitter-API zu einem bestimmten Hashtag zu laden. Die geladenen Tweets werden anschließend an die drei Algorithmus-Komponentten weitergegeben. Jede Komponente implementiert dabei einen bestimmten Klassifikationsalgorithmus. Die Ergebnisse der Klassifikation werden am Ende von der Frontend-Server-Komponente gesammelt und in geeigneter Form an den Client zurückgeliefert. Die Verantwortlichkeiten für die einzelnen Komponenten sind in Kapitel [Verantwortlichkeiten](#verantwortlichkeiten) aufgelistet.

![](/project_twitter_miner/img/Systemarchitektur.png)

## Gui Mock Ups

Ein Suchstring (suche nach Hashtag) wird über die Texbox eingegeben und mit der Betätigung des Buttons an den Server gesendet.
Die Antwort wird in Form einer Auflistung der Tweets in verkürzter Weise angezeigt. Mit einem Klick auf ein einzelnes Listenelement werden die Details auf der rechten Seite angezeitgt. Zu diesen gehören die Ergebnisse der Klassifizierungs-Algorithmen. Das erste, farblich hervorgehobene, Listenelement stellt eine Zusammenfassung der Suchergebnisse dar. Mit einem Klick auf dieses Element wird eine zusammenfassende Übersicht, einschließlich Kuchendiagramm über die Anzahl der Positiven und Negativen Tweets, gegeben.

![](/project_twitter_miner/img/Mockup.png)


## <a name="datenmodell"></a>Daten Modell

Um die Echtzeit-Anforderung zu erfüllen, soll mithilfe der Javascript Bibliothek _Socket.io_ eine Websocketverbindung zwischen Client und Server aufgebaut werden. Der Payload der Nachrichten wird nachfolgend aufgelistet.

Anfrage Client -> Server
```json
{  
   "hashtag":"string"
}
```

Server->Client
```json
{  
   "tweets":[  
      {  
         "text":"string",
         "bayes":true,
         "svm":true,
         "decisiontree":false
      }
   ]
}
```

## Projektplan
![](/project_twitter_miner/img/Projektplan.png)

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

