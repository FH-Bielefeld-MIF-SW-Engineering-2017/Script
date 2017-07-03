# Cloud Management Platforms
Autor: Philipp Viertel

Wenn man eine eigene Cloud betreiben bzw. nutzen möchte, kann man auf viele unterschiedliche Anbieter und Lösungen zurückgreifen. Wenn man eine Technologie für die eigenen gewünschten Bedürfnisse aussucht, muss man sich die Frage stellen, für welchen Zweck man sie nutzen möchte. Es gibt eine Reihe von Cloud Management Platforms (CMP), Implementierungen von Cloud-Lösungen, die man für einen bestimmten Anwendungsfall in Betracht ziehen kann. An dieser Stelle sollen einige dieser Lösungen vorgestellt werden. Drei große Projekte, welche näher beschrieben und miteinander verglichen werden, sind OpenStack, CloudStack und OpenNebula. Der Fokus liegt dabei auf OpenStack, da dieses System auch in der praktischen Arbeit verwendet wurde.

## OpenStack

OpenStack ist ein open-source Software Projekt zur Realisierung von Cloud Computing Diensten als infrastructure-as-a-service (IaaS). Es ist in Python geschrieben und ursprünglich wurde das Projekt als eine gemeinsame Arbeit von Rackspace Hosting und der NASA ins Leben gerufen. Seit 2016 wird es mittlerweile von der OpenStack Foundation verwaltet. Für die Beschreibung dieser Technologie wurde hauptsächlich die Dokumentation in [3] und [4] verwendet.

OpenStack ist ein sehr komplexes System. Es enthält eine große Anzahl von unterschiedlichen Komponenten, die das Projekt ausmachen. Diese sind für die Bereitstellung der einzelnen Dienste notwendig und sind selbst sehr umfangreich. Die wichtigsten Komponenten werden an dieser Stelle erläutert, um zu verstehen, was OpenStack im Kern ausmacht und wie es aufgebaut ist. Zu diesen gehören Nova (Compute), Glance (Image Service), Swift (Object Storage), Keystone (identity), Horizon (Dashboard), Cinder (Block Storage) und Neutron (Networking). Die zusätzlichen Komponenten Ceilometer (Telemetry Service), Heat (Orchestration Service), Trove (Database Service) und Sahara (Data Processing Service) werden der Vollständigkeit halber ebenfalls beschrieben.

Die im weiteren Verlauf näher erläuterten Komponenten von OpenStack und deren gegenseitiges Zusammenspiel, lassen sich in Abbildung 1 im Zusammenhang darstellen.

![](assets/osog_0001.png)Abbildung 1: Logische(r) Aufbau/Architektur von OpenStack. Quelle: https://docs.openstack.org/arch-design/design.html

### Nova (Compute)

Das Kernstück eines jeden Cloud-Dienstes ist der Cloud Computing Fabric Controller (CCFC). Dieser verwaltet die Ressourcen, welche in der Regel aus virtuellen Maschinen bestehen. Diese virtuellen Systeme werden über Nodes, also Compute-Knoten verteilt. Dies geschieht mittels eines Hypervisors (Virtual-Machine-Monitor). Ein Hypervisor ist dabei ein System welches zur Abstrahierung der tatsächlichen Hardware und den zusätzlichen Betriebssystemen eingesetzt wird. Auf dieser Ebene werden also virtuelle Umgebungen definiert, wobei man recht frei von den gegebenen Hardware-Bedingungen operieren kann. Als praktische Implementierung verwendet OpenStack dafür KVM und Xen.

##### KVM

KVM steht für Kernel-based Virtual Machine und ist ein open-source Typ2-Hypervisor zur Virtualisierung und seit Kernelversion 2.6.20 ein Bestandteil des Linux-Kernels. Bei der eigentlichen Virtualisierung kommt QEMU zum Einsatz; KVM sorgt für die notwendige Infrastruktur und QEMU für die virtuellen Elemente wie Festplatten, Grafikkarten, usw.

Verwendung findet dieser Hypervisor u.a. in Ubuntu und openSUSE.

#### Xen

Xen ist ein Typ1-Hypervisor um mehrere Systeme auf einem physischen Computer zu virtualisieren. Xen unterteilt die virtualisierten Systeme in sogenannte Domänen, die untereinander keinerlei Beziehung zueinander haben. Die Kommunikation und Steuerung erfolgt über die erste Domäne, welche in der Lage ist, andere Domänen zu verwalten und steuern.

Xen wird unterstützt von Unternehmen wie Microsoft, Intel und AMD.

### Glance (Image Service)

Der Glance Service macht es möglich, Abbilder, also Images von virtuellen Maschinen den Nutzern zur Verfügung zu stellen. Die Anbindung erfolgt hier über REST. Mit Glance können ebenfalls Metadaten wie z.B. Betriebssysteme gespeichert werden.

### Swift (Object Storage)

Zur Bereitstellung von Speicher kann auf Dienste wie SheepDog oder den hauseigenen Dienst von Openstack namens Swift zurückgegriffen werden. Ähnlich wie bei Nova, findet die Ansteuerung über eine REST API statt. Die Objekte werden hier gruppiert in Containern abgespeichert, welche wiederum an entsprechende Accounts gebunden sind bzw. diesen gehören.

### Keystone (identity)

Die Komponente Keystone fungiert als Authentifizierungs- und Rechtesystem in OpenStack für die Nutzung von Clouds. Der Nutzer einer Cloud wird als Mandant von Keystone betrachtet, wenn er einen erlaubten Zugriff auf ein Projekt innerhalb der Cloud besitzt. Es können mehrere Benutzer einem Mandanten zugeordnet werden, welche mit unterschiedlichen Rechten ausgestattet sind. Die Konfigurationsmöglichkeiten weisen dabei eine recht hohe Komplexität auf.

### Horizon (Dashboard)

Horizon ist das Webinterface (GUI) mit welchem man die unterschiedlichen Komponenten von OpenStack verwalten kann und mit der die einzelnen Funktionalitäten eingesehen und gesteuert werden können. Realisiert wird dies über eine REST API.

### Cinder (Block Storage)

Cinder ist ähnlich wie Swift, nur dass es hier nicht um Objektspeicher, sondern um die Verwaltung von Blockspeicher geht. Blockspeichermedien sind z.B. Festplatten, USB Datenträger oder CD/DVDs.

### Neutron (Networking)

Die Komponente Neutron übernimmt den Netzwerkdienst für OpenStack. Alle Netzwerkangelegenheiten, Subnetze und IP Adressen lassen sich hiermit verwalten. Hier wird auch der Zugang nach "Außen" definiert, also die IP, mit der die Cloud im öffentlichen Netzwerk erreichbar ist. Neutron hat auch eine eingebaute Firewall mit der sich das System absichern lässt und die Zugriffe reglementieren lassen.

### Ceilometer (Telemetry Service)

Ceilometer sammelt Daten über alle anderen Komponenten hinweg um diese für zukünftige Komponenten bereit zu stellen. Die gemessenen Daten können abgespeichert werden und für die Auswertung genutzt werden, um z.B. Ressourcen nachzuverfolgen. Ereignisse in der Cloud-Infrastruktur werden zu messbaren Gegenständen umgewandelt (metering). Es ist dabei so abstrakt gehalten wie möglich, um die Daten für unterschiedlichste Tätigkeiten zu verwerten.

Metering im Detail beschreibt den Prozess der Informationsgewinnung von Ereignissen die fakturiert werden können. Die Informationen umfassen alle möglichen Attribute (Wer hat was wann getan und wie oft?). Das Ergebnis bezeichnet eine Sammlung von Tickets.

### Heat (Orchestration Service)

Heat ist ein Dienst um einen Verbund von Cloud Applikationen zu orchestrieren. Dafür bietet es ein Template Format an, welches über eine REST API angesteuert wird. Ein Heat Template beschreibt dabei die Infrastruktur einer Cloud Applikation. So eine Template Datei ist für Menschen lesbar und auch bearbeitbar. Sie enthalten ebenfalls die Verbindungen zu Ressourcen. Gerade bei der Ausführung mehrerer Applikationen, die sensible Abhängigkeiten zwischeneinander besitzen, helfen solche Templates dabei, die Applikationen in der richtigen Reihenfolge und wohlgeordnet zu starten.

Zusätzlich erlauben die Templates auch bestimmte Ressourcen Typen zu erzeugen (Instanzen, Datenträger, Benutzer, etc.).

### Trove (Database Service)

Trove bietet einen relationalen Datenbank Service an. Dieser kann von Administratoren und Nutzern verwendet werden.

### Sahara (Data Processing Service)

Sahara zielt darauf ab, datenverarbeitende Frameworks wie z.B. Apache Hadoop auf OpenStack lauffähig zu machen. Die Einbindung solcher Frameworks findet grundsätzlich über umfangreiche Konfigurationen statt, um die notwendigen Ressourcen (Knoten, Hardware) dafür anzupassen.

### Sicherheitsaspekt

#### Domänen

OpenStack bietet eine umfassende und tiefgehende Dokumentation zum Thema Sicherheit an. Anhand von [5] orientiert sich folgende Beschreibung. OpenStack fasst Benutzer, Applikationen und Netzwerke, welche die gleichen Authentifizierungsanforderungen besitzen, in sogenannten Sicherheitsdomänen (oder Security Domains) zusammen. Standardmäßig um CloudStack einzusetzen gibt es minimal vier Sicherheitsdomänen:

* Public
* Guest
* Management
* Data

Alle Zugriffe, Rechte, Komponenten, usw. können in diese Domänen abgebildet werden. Es ist wichtig anzumerken, dass manche Elemente jedoch auch in gemischten Domänen vorkommen können, obwohl sie sich physisch in einem Netzwerk befinden. Die Sicherheitsregeln und Domänen sollten daher immer an der tatsächlichen Topologie des Systems angepasst sein, und der Art der Cloud Instanz (private, öffentliche oder hybride Cloud?).

Public ist nicht vertrauenswürdig, da es sich dabei um Netzwerke handelt, wo der Cloud Betreiber keinerlei Kontrolle hat wie z.B. das Internet. Aktionen in dieser Domäne sollten daher sehr vosichtig gehandhabt und besonders geschützt werden. Die Guest Domäne ist für den Verkehr zwischen Instanzen gedacht. Es betrifft die Daten die von den Instanzen generiert werden, nicht jedoch Dienste der Cloud die über API Aufrufe ausgeführt werden. Diese Domäne ist ebenfalls nicht vertrauenswürdig, egal ob es sich um eine private oder public Cloud handelt. Im Falle einer privaten Cloud kann es als vertrauenswürdig gelten, aber nur unter geeigneten Sicherheitsrichtlinien. In der Management Domäne interagieren Services, also Dienste miteinander. Hier werden sensible Daten übertragen wie z.B. Parameter der Cloud Konfiguration, Passwörter, Benutzernamen, usw. Der Zugriff auf diese Domäne sollte sehr gut abgesichert und überwacht sein. Diese Domäne wird als vertrauenswürdig betrachtet. Die Domäne Data enthält Daten bezüglich der Datenträger, also dem Storage Service. Diese Domäne ist ebenfalls vertrauenswürdig, und es muss strengstens auf die Integrität und Sicherheit der Daten geachtet werden.

#### Bridges

Unter einer Bridge versteht man eine Komponente, die sich in mehr als einer Domäne befindet, z.B. in einer vertrauenswürdigen und einer nicht vertrauenswürdigen Domäne. In diesem Fall muss eine Komponenten besonders vorsichtig konfiguriert werden. Oft stellen diese Komponente Schwachstellen dar und sind daher für Angriffe besonders verwundbar. Um diesen Fällen vorzubeugen, gibt es die Option, eine Bridge besonders abzusichern, das heisst, sicherer als beide Domänen in der sich die Komponente befindet. 

![](assets/bridging_domains_clouduser.png)

Abbildung 2: Beispielhaftes Szenario. Der API Endpoint in der Domäne Management überschneidet sich mit der Domäne Public. Quelle: https://docs.openstack.org/security-guide/introduction/security-boundaries-and-threats.html

In der Abbildung 2 ist ein solches Beispiel dargestellt. Der API Endpoint (aus der Domäne Management) befindet sich ebenfalls in der Domäne Public. Dies macht einen Angriff auf diese Stelle sehr wahrscheinlich, da die Sicherheitsrichtlinien entsprechend niedrig sind in dieser Domäne.

#### Angriffstypen

Das nachfolgende Diagramm stellt die möglichen Angriffe exemplarisch dar. Wieder sollte die Frage anstehen, welches Szenario für die Cloud am wahrscheinlichsten ist? Handelt es sich um eine private oder public Cloud, wie sensibel sind die Daten, die Ressourcen, etc.? Anhand dieser Analyse kann ermittelt werden, welches Angriffsszenario am wahrscheinlichsten ist, und welche Maßnahmen man anschließend ergreifen muss, um sich dagegen zu wehren.

![](assets/high-capability.png)

Abbildung 2: Verschiedene Angriffsszenarien. Quelle: https://docs.openstack.org/security-guide/introduction/security-boundaries-and-threats.html

## CloudStack

In [6] wird CloudStack als ein open-source Cloud Projekt vom Typ IaaS beschrieben. Es ist in Java geschrieben und wird von der Apache Software Foundation betrieben. Ein Vorteil von CloudStack ist die Unabhängigkeit von einer bestimmten Plattform. Als Webinterface wird eine AJAX-basierte GUI verwendet. Ähnlich wie OpenStack, ist es auch hier möglich KVM als Hypervisor zu nutzen, falls das System auf einer geeigneten Linux Distribution läuft, wie Ubuntu. Andernfalls gibt es auch die Möglichkeit Windows Server 2012 R2 zu verwenden, Xen und noch einige andere.

## OpenNebula

OpenNebula ist ebenfalls ein open-source Projekt zum Betrieb einer Cloud als IaaS. Zur Beschreibung und Definition dient die Dokumentation in [7]. Als Vorteil ist zu nennen, dass mit OpenNebula hybride Clouds möglich sind und auch die Nutzung von Computerclustern, also einer verteilten Infrastruktur. Als weitere wichtige Merkmale sind die Standardisierung und die Interoperabilität zu nennen. Das macht OpenNebula sehr flexibel und dynamisch. Im Gegensatz zu OpenStack ist OpenNebula wesentlich schlanker, und laut eigenen Aussagen einfach und simpel zu installieren, verwenden und warten. Geeignet ist diese Lösung für Linux Systeme und als Hypervisor lässt sich ebenfalls KVM oder Xen nutzen.

## Vergleich und Fazit

Um die unterschiedlichen Lösungen in Relation zueinander zu setzen, ist es möglich, eine Klassifizierung der Cloud Dienste anzugeben, wie dies in [2] getan wird. Dazu kann man die Cloud Plattformen in zwei verschiedene Kategorien einteilen: Datacenter Virtualization und Infrastructure Provision. Das erstere, versteht Clouds als eine Erweiterung der Datenverarbeitung. Eine Cloud-Infrastruktur soll die virtuellen Ressourcen verwalten und diesen Prozess vereinfachen. Die zweite Kategorie meint Clouds on-premise, also vor-Ort, und stellt daher die Anforderung zusätzliche virtuelle Ressourcen auf Abruf bereitstellen zu können.

Die Abbildung 3 stellt die Unterschiede und Spezifikationen die diese Einteilung mitsich bringt übersichtlich dar.

![](assets/cloudcomparison.png)

Abbildung 3: Gegenüberstellung der Anforderungen und Anwendungen von Cloud Lösungen. Quelle: https://opennebula.org/eucalyptus-cloudstack-openstack-and-opennebula-a-tale-of-two-cloud-models/

Eine Einteilung von CloudStack, OpenNebula, Eucalyptus und OpenStack lässt sich folgendermaßen darstellen, wie in Abbildung 4 abgebildet.

![](assets/CMP_Quadrant1.png)Abbildung 4: Positionierung vier unterschiedlicher Cloud Plattformen. Quelle: https://opennebula.org/eucalyptus-cloudstack-openstack-and-opennebula-a-tale-of-two-cloud-models/

Anhand von [1] kann man abschließend über die unterschiedlichen Cloud Lösungen folgendermaßen urteilen: OpenStack hat eine hohe Komplexität, jedoch ist es die am weitesten verbreiteste Cloud Lösung. Mehr als 150 Firmen wie z.B. AMD, Dell, IBM und Yahoo verwenden OpenStack und leisten auch ihren Beitrag zur Weiterentwicklung des Projekts. Dies macht OpenStack zu einem. Die erste stabile Version von CloudStack erschien 2013 und ist daher noch recht jung. Kritiker bemängeln die umständliche Installation, die einige Kenntnisse vom Anwender abverlangt. Der größte Nutzer von CloudStack, das Unternehmen DataPipe, nennt einige Gründe für ihre Wahl; zu den Wichtigsten gehören die Skalierbarkeit des Datenspeichers und die Nutzung von hochgeschwindigkeits VMs, welche damit ressourcensparender arbeiten. Auch wenn CloudStack mehr an Popularität gewinnt und in der Zukunft womöglich interessanter sein wird, ist die momentan verbreiteste und akzeptierteste Lösung OpenStack.

Anhand der grafischen Positionierung und den Beschreibungen der einzelnen Cloud Anbieter, wird es klar, dass die Wahl der Cloud immer vom speziellen Anwendungsfall abhängig ist. Daher haben die Einsteiger-freundliche OpenNebula, CloudStack und auch die umfangreiche OpenStack Plattform jeweils ihre Existenzberechtigung und man darf gespannt sein, wie sie in Zukunft vom Markt aufgenommen werden und sich weiter entwickeln.
