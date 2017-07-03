# Support Vector Machine

Die Support Vector Machine (SVM) gehört zur Familie der Klassifikationsalgorithmen.

Klassifikation bedeutet, eine Menge von Daten einer bestimmten Klasse bzw. Kategorie zuzuordnen.
Gegeben sei also eine Menge an Daten ![](https://latex.codecogs.com/gif.latex?\mathbb{D}=\left\{d_1,\cdots,d_n\right\}), wie beispielsweise ![](https://latex.codecogs.com/gif.latex?\left&space;\{&space;Berlin,&space;China,&space;Deutschland,&space;Rom&space;\right&space;\}) und eine Menge an Klassen ![](https://latex.codecogs.com/gif.latex?\mathbb{C}=\{c_1,\cdots,c_k\}), wie z.B. ![](https://latex.codecogs.com/gif.latex?\left&space;\{&space;Land,&space;Hauptstadt&space;\right&space;\}), wobei die Klassen i.d.R. von Menschen definiert werden. Die Trainingsdaten sind Zuordnungen von Daten zu Klassen, z.B.: ![](https://latex.codecogs.com/gif.latex?\langle&space;d,c\rangle&space;=&space;\langle&space;China,Land\rangle) mit ![](https://latex.codecogs.com/gif.latex?\langle&space;d,c\rangle&space;\in&space;\mathbb{D}&space;\times&space;\mathbb{C}). Algorithmen aus diesem Bereich können eine Klassifikator ![](https://latex.codecogs.com/gif.latex?\gamma) erlernen, der alle Daten zu einer Klasse zuordnen kann: ![](https://latex.codecogs.com/gif.latex?\gamma:&space;\mathbb{D}\to\mathbb{C}) .<sup id="manning2009a">[[1]](#manning2009)</sup>

Die Anfänge der Support Vector Machine liegen bereits einige Jahre zurück.
Bereits im Jahr 1963 stellten Vladimir N. Vapnik und Alexey Ya. Chervonenkis den SVM-Algorithmus vor.<sup id="svdwikia">[[2]](#svdwiki)</sup>
Die nächste größere Erfindung war der sogenannte *Kernel Trick*. Dieser wurde 1992 von Boser et. al. vorgestellt. <sup id="boser1992a">[[3]](#boser1992)</sup>
Mit Hilfe des Kernel Tricks ist es möglich die Support Vector Machine auch auf nicht linear separierbare Daten anzuwenden. In den folgenden Jahren wurden nur noch wenige geringe Verbesserungen und Varianten veröffentlicht. Auch heutzutage wird dieser Algorithmus noch oft genutzt und dient ihn vielen wissenschaftlichen Arbeiten als Vergleich zu modernen Ansätzen.<sup id="Lu2016a">[[4]](#Lu2016)</sup>


Der weitere Teil dieser Arbeit ist wie folgt gegliedert:

* [Algorithmus im Detail](support-vector-machine/algorithmus-im-detail.md)
  * [Ebenendarstellung](support-vector-machine/algorithmus-im-detail.md)
  * [Bedingungen](support-vector-machine/algorithmus-im-detail.md)
  * [Abstandsberechnung](support-vector-machine/algorithmus-im-detail.md)
  * [Optimierungsproblem](support-vector-machine/algorithmus-im-detail.md)
  * [Kernel Trick](support-vector-machine/algorithmus-im-detail.md)
* [Implementierungen](support-vector-machine/implementierungen.md)

Im Kapitel *[Algorithmus im Detail](support-vector-machine/algorithmus-im-detail.md)* wird die Support Vector Machine mathematisch beschrieben und hergeleitet. Das Kapitel *[Implementierungen](support-vector-machine/implementierungen.md)* enthält Verweise und Beispiele zu verschiedenen Implementierungen des Algorithmus.

___
<b id="manning2009"></b>1. Manning, C. D., Raghavan, P., & Schutze, H. (2009). An Introduction to Information Retrieval. Online, (c), 569. https://doi.org/10.1109/LPT.2009.2020494, S. 256 [↩](#manning2009a)

<b id="svdwiki"></b>2. https://en.wikipedia.org/wiki/Support_vector_machine [↩](#svdwikia)

<b id="boser1992"></b>3. Boser, B. E., Guyon, I. M., & Vapnik, V. N. (1992). A Training Algorithm for Optimal Margin Classiiers. Proceedings of the Fifth Annual Workshop on Computational Learning Theory, 144–152. https://doi.org/10.1.1.21.3818 [↩](#boser1992a)

<b id="Lu2016"></b>4. Lu, Y. (2016). Food Image Recognition by Using Convolutional Neural Networks (CNNs). Retrieved from http://arxiv.org/abs/1612.00983 [↩](#Lu2016a)

___
Author: Daniel Beneker
