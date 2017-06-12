# Viewpoints and Visualisation

## Architecture Viewpoints

Im Kontext von Architekturen dienen Viewpoints (Standpunkt) der Betrachtung einzelner Aspekte einer Architektur, die im Interesse der Stakeholder sind. Die Viewpoints sollten dabei nicht nur uni-direktional, sondern auch bi-direktional bei der Kommunikation mit den Stakeholdern anwendbar sein. So können Viewpoints sowohl zu Präsentationszwecken wie auch als Disskusionsgrundlage im Gespräch zwischen Architekten und Stakeholdern dienen. Dabei gibt es entsprechende Viewpoints für die verschiedenen Stakeholder-Interessen:

* Obere Managementebene: Steht das neue System nicht der Unternehmensstrategie im Widerspruch und hat es einen Mehrwert; unter Berücksichtigung des (finanziellen) Aufwands?
* Mittlere Managementebene: Wie ist die aktuelle Lage unter Berücksichtigung des computergestützten Business-Prozesses?
* Endnutzer: Wie wirkt sich das neue System auf die Aktivitäten des voraussichtlichen Nutzers aus? 
* Architekt: Ist die Wartbarkeit des Systems gegeben?
* Produktmanager: Braucht es neue Technologien? Müssen Prozesse oder Applikationen angepasst werden? Wie sicher ist das System?
* Projektmanager: Wo besteht die Abhängigkeit zwischen den Business Prozessen und den zu entwickelnden Applikationen? Wie performant sind die Prozesse?
* Systementwickler: Wo sind Änderungsbedarfe?
* Systemadministrator: Wie verändern sich die Aufgaben durch die neuen Prozesse?

Nach dem ISO/IEC/IEEE 42010:2011-Standard ist ein Viewpoint eine Spezifikation der Konventionen bei der Erstellung und Benutzung von Views. Zu erwähnen sind die Frameworks Zachman framework, Krutchens 4+1 View Model und TOGAF, die allesamt verwendbare Viewpoints definieren.

## Models, Views und Visualizations

Nach dem Prinzip Seperation of Concerns werden bei der Präsentation einer Architektur (Viewpoint) die drei Komponenten Model, View und Visualization unterschieden. Das Modell beinhaltet alle Informationen der Architektur, die durch die View gefiltert und aufbereitet werden, um in der Visualization dargestellt zu werden. Die Visualization bestitzt dabei keinerlei Logik, sondern dient nur der Anzeige (vgl. Abbildung). 

![](/assets/EAAW - Separation of concerns model view visualisation and viewpoint.png)

## Visualisierung und Interaktion

Die Modifizierung einer Architektur geschieht typischerweise direkt im Modell, was dessen Konsistenz gewährleisten kann. Darüberhinaus gibt es jedoch auch Werkzeuge, die eine Änderung direkt vom View aus erlauben. Das Werkzeug projektiert die Änderung der View möglichst intelligent auf das darunterliegende Modell (vgl. Abbildung).

![](/assets/EAAW - Editing a landscape map.png)

## Erstellung, Auswahl und Verwendung von Viewpoints

Die gegebenen Frameworks bieten nur eine begrenzte Anzahl an verschiedenen Viewpoints, was nicht immer genügt, um Modelle den Stakeholdern passend zu visualisieren. Die Erstellung individueller Viewpoints ist möglich, jedoch aufwendig und somit kostspielig. Es muss also entschieden werden, ob gegebene Viewpoints genügen oder neue erstellt werden müssen. Dazu werden die Anforderungen klassifiziert (vgl. Abbildung). Bei der Klassifizierung betrachtet man Zielsetzung und Inhaltsebene.

|             | Stakeholder | Zielsetzung | Beispiele |
|-------------|-------------|-------------|-----------|
| Gestalten   | Architekten, Software-Entwickler, Geschäftsprozessgestalter | navigieren, gestalten, Gestaltungsentscheidungen unterstützen, Alternativen vergleichen | UML-Diagramme, BPMN-Diagramme, Flowcharts, ER-Diagramme |
| Entscheiden | Manager, CIO, CEO | Entscheidungsfindung | Querverweistabelle, Landscape Map, Liste, Bericht |
| Informieren | Mitarbeiter, Kunde | erklären, überzeugen, Feedback einholen | Animationen, Cartoons, Prozessillustrationen, Grafik |

|               | Stakeholder | Zielsetzung | Beispiele |
|---------------|-------------|-------------|-----------|
| Details       | Software-Entwickler, Prozessverantwortlicher | gestalten, verwalten | UML-Klassendiagramme, Testbed process diagram |
| Zusammenhänge | Produktmanager | Abhängigkeiten analysieren, Änderungsauswirkungen | Views, die Zusamenhänge verdeutlichen ('use', 'realise', 'assign') |
| Überblick     | Enterprise-Architekt, CIO, CEO | Changemanagement | Landscape map |

![](/assets/EAAW - Classification of enterprise architecture viewpoints.png)

Richtlinien bei der Verwendung von Viewpoints sind:

* Scoping: Ein oder zwei Viewpoints auswählen, die zu modellierenden (Sub-)Domänen wählen und Rahmenbedingungen festlegen
* Creation of views: Inhalte für den Viewpoint erstellen oder extrahieren
* Validation: Zusammen mit den Stakeholdern die Viewpoints prüfen (lassen)
* Obtaining commitment: Verbindliche Zusage der Stakeholder für einen Viewpoint einholen
* Informing: Weitere Stakeholder informieren, die nur sekundär betroffen sind

## Basic Design Viewpoints

Zur Übersicht seien im Folgenden die gängigen Viewpoint-Arten erwähnt und auf die Erklärungen und beispielhaften Diagramme im Buch verwiesen:

* Introductory Viewpoint
* Organisation Viewpoint
* Actor Cooperation Viewpoint
* Business Function Viewpoint
* Product Viewpoint
* Service Realisation Viewpoint
* Business Process Cooperation Viewpoint
* Business Process Viewpoint
* Information Structure Viewpoint
* Application Cooperation Viewpoint
* Application Usage Viewpoint
* Application Behaviour Viewpoint
* Application Structure Viewpoint
* Technology Viewpoint
* Technology Usage Viewpoint
* Implementation and Deployment Viewpoint
* Physical Viewpoint

Motivation Viewpoints:

* Stakeholder Viewpoint
* Goal Realisation Viewpoint
* Goal Contribution Viewpoint
* Principles Viewpoint
* Requirements Realisation Viewpoint
* Motivation Viewpoint

Strategy Viewpoints:

* Strategy Viewpoint
* Capabilty Map Viewpoint
* Ressource Map Viewpoint
* Outcome Realisation Viewpoint

Implementation and Migration Viewpoints:

* Project Viewpoint
* Migration Viewpoint
* Implementation and Migration Viewpoint