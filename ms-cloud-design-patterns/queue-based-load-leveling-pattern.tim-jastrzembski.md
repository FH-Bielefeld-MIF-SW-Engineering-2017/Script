# Queue-Based Load Leveling Pattern
Das **Queue-Based Load Leveling Pattern** besteht darin, dass man Services um eine asynchrone Queue erweitert, welche die Anfragen der Tasks entgegennimmt und dem Service weiterreicht. Das soll verhindern, dass bei zu vielen Anfragen der Tasks an den Service dieser überlastet und seine Funktionalität verzögert oder gar nicht erfüllen kann.  Das Pattern erhöht somit die Verfügbarkeit und Verlässlichkeit der Services.
## Kontext und Problem
Viele Programme in der Cloud basieren darauf, dass sie Tasks ausführen, welche Services aufrufen. Wenn aber zu viele Tasks auf denselben Service zur gleichen Zeit zugreifen wollen, kann dies zur einer Überlastung des Service führen, was sich in Verzögerungen oder nicht Erreichbarkeit äußern kann (siehe Bild). 
![Bild: Queue-Based Load_Leveling Pattern.HeavyLoadAndItsConsequence.jpg]( https://github.com/FH-Bielefeld-MIF-SW-Engineering-2017/Script/blob/tjastrzembski-patch-1/assets/Queue-Based%20Load_Leveling%20Pattern.HeavyLoadAndItsConsequence.jpg?raw=true „Hoher Arbeitsfluss führt dazu, dass einige Tasks ihre Anfrage nicht senden können. (Quelle: Cloud Design Patterns)“)
## Lösung
Der Einsatz einer asynchronen Queue kann zwar die Verzögerung der Anfrage der Tasks nicht vollständig verhindern, sorgt aber dafür, dass die Anfragen nicht unbeantwortet bleiben. 
![BildQueue-Based Load_Leveling Pattern.AsynchronousQueue.jpg]( https://github.com/FH-Bielefeld-MIF-SW-Engineering-2017/Script/blob/tjastrzembski-patch-1/assets/Queue-Based%20Load_Leveling%20Pattern.AsynchronousQueue.jpg?raw=true „Prinzip der asynchronen Queue  (Quelle: Cloud Design Patterns)“)
Die Anfragen der Tasks werden in die Queue gesteckt und geordnet nach Zeitpunkt des Eintreffens abgearbeitet. 
Das bietet folgende Vorteile:
* Die Verfügbarkeit der Services wird maximiert, da Verzögerungen weniger Auswirkungen auf die Funktionalität haben. Selbst wenn der Service temporär nicht erreichbar ist, können die Anfragen nachgearbeitet werden.
* Der Service kann skaliert werden, da je nach Anforderung die Anzahl der Queues und Services angepasst werden können. 
* Es unterstützt bei der Kostenkontrolle bzgl. Ressourcen, da durch die Queue die Anzahl an Services anstatt für den Worst Case nur ausreichend für den Durchschnittsarbeitsfluss sein muss.

Das Pattern eignet sich ideal für Applikationen, bei denen hohe Zugriffszahlen in kurzer Zeit entstehen könnten. Es wäre entsprechend nicht effektiv, dies bei Applikationen einzusetzen, bei denen das Gegenteil der Fall ist.

Man sollte folgende Punkte beachten, sofern man dieses Pattern implementieren will:
* Es ist von Vorteil, eine Logik für die Applikation zu entwickeln, welche die Abarbeitungsrate der Services kontrolliert, damit der Service nicht überlastet. Es sollten grundsätzlich Arbeitsflussspitzen vermieden werden. Zur Sicherstellung kann das System unter realistischen Arbeitsfluss getestet werden, um bei Unstimmigkeiten die Anzahl der Queues und Services anzupassen.
* Die Queue funktioniert nur in einer Richtung. Wenn der Task eine Rückmeldung erwartet, müssen weitere Mechanismen implementiert werden, die dies sicherstellen (z.B. _Asynchronous Messaging Primer_).


