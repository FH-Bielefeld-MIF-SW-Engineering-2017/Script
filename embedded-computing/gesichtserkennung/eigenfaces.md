# Eigenfaces
Eigenfaces (auf deutsch Eigengesichter) ist ein von Matthew Turk und Alex Pentland entwickeltes Verfahren, um Gesichter einer Person oder bestimmten Merkmalen zuordnen zu können. Dabei setzt Eigenfaces auf eine Principal Component Analyse (PCA) auf deutsch Hauptkomponentenanalyse. Die Principal Component Analyse dient dazu mit einer Anzahl an statistischen Variabeln sich einer möglichst aussagekräftigen Linearkombination zu nähern. Dieses Verfahren ist besonders in der Bildverarbeitung beliebt.[10]

## Funktionsweise
Siehe: [5] (Die Rechnung ist ein wenig verkürzt aus Wikipedia kopiert und steht hier zum Verständnis der Funktionsweise.)

Hinweis: Die Rechnung erfolgt mit Hilfe der Matrix des Bildes (wie auch im Kapitel OpenCV beschrieben). Man darf sich dabei ein Bild als Matrix vorstellen. Auch das Differenz- und Durchschnittsbild sind Matrizen.

* Schritt 1: In jenem Verfahren werden eine Trainingsmenge an Bildern von Gesichter in lexikographischer Reihenfolge eingelesen und in Vektoren einer Länge k gespeichert.
<br><center><img height=21px width=137px src="../../assets/einlesen.png" /></center>
* Schritt 2: Aus der Trainingsmenge wird schließlich ein Durchschnittsgesicht gebildet.
<br><center><img height=66px width=135px src="../../assets/durchschnittsgesicht.png"></center>
* Schritt 3: Anschließend wird von jedem Bild aus dem Trainingsset ein Differenzbild zum Durchschnittsgesicht gebildet.
<br><center><img height=21px width=102px src="../../assets/differenzgesicht.png"></center>
* Schritt 4: Sind die Differenzbilder vollständig berechnet, kann man eine Kovarianzmatrix erstellen.
<br><center><img height=61px width=217px src="../../assets/kovarianzmatrix.png"></center>
* Schritt 5: Allerdings ist bei einer Kovarianzmatrix der Nachteil vorhanden, dass für einen modernen Computer schon das Rechnen von einer Anzahl von 300 100x100 Pixel großen Bildern rechenaufwendig ist. Um dies zu verhindern sollten die Eigenvektoren statt in einer Kovarianzmatrix in einer neuen Marix berechnet werden.
<br><center><img height=22px width=157px src="../../assets/neue_matrix.png"></center>
Das dies möglich ist, wird bewiesen durch:
 * Schritt 5.1: Sei die Eigenwertzerlegung von der Kovarianzmatrix gegeben durch:
<br><center><img height=25 width=172 src="../../assets/eigenwertzerlegungC.png"></center>
 * Schritt 5.2: Da die Kovarianzmatrix eine zu große Matrix ist, wird in diesem Schritt die Eigenwertzerlegung für L betrachtet.
<br><center><img height=25 width=176 src="../../assets/eigenwertzerlegungL.png"></center>
 * Schritt 5.3: Bei linksseitiger Multiplikation mit A ergibt sich:
<br><center><img height=25 width=148 src="../../assets/linksseitigMulti.png"></center>
 * Schritt 5.4: Sei nun <center><img height=21 width=90 src="../../assets/beweis.png"><br></center>
so ergibt sich aus der Eigenwertzerlegung von L dieselbe wie von C. Damit ist es bewiesen. Die erhaltenen Vektoren von v sind die Eigenvektoren, wobei nur die mit den höchsten Eigenwert von Interesse sind. Die u's müssen noch normalisiert werden.
* Schritt 6: Schlussendlich können die ausgerechneten Eigengesichter dann in einem Gesichtsraum projiziert werden, so dass man den daraus erhaltenen Vektor für die Gesichtswiedererkennung nutzen kann.
<br><center><img height=29px width=274px src="../../assets/projizieren.png"></center>
* Schritt 7: Der aus Schritt 6 erhaltene Vektor lässt sich für die Gesichtswiedererkennung nutzen:
<br><center><img height=26px width=159px src="../../assets/gesichtswiedererkennung.png"></center>

## Eigenfaces in OpenCV
Natürlich ist es nicht notwendig in OpenCV die komplette Berechnung selbst einzuprogrammieren. Dies wäre entsprechend viel Arbeit, ließe sich aber durch die Mat Klasse bewerkstelligen. Die Berechnung der Eigenfaces ist in OpenCV in einem Zusatzmodul namens Contrib vorhanden. Dieses muss zusätzlich zur OpenCV Library kompiliert oder kann auch in den Binaries zusätzlich installiert werden. Die Darstellung der Funktionsweise dient zum Verständnis, wie das Ganze eigentlich funktioniert.

OpenCV bietet noch eine kleine Besonderheit. Wenn man ein Bild auf das Trainingsset überprüfen lässt, ist es möglich einen Wert namens "Confidence" aus der Funktion herauszuholen. Der Confidence Wert errechnet sich nach der kNN (k-Nearest-Neighbour [auf dt. Nächste-Nachbarn-Klassifikation]) Methode und gibt die Distanz zu dem am ähnlichsten gefundenen Bild aus dem Trainingsset wieder.[6-7]
