# Product Line Engineering

Unter dem Begriff Product Line Engineering (PLE) wird die Entwicklung eines Portfolios von verwandten Produkten durch die Verwendung gemeinsamer Entwicklungsartefakten und effizienten Produktionshilfsmitteln verstanden. Anstatt verschiedene Produkte individuell zu entwickeln, steht beim Product Line Engineering die Entwicklung eines gesamten Produktportfolios in den frühen Phasen des Entwicklungsprozesses im Vordergrund. Durch diesen Ansatz können Synergien besser ausgeschöpft und die Wiederverwendung verbessert werden.

Beim Product Line Engineering werden die Produkte aufbauend auf einer Plattform entwickelt, die die Gemeinsamkeiten („Core Assets“) mehrerer Produkte zusammenfasst. Zu diesen Core Assets gehören z.B. Architekturen, Softwarekomponenten, Domain Models, Use-Cases oder Test Cases. Da diese Core-Assets bereitgestellt werden müssen, bevor ein konkretes Produkt entwickelt werden kann, ist die Zeit bis zur Markteinführung des ersten Produktes (time-to-market) und das Entwicklungsrisiko deutlich höher als bei der produktzentrischen Entwicklung. Jedoch können weitere Produkte später durch die Wiederverwendung deutlich schneller entwickelt werden. Die Zeit bis zur Markteinführung eines Produktes in Abhängigkeit der Anzahl der verschiedenen Produkte ist in Abbildung 9 dargestellt.

![](..\assets\effort_ple.png)

Im Product Line Engineering wird zwischen zwei Bereichenunterschieden:

Im **Domain Engineering **werden die „Core-Assets“ herausgearbeitet und auf dieser Basis eine gemeinsame Systemarchitektur entwickelt.

Im **Application Engineering **werden auf Grundlage der Ergebnisse des Domain Engineerings die Produkte der Produktlinie entwickelt.

In Abbildung 10 ist die grundlegende Struktur des *ProductLine Engineerings* dargestellt. Die beiden Bereiche werden im Folgenden genauer erläutert.

![](..\assets\PLE_Struktur.png)

## Domain Engineering

Ziel des *Domain Engineering* ist es, bereits vorhandenes Wissen über eine Domäne zu erfassen und dieses Wissen bei der Entwicklung neuer Produkte in dieser Domäne zu nutzen [CZAR00].

> „Domain Engineering is the activity of collecting, organizing, and storing past experience in building systems or parts of systems in a particular domain inthe form of reusable assets (i.e., reusable work products), as well as providing an adequate means of reusing these assets (i.e., retrieval,qualifcation, dissemination, adaptation, assembly, and so on) when building newsystems.“ [CZAR00]
>

Der *Domain Engineering*Ansatz ist hierbei in die drei Schritte *DomainAnalysis*, *Domain Design* und *Domain Implementation* (siehe Abbildung 10) aufgeteilt.

In der **Domain Analysis** wird zu Beginn die „domain of focus“ definiert und anschließend Informationen über diese Domäne gesammelt. Aus diesen Informationen wird das Domain Model (siehe Absatz 5.3) erstellt. Als Informationsquelle dienen Domänen-Experten, Anforderungen von dedizierten Produkten der Produktlinie, sowie vorhandene (Mitbewerber-)Produkte. Das Domain Model dient Eingangsartefakt für den nachfolgenden Schritt „Domain Design“. Die Ergebnisse gehen außerdem in die Anforderungsanalyse (Requirements Analysis) der Produkte der Produktlinie mit ein. Zusätzlich wird in der Domänen-Analyse über Feature-Modeling (siehe Absatz 5.5) die notwendigen Features der Produkte und deren Abhängigkeiten dargestellt. Die Feinheiten und Methoden des Feature-Modelings werden im späteren Verlauf des Kapitels erläutert.

Im **Domain Design** wird aus dem in der Domain-Analysis erstellten Domain-Model eine generische Systemarchitektur erstellt, die sich in allen Produkten der Produktlinie vereinigen lässt. (Vgl.[5])

In der **Domain Implementation** wird die generische Architektur implementiert. Diese kann in den diversen Produkten der Produktlinie Wiederverwendung finden. (Vgl. [5])

## Application Engineering

Das *Application Engineering* beschreibt den Prozess der Entwicklung von Systemen, basierend auf den Ergebnissen des Domain Engineerings. Auch hierbei findet eine Auftrennung in drei Teilschritte statt (*Requirements Analysis*, *Design Analysis* und *Integration and Test*– siehe Abbildung 10).

## Domain Model

Das Domain Model enthält alle Aspekte einer Domäne die zur Entwicklung einer Produktlinie innerhalb dieser Domäne von Relevanz sind. Das Domain Model ist hierbei eine abstrakte Beschreibung von Problemstellungen, die durch das System zu lösen sind. Ein einfaches Beispiel hierfür stellt eine Software zur Vertragsverwaltung dar. Das Domain Model enthält hierbei alle Informationen die zur Verwaltung der Verträge relevant sind - zum Beispiel die Beziehungen zwischen Verträgen und Kunden.

## Vorgehensmodelle

Im Produktlinienansatz wird zwischen drei unterschiedlichen Vorgehensmodellen unterschieden (Vgl. [APEL10]):

Im **proaktivenVorgehensmodell** wird eine Produktlinie komplett neu entwickelt. Hierbei wird zu Beginn der komplette Domain-Engineering-Prozess durchlaufen. Dies ist mit hohem initialen Aufwand und damit Kosten verbunden. Der proaktive Ansatz ist sinnvoll, wenn die Anforderungen gut definiert und konstant sind. (Vgl.[APEL10])

Das **reaktive Vorgehensmodell **lässt sich mit agilen Vorgehensmodellen in der Software-Entwicklung vergleichen. Zu Beginn erfolgt einer Implementierung einer kleinen Basis. Nachfolgend werden in kleinen Schritten die Domänen-Analyse mit anschließender weiterer Implementierung durchgeführt. Hierdurch erhält man ein zyklisches Arbeiten. Die Vorteile dieses Vorgehensmodell sind wie beim agilen Ansatz die geringen initialen Kosten, wie auch das Ausliefern schneller erster Ergebnisse. Es können allerdings auch Probleme entstehen, die zu einer teuren Umstrukturierung der Arbeitsweise im späteren Verlauf des Projektes führen. Das reaktive Vorgehensmodell ist vor allem geeignet, wenn die Anforderungen zu Beginn noch sehr unklar sind.

Beim **extraktiven Vorgehensmodell** dient eine bereits entwickelte Produktlinie als Grundlage. Aus dieser werden Informationen extrahiert, die in die neue zu entwickelnde Produktlinie einfließen. Da eine existente und funktionsfähige Produktlinie als Basis dient, halten sich die Risiken und Kosten in Grenzen. Allerdings steigt auch der Anspruch im Domain Engineering, da Informationen aus einem System extrahiert werden, das nicht im Produktlinienansatz entwickelt wurde. 

Das extraktive Vorgehensmodell ist geeignet, wenn man einen schnellen Wechsel vom traditionellen zum Produktlinien-Ansatz realisieren möchte.

## Feature Modeling

Im Folgenden wird gezeigt wie mit Feature Modeling die Features bzw. Varianten eines Produktes dargestellt werden können. Die hierbei verwendete Sprache ist die Feature Modeling Notation, die nicht in der UML bzw.SysML enthalten ist.

Ein *Feature* wird immer aus Anwendersicht betrachtet: 

> „A prominentor distinctive user-visible aspect, quality, or characteristic of a software system or systems“ [FODA90]

Zu Beginn erfolgt eine kurze Einleitung in die verwendete Notation, die abschließend in einem Beispiel angewendet wird.

Mit der **Konjunktion** (UND-Verknüpfung) wird beschrieben, dass alle verbundenen Elemente (Features) im Produkt umgesetzt werden müssen. In Abbildung 11 müssten also alle Elemente (A, B und C) vom Produkt implementiert werden:

A $\wedge$ B $\wedge$ C

![](..\assets\konjunktion.png)

Mit der **Disjunktion **(ODER-Verknüpfung) wird beschrieben, dass mindestens eines der verbundenen Elemente umgesetzt werden muss. Es besteht keine Abhängigkeit zwischen den Elementen. Es können also beliebige Kombinationen der Features umgesetzt werden. Die Disjunktion wird durch einen ausgefüllten Halbkreis am ausgehenden Feature-Strang markiert (siehe Abbildung 12).

Im Beispieldürften also beliebige Kombinationen aus den Features A, B und C umgesetzt werden. Jedoch mindestens eines von Ihnen:

A $\vee$ B $\vee$ C

![](..\assets\disjunktion.png)

Die **Kontravalenz** (Exklusiv-ODER-Verknüpfung) beschreibt, dass genau eines der verbundenen Elemente umgesetzt werden muss. Es darf kein weiteres Element umgesetzt werden. Die Kontravalenz wird durch einen Halbkreis am ausgehenden Feature-Strang markiert (siehe Abbildung 13). In Abbildung 13 müsste also entweder Feature A, B oder C umgesetzt werden:

A $\oplus$ B $\oplus$ C

![](..\assets\kontravalenz.png)

Mit **Implikationen **können Abhängigkeiten zwischen Features dargestellt werden. Wird ein Feature umgesetzt, kann dies bedeuten, dass auch ein anderes Feature umgesetzt werden muss. In Abbildung 14 können Feature A oder C oder beide umgesetzt werden. Wird C umgesetzt so muss auch B umgesetzt werden. Falls A umgesetzt wird darf B ebenfalls umgesetzt werden, muss es allerdings nicht. Es existiert keine Abhängigkeit zwischen A und B.

A $\vee$ (C $\wedge$ B)

![](..\assets\implikation.png)

**Obligationen** und **Optionen** werden eingesetzt um darzustellen, dass Features umgesetzt werden müssen (Obligation) bzw. umgesetzt werden können (Option). Die Obligation wird dabei durch einen ausgefüllten Kreis am entsprechenden Featuredargestellt, die Option durch einen nicht ausgefüllten. In Abbildung 15müssen sowohl Feature A als auch C umgesetzt werden. Feature B kann optional umgesetzt werden:

(A $\wedge$ B $\wedge$ C) $\vee$ (A $\wedge$ $\neg$B $\wedge$ C) = A $\wedge$ C

![](..\assets\obligation_option.png)

Im Folgenden wird eine exemplarisches Feature-Model eines Smartphones gezeigt. Dieses Model zeigt die Features, die ein Kunde bei der Auswahl seines Gerätes direkt konfigurieren kann.

![](..\assets\FM_smartphone.png)

Durch die zuvor erläuterten Notationselemente ist zu erkennen, dass der Kunde in jedem Fall eine Auswahl der Features *Farbe*, *Speicher* und *Display-Größe* treffen muss. Des Weiteren hat er die Möglichkeit eine *Hülle* zum Gerät hinzuzufügen. Hierbei hat er die Auswahl zwischen zwei *Materialien* (*Leder* und *Stoff*) und verschiedenen *Farben* (*Grün*, *Schwarz* und *Braun*). Entscheidet sich der Kunde für die Farbe *Grün* ist er gezwungen ebenfalls das Material *Stoff* zu nehmen, da diese Farbe für das Material *Leder* nicht zur Verfügung steht.

Aus diesem relativ übersichtlichen Feature-Model lassen sich bereits 108 unterschiedliche Varianten bilden (Berechnung siehe Anhang). Es ist also zu erkennen, dass auch eine geringe Variabilität von Features in einem Produkt zu einem schnellen Anstieg der Anzahl der Varianten führen kann.

![](..\assets\anzahl_varianten_nutzen.png)

Die Varianten und die Anzahl der Features sind in einem durchschnittlichen Software-System um ein vielfaches höher, als bei dem hier dargestellten Produkt. Umso wichtiger ist es die Variabilität so gering wie möglich zu gestalten, um auch die Komplexität auf einem kontrollierbaren Level zu halten. Die Variantenbildung ist oft eine Gratwanderung zwischen Kundennutzen und Komplexität. Dieser Sachverhalt wird in Abbildung 17 gezeigt. 