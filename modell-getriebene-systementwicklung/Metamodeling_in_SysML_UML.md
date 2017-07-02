# Metamodeling in SysML / UML

Die Modellierungssprachen wie UML, SysML oder die BPMN, welche durch die Object Management Group (OMG) definiert wurden, basieren auf dem Konzept von sprachbasierten Metamodellen. Ein sprachbasiertes Meta-Modell stellt die Elemente einer Modellierungssprache und ihre Beziehungen in einem Modell dar. [WIKI17c](Quellen.md)

Den Meta-Modellen der OMG liegt die Meta Object Facility (MOF) zu Grunde. Die MOF beschreibt eine Metadaten-Architektur, dessen Kernbestandteil das Meta-Meta-Modell ist. Sie wurde mit dem Ziel definiert, eine gemeinsame Grundlage für verschiedene Meta-Modelle zu definieren. Dieser Ansatz bietet einige Vorteile, da verschiedene Meta-Modelle dadurch gleichartig persistiert und verarbeitet werden können. Die Modelltransformation ist eine Art der Verarbeitung von Modellen. [WIKI17d](Quellen.md)

Die nachfolgende Abbildung zeigt beispielhaft den Zusammenhang der verschiedenen Ebenen der (Meta-)Modelle anhand der UML. 

![](/assets/hierarchie_der_metamodelle.png)

**Profil-Mechanismus**

Um eine Modellierungssprache wie UML oder SysML um domänenspezifische Sprachelemente zu erweitern, stellt die OMG einen Profil-Mechanismus bereit. Ein Profil ist eine konkrete Erweiterung eines Metamodells. Ein leichtgewichtiger Mechanismus für die Erweiterung eines Metamodells sind Stereotypen. Ein Stereotyp spezialisiert eine Metaklasse für ein spezifisches Einsatzgebiet. 

Für jeden Stereotypen können Stereotypeigenschaften definiert werden, in denen domänenspezifische Informationen gespeichert werden können. Der Profil-Mechanismus wird im Folgenden anhand von Beispielen erläutert.

Die folgende Abbildung erweitert die Metaklasse *Actor* um den Stereotypen *externalSystem*. Diese Erweiterung kann genutzt werden, um bei einem Use-Case-Diagramm die Akteurestärker zu differenzieren.

![](/assets/UseCases.png)

In der nachfolgenden Abbildung wird die konkrete Anwendung eines *externalSystems* in einem Use-Case-Diagramm gezeigt. Das Diagramm zeigt Use-Cases für ein Smart Home System. In dem Use-Case „Jalousien mit Smartphone steuern“ ist der Akteur „Bewohner“ und das *externalSystem* „Jalousie“ beteiligt.

![](/assets/Shadowing_Use_Cases.png)

Ein Stereotyp kann von anderen Stereotypen mit Hilfe einer „Generalisierung“ spezialisiert werden. In der folgenden Abbildung ist der Stereotyp „Requirement“ von der Metaklasse *Class* erweitert worden. Der Stereotyp besitzt zusätzliche Eigenschaften wie z.B. *Id* und *Text*. Von „Requirement“ wurde ein spezialisierter Stereotyp „ExtendedRequirement“ erzeugt, der alle Eigenschaften von „Requirement“ besitzt und zusätzlich die Attribute *obligation* und *priority* enthält. Für die bessere Differenzierung von Anforderungen wurden von „ExtendedRequirement“ die drei Anforderungstypen „Business Requirement“, „System Requirement“ und „Design Requirement“ abgeleitet.

![](/assets/Requirements.png)

Die folgende Abbildung zeigt die Visualisierung des Stereotypen „Business Requirement“ in einem Requirement Diagramm der SysML.

![](/assets/SH_Requirements.png)

