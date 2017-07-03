# 2. Unterschiede zwischen Web-Apps, Native Apps und Hybride Apps

## 2.1 Web-Apps
Web-Apps werden mit JavaScript, HTML und CSS entwickelt. Web-Apps laufen im Browser, da Web-Apps Mobile/Responsive Seiten sind. Sie passen sich jeder Größe genau an und sind plattformunabhängig, da jedes Smartphone einen eigenen Browser mit sich bringt. Sie können aber nicht im App Store veröffentlich werden und unterstützen keine nativen Gerätefunktionen wie z.B. die Benutzung der Kamera oder das Auslesen der Kontakte. [1]

## 2.2	Native Apps
Native Apps werden mit plattformabhängigen Programmiersprachen wie Java für Android, Objective-C für IOS usw. entwickelt. Dadurch können die Apps im App Store der jeweiligen Plattform angeboten und heruntergeladen werden. Native Apps unterstützen die nativen Gerätefunktionen z.B. die Benutzung der Kamera im Vergleich zu Web-Apps. Sie sind aber nicht plattformunabhängig wie Web-Apps, da Sie für jede Plattform (Android, IOS usw.) neu entwickelt werden. Denn jede Plattform hat ihre eigene Programmiersprache. Die Wartung ist hoch, denn jede einzelne App muss getestet und gewartet werden und Updates müssen einzeln angepasst werden. Es gibt viele verschiedene Geräte z.B. Smartphones und Tablets für die auch einzelnen Apps realisiert werden. [2]

## 2.3 Hybride Apps
Hybride Apps kombinieren die Vorteile beider vorherigen App Varianten in einer. Hybride Apps werden genau wie Web-Apps mit JavaScript, HTML und CSS entwickelt. Sie können aber im App Store veröffentlicht und heruntergeladen werden wie Native Apps. Sie laufen in einem spezifischen Browser der jeweiligen Plattform, unterstützen aber auch native Gerätefunktionen der gewählten Plattform. Sie haben nicht so eine gute Performanz wie Native Apps, bei Spielen kann es daher zu Leistungseinbrüchen kommen, da empfiehlt sich lieber native Apps zu entwickeln. Ein großer Vorteil von hybriden Apps ist, wenn sie einmal entwickelt und getestet wurden, können Sie für jede Plattform erstellt werden. Man spart sich die Zeit mehrere Apps für jedes System einzeln zu entwickeln. Dadurch ist die App leichter zu warten und auch Updates können besser eingespielt werden, da sie auf einer App basieren. [3]

Die folgende Tabelle zeigt die Unterschiede für die einzelnen App-Varianten im Vergleich zu den anderen.

| App-Varianten | Web-Apps | Native Apps | Hybride Apps |
| ------ | ------ | ------ | ------ |
| Performanz der App | Sehr gut | Sehr gut | Beim Start dauert es, da die App erst geladen werden muss. |
| Plattformabhängigkeit | Nein | Ja | Ja |
| App-Store Veröffentlichung | Kann nicht im App-Store veröffentlicht werden. | Kann im App-Store veröffentlicht werden. | Kann im App-Store veröffentlicht werden. |
| Unterstützt Gerätefunktionen | Es werden nur einige Gerätefunktionen mit der Nutzung von Web-APIs unterstützt. | Es werden alle Gerätefunktionen unterstützt. | Es werden alle Gerätefunktionen unterstützt, durch eigene und externe Plug-Ins. |

In der Tabelle sieht man in der Spalte für hybride Apps, dass es nur Leistungseinbrüche bei der Performanz der App gibt. Das merkt man aber auch beim direkt Start einer hybriden App sehr genau.

Hier sieht man eine Grafik, welche die internen Abläufe zeigen. Man sieht, dass eine Native App und eine Web-App sich darin unterscheiden, dass die Web-App in einem Browser ausgeführt wird. Der Browser wird vom Betriebssystem aufgerufen. Das ist auch der Grund, dass man keine Gerätefunktionen bei Web-Apps verwenden kann, da der Browser vom System abgekapselt ist. Wäre das nicht der Fall, dann könnte man mit einer einfachen Webseite auf alle Informationen eines PCs zugreifen und manipulieren. Das hat Sicherheitsgründe. Für einen Angreifer wäre das ein leichtes Spiel sich alle Kontakte und sonstige Informationen von einem Smartphone zu beschaffen. Bei nativen Apps ist das möglich Gerätefunktionen zu nutzen, da native Apps auf dem Betriebssystem installiert werden. Sie greifen direkt auf die System internen Prozesse und Daten zu. Eine hybride App muss beides kombinieren, dazu wird ein Browser simuliert, welches auf dem Betriebssystem installiert wird. Dieser spezifische Browser besteht aus einer Web View zum Anzeigen des HTML-Codes und einer nativen Schnittstelle. Die native Schnittstelle erlaubt native Zugriffe auf die Gerätefunktionen und stellt die native UI zur Verfügung, damit die hybride App wie eine native App aussieht.

![Abbildung 1: Der interne Ablauf einer App.](/assets/hybrid-native-web.png)

Abbildung 1: Der interne Ablauf einer App. [8]
