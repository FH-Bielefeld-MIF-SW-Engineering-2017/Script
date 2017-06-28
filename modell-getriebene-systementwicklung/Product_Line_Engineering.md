# Product Line Engineering

Unter dem Begriff Product Line Engineering (PLE) wird dieEntwicklung eines Portfolios von verwandten Produkten durch die Verwendunggemeinsamer Entwicklungsartefakten und effizienten Produktionshilfsmittelnverstanden. Anstatt verschiedene Produkte individuell zu entwickeln, steht beimProduct Line Engineering die Entwicklung eines gesamten Produktportfolios inden frühen Phasen des Entwicklungsprozesses im Vordergrund. Durch diesen Ansatzkönnen Synergien besser ausgeschöpft und die Wiederverwendung verbessertwerden.

Beim Product Line Engineering werden die Produkte aufbauendauf einer Plattform entwickelt, die die Gemeinsamkeiten („Core Assets“)mehrerer Produkte zusammenfasst. Zu diesen Core Assets gehören z.B. Architekturen,Softwarekomponenten, Domain Models, Use-Cases oder Test Cases. Da dieseCore-Assets bereitgestellt werden müssen, bevor ein konkretes Produktentwickelt werden kann, ist die Zeit bis zur Markteinführung des erstenProduktes (time-to-market) und das Entwicklungsrisiko deutlich höher als beider produktzentrischen Entwicklung. Jedoch können weitere Produkte später durchdie Wiederverwendung deutlich schneller entwickelt werden. Die Zeit bis zurMarkteinführung eines Produktes in Abhängigkeit der Anzahl der verschiedenenProdukte ist in Abbildung 9 dargestellt.

![](..\assets\effort_ple.png)

Im Product Line Engineering wird zwischen zwei Bereichenunterschieden:

Im **Domain Engineering **werden die „Core-Assets“ herausgearbeitet undauf dieser Basis eine gemeinsame Systemarchitektur entwickelt.

Im **Application Engineering **werden auf Grundlage der Ergebnisse desDomain Engineerings die Produkte der Produktlinie entwickelt.

In Abbildung 10ist die grundlegende Struktur des *ProductLine Engineerings* dargestellt. Die beiden Bereiche werden im Folgenden genauer erläutert.

![](..\assets\PLE_Struktur.png)

## Domain Engineering

Ziel des *Domain Engineering*ist es, bereits vorhandenes Wissen über eine Domäne zu erfassen und diesesWissen bei der Entwicklung neuer Produkte in dieser Domäne zu nutzen [CZAR00].

> „DomainEngineering is the activity of collecting, organizing, and storing pastexperience in building systems or parts of systems in a particular domain inthe form of reusable assets (i.e., reusable work products), as well asproviding an adequate means of reusing these assets (i.e., retrieval,qualifcation, dissemination, adaptation, assembly, and so on) when building newsystems.“ [CZAR00]
>

Der *Domain Engineering*Ansatz ist hierbei in die drei Schritte *DomainAnalysis*, *Domain Design* und *Domain Implementation* (siehe Abbildung 10)aufgeteilt.

In der **DomainAnalysis** wird zu Beginn die „domain of focus“ definiert und anschließend Informationen über diese Domänegesammelt. Aus diesen Informationen wird das Domain Model (siehe Absatz 5.3)erstellt. Als Informationsquelle dienen Domänen-Experten, Anforderungen vondedizierten Produkten der Produktlinie, sowie vorhandene (Mitbewerber-)Produkte.Das Domain Model dient Eingangsartefakt für den nachfolgenden Schritt „DomainDesign“. Die Ergebnisse gehen außerdem in die Anforderungsanalyse (RequirementsAnalysis) der Produkte der Produktlinie mit ein. Zusätzlich wird in derDomänen-Analyse über Feature-Modeling (siehe Absatz 5.5)die notwendigen Features der Produkte und deren Abhängigkeiten dargestellt. DieFeinheiten und Methoden des Feature-Modelings werden im späteren Verlauf desKapitels erläutert.

Im **Domain Design** wird aus dem in der Domain-Analysis erstellten Domain-Model eine generische Systemarchitekturerstellt, die sich in allen Produkten der Produktlinie vereinigen lässt. (Vgl.[5])

In der **Domain Implementation** wird die generische Architektur implementiert. Diese kann in den diversen Produkten der Produktlinie Wiederverwendung finden. (Vgl. [5])

## Application Engineering

Das *Application Engineering* beschreibt den Prozess der Entwicklung von Systemen, basierend auf den Ergebnissen des Domain Engineerings. Auch hierbei findet eine Auftrennung in drei Teilschritte statt (*RequirementsAnalysis*, *Design Analysis* und *Integration and Test*– siehe Abbildung 10).

## Domain Model

Das Domain Model enthält alle Aspekte einer Domäne die zurEntwicklung einer Produktlinie innerhalb dieser Domäne von Relevanz sind. Das Domain Model ist hierbei eine abstrakte Beschreibung von Problemstellungen, die durch das System zu lösen sind. Ein einfaches Beispiel hierfür stellt eine Software zur Vertragsverwaltung dar. Das Domain Model enthält hierbei alle Informationen die zur Verwaltung der Verträge relevant sind - zum Beispiel die Beziehungen zwischen Verträgen und Kunden.

## Vorgehensmodelle

Im Produktlinienansatz wird zwischen drei unterschiedlichenVorgehensmodellen unterschieden (Vgl. [APEL10]):

Im **proaktivenVorgehensmodell** wird eine Produktlinie komplett neu entwickelt. Hierbeiwird zu Beginn der komplette Domain-Engineering-Prozess durchlaufen. Dies istmit hohem initialen Aufwand und damit Kosten verbunden. Der proaktive Ansatz istsinnvoll, wenn die Anforderungen gut definiert und konstant sind. (Vgl.[APEL10])

Das **reaktiveVorgehensmodell **lässt sich mit agilen Vorgehensmodellen in derSoftware-Entwicklung vergleichen. Zu Beginn erfolgt einer Implementierung einerkleinen Basis. Nachfolgend werden in kleinen Schritten die Domänen-Analyse mitanschließender weiterer Implementierung durchgeführt. Hierdurch erhält man einzyklisches Arbeiten. Die Vorteile dieses Vorgehensmodell sind wie beim agilenAnsatz die geringen initialen Kosten, wie auch das ausliefern schneller ersterErgebnisse. Es können allerdings auch Probleme entstehen, die zu einer teurenUmstrukturierung der Arbeitsweise im späteren Verlauf des Projektes führen. Dasreaktive Vorgehensmodell ist vor allem geeignet, wenn die Anforderungen zuBeginn noch sehr unklar sind.

Beim **extraktiven Vorgehensmodell** dient einebereits entwickelte Produktlinie als Grundlage. Aus dieser werden Informationenextrahiert, die in die neue zu entwickelnde Produktlinie einfließen. Da eineexistente und funktionsfähige Produktlinie als Basis dient, halten sich dieRisiken und Kosten in Grenzen. Allerdings steigt auch der Anspruch im DomainEngineering, da Informationen aus einem System extrahiert werden, das nicht imProduktlinienansatz entwickelt wurde. 

Das extraktive Vorgehensmodell ist geeignet, wenn man einenschnellen Wechsel vom traditionellen zum Produktlinien-Ansatz realisieren möchte.

## Feature Modeling

Im Folgenden wird gezeigt wie mit Feature Modeling dieFeatures bzw. Varianten eines Produktes dargestellt werden können. Die hierbeiverwendete Sprache ist die Feature Modeling Notation, die nicht in der UML bzw.SysML enthalten ist.

Ein *Feature* wirdimmer aus Anwendersicht betrachtet: 

> „A prominentor distinctive user-visible aspect, quality, or characteristic of a softwaresystem or systems“ [FODA90]

Zu Beginn erfolgt eine kurze Einleitung in die verwendeteNotation, die abschließend in einem Beispiel angewendet wird.

Mit der **Konjunktion**(UND-Verknüpfung) wird beschrieben, dass alle verbundenen Elemente (Features)im Produkt umgesetzt werden müssen. In Abbildung 11 müssten also alle Elemente (A, B und C) vom Produkt implementiert werden:

A $\wedge$ B $\wedge$ C

![](..\assets\konjunktion.png)

Mit der **Disjunktion**(ODER-Verknüpfung) wird beschrieben, dass mindestens eines der verbundenenElemente umgesetzt werden muss. Es besteht keine Abhängigkeit zwischen denElementen. Es können also beliebige Kombinationen der Features umgesetztwerden. Die Disjunktion wird durch einen ausgefüllten Halbkreis am ausgehendenFeature-Strang markiert (siehe Abbildung 12).

Im Beispieldürften also beliebige Kombinationen aus den Features A, B und C umgesetztwerden. Jedoch mindestens eines von Ihnen:

A $\vee$ B $\vee$ C

![](..\assets\disjunktion.png)

Die **Kontravalenz** (Exklusiv-ODER-Verknüpfung) beschreibt, dass genau eines der verbundenen Elemente umgesetzt werden muss. Es darf kein weiteres Element umgesetzt werden. Die Kontravalenz wird durch einen Halbkreis am ausgehenden Feature-Strang markiert (siehe Abbildung 13). In Abbildung 13 müsste also entweder Feature A, B oder C umgesetzt werden:

A $\oplus$ B $\oplus$ C

![](..\assets\kontravalenz.png)

Mit **Implikationen **können Abhängigkeiten zwischen Features dargestellt werden. Wird ein Feature umgesetzt, kann dies bedeuten, dass auch ein anderes Feature umgesetzt werden muss. In Abbildung 14 können Feature A oder C oder beide umgesetzt werden. Wird C umgesetzt so mussauch B umgesetzt werden. Falls A umgesetzt wird darf B ebenfalls umgesetztwerden, muss es allerdings nicht. Es existiert keine Abhängigkeit zwischen A und B.

A $\vee$ (C $\wedge$ B)

![](..\assets\implikation.png)

**Obligationen** und **Optionen** werden eingesetzt um darzustellen, dass Features umgesetzt werden müssen (Obligation) bzw. umgesetzt werden können (Option). Die Obligation wird dabei durch einen ausgefüllten Kreis am entsprechenden Featuredargestellt, die Option durch einen nicht ausgefüllten. In Abbildung 15müssen sowohl Feature A als auch C umgesetzt werden. Feature B kann optional umgesetzt werden:

(A $\wedge$ B $\wedge$ C) $\vee$ (A $\wedge$ $\neg$B $\wedge$ C) = A $\wedge$ C

![](..\assets\obligation_option.png)

Im Folgenden wird eine exemplarisches Feature-Model eines Smartphones gezeigt. Dieses Model zeigt die Features, die ein Kunde bei der Auswahl seines Gerätes direkt konfigurieren kann.

![](..\assets\FM_smartphone.png)

Durch die zuvor erläuterten Notationselemente ist zuerkennen, dass der Kunde in jedem Fall eine Auswahl der Features *Farbe*, *Speicher* und *Display-Größe* treffen muss. Des Weiteren hat er die Möglichkeit eine *Hülle* zum Gerät hinzuzufügen. Hierbei hat er die Auswahl zwischenzwei *Materialien* (*Leder* und *Stoff*) und verschiedenen *Farben*(*Grün*, *Schwarz* und *Braun*).Entscheidet sich der Kunde für die Farbe *Grün*ist er gezwungen ebenfalls das Material *Stoff* zu nehmen, da diese Farbe für das Material *Leder* nicht zur Verfügung steht.

Aus diesem relativ übersichtlichen Feature-Model lassen sich bereits 108 unterschiedliche Varianten bilden (Berechnung siehe Anhang). Es istalso zu erkennen, dass auch eine geringe Variabilität von Features in einemProdukt zu einem schnellen Anstieg der Anzahl der Varianten führen kann.

![](..\assets\anzahl_varianten_nutzen.png)

Die Varianten und die Anzahl der Features sind in einem durchschnittlichen Software-System um ein vielfaches höher, als bei dem hierdargestellten Produkt. Umso wichtiger ist es die Variabilität so gering wiemöglich zu gestalten, um auch die Komplexität auf einem kontrollierbaren Level zu halten. Die Variantenbildung ist oft eine Gradwanderung zwischen Kundennutzen und Komplexität. Dieser Sachverhalt wird in Abbildung 17 gezeigt. 