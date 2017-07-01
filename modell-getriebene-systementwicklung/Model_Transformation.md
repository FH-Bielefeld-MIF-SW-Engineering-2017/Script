# Model Transformation

Eine zentrale Technik bei der modellbasierten Entwicklungist die Modelltransformation. Die Modelltransformation wird benötigt, um Informationen eines Datenmodells in ein anderes Datenmodell, welches eine andere Struktur besitzt, zu überführen. [OSTF17](Quellen.md) 

Die Bandbreite der Anwendungsgebiete reicht von der Dokumentengenerierung über die Variantengenerierung bis hin zur die Erstellung neuer Modelle und der Codegenerierung.  Dabei ist die Vorgehensweise der Transformation immer gleich. Es werden Informationen aus dem Quellmodell abgefragt und diese nach definierten Regeln in eine andere Form gebracht. Diese Regeln werden auch als Transformationsregeln bezeichnet und werden auf der Ebene der Metamodelle definiert.

Bei der Modelltransformation wird zwischen Modell-zu-Modell-Transformation (M2M-Transformation) und Model-zu-Text-Transformation (M2T-Transformation) unterschieden. [WIKI17b](Quellen.md)

**Modell-zu-Modell-Transformation**

Innerhalb der M2M-Transformation kann erneut in den zwei Varianten Inplace-Transformation und Outplace-Transformation unterschieden werden. Bei der Inplace- Transformation wird durch die Transformation kein neues Modell erzeugt, sondern das bestehende Modell modifiziert. Die Outplace-Transformation generiert dagegen ein neues Modell und modifiziert das Quellmodell nicht. [WIKI17b](Quellen.md)

Im Folgenden sollen verschiedene Transformationssysteme im Überblick dargestellt werden.

**Query ViewTransformation (QVT)**

Die Query View Transformation (QVT) ist eine formale Sprache für M2M-Transformation und wurde von der OMG standardisiert. Sie ist Teil der Meta Object Facility (MOF). Unter einer Query werden Anfragen auf ein MOF-Modell verstanden, um bestimmte Modellelemente zu finden, die transformiert werden sollen. Unter einer View versteht die OMG ein Modell, welches aus einem Quellmodell abgeleitet wurde. Die Transformation ist die Überführung von ein oder mehrere Quellelemente in ein oder mehrere Zielelemente. Für dieTransformation stehen innerhalb der QVT zwei Sprachen zur Verfügung:

* die QVT Operational Mappings Language, welche eine imperative Sprache ist.
* die QVT Relations Language, die eine deklarative Sprache ist und neben einer textuellen auch eine grafische Syntax definiert. [ITWI17a](Quellen.md)

**Atlas Transformation Language (ATL)**

Die Atlas Transformation Language ist eine Sprache zur Modelltransformation und wurde auf Grund einer Ausschreibung der OMG für eine allgemeine Programmiersprache zur Modell- und Codetransformation entwickelt. Die ATL ist eine hybride Sprache. Dies bedeutet, dass sie Konzepte imperativer und deklarativer Programmierung vereint. [ITWI17b](Quellen.md)

**MOF Model to Text Transformation Language (MOFM2T)**

Die MOF Model to Text Transformation Language ist ein weiterer Standard der OMG zur metamodellbasierten Modell-zu-Text-Transformation. Sie kann genutzt werden, um z.B. Code auf einem UML oder SysML-Modell zu generieren. [WIKI17e](Quellen.md)