# Model Based Systems Engineering

Dieses Kapitel beschäftigt sich mit dem Model Based Systems Engineering (MBSE). Anhand von Definitionen und Erläuterungen wichtiger Fachbegriffen, die in Verbindung mit MBSE stehen, soll der Leser ein besseres Verständnis erlangen.

Das Model Based Systems Engineering setzt sich aus den Begriffen „Systems Engineering“ und „Model“ zusammen. Das Modell wird im Kontext von MBSE auch als Systemmodell bezeichnet. Dieses Systemmodell ist eine Abstraktion eines komplexen Systems. Die Abstraktion hilft die Komplexität eines Systems zu reduzieren, sodass Vorgänge und Funktionen einfacher dargestellt, verstanden und gestaltet werden können. [THM17](Quellen.md)

Das Systemmodell enthält alle relevanten Informationen eines Systems für die verschiedenen Stakeholder (z.B. Projektleiter, Entwicklungsleiter, Testingenieur) und ist die primäre Informationsquelle während der kompletten Entwicklung. Die unterschiedliche Darstellung dieser Informationen wird als Sicht (engl. View) bezeichnet und richtet sich nach den Interessen der Stakeholder. Weiterhin kann das Systemmodell wichtige Informationen für Entscheidungen liefern oder für frühe Analysen (z.B. FMEA, Risikoanalyse) genutzt werden. Ein entscheidender Vorteil, der sich durch die Verwendung eines Systemmodells ergibt, ist jedoch die Wiederverwendung von Elementen (z.B. Komponenten). Diese sind im Modell einmal hinterlegt und können in unterschiedlichen Systemarchitekturen visualisiert werden. Eine Änderung an diesem Element sorgt für eine Aktualisierung in allen Systemarchitekturen, die dieses Element verwenden.

Ein Systemmodell zeichnet sich durch folgende Eigenschaften aus:

* Das Modell darf sich aus mehreren Repositories zusammensetzen, solange diese in sich konsistent sind und sich nach außen wie ein einzelnes Modell repräsentieren.
* Das Modell erlaubt unterschiedliche Sichten auf die Informationen.
* Das Modell ist maschinell auswertbar und liegt in einer abstrakten Syntax vor, die explizit MBSE-Konzepte wie Anforderungen oder Systemarchitekturen unterstützt. [THM17](Quellen.md)

Die nachfolgenden Abbildung zeigt mögliche beteiligte Rollen in einem Systems Engineering Ansatz, die an einem gemeinsamen Systemmodell arbeiten. Die Rollenbezeichnungen und Prozesse können von Unternehmen zu Unternehmen variieren.    

Der Produktmanager oder Kunde auf der linken Seite der Abbildung übergibt dem Systemanalytiker die Anforderungen in einem Lastenheft oder über ein ReqIF-File. ReqIF steht für Requirements Interchange Format und ist ein standardisiertes XML-Dateiformat von der Object Management Group, mit welchem Anforderungen inkl. ihrer Metadaten zwischen verschiedenen Requirements Management Tools ausgetauscht werden können. Der Systemanalytiker hat die Aufgabe diese Anforderungen zu analysieren, abzustimmen und zu verfeinern. Zusätzlich muss er die Anforderungen von weiteren Stakeholder (z.B. Gesetzgebung) berücksichtigen. Die Analyse der Anforderungen erfolgt durch die Modellierung von Use Cases bis hin zu einem umfangreichen Domänenmodell. Die textuellen Anforderungen in dem Requirements Management Tool können dazu als grafische Elemente in ein Modellierungstool importiert werden. Für die Modellierung von Systemen eignet sich die Notation SysML der Object Management Group, welche Teile der UML-Notationselemente übernimmt und zusätzlich um domänenspezifische Sprachelement erweitert.

Auf Basis der verfeinerten Anforderungen kann der Testingenieur seine Testfälle erstellen und der Systemarchitekt das System genauer spezifizieren.  Sowohl die Beschreibung der Testfälle als auch die Spezifizierung des Systems erfolgt erneut in SysML. Die einzelnen Komponenten, die während der Spezifizierung vom Systemarchitekt identifiziert wurden, werden anschließend jeweils an die Experten-Teams für Software, Hardware und Mechanik / Konstruktion weitergegeben. 

Die Teams haben die Aufgabe diese Komponenten mit ihren Werkzeugen weiter zu detaillieren. Damit die Teams mit ihren Werkzeugen an einer Komponente weiterarbeiten können, kann es notwendig sein, dass das SysML-Modell durch Modelltransformation in ein anderes Modell übersetzt werden muss.

![](/assets/SystemsEngineering_BeteiligteRollen.PNG)
Abbildung 1: Vereinfachte Darstellung der beteiligten Rollen

Obwohl die vorgestellte Vorgehensweise stark an das Wasserfallmodell erinnert, handelt es sich in der Realität um einen stark iterativen Entwicklungsprozess mit vielen Feedbackzyklen. Sobald z.B. die Anforderungen in ausreichender Qualität vorliegen, können erste Entwürfe der Systemarchitektur entstehen und Lösungsideen mit Fachexperten abgestimmt werden. In den Experten-Teams kann ein agiles Vorgehen angestrebt werden.