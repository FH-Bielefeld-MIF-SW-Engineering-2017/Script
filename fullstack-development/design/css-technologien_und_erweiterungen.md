CSS-Technologien und Erweiterungen
==================================

 

Mit Cascading Stylesheets kann unter anderem das Aussehen von HTML-Elementen
bestimmt werden. Auch die Anordnung von Elementen innerhalb anderer Elemente
wird hierdurch gesteuert. CSS ist eine sehr leichtgewichtige Technologie, die
durch andere Ansätze erweitert wurde. Dies soll im Folgenden näher beleuchtet
werden.

 

CSS Grid
--------

 

CSS Grid bietet die Möglichkeit (HTML-)Elemente innerhalb eines anderen
(HTML-)Elements in einem zweidimensionalen System anzuordnen. Das umschließende
Element wird durch das Setzen eines Attributes zum Grid. Hier wird auch die
Spalten- und Zeilenanzahl definiert. Die einzelnen Elemente innerhalb des Grids
können durch Angabe der Zeile und Spalte innerhalb des CSS positioniert werden.
Die einzelnen Zellen, Zeilen und Spalten können ebenfalls durch CSS bearbeitet
werden, wodurch viele Möglichkeiten der Darstellung entstehen. Ein Element muss
nicht zwingend nur in einer Zelle dargestellt werden, sondern kann durch Angabe
von Endzeile und Spalte auch über einen größeren Bereich gehen. Es ist ebenfalls
möglich eine Zelle aufzuteilen, indem das beinhaltete Element zu einem Sub-Grid
wird.

Die Möglichkeiten der Darstellungsanpassung mit dem CSS Grid sind enorm und
können vorallem im Zusammenhang mit Media Queries gut für responsive Anwendungen
verwendet werden, da das Grid hierbei komplett umgestaltet werden kann. (vgl.
[8])

 

Flexbox
-------

 

Die Flexbox stellt im Gegensatz zum CSS Grid einen eindimensionalen Container
dar. Es werden hier ebenfalls Elemente innerhalb eines anderen Elements
dargestellt. Die Anordnung der inneren Elemente kann vertikal oder horizontal
sein, wobei die Reihenfolge der Elemente gespiegelt werden kann. Der große
Vorteil der Flexbox ist, dass die Größen der Komponenten sehr viel dynamischer
als die des CSS Grids dargestellt werden können. Beispielsweise kann der, durch
den Container zur Verfügung gestellte, Platz gleichmäßig unter allen inneren
Elementen aufgeteilt oder aber einem einzelnen Element gutgeschrieben werden.
Die Anordnung der einzelnen Elemente kann sehr dynamisch gestaltet werden und
auch hier ergibt sich die Möglichkeit, durch Media Queries die Reihenfolge der
Elemente zu ändern oder andere Anpassungen vorzunehmen. Allerdings ist dies oft
nicht nötig, da sich der Inhalt der Flexbox flexibel an die vorgegebene
Containergröße anpasst. (vgl. [9])

 

Erweiterungen
-------------

 

Es gibt viele Erweiterungen von CSS, wobei der angefertigte Code durch einen
Compiler in CSS umgewandelt wird. Durch dieses Compiling können Entwickler
einiges an Zeit und Code sparen, da viele Grundprinzipien von einfachen
Programmiersprachen, wie das Anlegen von Variablen, benutzt werden können. Somit
muss der Entwickler die Hauptfarbe einer Anwendung nicht in jeder einzelnen
CSS-Klasse aktualisieren, sondern kann die Änderung an einer zentralen Stelle
durchführen.

Es gibt sehr viele dieser Tools, welche sich hauptsächlich in der Syntax
unterscheiden. Außerdem wird bei der Nutzung mancher Frameworks eine bestimmte
CSS Erweiterung vorausgesetzt, wodurch der Entwickler gezwungen ist, die Syntax
zu lernen.

SCSS (Sassy CSS) nutzt die gleiche Formatierung wie CSS, wodurch es einfach zu
lernen ist. Die bekannteren Erweiterungen SASS (Syntactically Awesome
Stylesheets) und Less haben hingegen andere Formatierungen. (vgl. [10])

 

Alle Erweiterungen haben gemeinsam, dass sie die Stylesheets wiederverwendbarer
machen. Zum einen können Variablen genutzt werden, welche alle gültigen
Attributwerte wie Farben oder Zahlen speichern und verwalten. Außerdem können
CSS-Klassen ineinander verschachtelt werden, wodurch die Regeln für die innere
Klasse nur auf Elemente angewendet werden, welche in der (HTML-)Struktur
innerhalb der äußeren Klasse liegen.

Mixins in den Erweiterungen können mit Funktionen aus Programmiersprachen
verglichen werden. Sie können Parametrisiert sein und dementsprechend CSS-Werte
einsetzen. Diese Mixins können dann in Klassen inkludiert werden. Auch die
Vererbung von Attributen einer Klasse an eine andere ist möglich. (vgl. [11])

 

Die Nutzung der Erweiterungen erfüllt meist eher die Anforderungen eines
Entwicklers, da dieser die gegebenen Unterstützungen von Programmiersprachen
kennt. Außerdem ist die Wartbarkeit deutlich besser als bei der Nutzung von
reinem CSS.
