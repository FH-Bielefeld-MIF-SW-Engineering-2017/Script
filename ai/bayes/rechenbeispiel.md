# Rechenbeispiel

Als Datengrundlage dient das Dataset auf github:
<https://github.com/gr8Adakron/naive-bayes-using-python/blob/master/tennis.csv>

Die Tabelle enthält die normalen Attrbiute *Outlook*, *Temperatur*, *Humidity* und *Windy*.
*Play* ist das Label Attribut, nach dem es zu klassifizieren gilt.

|Outlook	|Temp.		|Humidity	|Windy		|Play		|
|-----------|-----------|-----------|-----------|-----------|
|sunny		|hot		|high		|false		|no			|
|sunny		|hot		|high		|true 		|no			|
|overcast	|hot		|high		|false 		|yes		|
|rainy		|mild		|high		|false 		|yes		|		
|rainy		|cool		|normal		|false 		|yes		|
|rainy		|cool		|normal		|true 		|no			|
|overcast	|cool		|normal		|true 		|yes		|
|sunny		|mild		|high		|false 		|no			|
|sunny		|cool		|normal		|false 		|yes		|
|rainy		|mild		|normal		|false 		|yes		|
|sunny		|mild		|normal		|true 		|yes		|
|overcast	|mild		|high		|true 		|yes		|
|overcast	|hot		|normal		|false 		|yes		|
|rainy		|mild		|high		|true 		|no			|

Der folgende Datensatz soll klassifiziert werden.

|Outlook	|Temp.		|Humidity	|Windy		|Play		|
|-----------|-----------|-----------|-----------|-----------|
|sunny		|hot		|high		|false		|?			|

Wir suchen also die Wahrscheinlichkeiten für die Klassen *yes* und *no* unter der Bedingung der Instanzen.

Für die erste Instanz sieht dies so aus:

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edoi.png)
<!--- Latex Code:
P(yes|I )= \frac{P( I _{ 1 } = sunny |yes) * P( I _{ 2 } = hot|yes) * 
P( I _{ 3 } = high|yes) * P( I _{ 4 } = true|yes) * P(yes)}
{ P(I) }
-->

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edoj.png)
<!--- Latex Code:
P(no|I )= \frac{P( I _{ 1 } = sunny |no) * P( I _{ 2 } = hot|no) * 
P( I _{ 3 } = high|no) * P( I _{ 4 } = true|no) * P(no)}
{ P(I) }
-->

Fangen wir mit der Klasse *yes* und folgendem Term an.

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edom.png)
<!--- Latex Code:
P( I _{ 1 } = sunny |yes) 
-->

Unter der Bedingung der Klasse *yes* (Anzahl 9) zählen wir 2 Instancen mit *sunny*. Somit beträgt die bedingte Wahrscheinlichkeit für den Term:

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edoq.png)
<!--- Latex Code:
P( I _{ 1 } = sunny |yes) = \frac{ 2 }{ 9 }
-->

Wir verfahren analog mit den anderen Attributen:

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edos.png)
<!--- Latex Code:
P( I _{ 2 } = hot|yes) = \frac{ 2 }{ 9 }
-->

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edot.png)
<!--- Latex Code:
P( I _{ 3 } = high|yes) = \frac{ 3 }{ 9 }
-->

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edou.png)
<!--- Latex Code:
P( I _{ 4 } = false|yes) = \frac{ 6 }{ 9 }
-->


![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edov.png)
<!--- Latex Code:
P(yes) = \frac{ 9 }{ 14 }
-->

Nun können wir bereits den Likelihood für die Klasse *yes* ausrechnen bzw. fast den kompletten Term außer P(i). 

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edpi.png)
<!--- Latex Code:
Likelihood(yes) = \frac{ 2 }{ 9 } * \frac{ 2 }{ 9 } * \frac{ 3 }{ 9 } * \frac{ 6 }{ 9 } * \frac{ 9 }{ 14 } = \mathbold{ \frac{ 4 }{ 567 } } = \mathbold{ 0,0071 }
-->


Wir verfahren analog zu der Klasse *no*,

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edp1.png)
<!--- Latex Code:
P( I _{ 1 } = sunny |no) = \frac{ 3 }{ 5 }
-->

sowie mit den anderen Attributen und erhalten die Formel für den Likelihood.

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edpp.png)
<!--- Latex Code:
Likelihood(no) = \frac{ 3 }{ 5 } * \frac{ 2 }{ 5 } * \frac{ 4 }{ 5 } * \frac{ 3 }{ 5 } * \frac{ 5 }{ 14 } = \mathbold{ \frac{ 36 }{ 875} } = \mathbold{ 0,0411 }
-->

Der Likelihood für die Klasse *no* ist höher und die Instanz wird somit als *no* klassifiziert.
Der Term P(I), die Wahrscheinlichkeit für die Instanz, ist uns unbekannt. Dennoch können wir die Wahrscheinlichkeit für die Klasse anhand der bereits errechneten Likelihoods bestimmen.

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edpq.png)
<!--- Latex Code:
P(yes|I)=\frac{ Likelihood(yes) }{ Likelihood(yes) + Likelihood(no ) }
-->

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edpv.png)
<!--- Latex Code:
P(yes|I)=\frac{ 0,0071 }{ 0,0071 +0,0411 } = \mathbold{ 0.1473 }
-->

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edpr.png)
<!--- Latex Code:
P(no|I)=\frac{ Likelihood(no) }{ Likelihood(yes) + Likelihood(no ) }
-->

![Alternativer Text](https://www.zahlen-kern.de/editor/equations/edq0.png)
<!--- Latex Code:
P(no|I)=\frac{ 0,0411  }{ 0,0071 +0,0411 } = \mathbold{ 0.8527 }
-->

Zu 85% trifft die Klassifizierung zu *no* zu.
