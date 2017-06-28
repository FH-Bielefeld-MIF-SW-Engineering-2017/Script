# Model Transformation

Eine zentrale Technik bei der modellbasierten Entwicklungist die Modelltransformation. Die Modelltransformation wird benötigt, umInformationen eines Datenmodells in ein anderes Datenmodell, welches eine andereStruktur besitzt, zu überführen. [OSTF17] 

Die Bandbreite der Anwendungsgebiete reicht von derDokumentengenerierung über die Variantengenerierung bis hin zur die Erstellungneuer Modelle und der Codegenerierung.  Dabeiist die Vorgehensweise der Transformation immer gleich. Es werden Informationenaus dem Quellmodell abgefragt und diese nach definierten Regeln in eine andereForm gebracht. Diese Regeln werden auch als Transformationsregeln bezeichnetund werden auf der Ebene der Metamodelle definiert.

Bei der Modelltransformation wird zwischenModell-zu-Modell-Transformation (M2M-Transformation) undModel-zu-Text-Transformation (M2T-Transformation) unterschieden. [WIKI17b]

**Modell-zu-Modell-Transformation**

Innerhalb der M2M-Transformation kannerneut in den zwei Varianten Inplace-Transformation und Outplace-Transformation unterschiedenwerden. Bei der Inplace- Transformation wird durch die Transformationkein neues Modell erzeugt, sondern das bestehende Modell modifiziert. DieOutplace-Transformation generiert dagegen ein neues Modell und modifiziert dasQuellmodell nicht. [WIKI17b]

Im Folgenden sollen verschiedene Transformationssysteme imÜberblick dargestellt werden.

**Query ViewTransformation (QVT)**

Die Query View Transformation (QVT) ist eine formale Sprachefür M2M-Transformation und wurde von der OMG standardisiert. Sie ist Teil derMeta Object Facility (MOF). Unter einer Query werden Anfragen auf einMOF-Modell verstanden, um bestimmte Modellelemente zu finden, die transformiertwerden sollen. Unter einer View versteht die OMG ein Modell, welches aus einemQuellmodell abgeleitet wurde. Die Transformation ist die Überführung von einoder mehrere Quellelemente in ein oder mehrere Zielelemente. Für dieTransformation stehen innerhalb der QVT zwei Sprachen zur Verfügung:

* die QVT Operational Mappings Language, welcheeine imperative Sprache ist.
* die QVT Relations Language, die eine deklarativeSprache ist und neben einer textuellen auch eine grafische Syntax definiert.[ITWI17a]

**Atlas Transformation Language (ATL)**

Die AtlasTransformation Language ist eine Sprache zur Modelltransformation und wurde aufGrund einer Ausschreibung der OMG für eine allgemeine Programmiersprache zurModell- und Codetransformation entwickelt. Die ATL ist eine hybrideSprache. Dies bedeutet, dass sie Konzepte imperativer und deklarativerProgrammierung vereint. [ITWI17b]

**MOF Model to Text Transformation Language (MOFM2T)**

Die MOF Model to Text Transformation Language ist einweiterer Standard der OMG zur metamodellbasierten Modell-zu-Text Transformation.Sie kann genutzt werden, um z.B. Code auf einem UML oder SysML-Modell zugenerieren. [WIKI17e]