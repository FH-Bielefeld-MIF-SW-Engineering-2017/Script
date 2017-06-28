Grundlagen
==========

 

Bei der Erstellung eines Design-Konzepts werden oft grundlegende Dinge
vergessen, da versucht wird ein für sich persönlich ansprechendes Design zu
erstellen. Allerdings ist die eigentliche Zielgruppe meist eine andere. Außerdem
werden häufig Gadgets eingebaut, welche zwar einen gewissen Nutzen erfüllen,
aber für die Anforderungen der Anwendung nicht notwendig sind.

 

10 Gesetze der Einfachheit
--------------------------

 

Bereits 2006 machte sich John Maeda Gedanken über Designentscheidungen. Damit
eine Anwendung verständlich ist, muss sie einfach gehalten sein. Das Wort
“einfach” wird hierbei durch 10 Gesetze definiert, welche auch heute noch auf
die Entwicklung von Design-Konzepten zutreffen. Die letzten Gesetze werden hier
nicht betrachtet, da sie keinen direkten Einfluss auf das Design einer Anwendung
haben, beziehungsweise die vorigen Gesetze zusammenfassen. (vgl. [1] S.1-82)

 

### 1. Reduzieren

Durch das gezielte Weglassen von Komponenten wird die Anwendung übersichtlicher.
Es sollten nur Komponenten verwendet werden, welche aufgrund der Anforderungen
unumgänglich sind. Natürlich sollten Komponenten, welche die Nutzung der
Software vereinfachen dennoch beibehalten werden. Ein Beispiel wäre die Nutzung
eines Datepickers mit Eingabefeld, anstatt eines einfachen Eingabefelds um Daten
abzufragen.

 

### 2. Organisieren

Durch eine gezielte Anordnung von zusammengehörigen Komponenten erscheint das
Gesamtbild übersichtlicher.

In einem Eingabeformular werden hierfür alle, eine Adresse betreffenden,
Eingabefelder beieinander dargestellt.

 

### 3. Zeit

Eine Anwendung sollte für den Nutzer zielführend gestaltet sein. Ein einfaches
Beispiel ist die Startseite, wie sie Anfang der 2000er Jahre genutzt wurde.
Diese beinhaltete oft nur den Namen der Seite und einen Link zur eigentlichen
Hauptseite. Unnötige Klicks verbunden mit erneuter Ladezeit fühlen sich für den
Nutzer komplex an.

Sind Wartezeiten unumgänglich aufgrund von Hintergrundberechnungen einer
Anwendung oder ähnlichem, so sollte die Wartezeit durch eine Fortschrittsleiste
oder ähnliches angezeigt oder anders überbrückt werden.

 

### 4. Lernen

Die Anwendung sollte nach Möglichkeit einfach zu handhaben sein. Dies kann
dadurch erzielt werden, dass Komponenten genutzt werden, welche die Nutzer
bereits von anderen ähnlichen Anwendungen kennen. Das Rad sollte nicht neu
erfunden, sondern wiederverwendet werden, damit der Nutzer keine Zeit
verschwendet, in welcher er sich die neuen Technologien aneignen muss. Dieses
Argument steht außerdem im Zusammenhang mit dem 3. Gesetz der Einfachheit. Wenn
eine neue Technologie verwendet wird, die der Nutzer höchstwahrscheinlich nicht
kennt, so sollten Hilfestellungen zur Nutzung gegeben werden. Das Lesen der
Anleitung ist meist weniger zeitintensiv als das Lernen durch ausprobieren.

 

### 5. Unterschiede

Es ist nicht möglich nur einfache Anwendungen zu haben. Es könnte nur der
Maßstab für die Einfachheit niedriger gesetzt werden und das was zuerst simpel
erschien, ist nun komplex. Somit ist es nicht falsch auch komplexe Konstrukte zu
verwenden, solange die gesamte Anwendung einfach wirkt.

Außerdem sollte versucht werden Unterschiede zu anderen Anwendungen
hervorzuheben, um Nutzer von der eigenen Software zu überzeugen. Durch Kontraste
lernt der Nutzer manche Dinge zu schätzen, welche er sonst als
selbstverständlich ansehen würde.

 

### 6. Kontext

Nicht alle Komponenten einer Darstellung erhalten gleich viel Aufmerksamkeit vom
Nutzer. Dies liegt zum Teil an der Platzierung und die Gestaltung dieser.
Zentrierte und gestalterisch auffällige Komponenten erhalten eher Beachtung.
Dieser Effekt kann zwar erwünscht sein, jedoch können Komponenten hierdurch auch
übersehen werden, was einen negativen Effekt hat.

 

### 7. Emotionen

Zwar sollte eine Anwendung einfach gestaltet sein, jedoch sollte sie nicht kalt
auf den Nutzer wirken. Dieser Punkt ist extrem abhängig von der Zielgruppe,
welche womöglich ein sehr modernes, einfaches und flaches Design bevorzugt oder
aber viele Verzierungen erwartet.

 

### 8. Vertrauen

Dieser Punkt ist sehr eng mit dem 4. Gesetz verwoben. Sobald ein Nutzer weiß,
wie man mit einer Komponente umgeht, vertraut dieser darauf, dass diese ihn
immer zu dem gewünschten Ergebnis führt. Der Anwender kann die Software ohne
groß nachdenken zu müssen nutzen. Wird die Komponente jetzt verändert oder
ausgetauscht, muss der Nutzer sich den Ablauf neu aneignen. Dies sollte wenn
möglich umgangen werden.

###  

 

Zielgruppe erkennen
-------------------

 

Bereits bevor mit dem Design-Konzept begonnen wird, sollte die Zielgruppe einer
Anwendung feststehen. Von der Zielgruppe hängen viele Gestaltungsmerkmale ab.
Ältere Personen lernen neue Technologien in der Regel langsamer kennen und
weigern sich eher eine neue Technologie zu nutzen. Aus diesem Grund sollte hier
auf den Skeumorphismus (siehe [Konzepte und
Design-Ansätze](konzepte_und_design-ansätze.md)) zurückgegriffen werden.

Auch auf Gesetze in bestimmten Ländern oder auf religiöse Beschränkungen der
Zielgruppe muss geachtet werden. Desweiteren ist die Sprache und die Bedeutung
von Symbolen in anderen Ländern zu beachten.

Abgesehen von der Zielgruppe müssen allerdings auch alle weiteren Personen
betrachtet werden, welche die Anwendung nutzen könnten. Hier muss die Frage
gestellt werden, ob eine Anpassung des Designs aufgrund dieser einfach
umzusetzen, beziehungsweise ob sie überhaupt nötig ist.

 

Barrierefreiheit
----------------

 

Der Zugang zu Informations- und Kommunikations-Technologien gilt als
Menschenrecht. Dies ist einer der Gründe, aus welchem eine Anwendung
barrierefrei, also auch nutzbar für Personen mit körperlichen oder geistigen
Behinderungen, sein sollte. Häufig unterstützen die Ansätze für eine
barrierefreie Anwendung auch die Nutzbarkeit durch ältere oder technologisch
eingeschränkte (niedrige Bandbreite) Anwender. Somit kann die Zielgruppe schnell
erweitert werden. Im Folgenden ist eine Auflistung von Möglichkeiten, eine
(Web-)Anwendung barrierefrei zu machen.

 

| Behinderung                                 | Maßnahme                                                                                                                                  |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Schlechtes Sehvermögen, niedrige Bandbreite | Bereitstellung eines Alternativtexts (alt Atrribut in einem HTML-img Tag) für Bilder, welcher auch von Screenreadern erkannt werden kann. |
| eingeschränkte Farbwahrnehmung              | Anbieten alternativer Styles. Nutzung von kontrastreichen Farben.                                                                         |
| eingeschränkte Feinmotorik der Hände        | Steuerung einer Anwendung komplett durch die Tastatur ermöglichen (Tastatur kann durch Sprachsteuerung immitiert werden).                 |
| eingeschränktes Hörvermögen                 | Abschriften von Audiodateien zur Verfügung stellen                                                                                        |

(vgl. [2])
