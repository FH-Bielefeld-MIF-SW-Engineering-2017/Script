# 4. Ionic

## 4.1 Allgemein
Ionic ist ein Frontend-Framework für das Erstellen von hybriden Apps. Ionic legt einen besonderen Wert auf eine Native UI, sodass die UI-Elemente ein natives Aussehen haben.  Für die Architektur von Ionic wird Angular 2 verwendet. Die hybride App wird mit PhoneGap/Cordova aufgerufen, dadurch können die nativen Gerätefunktionen benutzt werden, um zum Beispiel die Kamera zu benutzen. [6] [7]

## 4.2 Komponenten
Für die Erstellung der hybriden Apps benutzt Ionic verschiedene Frameworks als Komponenten.

### 4.2.1 SASS
SASS wird zur Erzeugung von Cascading Style Sheets genutzt, da SASS eine Stylesheet-Sprache ist. SASS generiert CSS mit einem Präprozessor. Der Vorteil von SASS gegenüber CSS ist, dass der Entwickler auf Vererbung, Variablen usw. verwenden kann, wie bei einer Programmiersprache. Wenn man SASS kompiliert, dann erhält der Entwickler am Ende den CSS Code. Ionic verwendet SASS, um das Design der App festzulegen. Das Design kann über SASS Variablen verändert werden und der Entwickler kann eigene hinzufügen. Es existiert für Android, IOs und andere eigene Variablen, um für jedes Betriebssystem ein individuelles Design festzulegen. [7]

### 4.2.2 Apache Cordova/PhoneGap
Ionic benutzt zum Anzeigen und installieren der App das Framework PhoneGap/Cordova. Das Framework PhoneGap/Cordova  stellt eine API bereit. Mit dieser API kann man auf die Gerätefunktionen zugreifen. PhoneGap/Cordova wird weiter oben genauer beschrieben. [7]

### 4.2.3 AngularJS und Angular 2
AngularJS und Angular 2 sind ein JavaScript-Framework. AngularJs wird in Ionic 1 verwendet und ab Ionic 2 wird nur noch Angular 2 verwendet. Die Programmlogik wird in Ionic mit Angular umgesetzt, da Ionic auf Angular basiert. Durch die Verwendung von Angular  hat Ionic eine MVC-Architektur. Mit Angular lassen sich Single-Page-Applikationen entwickeln. Angular benutzt für die Funktionalität Direktiven und diese können in der View verwendet werden. [7]

### 4.2.4 Node.js
Node.js ermöglicht es JavaScript serverseitig zu verwenden und Node.js stellt einen eigenen Anwendungsserver. Andere Anwendungen können auf diesen Server zugreifen. So kann Node.js als Schnittstelle zwischen der Datenbank und einer Single-Page-Applikation genutzt werden. Ein Vorteil von Node.js ist, dass seine Architektur ressourcensparend ist und man sie ständig mit neuen Modulen erweitern kann. Damit man Ionic benutzen kann muss man Node.js installieren, da Ionic über den Browser auf Node.js zugreift. [7]

In der folgenden Abbildung 3 werden die einzelnen Komponenten und deren Beziehungen untereinander dargestellt. Man sieht, dass für die Hardware also die Gerätefunktionen PhoneGap/Cordova verwendet wird. PhoneGap/Cordova stellt die Schnittstelle zu der Hardware her. Für die Architektur wird Angular 2 bzw. AngularJS verwendet. Angular stellt auch die Schnittstelle zwischen der Ionic-UI Komponenten und PhoneGap/Cordova da. Die Ionic-UI Komponeten werden mit SASS gestaltet und verwenden HTML5 und CSS3. Über Service und Direktiven kann auf die einzelnen Elemente zugegriffen werden.

![Abbildung 3: Allgemeine Architektur von Ionic.](/assets/ionic-app-entwicklung.jpg)

Abbildung 3: Allgemeine Architektur von Ionic. [10]
