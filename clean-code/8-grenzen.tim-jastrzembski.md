#  8 Grenzen

Unternehmen produzieren selten die komplette Software eines Systems. Meist arbeiten sie mit anderen Teams zusammen, welche ihre eigene Software schreiben, oder sie beziehen fertige Software von Drittabbietern(sowohl lizensiert als auch Open Source). Damit diese auch sauber in das eigene System eingebunden werden kann, sollte man das folgende Kapitel berücksichtigen.

## Fremdcode nutzen

In der Regel kann die angebotene API von Drittanbietern wesentlich mehr als der Nutzer für sein spezielles Problem braucht. Die Drittanbieter wollen nämlich viele Leute für ihre API begeistern. Der Nutzer hingegen erwartet Funktionen von der API, die speziell für sein Problem geeignet sind. Dieser Interessenskonflikt kann die Grenzen unseres Systems unnötig verkomplizieren.

## Die Grenzen erforschen

Das Nutzen von Drittabbieter-Code ermöglicht das Gestalten von mehr Funktionalitäten in weniger Zeit. Wie und wo soll man jedoch jenen Code verwenden? Wie benutzt man ihn? Um das Verständnis für solchen Code zu verbessern, liegt es im eigenem Interesse, diesen auszutesten. Dafür bieten sich sogenannte **Learning Tests** an. 
**Learning Tests** bestehen darin, dass man den Fremdcode weitestgehend auf die benötigten Funktionalitäten testet, wie sie später im eigenen Code verwendet werden. Das ermöglicht ein präzises Lernen der API in einer isolierten Testumgebung. Zudem eignen sich diese Tests zur Evaluation für spätere Updates des Drittabbieter-Codes, da diese direkt ungewollten Veränderungen bzgl. der genutzten Funktionen aufzeigen können.
Die Tests sollten eine saubere Grenzeinhaltung wie im richtigen Quellcode gewährleisten. Ohne diese Grenztests könnte man an ältere Versionen von Drittabbieter-Codes gebunden werden, was nicht unbedingt von Vorteil ist und zumeist mit weiteren Umstrukturierungsmaßnahmen im eigenen Quellcode endet. 

## Code nutzen, der (noch) nicht existiert

Es kann vorkommen, dass in der Softwareentwicklung Funktionen benötigt werden, die zwar beschlossen, jedoch dessen Schnittstellen noch nicht weitestgehend definiert worden sind. Damit dies die Entwicklung nicht unnötig aufhält, kann man die Schnittstellen vorerst so definieren, wie man sie sich später im Quellcode vorstellt.

![](/assets/Boundaries-AdapterPattern.jpg) 

\Abbildung 1(Quelle: Clean Code\)"\)

Abbildung 1 zeigt einen Fall, wo ein Transmitter für die weitere Entwicklung benötigt wird. Die Transmitter API dazu ist jedoch noch nicht fertiggestellt, sodass die Funktionen weder bekannt sind noch genutzt werden können. Der Einsatz vom Adapterpattern erlaubt es trotzdem, Tests für die fehlende Funktionalität zu schreiben und somit eine saubere Grenzeinhaltung zu definieren. Sobald die API fertig wird, zeigen die Tests sogar, ob sie, wie erwartet, arbeitet.

# Saubere Abgrenzung

Es kann vorkommen, dass sich die fremde API im Laufe der Zeit verändert. Wenn das der Fall ist, ist es von Vorteil, die Schnittstellen zum eigenen Quellcode so sauber wie möglich gestaltet zu haben. Das spart nämlich Zeit und Arbeit, die man dann in das Überarbeiten dieser Schnittstellen investieren muss. 
Der eigene Code an den Schnittstellen muss klar definiert und eine klare Abgrenzung zu Fremdcode haben. Dabei helfen Tests, welche die Funktionserwartungen definieren. Es ist immer besser auf etwas angewiesen zu sein, was man kontrollieren kann, als auf etwas, was man nicht kontrollieren kann, da es ansonsten einen selbst kontrolliert.  
