# Unterstützende Tools
## Virtualisierung vs. Containerisierung
## Build Server
*von Lukas Taake*

Build Server sind ein zentraler Bestandteil im Continuous Software
Engineering. Sie stellen einen zentralen Ort dar, an dem
der aktuelle Stand der Software, z.B. in Form von Testergebnissen
und kompilierten Artefakten, einsehbar ist.

Ein großer Vorteil ist, dass alle Prozesse innerhalb eines
Build Server vollautomatisch ablaufen und somit Fehler
durch falsche, ausgelassene oder vertauschte Prozess-Schritte
ausgeschlossen werden können.
Darüber hinaus stellt ein zentraler Build Server eine
isolierte Umgebung dar, sodass es nicht dazu kommen kann,
dass die Software aufgrund unterschiedlicher Konfiguration
auf einem Entwickler-Rechner funktioniert
(bzw. Tests erforlgreich sind) und auf einem anderen nicht.
Wenn also der Build-Server erfolgreich ist und ein
Entwickler-Rechner nicht, muss es sich um eine Fehlkonfiguration
des Entwicklers handeln, da die des Build-Servers im Optimalfall
möglichst nah an der eines Produktivsystems liegt.

Über das Kompilieren und Testen hinaus werden Build-Server auch
zur Durchführung von Continuous Delivery und Deployment
verwendet. Oftmals existieren bereits Build-Server-Plugins
zur Unterstützung verbreiteter Deployment-Ziele.

Die konkrete Funktionsweise soll Beispielhaft am Beispiel von
Jenkins und Travis CI dartestellt werden, wobei Jenkins
ein Open Source Projekt ist und weitreichende
Konfigurationsmöglichkeiten bietet, während es sich bei Travis
um eine SaaS handelt.

### Jenkins
Jenkins ist eins der populärsten CI-Tools, vor allem im
Java-Umfeld. Üblicherweise wird es selbst gehostet und ist
tiefgreifend konfigurierbar.
Es unterstützt verschiedene Build-Tools, wie
Ant, Maven, Gradle oder MSBuild, außerdem Versionskontrollsysteme,
wie Git, Mercurial oder SVN.
Darüber hinaus gibt es eine Vielzahl an Plugin, über die
es um neue Funktionaliät erweitert werden kann.

Gewöhnliche Build-Jobs können zwar aus mehreren
auszuführenden Schriten bestehen, liefern als Ergebnis allerdings
nur das Gesamtergebnis (und evtl. einen Test-Report) zurück.
Im Gegensatz dazu können Pipeline-Jobs 

### Travis CI


## Docker
### Dockhub
