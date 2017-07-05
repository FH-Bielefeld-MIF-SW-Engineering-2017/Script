# Dokumentenorientierte Datenbanken (vgl. [1 Kap. 7.4],[2 Kap. 4],[13 Kap. 3],[14 Kap. 5.8],[72,108-114])
Diese Art der NoSQL Datenbanken speichern ihre Daten in Dokumenten ab, beispielsweise in Form von JSON, XML aber auch in beliebig anderer Form. Dabei sind diese Dokumente Schemafrei, das heißt es existieren keine Regeln nach denen der Inhalt dieser Dokumente aufgebaut werden muss. Jedes einzelne Dokument ist also in der Lage, einen völlig anderen Inhalt zu speichern. Häufig werden diese Datenbanken im Bereich der Web-Applikationen verwendet und bei unstrukturierten Daten.

## Funktionsweise
In den meisten Fällen bestehen die Dokumente aus einer Sammlung von Key-Value Paaren. Die entsprechenden Values müssen dabei nicht atomar sein, sondern können auch aus Arrays, Listen oder ganzen weiteren Objekten bzw. Datensätzen bestehen. Das folgende Beispiel zeigt ein Dokument im JSON Format.

{  
"Vorname": "Dieter",  
"Nachname": "Skolmsund",  
"Gehalt": "40000",  
"Bisherige Positionen": ["Gärtner", "Entwickler", "Abteilungsleiter"],  
"Kinder":  
[    
{"Name": "Bjorn"},      
{"Name": "Freya"}  
]  
}  

In vielen Datenbanken wird zusätzlich eine ID für das Dokument gespeichert, diese kann manuell angegeben werden oder wird vom Datenbankmanagementsystem selbst angelegt. 

## Vorteile
Aufgrund der Schemafreiheit bieten dokumentorientierte Datenbanken eine große Freiheit bei der Gestaltung der Datenstrukturen. Änderungen können meist sehr einfach umgesetzt werden, gerade in der Entwicklungsphase sind sie daher äußerst praktisch. Des Weiteren können zusammenhängende Objekte bzw. Datensätze innerhalb eines einzelnen Dokuments gespeichert werden. Operationen die auf all diese Daten zugreifen müssen, sind daher schneller als bei relationalen Datenbanken, bei denen viele Join Befehle dafür nötig wären. 

## Nachteile
Zwischen den einzelnen dokumentorientierten Datenbankmanagementsystemen existieren viele Unterschiede, sodass ein Wechsel von einem Anbieter zu einem anderen nicht immer ganz einfach ist. Beispielsweise erlauben manche Anbieter das Speichern eines Dokuments in XML Format, andere wiederum nicht. Auch in den entsprechend genutzten Abfragesprachen gibt es häufig Unterschiede. Die Eigenschaft der Schemafreiheit kann unter Umständen auch als Nachteil angesehen werden. Anwendungsfälle, bei denen es auf eine Konsistente und strukturierte Speicherung der Daten ankommt, können mit dokumentorientierten Datenbanken nur deutlich schwerer gelöst werden als mit klassischen relationalen Datenbanken. Während bei relationalen Datenbanken ein Anwendungsprogramm keine Daten speichern kann, die nicht zum Schema passen, muss bei dokumentorientierten Datenbanken eine Überprüfung auf Programm Ebene erfolgen. Bei Fehlern in der Programmierung kann es also schnell dazu kommen, dass Daten in der Datenbank gespeichert werden, die an anderer Stelle nicht mehr korrekt interpretiert werden können.

## Anbieter [115]
Die am häufigsten genutzten dokumentenorientierten Datenbanken laut db-engines.com (Stand Juli 2017)

* MongoDB: 332,77 Punkte
* Amazon DynamoDB: 36,46 Punkte
* Couchbase: 33,02 Punkte