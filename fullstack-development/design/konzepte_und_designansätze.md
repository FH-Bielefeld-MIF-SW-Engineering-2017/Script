# Konzepte und Designansätze

 

Bisher wurde die Designkonzeption nur sehr abstrakt geschildert. Im Folgenden
sollen jetzt einige Konzepte und Ansätze erläutert werden, welche diese
aufgreifen und ergänzen. Bei der Konzeptionierung eines Designs hat der
Entwickler meist schon eine grobe Vorstellung des Aussehens einer Anwendung im
Kopf. Nachdem die Zielgruppen analysiert wurden kann diese Vorstellung jetzt
überarbeitet werden.

 

## Skeumorphismus

 

Beim Skeumorphsimus wird versucht, das Aussehen von Dingen zu immitieren. Der
Skeumorphismus taucht in der Softwareentwicklung bereits bei den Anfängen der
Betriebssysteme mit grafischer Oberfläche auf. Icons wie der Papierkorb oder
Ordner sollten hier ein schnelles Verständnis und einen leichten Einstieg in die
Computerwelt bieten. Wenn eine Anwendung zur Verwaltung von Notizen geschrieben
werden soll, so könnte man diese Notizen beispielsweise wie reale Notizzettel
aussehen lassen. Hierbei wird das dritte, vierte, siebte und achte Gesetz der
Einfachheit erfüllt. Der Anwender kennt, was er sieht und braucht somit keine
Zeit für das Lernen der Handhabung. Es kann auf eine Nutzbarkeit wie bei
normalen Notizzetteln vertraut werden und durch das reale Aussehen werden bei
den Nutzern positive Emotionen ausgelöst. Aus den genannten Gründen ist der
Skeumorphismus besonders bei Zielgruppen angebracht, welche sich nicht schnell
an neue Technologien anpassen. In der Regel sind dies ältere Personen, welche
technisch nicht sonderlich bewandt sind.

Ein weiterer sinnvoller Anwendungsfall ist gegeben, wenn die Anwendung der
Nutzung des realen Gegenstands ähnelt. Ein DJ-Pult kann digital ähnlich
dargestellt werden wie ein reales. Außerdem können die Schalter, Regler und
Scheiben intuitiv genutzt werden, wie in der folgenden Abbildung dargestellt.

Oft bekommen Anwendungen einen Hintergrund aus der realen Welt, ohne dass dieser
einen Zusammenhang zu der Anwendung darstellt. Beispielsweise könnte eine
Kalenderanwendung einen Baumrinden- oder Leder-Hintergrund bekommen, um ein
edleres Aussehen zu vermitteln. (vgl [3])

 

![](/assets/Mischpult.png)

Mischpult im Skeumorphismus Design ([4])

 

## Flat Design

 

Das Flat Design wurde mit dem Kachel-Design des ersten Windows Phones bekannt.
Hier wird nicht versucht die Realität zu immitieren, sondern Elemente so einfach
wie möglich ohne große Schnörkel darzustellen. Dies bringt die Möglichkeit mit
sich, Elemente viel freier zu gestalten und völlig neue Ansätze für bereits
vorhandene Dinge zu definieren. Beispielsweise könnte ein Taschenrechner einen
größeren Fokus auf Funktionalität bekommen, anstatt mit dem bekannten Layout nur
die einfachsten Rechenfunktionen zur Verfügung zu stellen.

Die dargestellten Elemente sind meist in einer Farbe gestaltete, flache Objekte
ohne 3D-Effekte wie einen Schlagschatten. Dies sorgt für eine schnellere
Umsetzung der Design-Konzeption, da keine Grafiken pixelgenau platziert werden
müssen. Die gesparte Zeit kann dann in die Logik der einzelnen Komponenten
investiert werden.

Durch das Flat Design kann das erste, zweite, fünfte und sechste Gesetz der
Einfachheit erfüllt werden. Die Darstellung der Elemente wird auf ein Minimun
reduziert, wodurch die Anwendungen meist geordneter wirken. Außerdem wird die
Anwendung durch einheitlich große Elemente, eine gleiche Farbgestaltung dieser
oder eine Gruppierung dieser, organisiert. Zuerst mag das Flat Design aufgrund
seiner geringeren Ausprägungen der gestalterischen Merkmale komplexer
erscheinen, jedoch wird die Nutzung nach kurzer Einarbeitungszeit intuitiver, da
es in vielen verschiedenen Anwendungen ähnlich eingesetzt wird. Es ist sehr
einfach den gewünschten Kontext mit den Elementen zu schaffen, da hierbei großer
Wert auf die Farbgestaltung sowie die Positionierung gelegt werden kann. (vgl.
[3])

 

## Material Design

 

Im Jahr 2014 hat Google das Material Design vorgestellt. Auf den ersten Blick
ähnelt es stark dem Flat Design aufgrund seiner einfachen Darstellung.
Allerdings wird beim Material Design die Dreidimensionalität durch eine
z-Koordinate ergänzt. Jede Komponente hat die gleiche Dicke von 1dp (Pixel in
Abhängigkeit zur Bildschirmgröße). Es ist möglich, Komponenten übereinander
darzustellen, wodurch diese einen Schatten auf die unterliegende Ebene werfen.
Desweiteren können die Komponenten durch dp Angaben skaliert und verschoben
werden, was für eine bessere Darstellung auf verschiedenen Bildschirmgrößen
sorgt. Der Inhalt von Komponenten kann ebenfalls frei auf diesen Verschoben und
skaliert werden. Die Form der Komponenten kann sich während der Laufzeit ändern
was für neue Möglichkeiten des Designs sorgt. Google entwickelt das Material
Design stetig weiter und stellt bereits viele Komponenten zur Verfügung, welche
sich einfach in eigene Projekte einbauen und verändern lassen. Besonders
hervorzuheben sind die vielseitigen Animationen, welche im Material Design
eingesetzt werden können und somit, abgesehen von den im Flat Design
besprochenen, besonders das siebte Gesetz der Einfachheit ansprechen. (vgl. [5])

 

## Skeumorphismus vs Flat Design vs Material Design

 

Welches Design Konzept angewendet wird, ist weitesgehend geschmackssache.
Allerdings sollte der Designer bei der Wahl des Konzepts die Zielgruppe
beachten. Für Personen, welche sich nicht schnell an neue Technologien gewöhnen,
beziehungsweise diese verweigern, ist der Skeumorphismus eine gute Wahl, da in
diesem bekannte Dinge der realen Welt eingesetzt werden. Auch wenn die Anwendung
lediglich einen realen Gegenstand immitieren soll, ist es sinnvoll, den
Skeumorphismus anzuwenden, da der Nutzer bereits mit dem Umgang oder dem
Aussehen des Gegenstands vertraut ist.

Steht die Funktionalität oder die Einfachheit einer Anwendung hingegen im
Vordergrund, so ist das Flat Design oder das Material Design aufgrund der
einfacheren Designerstellung vorteilhaft. Auch abstrakte Dinge können mit diesen
Konzepten einfacher dargestellt werden. (vgl. [3])

Das Material Design wirkt zwar durch 3D-Ebenen und Animationen freundlicher als
das Flat Design, allerdings stellen diese Eigenschaften auch einen gewissen
Overhead dar. Bei Anwendungen, welche häufig genutzt werden, beispielsweise weil
der Beruf die Nutzung erfordert, kann dies auf Dauer eher negativ als positiv
wirken. Also sollten vor allem die Animationen mit Bedacht eingesetzt werden, da
sie gegen das dritte Gesetz der Einfachheit, die Zeit, sprechen.

 

## Dynamische Bildschirmgrößen

 

Häufig werden Anwendungen für verschiedene Plattformen oder Geräte zur Verfügung
gestellt. So ist eine Webanwendung beispielsweise auf einem Desktop-PC, einem
Tablet, einem Smartphne oder ähnlichem ansteuerbar. Hierbei ergibt sich das
Problem, das Komponenten der Anwendung entweder mit der Displaygröße skalieren
oder austauschbar sein müssen. Für diese Problemstellung gibt es mehrere
Ansätze, wovon einige im Folgenden beschrieben werden sollen. Diese arbeiten mit
Media Queries, welche die verschiedenen Viewportgrößen des Displays an die
Anwendung weitergeben. (vgl. [6])

 

### Adaptive Design

Beim Adaptive Design werden mehrere Layouts erstellt, welche für verschiedene
Bildschirmgrößen verwendet werden sollen. Meist wird ein Layout für ungefähr 19
Zoll und größer, 13 Zoll und größer und kleiner als 13 Zoll erstellt. Die
Layouts werden in CSS mit dem Zusatz der Bildschirmgrößen formuliert und
entsprechend der Viewportgröße des Endgeräts angezeigt. Das Adaptive Design ist
also an die Endgeräte ausgerichtet, von welchen die Anwendung genutzt wird.
(vgl. [6])

 

### Responsive Design

Beim Responsive Design werden die Komponenten so gestaltet, dass sie sich
dynamisch der vorhandenen Bildschirmgröße anpassen. Auch hier gibt es einige
Layoutvorgaben, welche bei bestimmten Viewportgrößen angewendet werden. Diese
beziehen sich allerdings meist auf eine Umstrukturierung des Layouts. Hierdurch
können Elemente versteckt, anders angeordnet oder sichtbar gemacht werden. (vgl.
[6])

Eine Navigationsleiste am linken Bildschirmrand wird bei großen Bildschirmen
beispielsweise meist mit einem Icon und einem beschreibenden Namen pro Element
versehen. Auf mittelgroßen Bildschirmen wird dann nur noch das entsprechende
Icon angezeigt. Auf einem Smartphone verbirgt sich die Navigationsleiste dann
oft hinter einem sogenannten Burger-Menü, welches ein Button ist, der durch
Anklicken die Navigationsleiste erscheinen lässt.

 

### Adaptive Design vs Responsive Design

Das Adaptive Design lässt sich schneller umsetzen, da es nur für eine bestimmte
Anzahl an Bildschirmgrößen getestet werden muss. Außerdem ähneln die Resultate
meist stärker den Mockups als beim Responsive Design, da hauptsächlich die Größe
der Elemente angepasst wird. Beim Responsive Design können verschiedene
Viewportgrößen zu unterschiedlichen Layouts führen, was den Nutzer verwirren
kann, allerdings ist beim Responsive Design eine gute Darstellung für alle
Viewportgrößen bis zu einem gewissen Maximum gegeben. Wenn jemand bei einer
adaptiv gestalteten Anwendung auf einem 17 Zoll Monitor eine Anwendung startet,
welche für 13 und 19 Zoll optimiert wurde, so gibt es viele Leerräume, welche
aufgrund der statischen Darstellung entstehen. Somit kann man sagen, dass der
Entwicklungsaufwand eines adaptiven Designs zwar deutlich geringer ist, jedoch
das Resultat eines Responsive Designs meist besser aussieht und zukunftssicherer
ist, was neue Bildschirmgrößen anbelangt. (vgl. [6])

 

## Pagination vs Infinite Scrolling

 

Muss in einer Anwendung eine Liste mit vielen Einträgen dargestellt werden, so
gibt es hierfür zwei Möglichkeiten mit Vor- und Nachteilen. Die bekannteste
Variante ist wohl eine Tabelle, welche eine gewisse Anzahl an Elementen auf
einer Seite darstellt. Durch einen Klick auf die nächste Seitenzahl werden neue
Elemente geladen und anstatt der bisher angezeigten, dargestellt. Dieses Prinzip
ist bei den meisten Onlineshops anzutreffen, da schnell durch die Elemente
navigiert werden kann. Wird eine Liste beispielsweise nach dem Preis sortiert
und man ist auf der Suche nach etwas aus dem mittleren Preissegment, so muss man
nur auf die mittlere Seitenzahl gehen und kann von dort aus weiternavigieren.

Auch beim Infinite Scrolling gibt es häufig die Möglichkeit Suchergebnisse zu
sortieren. Hier werden die einzelnen Elemente allerdings nicht auf mehreren
Seiten angezeigt, sondern durch das Runterscrollen automatisch nachgeladen.
Dieser Prozess wird “Lazy Loading” genannt. Ein Entwickler muss sich hierbei
allerdings die Frage stellen, wie viele Elemente pro Ladezyklus geladen werden
sollen und wann dieser Zyklus ausgelöst wird. Auf mobilen Endgeräten sollten
beispielsweise maximal 15 bis 30 Elemente geladen werden, da das Display kleiner
ist und das Datenaufkommen möglichst gering gehalten werden sollte. Teilweise
wird das Infinite Scrolling auch mit einem “Elemente Nachladen” Button versehen,
wodurch der Ladezyklus manuell ausgeführt werden muss. Dieser Ansatz ähnelt dann
bereits wieder der Paginierung, allerdings werden die neuen Elemente zusätzlich,
zu den bereits geladenen, angezeigt und nicht stattdessen.

Auch muss für das Infinite Scrolling eine Routine definiert werden, die bei der
anwendungsinternen Navigation dafür sorgt, dass nach der Detailansicht eines
Elements wieder die richtige Stelle der Liste präsentiert wird, damit der Nutzer
die Liste nicht ein weiteres Mal durchscrollen muss.

Somit kann man sagen, dass das Infinite Scrolling flüssiger abläuft, die
Pagination allerdings Vorteile beim Wiederfinden von Elementen hat. (vgl. [7])
