# Objektorientierte Datenbanken (vgl. [2 Kap. 8.5],[14 Kap. 2.11,7],[72-86])
Heutzutage werden sehr viele Programme mit dem Konzept der Objektorientierung programmiert, bekannte Sprachen sind dabei beispielsweise Java und C#. Daten werden dabei als Objekte betrachtet, mit denen gearbeitet werden kann. Relationale Datenbanken haben jedoch keine Möglichkeit diese Objekte einfach so zu speichern, da diese immer mit Tabellen arbeiten. Dieses Problem wird als Impedance Mismatch bezeichnet.

## Impedance Mismatch (vgl. [70-71])
Impedance Mismatch (zu Deutsch: Objektrelationale Unverträglichkeit) beschreibt die Unverträglichkeit zwischen dem objektorientiertem und dem relationalen Modell. Die Probleme sind dabei einerseits Unterschiede zwischen den Datentypen einer Datenbank und einer Programmiersprache. Der Datentyp String kann beispielsweise in einer Datenbank anders aufgebaut sein als in einer Programmiersprache und eventuell Beschränkungen in der Länge haben. Andererseits sind es vor allem die Unterschiede in den Datenstrukturen an sich. Objekte sind anders aufgebaut als Tabellen. Häufig müssen Daten von Objekten in verschiedene Tabellen aufgeteilt werden. Des Weiteren ist es nicht möglich objektorientierte Eigenschaften wie Vererbung, Objektidentität und das Objektverhalten in einer Relation zu speichern

## Funktionsweise
Objektorientierte Datenbanken sind dabei eine Antwort auf das Problem des Impedance Mismatch. Diese Datenbanken speichern die Daten als Objekte gemäß der Objektorientierung. Objekte können somit direkt gespeichert werden, ohne dass ihre Daten erst aufgeteilt werden müssen. Dazu gehört auch die Objektidentifikation, es müssen für Objekte also keine zusätzlichen Primärschlüssel generiert werden, wie es bei relationalen Datenbanken der Fall ist. Dadurch, dass Objekte auch komplexe Datentypen halten können, sprich andere Objekte, lassen sich somit auch direkte Objektreferenzen speichern. Beziehungen über Primär- und Fremdschlüssel sind daher nicht notwendig. Auch lassen sich Vererbungshierarchien speichern und abbilden. Zusätzlich kann das Objektverhalten definiert und gespeichert werden, eine Eigenschaft, für die es im klassischen relationalen Modell kein Gegenstück gibt.  
In vielen Objektorientierten Datenbanken wird als Abfragesprache OQL (Object Query Language) verwendet, eine Abfragesprache angelehnt an SQL. Häufig werden Anbindungen für die wichtigsten Objektorientierten Programmiersprachen angeboten.

## Vorteile
Durch die komplette Speicherung der Daten als Objekte gemäß der Objektorientierung ist es deutlich einfacher Anwendungen zu programmieren, da keine Möglichkeit mehr gefunden werden muss, wie sich die Objekte am besten in Relationen abbilden lassen. Beim Arbeiten mit wenigen, aber sehr komplexen Objekten mit Verknüpfungen, sind Objektdatenbanken oft schneller als relationale, da keine großen Join Abfragen benötigt werden.

## Nachteile
Der größte Nachteil objektorientierter Datenbanken ist ihre Verbreitung, bzw. das Fehlen davon. Obwohl die Entwicklung dieser Datenbanken bereits seit den 80er Jahren stattfindet, werden sie nicht sehr häufig genutzt und es gibt nur wenige Anbieter. Bedingt dadurch sind sie auch meist nicht so ausgereift, wie die älteren relationalen Datenbanken. Ihre Performance beim Arbeiten mit großen aber einfachen Datenmengen liegt deutlich unter der von relationalen Datenbanken. 

## Anbieter [87]
Die am häufigsten genutzten Objektorientierten Datenbanken laut db-engines.com (Stand Juli 2017)

* Caché: 2,72 Punkte
* Db40: 1,42 Punkte
* ObjectStore: 1,10 Punkte