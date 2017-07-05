# Key-Value Datenbanken (vgl. [1 Kap. 7.2],[2 Kap. 5],[12 Kap. 6],[13 Kap. 3],[72,116-123])
Key-Value Datenbanken existieren schon seit den 70er Jahren und gehören somit zu den ältesten NoSQL Datenbanken. Durch das Internet und der damit einhergehenden Notwendigkeit mit extrem große Datenmengen arbeiten zu können, haben diese Datenbanken einen neuen Aufschwung erlebt. Sie speichern ihre Daten in Form von Schlüssel-Wert Paaren, eine sehr einfache, aber dadurch auch sehr effiziente Form der Datenverwaltung. 

## Funktionsweise
Je nach Anbieter unterscheiden sich die Freiheiten beim Setzen der Schlüssel und Werte. Im Allgemeinen sind sie jedoch Schemafrei, die Schlüssel und die Werte können daher vollkommen beliebig aufgebaut sein. Häufig können Werte daher nicht nur einfache Strings halten, sondern auch Listen und Sets, also mehrere Werte. Auch Hashs können gespeichert werden, welche aus weiteren Key-Value Paaren aufgebaut sind.  

## Vorteile
Der größten Vorteile von Key-Value Datenbanken sind ihre Skalierbarkeit und ihre Geschwindigkeit. Die Daten lassen sich sehr leicht verteilen und der Zugriff auf Werte über ihre Schlüssel erfolgt sehr schnell. Durch die Schemafreiheit können beliebige Strukturen aufgebaut werden, daher sind sie flexibel und lassen sich leicht anpassen. Oft werden diese Datenbanken auch als In-Memory Datenbanken verwendet, wodurch sie noch schneller werden.

## Nachteile
Da der Zugriff auf Werte nur über deren Schlüssel erfolgen kann, sind die Abfragemöglichkeiten bei diesen Datenbanken deutlich eingeschränkt. Komplexe Abfragen müssen somit von den Entwicklern in ihrem Programmcode selbst erstellt werden. Des Weiteren lassen sich Objektbeziehungen nur sehr schwer darstellen. Integritätsbedingungen dieser Beziehungen müssen immer im Programmcode definiert werden. Key-Value Datenbanken sind daher nicht dafür geeignet, Datensätze, mit vielen komplexen Beziehungen untereinander, zu speichern. 

## Anbieter [123]
Die am häufigsten genutzten Key-Value Datenbanken laut db-engines.com (Stand Juli 2017)

* Redis: 121,51 Punkte
* Memcached: 28,53 Punkte
* Hazelcast: 8,91 Punkte