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
Im Gegensatz dazu gibt es auch Pipeline-Jobs,
bei denen ein Job explizit in mehrere Stufen (Stages) unterteilt wird
(z.B. Compile, Unit Test, Integration Test).
Dann wird der Status jeder einzelnen Stufe ausgegeben,
wenn also ein Integrationstest fehlschlägt, ist das sofort
ersichtlich (vgl. Abbildung).

![Jenkins Pipeline View](https://wiki.jenkins.io/download/attachments/102662163/who-broke-it.png?version=1&modificationDate=1478695629000&api=v2)
Abbildung: Übersicht der Build-Historie mit einzelnen Stages. Quelle:
[Jenkins Wiki, Pipeline Stage View Plugin](https://wiki.jenkins.io/display/JENKINS/Pipeline+Stage+View+Plugin)

In komplexen Setups, oder wenn viele Projekte zentral
verwaltet werden, ist es möglich, einzelne Build-Jobs auf Slave-Knoten
zu verteilen. In Pipeline-Jobs ist es sogar möglich, verschiedene Stages
auf verschiedenen Slaves ausführen zu lassen, um die Geschwindigkeit
zu steigern.

### Travis CI
Travis CI verfolgt einen anderen Ansatz als Jenkins,
indem es ausschließlich als Software as a Service angeboten wird
und als Versionskontrollsystem ausschließlich Github-Repositories
akzeptiert. Dafür ist als Ausgleich zur dieser Einschränkung
die Integration zu Github sehr komfortabel.
So können Build Jobs für neue Repositories mit einem Maus-Klick
erstellt werden und die Konfiguration geschieht über eine
YAML-Datei (siehe Listing).

```
language: java

jdk: oraclejdk8

services:
 - mysql

before_install:
 - mysql -e 'CREATE DATABASE newsboard'
 - mysql newsboard < src/main/resources/sql/create_script.sql
 - mysql newsboard < src/main/resources/sql/example_data.sql

install: mvn install -DskipTests=true -Dmaven.javadoc.skip=true
script: mvn verify -Dspring.profiles.active=travis 
```
Listing: Beispielhafte Travis CI Build Definition

Jede Ausführung eines Build-Jobs geschieht auf einer neu erstellten
virtuellen Maschine um absolute Isolation sicherzustellen.
Über die Angabe der Programmiersprache in der Konfiguration
wird bestimmt, wie die Maschine vorkonfiguriert ist.
Darüber hinaus können mit `services` auch Abhängigkeiten, z.B.
Datenbanken, installiert werden und mit `before_install`
initialisiert werden.
Mit `install` und `script` werden die Befehle zum Kompilieren
und Ausführen der Tests angegeben.

Auf den ersten Blick ähnlich dem Konzept der Pipeline bei Jenkins
sind die Build Stages. 

## Docker
### Dockhub
