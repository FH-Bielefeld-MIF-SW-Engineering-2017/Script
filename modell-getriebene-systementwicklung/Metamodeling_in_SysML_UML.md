# Metamodeling in SysML / UML

Die Modellierungssprachen wie UML, SysML oder die BPMN,welche durch die Object Management Group (OMG) definiert wurden, basieren auf demKonzept von sprachbasierten Metamodellen. Ein sprachbasiertes Meta-Modellstellt die Elemente einer Modellierungssprache und ihre Beziehungen in einemModell dar. [WIKI17c]

Den Meta-Modelle der OMG liegt die Meta Object Facility (MOF)zu Grunde. Die MOF beschreibt eine Metadaten-Architektur, dessenKernbestandteil das Meta-Meta-Modell ist. Sie wurde mit dem Ziel definiert,eine gemeinsame Grundlage für verschiedene Meta-Modelle zu definieren. DieserAnsatz bietet einige Vorteile, da verschiedene Meta-Modelle dadurch gleichartigpersistiert und verarbeitet werden können. Die Modelltransformation ist eineArt der Verarbeitung von Modellen. [WIKI17d]

Die Abbildung 4 zeigt beispielhaft den Zusammenhang der verschiedenen Ebenen der (Meta-)Modelleanhand der UML. 

![](..\assets\hierarchie_der_metamodelle.png)

**Profil-Mechanismus**

Um eine Modellierungssprache wie UML oder SysML umdomänenspezifische Sprachelemente zu erweitern, stellt die OMG einenProfil-Mechanismus bereit. Ein Profil ist eine konkrete Erweiterung eines Metamodells.Ein leichtgewichtiger Mechanismus für die Erweiterung eines Metamodells sindStereotypen. Ein Stereotyp spezialisiert eine Metaklasse für ein spezifischesEinsatzgebiet. 

Für jeden Stereotypen können Stereotypeigenschaftendefiniert werden, in denen domänenspezifische Informationen gespeichert werdenkönnen. Der Profil-Mechanismus wird im Folgenden anhand von Beispielenerläutert.

Die Abbildung 5erweitert die Metaklasse *Actor* um denStereotypen *externalSystem*. DieseErweiterung kann genutzt werden, um bei einem Use-Case-Diagramm die Akteurestärker zu differenzieren.

![](..\assets\usecases.png)

Die Abbildung 6 zeigt die konkrete Anwendung eines *externalSystems* in einem Use-Case-Diagramm. Das Diagramm zeigt Use-Cases für ein Smart Home System. In dem Use-Case „Jalousien mit Smartphone steuern“ ist der Akteur „Bewohner“ und das *externalSystem* „Jalousie“ beteiligt.

![](..\assets\shadowing_use_cases.png)

Ein Stereotyp kann von anderen Stereotypen mit Hilfe einer „Generalisierung“ spezialisiert werden. In Abbildung 7 ist der Stereotyp „Requirement“ von der Metaklasse *Class* erweitert worden. Der Stereotyp besitzt zusätzliche Eigenschaften wie z.B. *Id* und *Text*. Von „Requirement“ wurde einspezialisierter Stereotyp „ExtendedRequirement“ erzeugt, der alle Eigenschaftenvon „Requirement“ besitzt und zusätzlich die Attribute *obligation* und *priority* enthält. Für die bessere Differenzierung von Anforderungen wurden von „ExtendedRequirement“ die drei Anforderungstypen „Business Requirement“, „System Requirement“ und „Design Requirement“ abgeleitet.

![](..\assets\requirements.png)

Die Abbildung 8 zeigt Visualisierung des Stereotypen „Business Requirement“ in einem Requirement Diagramm der SysML.

![](..\assets\SH_Requirements.png)

