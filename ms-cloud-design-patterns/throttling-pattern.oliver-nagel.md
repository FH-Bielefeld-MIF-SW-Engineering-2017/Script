# Throttling Pattern

## Problemstellung
Die Auslastung einer Cloud unterliegt zeitlichen Schwankungen. Sie ist abhängig von der Anzahl der aktiven Benutzer und deren Tätigkeiten. Daher kann es zu plötzlichen und unerwarteten Anstiegen der Auslastung kommen, die das System an die Grenzen seiner Ressourcen bringt. Die vereinbarten Service-Level können auf Grund der resultierenden Performanceeinbußen nicht mehr eingehalten werden. Um schwankende Auslastungen zu bewältigen, können Strategien wie Autoscaling oder Throttling angewendet werden. 

## Strategien
Beim Autoscaling kann die Cloud die Bereitstellung weiterer Ressourcen anfragen, wenn die eigenen Ressourcen nicht ausreichen. Bei einem unerwartet starken Anstieg der Auslastung kann es dennoch zum Defizit kommen, da diese Bereitstellung nicht unmittelbar erfolgt. 
Bei der Throttling-Strategie dürfen Anwendungen die Ressourcen bis zu einem Softlimit verbrauchen. Wenn dieses Softlimit überschritten wird, werden Anwendungen gedrosselt, sodass das System weiterhin seine Funktion erbringen kann und die vereinbarten Service-Level eingehalten werden. Das Drosseln kann durch Ablehnen von Benutzeranfragen über eine Zeitperiode oder durch das Deaktivieren / Einschränken von Funktionalität bestimmter nicht essentieller Services erreicht werden (z.B. Begrenzung der Auflösung bei Videostreaming). Dabei können die Ressourcen aller Benutzer gleichermaßen (Queue-based Load Leveling Pattern) oder bei Benutzer mit einem höheren Service-Level geringer eingeschränkt werden (Priority Queue Pattern).
Im Folgenden soll der Ablauf der zwei Strategien Throttling und Autcoscaling in Kombination gezeigt werden. Die Abbildung 1 zeigt dazu den Ressourcenverbrauch aller Anwendungen über die Zeit an. Bis zu dem Zeitpunkt T1 ist der Ressourcenverbrauch unterhalb des Softlimits.  Ab dem Zeitpunkt T1 wird dieses Limit überschritten und das System fragt die Bereitstellung weiterer Ressourcen an (Autoscaling). Bei einem schnellen Anstieg des Ressourcenbedarfs kann das System die maximale Belastung erreichen, da das Autoscaling Zeit in Anspruch nimmt. Um dies zu verhindern, kann eine Throttling-Strategie zwischen der Zeitspanne T1 und T2 eingesetzt werden. Das Throttling kann zum Zeitpunkt T2, wenn die angefragten Ressourcen zur Verfügung stehen, wieder verringert werden.

![throttling](/assets/throttling_autoscaling.PNG) Abbildung 1: Kombination der Throttling- und Autoscaling-Strategie [[Cloud Design Patterns, S. 157]](https://www.google.de/url?sa=t&rct=j&q=&esrc=s&source=web&cd=7&ved=0ahUKEwjBp_bjh-rTAhWIZVAKHR05CSYQFghMMAY&url=https%3A%2F%2Fdownload.microsoft.com%2Fdownload%2FB%2FB%2F6%2FBB69622C-AB5D-4D5F-9A12-B81B952C1169%2FCloudDesignPatternsBook-PDF.pdf&usg=AFQjCNGfN9eRS1NDFxLihCC4R3k-mvGmvg&sig2=yScohHzNzZ06OrbI6Lr51Q&cad=rja "Cloud Design Patterns").

## Weitere Betrachtungen
- Eine Throttling-Strategie hat Auswirkungen auf das Systemdesign und muss daher früh betrachtet werden.
- Das System muss das Drosseln schnell umsetzen können.
- Das System muss einer gedrosselten Client-Applikation eine aussagekräftige Fehlermeldung zurückgeben, sodass diese entsprechend reagieren kann.
- Bei kurzen Anstiegen des Ressourcenbedarfs sollte auf Autoscaling verzichtet werden, da diese Strategie kostspielig ist.
- Eine aggressivere Throttling-Strategie oder eine größere Ressourcenreserve sollte betrachtet werden, wenn das System trotz einer aktiven Drosselung an die Grenzen geht und dies nicht tolerierbar ist. 

## Einsatz des Pattern
- Einhaltung von Service-Level-Vereinbarungen.
- Verhindern, dass eine Teilnehmer-Applikation große Mengen an Ressourcen für sich selbst beansprucht.
- Abfangen von Spitzen des Ressourcenverbrauchs.



