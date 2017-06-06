# 24 Principles
Um eine hohe Konsistenz zu gewährleisten ist es wichtig, _Prinzipien_ zu einzuführen um standardisierte Herangehensweisen bei der Entwicklung von Software zu verwenden. Prinzipien lassen sich in Bezug zur Entwicklung und Architektur einteilen.

## Entwicklungs-Prinzipien
Für die Entwicklung von Software gibt es unter anderem die nachfolgenden Prinzipien:

* Coding Standards und Konventionen
* Automatisiertes Unit-Testing
* Statische Analyse Tools
* etc.

## Architektur Prinzipien
Nachfolgend werden einige Prinzipien vorgestellt, welche sich auf die Struktur von Software beziehen.

* **Schichtenstrategie:** Eine Schichtenstrategie bzw. eine Schichtenarchitektur wird realisiert, in dem die zu Entwickelnde Software in, voneinander isolierte, Schichten eingeteilt wird. Diese können beispielsweise einen fachlichen Zweck erfüllen. Dadurch wird eine hohe Flexibilität gewährleistet, denn Änderungen bzw. Updates können nur Softwarekomponenten innerhalb einer Schicht beeinflussen.
* **Plazierung der Geschäftslogik:** Aus Performance und Wartungsgründen ist es oft sinnvoll, wenn die Geschäftslogik auf einem Server ausgeführt wird. Im Allgemeinen ist es von Vorteil, wenn so viel Rechenlast wie möglich auf einen Server ausgelagert wird anstatt Performance schwache Clients o. ä. zu beanspruchen.
* **Hohe Kohäsion, lose Kopplung, SOLID, etc.**
* **Zustandslose Komponenten:** Komponenten, welche keine festen Zustände einnehmen, können besser skaliert werden. Die Replikation einer Komponente mit dem Ziel der Rechenlastverteilung ist ein Beispiel der Skalierung.
* **Domain model - rich vs anaemic:** Manche Entwickler bevorzugen einen Programmierstil, mit dem Domain models als Funktionsreiche Objekte entwickelt werden. Beispielsweise eine OOP-Klasse mit fachlichen Daten und allen Funktionen, die mit diesen Daten einhergehen. Andere Entwickler wiederum bevorzugen es, reine Datenobjekte zu verwenden welche von Grobkörnigen Komponenten und Services verwendet werden.
* **Immer konsistent vs eventuell konsistent:** Viele Entwickler haben festgestellt, dass die Erfüllung von vielen nicht-funktionale Anforderungen die Konsistenz leidet. Beispielsweise erhöht sich in manchen Fällen die Performance, wenn man Dateninkonsistenz in Kauf nimmt.
