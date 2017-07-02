# Fazit
Abschließend kann festgestellt werden, dass es mehrere Möglichkeiten zur Gesichtserkennung gibt. Es wurde aufgezeigt, dass es für die Gesichtserkennung wichtig ist, das Gesicht zu erkennen und anschließend zu klassifizieren.
Wie man vorgeht, um das Ziel zu erreichen, ist jedem selbst überlassen. Es wurde die Möglichkeit der Haarcascade (um Gesichter zu erkennen) veranschaulicht, welche bei OpenCV der Standard ist, aber natürlich gibt es auch noch andere Möglichkeiten.

Um Gesichter zu klassifizieren, kann man Eigenfaces, Fisherfaces oder LBPH einsetzen. Dabei muss man natürlich die Pros- und Contras abwägen. Möchte man eine möglich effiziente Gesichtserkennung oder man hat über- oder unterbelichtete Bilder, so eignet sich LBPH am besten. Bei LBPH muss berücksichtigt werden, dass Genauigkeit und Effizienz von der Konfiguration abhängen.
Möchte man eine möglichst genaue Gesichtserkennung, dann sollt man eher auf Eigenfaces setzen. Hat man dabei nur wenig Bilder einer Person im Trainingsset, sollt man eher auf Fisherfaces statt Eigenfaces einsetzen.
