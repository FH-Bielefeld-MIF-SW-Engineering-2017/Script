# Retry Pattern

Dieses Muster (Retry Pattern) ermöglicht, dass eine Anwendung erwartete und temporäre Fehler behandelt. Wenn eine Anwendung versucht, sich mit einem Service oder Netzwerk zu verbinden, wiederholt sie die Operation, weil die Ursache des Fehlers vorübergehend (transient) sein kann.

## Problem
Wenn eine Anwendung mit Elementen in einer Cloud kommuniziert, können vorübergehende Fehler auftreten: der kurzzeitige Untergang der Netzwerkkonnektivität, die kurzzeitige Nichtverfügbarkeit eines Services...
Die Aktion, die diese Fehler auslöst, kann erfolgreich sein, wenn sie mit einer Zeitverzögerung wiederholt wird.

## Lösung
Eine Anwendung kann diese Fehler folgendermaßen behandeln:
- Wenn der Fehler nicht vorübergehend ist (z.B. Authentifizierungsfehler), sollte die Anwendung die Operation abbrechen und eine 'Exception' werfen.
- Wenn der bestimmte Fehler ungewöhnlich oder selten ist, sollte die Anwendung die Operation sofort wiederholen. (Warscheinlich wird der Fehler nicht erneut auftreten.)
- Wenn der Fehler ein 'busy' Fehler ist, sollte die Anwendung warten, bevor die Operation wiederholt wird. Wenn die Operation nach einer bestimmten Anzahl von Versuchen immer noch nicht erfolgreich ist, sollte die Anwendung den Fehler als eine Ausnahme (Exception) behandeln.
Es ist hilfreich Fehler, die mit Retry lösen kann, in einem log detailiert aufzuzeichnen.


## Was es zu beachten gilt 
-  Die Retry policy sollte an die Art der Anwendung und des Fehlers angepasst werden. Wenn die Operation für die Anwendung nicht essentiell ist, kann es manchmal für die Anwendung besser sein nicht die Operation zu wiederholen, sondern abzubrechen.
-  Wenn man zu viel und zu schnell erneut versucht, kann man sowohl den 'busy' service, als auch die Anwendung überlasten.
-  Nach einer Vielzahl von Wiederholungen kann man erstmal einen Fehlerbericht ausgeben, dann eine Weile warten und erst dann ein oder zwei Mal erneut die Operation versuchen.
-  Es ist wichtig, dass die Zeitverzögerung zwischen erneuten Anfragen an die Art des Fehlers angepasst ist.
-  Retry Code muss die Zuverlässigkeit und Performance des gesamten Codes nicht beeinträchtigen. Man muss den Retry Code vielfältig testen.
-  Es soll keine verschachtelten Retry Codes geben. Ein Retry Code ist z.B. verschachtelt, wenn eine Aufgabe, die Retry Code hat, eine andere Aufgabe, die auch Retry Code hat, aufruft.
-  Man sollte versuchen herauszufinden, ob die Fehler lang andauernd sind. In diesem Fall sollte man den Fehler als Ausnahme behandeln.

## Wann sollte man Retry Pattern benutzen?
Retry Pattern sollte benutzt werden:
- Wenn bei einer Anwendung, die mit einem fernen Service interagiert, vorübergehende Fehler auftreten können, sollte man Retry Pattern benutzen.

Retry Pattern sollte nicht benutzt werden:
- Wenn ein Fehler lang andauernd ist.
- Für nicht vorübergehende Fehler
- Wenn ein 'busy' Fehler bei einem bestimmten Service häufig ist.
