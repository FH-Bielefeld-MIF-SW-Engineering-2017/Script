# Entwurfsmuster

Entwurfsmuster beschreiben einen abstrakten Lösungsansatz für Problemstellungen in der Softwarearchitektur und -entwicklung, der für ein individuelles Problem entsprechend wiederverwendet werden kann.

### Model-View-Controller

Das MVC Muster beschreibt die Trennung einer Software-Architektur in drei Komponenten. Das Datenmodell \(Model\), die Präsentation \(View\) und die Programmsteuerung / Logik \(Controller\)._ \(Lahres 2006\)_

![](/assets/diagram-mvc-480x241.png)

_Abbildung 1: MVC \(Peres 2016\)_

#### Model

Das Model enthält die darzustellenden Daten und ist von den anderen beiden Schichten unabhängig. Das Model publisht entsprechende Änderungen an seinen Daten, welche von den lauschenden Komponenten registriert werden. Dies geschieht nach dem sogenannten Beobachter-Muster.

#### View

Die View Komponente subscribed auf die Daten des Models und updated seine Sichten entsprechend der Daten, sollten sie geändert werden. Mit der View Komponente werden die Benutzerinteraktion realisiert. Diese kennt ebenfalls den Controller, ist jedoch nicht für die Weiterverarbeitung der Daten zuständig.

#### Controller

Der Controller enthält in der Regel die Geschäftslogik \(diese kann auch direkt im Model liegen, je nach Programmiersprache und Implementierung des MVC\) und kann mehrere Views verwalten, wobei zu jeder View eine Steuerung existiert. Der Controller sorgt dafür, dass die Benutzerinteraktionen in der View ihre entsprechende Wirkung haben, verändert gegebenenfalls die View und gibt z.B. eingegebene Daten aus der View weiter an das Model.

### Model-View-Presenter

Das MVP-Muster ist aus dem MVC-Muster heraus entstanden und setzt auf einen neuen Ansatz, um das Model komplett von der View zu trennen und über einen sogenannten Presenter zu verbinden. Dies soll eine bessere Testbarkeit als auch eine bessere Übersicht bei der Implementierung zur Folge haben. _\(Fowler 2006a\)_

![](/assets/diagram_2.png)_Abbildung 2: MVP \(Ziomacki 2016\)_

#### Model

Das Modell stellt die Logik der Ansicht bzw. die Geschäftslogik dar und kennt dabei weder die View noch den Presenter. Es muss  jedoch alle Funktionalitäten implementiert haben um die View betreiben zu können. Die Steuerung des Models erfolgt durch den Presenter.

#### View

Die View kennt ebenfalls weder das Model noch den Presenter und ist nur für die Ein- und Ausgabe von Daten zuständig, sowie die allgemeine Darstellung der Software. Die Steuerung der View erfolgt durch den Presenter.

#### Presenter

Der Presenter ist das Bindeglied zwischen View und Model, welche jeweils ihre Schnittstellen definieren, die anschließend vom Presenter miteinander verknüpft werden. Die Schnittstellen beschreiben dabei den genauen Aufbau der anderen zwei Komponenten. Dies resultiert in einer vollkommenden Austauschbarkeit von View und Model.

#### Supervising Controller

In einer Abwandlung des MVP-Musters kann die View zusätzlich für die Datensynchronisation zuständig sein, wodurch der Presenter sich lediglich um alle anderen Abläufe zwischen Model und View kümmert. Der Presenter kann zum data-binding hierbei Klassen zur Verfügung stellen, die View als auch Model bekannt sind, wodurch weiterer Synchronisationsaufwand entfällt und bei veränderten Daten die View direkt ihre Sicht aktualisiert. _\(Fowler 2006b\)_

### Model-View-ViewModel

Das MVVM-Muster ist eine weitere abgewandelte Variante des MVC. Es ist eine Spezialisierung des MVP-Musters und kommt ebenfalls ohne Controller aus, da auch hier Zustand und Verhalten die Presenter bzw. ViewModel Komponenten regeln. Die Testbarkeit wird verbessert und die Arbeitsteilung zwischen UI-Designer und Programmierern gefördert, wodurch separate Teams gleichzeitig an einer Software entwickeln können. _\(Kühnel 2013\)_

![](/assets/ViewModel_thumb.png)

Abbildung 3: MVVM \[Hill2009\]

#### Model

Das Model hält die komplette Geschäftslogik sowie die dem Nutzer präsentierten Daten inne, welche nach Manipulation des Nutzers aktualisiert und validiert werden können.

#### View

Die View enthält alle Elemente zur Präsentation von Software und Daten. Sie bindet sich an Funktionen und Objekte des ViewModel um Daten darzustellen und Interaktionen der Nutzer weiterzugeben.

#### ViewModel

Das ViewModel dient als Bindeglied zwischen View und Model, wobei das ViewModel die View nicht kennt. Es stellt der View öffentliche Methoden und Eigenschaften zur Verfügung, über die die View Daten holen kann und Ereignisse in der View weiter an das ViewModel gibt. Das ViewModel wiederum ruft Methoden und Elemente des Models aus um Informationen auszutauschen.

### Flux

Flux ist eine Architektur die erstmals 2013 von Facebook in Zusammenhang mit react.js vorgestellt wurde. Bei react bestehen Komponenten aus HTML, JavaScript Code als auch CSS und es herrscht somit keine Trennung von View und Model, wie man es aus den vorherigen Mustern kennt._ \(Deutsch 2015\)_

![](/assets/flux-simple-f8-diagram-with-client-action-1300w.png)_Abbildung 4: Flux \(Zeigermann 2015\)_

#### Action

Eine Action ist ein normales JavaScript Objekt, welches aus seinem Payload \(beliebig viele Attribute / Daten\) sowie dem festen Attribut "type" besteht, welches in der Regel ein konstanter String ist. Über das type-Attribut können die Stores erkennen, ob es sich um eine für sie relevante Aktion handelt.

Sogenannte ActionCreators werden aus den Views \(React Komponenten\) heraus aufgerufen, um eine Action zu erstellen und diese zum Dispatchter weiter zu reichen, welches sie den jeweiligen Stores zuordnet. Die Views wiederum sind mit den Stores verbunden und werden bei Veränderungen der Daten im Store durch Actions neu gerendert.

#### Dispatcher

Der Dispatcher ordnet lediglich die Action Objekte einem Store zu, dabei behandelt er immer nur ein Objekt gleichzeitig.

#### Store

In Stores werden die Logik einer Applikation verwaltet und fungieren als Datenquellen für die Komponenten. Sie empfangen Actions, welche die Daten der Stores verändern können, woraufhin ein Store seine React Komponenten benachrichtigt.

#### View

Die React Komponenten subscriben auf ihre Stores und rendern sich bei Veränderungen gegebenenfalls neu. Es wird zwischen einfachen und smarten Komponenten unterschieden.

Einfache Komponenten sind abstrakter und leichter wieder zu verwenden, erhalten ihre Daten und selbst ausgelöste Actions als Properties.

Smarte Komponenten wiederum haben Funktionen um auf Stores zu subscriben und Actions zu dispatchen.

Da der Datenfluss von den Views über Actions und Dispatcher zu den Stores verläuft, spricht man auch von einem **Single-Directional-Dataflow**.

