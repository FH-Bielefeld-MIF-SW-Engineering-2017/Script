# Bayesches Theorem als Klassifikator

Dieses Theorem ist als Klassifikator anwendbar und bestimmt die Zugehörigkeit einer Instanz zu einer Klasse anhand der errechneten bedingten Wahrscheinlichkeiten.


So können wir den folgenden Term 

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edo5.png)
<!--- Latex Code:
P(A|B) = \frac{ P(B|A) * P(A) }{ P(B) }
-->

ummünzen, um die Wahrscheinlichkeit für eine Klassenzugehörigkeit zu errechnen.

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/ednt.png)
<!--- Latex Code:
P(K|I) = \frac{ P( I _{ 1 }|K) * P( I _{ 2 }|K) * ... * P( I _{ n }|K) *  P(K)}{ P(I) }
-->

Wobei 

I die Instanz, 

I*n* die einzelnen Attribute der Instanz und
 
K das Ereignis bzw. die Klasse der Instanz beschreibt.

Hierbei ist davon auszugehen, dass alle Attribute unabhängig voneinander sind, sodass wir die Attribute einfach aufteilen können.
Deswegen wird dieser Bayes Klassifikator auch als naiv oder simpel bezeichnet. 
