# Mathematische Grundlagen
Grundlage des Naive Bayes Klassifikatoren bildet die Wahrscheinlichkeitstheorie. Folgend werden die allgemeinen Grundlagen beschrieben.
Beim einmaligen Werfen eines fairen Würfels sind die möglichen Elementarereignisse des Experiments:

![](https://www.zahlen-kern.de/editor/equations/edda.png)
<!--- Latex Code:
\Omega=\left\{ 1, 2, 3, 4, 5, 6 \right\}
-->

Für jedes Element ω aus der Menge Ω gilt die gleiche Wahrscheinlichkeit.

![](https://www.zahlen-kern.de/editor/equations/edea.png)
<!--- Latex Code:
\forall \omega \in \Omega : P(\omega) = \frac{ 1 }{ 6 }
-->

Demnach ist die Summe der Wahrscheinlichkeiten der Elementarereignisse 1.

(Streng mathematisch genommen ist diese Definition für unendlich große Ω nicht korrekt, aber für den Bayes Klassifikator und für dieses Beispiel ist dies irrelevant, da der Wahrscheinlichkeitsraum diskret ist)

![](https://www.zahlen-kern.de/editor/equations/edf0.png)
<!--- Latex Code:
\Sum{ \omega \in \Omega }{  }{ P(\omega) } = 1
-->

![](https://www.zahlen-kern.de/editor/equations/edko.png)
<!--- Latex Code:
P(\omega) = \frac{ 1 }{ \left\lvert \Omega \right\rvert }
-->


Die Wahrscheinlichkeit eine 6 zu Würfeln ist zufolge 1/6.

Eine Teilmenge A aus Ω wird als Ereignis bezeichnet.
Die Wahrscheinlichkeit des Ereignisses A ist die Summe der Wahrscheinlichkeiten aller Elementarereignisse aus A

![](https://www.zahlen-kern.de/editor/equations/eedx.png)
<!--- Latex Code:
P(A) = \Sum{ \omega \in A }{  }{ P(\omega) }
-->

Das Ereignis A könnte z.B. das Würfeln einer geraden Zahl sein.

![](https://www.zahlen-kern.de/editor/equations/edf9.png)
<!--- Latex Code:
A = \left\{  2, 4, 6 \right\}
-->
Die Wahrscheinlichkeit für das Eintreffen von A beträgt 50%. 

![](https://www.zahlen-kern.de/editor/equations/eee0.png)
<!--- Latex Code:
P(A) = P(\left\{ 2 \right\}) + P(\left\{ 4 \right\}) + P(\left\{ 6 \right\}) = \frac{ 1 }{ 6 } + \frac{ 1 }{ 6 } + \frac{ 1 }{ 6 } = \mathbold{ \frac{ 1 }{ 2 } }
-->

Nun erweitern wir unser Experiement auf das zweifache Werfen eines fairen Würfel.

![](https://www.zahlen-kern.de/editor/equations/edgu.png)
<!--- Latex Code:
\Omega = \{ (1, 1), (1,2), (1,3), (1,4) ,(1,5), (1,6), 
            (2, 1), ... (6, 6) \}
-->

![](https://www.zahlen-kern.de/editor/equations/edi9.png)
<!--- Latex Code:
\forall \omega \in \Omega : P(\omega) = \frac{ 1 }{ 36 }
-->

Wir definieren das Ereignis A neu: die summierte Augenzahl beider Wüfel ist 10.

![](https://www.zahlen-kern.de/editor/equations/edic.png)
<!--- Latex Code:
A = \left\{ (4,6), (5, 5), (6,4) \right\}
-->

![](https://www.zahlen-kern.de/editor/equations/eee4.png)
<!--- Latex Code:
P(A) = P(\{(4,6)\}) + P(\{(5, 5)\}) + P(\{(6,4)\}) = \frac{ 1 }{ 36 } + \frac{ 1 }{ 36 } + \frac{ 1 }{ 36 } = \mathbold{ \frac{ 3 }{ 36 } }
-->

Das Ergebnis B bedeutet, dass der erste Wurf eine 6 ist.

![](https://www.zahlen-kern.de/editor/equations/edjb.png)
<!--- Latex Code:
B = \left\{ (6,1), (6, 2), (6, 3), (6,4), (6, 5), (6, 6) \right\}
-->

![](https://www.zahlen-kern.de/editor/equations/eeea.png)
<!--- Latex Code:
P(B) = P(\{(6,1)\}) + P(\{(6, 2)\}) + P(\{(6,3)\}) + P(\{(6,4)\}) + P(\{(6,5)\}) + P(\{(6,6)\}) = 6 * \frac{ 1 }{ 36 } = \mathbold{ \frac{ 6 }{ 36 } }
-->

Wenn man die Ereignisse A und B miteinander verknüpft, dann muss der erste Wurf eine 6 sein und die Augenzahl muss 10 betragen.

![](https://www.zahlen-kern.de/editor/equations/edk8.png)
<!--- Latex Code:
A\intsec B = {(6,4)}
-->

![](https://www.zahlen-kern.de/editor/equations/eeeo.png)
<!--- Latex Code:
P(A\intsec B) = P(\{ (6,4) \}) = \frac{ 1 }{ 36 }
-->
## Bedingte Wahrscheinlichkeit

Die bedingte Wahrscheinlichkeit P(A|B) beschreibt, die Wahrscheinlichkeit, dass das Ergebnis A eintritt, unter der Bedingung, dass das Ergebnis B bereits eingetreten ist. In unserem Beispiel bedeutet dies folgendes.
Unter der Bedingung, dass die erste Zahl eine 6 ist (Ergebnis B), wie groß ist dann die Wahrscheinlichkeit, dass die Augensumme 10 beträgt (Ergebnis A)?  

B ist gegeben:
 
![](https://www.zahlen-kern.de/editor/equations/edjb.png)
<!--- Latex Code:
B = \left\{ (6,1), (6, 2), (6, 3), (6,4), (6, 5), (6, 6) \right\}
-->

In der Menge B gibt es ein Element, welches auch A entspricht.

![](https://www.zahlen-kern.de/editor/equations/edk8.png)
<!--- Latex Code:
A\intsec B = {(6,4)}
-->
Somit beträgt die Wahrscheinlichkeit von A innerhalb B:

![](https://www.zahlen-kern.de/editor/equations/eeeq.png)
<!--- Latex Code:
P(A|B) = \frac{ P (\{(6,4)\} ) }{ P( \left\{ (6,1), (6, 2), (6, 3), (6,4), (6, 5), (6, 6) \right\} ) }
-->

![](https://www.zahlen-kern.de/editor/equations/ednh.png)
<!--- Latex Code:
P(A|B) = \frac{  \frac{ 1 }{ 36 } }{ \frac{ 1 }{ 6 } } = \frac{ 1 }{ 6 }
-->

Da für P(A|B) gilt: 

![](https://www.zahlen-kern.de/editor/equations/edl4.png)
<!--- Latex Code:
P(A|B) = \frac{ P(A\intsec B) }{ B }
-->

auch bekannt als Bayesches Theorem.
 
Komplette Definition des Theorems:


![](https://www.zahlen-kern.de/editor/equations/edo3.png)
<!--- Latex Code:
P(A|B) = \frac{ P(A \intsec B) }{ P(B) } = 
\frac{ \frac{ P(A \intsec B) }{ P(A) }  *P(A)}{ P(B) } =
\frac{ P(B|A) * P(A) }{ P(B) }
-->

___	
Author: Sven Schirmer
