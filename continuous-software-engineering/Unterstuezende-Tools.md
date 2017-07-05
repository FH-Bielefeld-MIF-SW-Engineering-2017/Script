# Unterstützende Tools

Die in den vorangegangenen Kapiteln beschriebenen agilen Vorgehensmodelle und deren Workflows für die Entwicklung komplexer Softwareprodukte benötigen für die Sicherstellung der Softwarequalität kontinuierliche Tests. Dedizierte Server führen die Prozessschritte der vorgestellten Workflows (Continuous Integration, Deployment und Delivery) in sogenannten Pipelines durch. Dazu gehören neben den Modul- und Integrationstests, die der Entwickler auch in seiner lokalen Entwicklungsumgebung durchführen kann, umfangreichere Systemtests bzw. Ende-zu-Ende-Tests. Diese Systemtests benötigen definierte Produktivumgebungen, die sich mit Virtualisierungstechnologien oder neuerdings auch Containerisierungs-Technologien etablieren lassen.

## Virtualisierung versus Containerisierung
Bis Anfang der 2010er fand fast ausschließlich die Virtualisierung von Betriebssystemen auf Personal Computern und Servern Anwendung; so auch im Kontext der CI- und CD-Workflows. In den letzten Jahren gewinnt die Technologie der Containerisierung immer mehr an Bedeutung und hat das Potenzial Virtualisierungslösungen teilweise abzulösen. In diesem Kapitel wird zuerst der Bedarf zur Virtualisierung im Kontext von Continuous Software Engineering hergeleitet. Danach wird die jeweilige Funktionsweise der konkurrierenden Technologien grundlegend erklärt, um sie daraufhin vergleichend gegenüberzustellen. Abschließend kommt ein Überblick über etablierte Frameworks. 

### Bedarf zur Virtualisierung
Im Kapitel zu unterstützenden Workflows wurde der Bedarf von Tests auf allen Integrationsebenen einer Software zur Qualitätssicherung hergeleitet. Bei diesen Tests stehen am Ende die Systemstests, die eine Produktivumgebung für die Applikation voraussetzen. Eine solche Umgegbung kann auf dem Hauptbetriebssystem eines Servers konfiguriert werden. Dieses Vorgehen beansprucht einen Server in der Regel nur wenig, da eine Applikation typischerweise ein System nicht voll auslastet. Er ergibt sich somit ein hohes Maß an ungenutzten Ressourcen, was sich negativ auf die Wirtschaftlichkeit solcher Server auswirkt.

Das Konzept der Virtualisierung bietet an dieser Stelle die Möglichkeit die Ressourcen eines Servers deutlich besser auszunutzen, indem entsprechend der Leistungsfähigkeit eines Servers mehrere virtuelle Systeminstanzen erzeugt und parallel ausgeführt werden. Ein weiterer Vorteil der Virtualsierung ergibt sich, wenn eine Applikation auf verschiedenen Betriebssystemen lauffähig sein soll. Dazu kann für alle zu unterstützenden Betriebssysteme eine separate virtuelle Produktivumgebung bereitgestellt werden. Für verschiedene und parallele Tests genau einer Produktivumgebung kann zudem ein virtuelles Systemabbild beliebig vervielfacht und betrieben werden.

### Arten der Virtualisierung
Eine triviale und einfache Form, eine relativ isolierte Umgebung zu schaffen, ist das Partitionieren eines Systems. Diese Vorgehen ermöglicht aber kein wirklich paralleles Ausführen von Applikationen, da es stets zu Kollisionen bei der Verwendung von Hardware-Ressourcen kommen kann.

Tatsächlich brauchbare Möglichkeiten sind die vollständige Virtualisierung, die Paravirtualisierung und die Hardware-Virtualisierung. Wird in der Literatur von Virtualisierung gesprochen ist typischerweise implizit die vollständige Virtualisierung gemeint, da diese Variante meist zur Anwendung kommt. Es beschreibt die Bereitstellung, respektive Simulation eines gesamten Betriebssystems mit Zugriff auf alle Hardware-Ressourcen. Auf die anderen beiden Varianten soll nicht weiter eingegangen werden, da sie aufgrund von bestimmten Nachteilen gegenüber der vollständigen Virtualisierung in der Praxis kaum Anwednungsfälle haben.

### Virtuelle Maschinen
Das Konzept der virtuellen Maschine ist die geläufige Technologie, um virtuelle Umgebungen auf einem Hardwaresystem zu betreiben. Die Basis ist das reale Hardwaresystem (Personal Computer oder Server) mit Prozessor, Hauptspeicher, Massenspeicher und diverser weiterer Peripherie. Je nach Zugriffsrechten einer Applikation können von dieser in bestimmten Adressräumen Daten ausgetauscht und Ereignisnachrichten übermittelt werden.

Auf dem Hardwaresystem wird das Gastgeber- bzw. Hauptbetriebssystem ausgeführt, das direkten Zugriff auf die Hardware hat. Im Hauptbetriebssystem wird eine virtualisierende Software als Benutzerprogramm ausgeführt, die man als Virtual Machine Monitor (VMM) oder Hypervisor bezeichnet. Bei einem solchen Hypervisor handelt es sich um einen Typ-2-Hypervisor bzw. Hosted Hypervisor, da er auf dem Hauptbetriebssystem aufsetzt und über dessen Gerätetreiber auf die Hardware-Ressourcen zugreift; das Gegenstück ist der Typ-1-Hypervisor bzw. Native Hypervisor, der als Metabetriebssystem mit eigenen Gerätetreibern direkt auf der Hardware aufsetzt und diese virtuell dupliziert, um sie mehreren Gastbetriebssystemen zur Verfügung zu stellen (vgl. Abbildung). [11](quellen.md)

![Location of type 1 and type 2 hypervisors](/assets/location-of-type-1-and-type-2-hyperisors.png "Abbildung: Unterschied zwischen einem Typ-1- und einem Typ-2-Hypervisor [11](quellen.md)")
Abbildung: Unterschied zwischen einem Typ-1- und einem Typ-2-Hypervisor [11](quellen.md)

Gebräuchlich ist die Virtualisierung mittels Typ-2-Hypervisor (im Folgenden Hypervisor), da dieser betriebssystemspezifisch ist und dadurch eine Virtualisierung auf verschiedensten Hardware-Systemen möglich ist, sofern das Hauptbetriebssystem über die Gerätetreiber verfügt (was bei etablierten Betriebssystemen gegeben ist).

Durch den Hypervisor wird ein Gastbetriebssystem als Benutzerprogramm gestartet, für das ein vollständiges Hardwaresystem simuliert wird. Ein zu lösendes Problem dabei ist das Ausführen von sensitiven Befehlen durch das Gastbetriebssystem, was letzteres als Benutzerprogramm prinzipiell nicht kann. Zur Lösung des Problems verfügen mordene Prozessoren jedoch über Virtualisierungstechnologien mit speziellen Berechtigungsmodi (Intel Virtualization Technology und AMD Secure Virtual Machine). Neben dem Ring-Konzept als Berechtigungskonzept (Ring-0 für Kernmodule mit vollen Zugriffsrechten, Ring-3 für Benutzerprogramme mit eingeschränkten Privilegien) implementieren die Virtualisierungstechnologien das "trap-and-emulate"-Verfahren, das die zwei Modi "Root Operation" und "Non Root Operation" definiert. Der Hypervisor wird im Modus "Root Operation" und das Gastbetriebssystem im Modus "Non Root Operation" ausgeführt. Mit beiden Modi können Ring-3- als auch Ring-0-Befehle ausgeführt werden. Führt jedoch das Gastbetriebssystem Ring-0-Befehle im "Non Root Operation"-Modus aus, können diese durch den Hypervisor im "Root Operation"-Modus abgefangen und verarbeitet werden, was den sensitiven Bereich schützt. [12](quellen.md)

Auf einem Continuous Integration Server können auf diese Art mehrere virtuelle Maschinen ausgeführt werden. Auf dem Hauptbetriebssystem läuft die Server-Applikation als Master, während die Gastbetriebssysteme eine Slave-Applikation ausführen und Kontakt zum Master halten. Der Master kann so Bau- und Testaufgaben auslastungsregelnd an seine Slaves deligieren.

### Containerisierung
Eine andere Art der Virtualisierung ist die sogenannte Virtualisierung auf Betriebssystemebene bzw. Containerisierung. Bei dieser Virtualisierungsart wird das Prinzip der Speicheraufteilung in Kernel und User Space genutzt, worüber moderne Betriebssysteme für Personal Computer und Server die Zugriffsverwaltung regeln.

Bei dieser Virtualisierungsart werden mehrere Instanzen des User Space erzeugt, die man Container nennt. Die Trennung ergibt sich durch die Verwendung einzigartiger Namespaces für jeden Container. Innerhalb eines Containers wird eine Applikation zusammen mit allen benötigten Bibliotheken und Binaries ausgeführt. Durch die verschiedenen Namespaces sind die Container voneinander unabhängig und isoliert, wordurch es wiederum für die jeweilig eingebetten Applikationen den Schein eines eigenen Systems macht. Verwaltet werden die Container im Hauptbetriebssystem durch ein Container-Subsystem. Gemeinsame Systemgrundlage der Container ist der Kernel des Hauptbetriebssystems. Das bringt die Einschränkung mit sich, das bei Containerisierung kein anderes Betriebssystem als das des Hosts simuliert werden kann. Unter Linux können jedoch verschiedene Distributionen in Containern auf einem Hardwaresystem ausgeführt werden, sofern diese auf der gleichen Kernelversion beruhen.

![Virtualization vs. Containers](/assets/virtualization-vs-containers.png "Abbildung: Architektonischer Unterschied zwischen Virtalisierung und Containerisierung [13](quellen.md)")
Abbildung: Architektonischer Unterschied zwischen Virtalisierung und Containerisierung [13](quellen.md)

Anders als bei einer virtuellen Maschine wird neben dem Hauptbetriebssystem kein weiteres Betriebssystem ausgeführt, weshalb es keinen Hypervisor braucht (vgl. Abbildung). Die verschiedenen Größen der einzelenen Komponeten in der Abbildung verdeutlichen den ungleich großen Ressourcenbedarf zwischen Virtualisierung- und Container-Frameworks. [13](quellen.md)

### Gegenüberstellung
Bei der Bewertung der beiden Technologien sind Konfigurierbarkeit, Simulationsfähigkeiten und Ressourcenbedarf maßgebend. Die Konfigurationsmechanismen bei der Containerisierung sind sehr dynamisch und flexibel durch dedizierte Orchestrierung verschiedener Container. Es können einzelne gekapselte Container entfernt und andere hinzugefügt werden, was am Ende ein neues lauffähiges System ergibt. Virtuelle Maschinen müssen hingegen stets als Ganzes rekonfiguriert und auch wieder verteilt und installiert werden. Hier ist die Containerisierung sehr attraktiv, was der Hauptgrund der wachsenden Anwendung in den letzten Jahren ist.

Hinsichtlich Simulationsfähigkeiten können mit virtuellen Maschinen verschiedene Gastbetriebssysteme beliebigen Typs auf einem Hauptbetriebssystem ausgeführt werden. Container sind hingegen an die systemische Umgebung des Hauptbetriebssystem und dessen Gerätetreiber und Kernelmodule gebunden. Andere Betriebssysteme oder andere Versionen des Hauptbetriebssystems können in Containern nicht simuliert werden.

Beim Ressourcenbedarf liegt der Vorteil bei der Containerisierung, da Container nativ Systembefehle ausführen können. Es braucht kein separates Betriebssystem, was einen Hypervisor erübrigt und einen effizienteren Umgang mit den verfügbaren Ressourcen mit sich bringt. Hinzu kommt, dass virtuelle Maschinen immer ein gesamtes Betriebssystem beinhalten und mindestens mehrere Hundert Megabyte groß sind, während Container teilweise nur wenige Megabyte umfassen. Das macht zusammen mit der dynamischen Konfigurierbarkeit die Verteilung besonders schnell und einfach.

Solange also nicht der Bedarf eines anderen Kernels als der des Hauptbetriebssystems benötigt wird, ist die Containerisierung im Vergleich zur klassischen Virtualisierung im Vorteil. Letztere ist bei der Simulation von verschiedenen Systemen auf einer Hardware weiterhin die einzige Möglichkeit. 

### Implementierungen und Standards
Im kommerziellen Umfeld sind die Virtualisierungsprodukte der Firma VMware mit leistungsfähigen Hypervisors für virtuelle Maschinen auf Personal Computern und Servern marktführend [14](quellen.md). Als einfache und zuverlässige Open Source-Alternative für Personal Computer erfreut sich der Hypervisor VirtualBox der Firma Oracle großer Beliebtheit [15](quellen.md).

Das erste Werkzeug, mit dem eine Art Containerisierung möglich war, ist das Linux-Programm chroot (change root), das durch das Ändern des Stammverzeichnis' eines Prozess' die Kapselung einer Applikation ermöglicht [16](quellen.md). Und obwohl andere Frameworks wie Solaris Containers oder FreeBSD jail bereits seit Anfang der 2000er Jahre verfügbar sind [17](quellen.md) [18](quellen.md), wurde die Containerisierung erst 2013 mit dem Release des Frameworks Docker durch die gleichnamige Firma Docker Inc. populär.

Docker setzte sich im Laufe der letzten Jahre sowohl im Open Source als auch im industriellen bzw. kommerziellen Umfeld durch und ist mittlerweile der defacto-Standard (vgl. Abbildung) [19](quellen.md).

![Docker Pulls Chart](/assets/docker-pulls-chart.png "Abbildung: Veranschaulichung des Wachstums des Docker-Ökosystems anhand der steigenden Anzahl an Pulls auf DockHub [19](quellen.md)")
Abbildung: Veranschaulichung des Wachstums des Docker-Ökosystems anhand der steigenden Anzahl an Pulls auf DockHub [19](quellen.md)

Das Docker-Framework besitzt mit der Docker-Engine sein eigenes Container-Subsystem zur Ausführung von Containern. Die Implementierug basiert auf der Container-Runtime containerd [20](quellen.md). Die Stärke des Docker-Frameworks liegt in der Verfügbarkeit von etlichen standardisierten Images aller gebräuchlich Systemkoponenten (JRE, .NET, Apache Server, SQL Datenbank u.v.m.), die dynamisch konfiguriert und miteinander verknüpft werden können. Bereitgestellt werden alle Images über die Online-Plattform DockHub, von der die lokale Docker-Applikation bei Bedarf auch automatisch benötigte Images bezieht, um einen Container zusammenzubauen. Neue standardisierte Images können von jedermann implementiert und über DockHub angeboten werden. Die Konfiguration eines Containers erfolgt entweder aus der Konsole heraus über den parametrisierten Startbefehl oder mit einem Konfigurationsskript in YAML über das separate Werkzeug Docker-Compose (vgl. Abbildung). Letzteres macht die Verwendung im Kontext von CI-Servern sehr attraktiv.

![Docker Workflow](/assets/docker-workflow.jpg "Erzeugung eines konfigurierten Containers mit Docker-Compose [21](quellen.md)")
Abbildung: Erzeugung eines konfigurierten Containers mit Docker-Compose [21](quellen.md)

## Build Server
*von Lukas Taake*

Build Server sind ein zentraler Bestandteil im Continuous Software Engineering. Sie stellen einen zentralen Ort dar, an dem der aktuelle Stand der Software, z.B. in Form von Testergebnissen und kompilierten Artefakten, einsehbar ist.

Ein großer Vorteil ist, dass alle Prozesse innerhalb eines Build Server vollautomatisch ablaufen und somit Fehler durch falsche, ausgelassene oder vertauschte Prozess-Schritte ausgeschlossen werden können.
Darüber hinaus stellt ein zentraler Build Server eine isolierte Umgebung dar, sodass es nicht dazu kommen kann, dass die Software aufgrund unterschiedlicher Konfiguration auf einem Entwickler-Rechner funktioniert (bzw. Tests erforlgreich sind) und auf einem anderen nicht.
Wenn also der Build-Server erfolgreich ist und ein Entwickler-Rechner nicht, muss es sich um eine Fehlkonfiguration des Entwicklers handeln, da die des Build-Servers im Optimalfall möglichst nah an der eines Produktivsystems liegt.

Über das Kompilieren und Testen hinaus werden Build-Server auch zur Durchführung von Continuous Delivery und Deployment verwendet. Oftmals existieren bereits Build-Server-Plugins zur Unterstützung verbreiteter Deployment-Ziele.

Die konkrete Funktionsweise soll Beispielhaft am Beispiel von Jenkins und Travis CI dartestellt werden, wobei Jenkins ein Open Source Projekt ist und weitreichende Konfigurationsmöglichkeiten bietet, während es sich bei Travis um eine SaaS handelt.

### Jenkins
Jenkins ist eins der populärsten CI-Tools, vor allem im Java-Umfeld. Üblicherweise wird es selbst gehostet und ist tiefgreifend konfigurierbar.
Es unterstützt verschiedene Build-Tools, wie Ant, Maven, Gradle oder MSBuild, außerdem Versionskontrollsysteme, wie Git, Mercurial oder SVN.
Darüber hinaus gibt es eine Vielzahl an Plugin, über die es um neue Funktionaliät erweitert werden kann. (vgl. [9])

Gewöhnliche Build-Jobs können zwar aus mehreren auszuführenden Schritten bestehen, liefern als Ergebnis allerdings nur das Gesamtergebnis (und evtl. einen Test-Report) zurück.
Im Gegensatz dazu gibt es auch Pipeline-Jobs, bei denen ein Job explizit in mehrere Stufen (Stages) unterteilt wird (z.B. Compile, Unit Test, Integration Test).
Dann wird der Status jeder einzelnen Stufe ausgegeben, wenn also ein Integrationstest fehlschlägt, ist das sofort ersichtlich (vgl. Abbildung).

![Jenkins Pipeline View](https://wiki.jenkins.io/download/attachments/102662163/who-broke-it.png?version=1&modificationDate=1478695629000&api=v2)
Abbildung: Übersicht der Build-Historie mit einzelnen Stages. Quelle:
[Jenkins Wiki, Pipeline Stage View Plugin](https://wiki.jenkins.io/display/JENKINS/Pipeline+Stage+View+Plugin)

In komplexen Setups, oder wenn viele Projekte zentral verwaltet werden, ist es möglich, einzelne Build-Jobs auf Slave-Knoten zu verteilen. In Pipeline-Jobs ist es sogar möglich, verschiedene Stages auf verschiedenen Slaves ausführen zu lassen, um die Geschwindigkeit zu steigern.

### Travis CI
Travis CI verfolgt einen anderen Ansatz als Jenkins, indem es ausschließlich als Software as a Service angeboten wird und als Versionskontrollsystem ausschließlich Github-Repositories akzeptiert. Dafür ist als Ausgleich zur dieser Einschränkung die Integration zu Github sehr komfortabel.
So können Build Jobs für neue Repositories mit einem Maus-Klick erstellt werden und die Konfiguration geschieht über eine YAML-Datei (siehe Listing).

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

Jede Ausführung eines Build-Jobs geschieht auf einer neu erstellten virtuellen Maschine um absolute Isolation sicherzustellen. Über die Angabe der Programmiersprache in der Konfiguration wird bestimmt, wie die Maschine vorkonfiguriert ist.
Darüber hinaus können mit `services` auch Abhängigkeiten, z.B. Datenbanken, installiert werden und mit `before_install` initialisiert werden.
Mit `install` und `script` werden die Befehle zum Kompilieren und Ausführen der Tests angegeben.

Auf den ersten Blick ähnlich dem Konzept der Pipeline bei Jenkins sind die Build Stages bei Travis.
Die Verwendung ist allerdings im Gegensatz zu Jenkins Pipelines ausschließlich sinnvoll, um unterschiedliche zeitaufwändige Teststufen parallel ablaufen zu lassen. Es wird nämlich für jede einzelne Stage eine eigene virtuelle Maschine erstellt und die Software dort kompiliert. Um also z.B. Unit- und Integrationstests zu parallelisieren, sind sie nicht unbedingt geeignet.
Darüber hinaus ist es nicht möglich, ohne zuhilfenahme externer Dienste, Daten (z.B. Test Reports) zwischen den einzelnen Stages auszutauschen.
Eine Gesamt-Coverage unter Berücksichtigung aller Teststufen wäre so nicht mehr möglich. (vgl. [8])
