# Objektrelationale Datenbanken (vgl. [1 Kap. 6.6],[14 Kap. 7],[72-86])  
Neben den Objektorientierten Datenbanken gibt es auch die sogenannten objektrelationalen Datenbanken. Auch diese haben zum Ziel das Problem des Impedance Mismatch anzugehen, allerdings streben sie eher eine Verminderung statt vollständiger Beseitigung des Problems an. objektrelationale Datenbanken versuchen die Vorteile von relationalen und objektorientierten Datenbanken zu vereinen. Dazu verwenden sie das relationale Grundgerüst und erweitern es um objektorientierte Features. Als Abfragesprache wird weiterhin das bekannte SQL genutzt. Die Forschung an objektrelationalen Datenbanken begann Anfang der 90er Jahren, erste kommerzielle Produkte gab es gegen Ende der 90er. Ihre Entwicklung wurde durch den SQL:1999 Standard und seine Structured Types vorangetrieben, welche es ermöglichen eigene komplexe Datentypen in Datenbanken zu definieren. 

## Funktionsweise
Objektrelationale Datenbanksysteme sind zum Großteil bestehende relationale Datenbanksysteme, die zusätzlich manche der folgenden objektorientierten Eigenschaften bieten:

* Komplexe Datentypen:  
Neben den einfachen Datentypen wie Int und String sind auch komplexe wie Geldbeträge, Geometrie Daten und Dokumenttypen wie JSON und XML verwendbar.
* Benutzerdefinierte Datentypen:  
Benutzer können eigene Datentypen spezifizieren und nutzen. Diese können aus einfachen, komplexen oder auch aus benutzerdefinierten Datentypen bestehen.
* Objekttabellen/Typisierte Tabellen:  
Es lassen sich Tabellen anhand eines Datentyps erstellen. Die Tabelle hält dann Objekte/Datensätze des spezifizierten Typs. Die Attribute eines Datentyps werden dabei zu den Spalten der Tabelle.
* Objektidentifikation:  
Objekte lassen sich durch einen Objektidentifikator identifizieren. 
* Objektreferenzen:  
Mithilfe der Objektidentifikatoren lassen sich Objekte einfach referenzieren. Beziehungen über Primär- und Fremdschlüssel werden dadurch überflüssig. 
* Methoden:  
Es lassen sich Objektmethoden erstellen.
* Vererbung:  
Es lassen sich Vererbungshierarchien zwischen Objekten herstellen.

## Vorteile
Der Vorteil objektrelationaler Datenbanken ist, dass das Impedance Mismatch verringert wird und dennoch das relationale Modell verwendet werden kann. Es ist daher sehr einfach, bestehende relationale Systeme in objektrelationale Datenbanken zu migrieren, um die Vorteile der Objektorientierung zu nutzen.

## Nachteile
Ein großer Nachteil der objektrelationalen Datenbanken ist der große Unterschied zwischen den einzelnen Anbietern. Nicht alle objektorientierten Features werden immer umgesetzt und auch generell gibt es große Unterschiede in der Umsetzung. Während Oracle beispielsweise fast alle objektorientierten Features umsetzt, bietet der Microsoft SQL Server nur benutzerdefinierte Datentypen an. Das Wechseln auf ein anderes objektrelationales Datenbankmanagementsystem ist daher in vielen Fällen nur schwer oder gar nicht möglich.

## Anbieter [88]
Die am häufigsten genutzten relationalen Datenbanken mit objektorientierten Features laut db-engines.com (Stand Juli 2017)

* Oracle: 1374,88 Punkte
* Microsoft SQL Server: 1226,00 Punkte 
* PostgreSQL: 369,44 Punkte