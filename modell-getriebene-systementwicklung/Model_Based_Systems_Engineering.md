# Model Based Systems Engineering

Dieses Kapitel beschäftigt sichmit dem Model Based Systems Engineering (MBSE). Anhand von Definitionen undErläuterungen wichtiger Fachbegriffen, die in Verbindung mit MBSE stehen, sollder Leser ein besseres Verständnis erlangen.

Das Model Based Systems Engineeringsetzt sich aus den Begriffen „Systems Engineering“ und „Model“ zusammen. DasModell wird im Kontext von MBSE auch als Systemmodell bezeichnet. DiesesSystemmodell ist eine Abstraktion eines komplexen Systems. Die Abstraktionhilft die Komplexität eines Systems zu reduzieren, sodass Vorgänge undFunktionen einfacher dargestellt, verstanden und gestaltet werden können. [THM17]

Das Systemmodell enthält allerelevanten Informationen eines Systems für die verschiedenen Stakeholder (z.B.Projektleiter, Entwicklungsleiter, Testingenieur) und ist die primäreInformationsquelle während der kompletten Entwicklung. Die unterschiedlicheDarstellung dieser Informationen wird als Sicht (engl. View) bezeichnet undrichtet sich nach den Interessen der Stakeholder. Weiterhin kann dasSystemmodell wichtige Informationen für Entscheidungen liefern oder für früheAnalysen (z.B. FMEA, Risikoanalyse) genutzt werden. Ein entscheidender Vorteil,der sich durch die Verwendung eines Systemmodells ergibt, ist jedoch dieWiederverwendung von Elementen (z.B. Komponenten). Diese sind im Modell einmalhinterlegt und können in unterschiedlichen Systemarchitekturen visualisiertwerden. Eine Änderung an diesem Element sorgt für eine Aktualisierung in allenSystemarchitekturen, die dieses Element verwenden.

* Ein Systemmodell zeichnet sichdurch folgende Eigenschaften aus.
* Das Modell darf sich aus mehreren Repositorieszusammensetzen, solange diese in sich konsistent sind und sich nach außen wie ein einzelnes Modell repräsentieren.
* Das Modell erlaubt unterschiedliche Sichten aufdie Informationen.
* Das Modell ist maschinell auswertbar und liegtin einer abstrakten Syntax vor, die explizit MBSE-Konzepte wie Anforderungen oder Systemarchitekturen unterstützt. [THM17]

Die Abbildung 1 zeigt mögliche beteiligte Rollen in einem Systems Engineering Ansatz, die aneinem gemeinsamen Systemmodell arbeiten. Die Rollenbezeichnungen und Prozessekönnen von Unternehmen zu Unternehmen variieren.    

Der Produktmanager oder Kunde auf der linken Seite derAbbildung übergibt dem Systemanalytiker die Anforderungen in einem Lastenheftoder über ein ReqIF-File. ReqIF steht für Requirements Interchange Format undist ein standardisiertes XML-Dateiformat von der Object Management Group, mitwelchem Anforderungen inkl. ihrer Metadaten zwischen verschiedenen RequirementsManagement Tools ausgetauscht werden können. Der Systemanalytiker hat dieAufgabe diese Anforderungen zu analysieren, abzustimmen und zu verfeinern.Zusätzlich muss er die Anforderungen von weiteren Stakeholder (z.B.Gesetzgebung) berücksichtigen. Die Analyse der Anforderungen erfolgt durch dieModellierung von Use Cases bis hin zu einem umfangreichen Domänenmodell. Dietextuellen Anforderungen in dem Requirements Management Tool können dazu alsgrafische Elemente in ein Modellierungstool importiert werden. Für dieModellierung von Systemen eignet sich die Notation SysML der Object ManagementGroup, welche Teile der UML-Notationselemente übernimmt und zusätzlich umdomänenspezifische Sprachelement erweitert.

Auf Basis der verfeinerten Anforderungen kann derTestingenieur seine Testfälle erstellen und der Systemarchitekt das System genauerspezifizieren.  Sowohl die Beschreibungder Testfälle als auch die Spezifizierung des Systems erfolgt erneut in SysML.Die einzelnen Komponenten, die während der Spezifizierung vom Systemarchitektidentifiziert wurden, werden anschließend jeweils an die Experten-Teams für Software,Hardware und Mechanik / Konstruktion weitergegeben. 

Die Teams haben die Aufgabe diese Komponenten mit ihrenWerkzeugen weiter zu detaillieren. Damit die Teams mit ihren Werkzeugen aneiner Komponente weiterarbeiten können, kann es notwendig sein, dass dasSysML-Modell durch Modelltransformation in ein anderes Modell übersetzt werden muss.

![](..\assets\SystemsEngineering_BeteiligteRollen.png)



Obwohl die vorgestellte Vorgehensweise stark an das Wasserfallmodell erinnert, handelt es sich in der Realität um einen stark iterativen Entwicklungsprozess mit vielen Feedbackzyklen. Sobald z.B. die Anforderungen in ausreichender Qualität vorliegen, können erste Entwürfe der Systemarchitektur entstehen und Lösungsideen mit Fachexperten abgestimmt werden. In den Experten-Teams kann ein agiles Vorgehen angestrebt werden.