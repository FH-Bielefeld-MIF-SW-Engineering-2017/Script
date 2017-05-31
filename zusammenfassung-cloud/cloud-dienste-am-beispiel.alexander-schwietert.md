# Cloud-Dienste am Beispiel

Die schnelle Verbreitung von Cloud Services ist vor allem durch die großen Provider wie Amazon, Google, Microsoft, Rackspace oder Terremark ermöglicht worden. Diese investieren große Summen in ihre Infrastruktur und errichten weltweit Datenzentren, die  redundant und nach den Gesetzen des jeweiligen Standortes, die Daten ihrer Kunden verwalten und ihnen entsprechende Services zur Verfügung stellen.

Neben den großen Cloud Service Providern gibt es auch kleinere Angebote wie Apple, Salesforce, VMware oder Dropbox, welche sich auf bestimmte Services spezialisiert haben,  z.B. die Distribution von Musik oder CRM.

Im Folgenden werden die Angebote von Amazon und Google genauer betrachtet.

### Amazon Web Services

Amazon ist der größte der Clouddienstleister und übertrifft in Sachen Kapitalausstattung seine Konkurrenten um das Fünffache. Dabei bietet Amazon neben kostenpflichtigen Premiumservices auch kostenlose Angebote, mit denen Kunden die Möglichkeiten der AWS testen können. Nutzern wird ein einziger Einstiegspunkt für alle Services der Cloud geboten, was es für Einsteiger leichter macht sich zu orientieren und das genutzte Portfolio zu erweitern.

Seit dem Start der AWS im Jahr 2006 hat Amazon schätzungsweise 12 Milliarden Dollar in seine Services investiert und liegt damit hinter den Investitionen mancher Konkurrenten. Die AWS werden von Unternehmen in über 190 Ländern verwendet, entsprechend verteilen sich die Datenzentren über alle Kontinente, mit einem Fokus auf Asien und Nordamerika. Zusätzlich bietet Amazon seinen Kunden an, verschiedene Standorte je nach Service zu wählen, wo beispielsweise Daten verwaltet und von welchem Standort Rechenleistung bezogen werden soll.

AWS bietet dabei SaaS, PaaS, IaaS Services, die in Form von privaten und öffentlichen Clouds angeboten werden. Amazon garantiert dabei eine Verfügbarkeit von 99.9% der Zeit, was umgerechnet maximal 52 Minuten Ausfallzeit im Jahr bedeutet. Selbst kurze Ausfallspannen können bereits enorme Folgen aufgrund der schieren Größe und Verbreitung der AWS bedeuten, wie Vorfälle in den vergangenen Jahren zeigten.

**Elastic Compute Cloud \(EC2\)**

Mit der EC2 können Nutzer virtuelle Server verwalten, dabei kann man zwischen 4 Standorten wählen. In einem nächsten Schritt wählt der Benutzer dann eine Verfügbarkeitsregion für den gewählten Standort aus, auf der sein Server laufen wird. Weiterhin müssen Arbeitsspeicher, Prozessorleistung und Festplattenspeicher spezifiziert werden.

Die virtuellen Server werden aus Amazon Machine Images \(AMI\) erzeugt. Amazon bietet verschiedene vorgefertigte AMIs an, die sich in Betriebssystem und vorinstallierter Software unterscheiden. Sie stellen es dem Benutzer aber auch frei selber eine widerverwendbare AMI zu erzeugen. Diese kann sogar veröffentlicht und vom Kunden als eigenes Produkt vertrieben werden.

Zur Identifikation gegenüber einer gehosteten Instanz wird ein Public Key Verfahren eingesetzt. Für weitere sicherheitsrelevante Einstellungen befindet sich jede Instanz in einer sogenannten Security Group, die frei konfigurierbare Regeln anbietet.

Nach erfolgreicher Einrichtung wird einer Instanz eine private sowie eine öffentliche IP eingerichtet. Über die öffentliche IP ist der Server aus dem Web erreichbar, die Private dient zur Kommunikation zwischen Instanzen in der AWS. Beide IPs sind jedoch dynamisch und werden nach Neustart der Instanz neu vergeben, daher muss man zusätzlich eine statische elastische IP Adresse reservieren.

Änderungen an der laufenden Instanz werden nicht gespeichert, dafür müssen Zustandsänderungen entweder bei großen Datenmengen Amazons S3 verwendet werden oder Amazons Elastic Block Store \(EBS\). EBS funktioniert in dem Fall wie eine externe Festplatte die an die Instanz angeschlossen wird.

Alle Vorgänge lassen sich über Kommandozeilenbefehle realisieren, es gibt jedoch auch weitere Werkzeuge wie die AWS Management-Konsole sowie das AWS Toolkit für Eclipse, um mit seinen Instanzen zu interagieren.

**Amazon Simple Storage Service \(S3\)**

S3 ist ein Massenspeicher mit einem eigenen Dateisystem. Die bis zu 5 GB großen Web-Objekten liegen hier in sogenannten Buckets und können über einen Bucket-Namen angesprochen werden. Der Zugriff auf die Objekte erfolgt standardmäßig über Web Services und ist über eine SOAP oder REST API möglich. Hierfür stehen ebenfalls komfortable, grafische Werkzeuge zur Verfügung. Zusätzlich gibt es auch Tools von Drittanbietern, die einen Zugriff auf den Speicher, wie auf weit entfernte Festplatten ermöglichen.

**Amazon Elastic Block Store \(EBS\)**

Mit dem Speicherdienst können Datenspeicher von 1GB bis 1TB erzeugt werden, sogenannte Volumes. Ein Volumen kann ein beliebiges Dateisystem beinhalten und verhält sich dabei wie ein USB Stick. Ein Volumen kann lediglich an einer Instanz \(AMI\) angehängt werden, die in derselben Verfügbarkeitszone angelegt wurde wie das Volumen. Der Speicher ist persistent.

**Amazon Simple Queue Service \(SQS\)**

Die Nachrichtenwarteschlange SQS wird zur Skalierung von Anwendungen in der AWS eingesetzt. Sender können hier Nachrichten in die Warteschlange einstellen, welche von registrierten Empfängern dann abgearbeitet werden. Eine dienstnehmende Komponente kann ihre Arbeitsaufträge in die Warteschlange einstellen, wo sie eine dienstgebende Komponente abholt. So können bei Engpässen der kritischen Komponenten, diese parallel auf mehreren EC2 Instanzen laufen.

**Amazon SimpleDB**

SimpleDB ist auf eine einfach strukturierte, dafür hoch effiziente und zuverlässige Datenhaltung ausgelegt. Die transaktionalen Möglichkeiten sind hierbei stark eingeschränkt, werden jedoch für ein breites Spektrum an Anwendungen als ausreichend erachtet.

**Amazon Relational Database Service**

Als Gegenwurf zur SimpleDB steht das Amazon RDS, ein Plattformdienst zur einfachen Einrichtung, Betreiben und Skalieren von relationalen Datenbanken in der Cloud. Dabei gewährt Amazon Zugriff über die bekannten Funktionen einer MySQL Datenbank. Bei der Einrichtung wählt RDS automatisch die optimalen Parameter, unter Berücksichtigung von Rechenressourcen und Speicherkapazitäten. Diese lassen sich jedoch im Nachhinein auch entsprechend anpassen.

RDS stellt elastische Kapazitäten zur Verfügung und erledigt gleichzeitig zeitraubende Datenbankverwaltungsaufgaben. Automatisierte Backups und Snapshots können in individuell definierten Intervallen durchgeführt werden und wodurch eine hohe Zuverlässigkeit erreicht wird.

Bei Bedarf kann die Datenbank vertikal skaliert werden, bei sehr aufwendigen Leseoperation kann durch sogenannte Read-Replika Instanzen horizontal repliziert werden. Ein kostenloses Hochverfügbarkeitsangebot bietet die Möglichkeit synchron replizierte Instanzen in mehreren Verfügbarkeitszonen bereit zu stellen. Bei Ausfällen oder Wartungsfenstern in einem Standort wird automatisch zwischen den replizierten Instanzen gewechselt. Über Amazon CloudWatch kann man schließlich die Auslastung der Datenbank überwachen.

### Google Apps

Das App-Angebot von Google ist stark gewachsen in den vergangenen 5 Jahren. Das erste Angebot war Google Docs, was zum direkten Konkurrenten Microsoft Office, die Probleme von verschiedenen Versionen und inkompatiblen Formaten untereinander umgehen sollte. Zusätzlich wurden Features wie das kollaborative Arbeiten an einem Dokument hinzugefügt, sowie die Möglichkeit geboten Dokumente in verschiedenen Formaten jederzeit hoch und runterzuladen.

In den nächsten Jahren wurden die Services mit Gmail, Google Drive, Google Talk, Google Calendar, Google Video, Google Labs und Google Play erweitert. Da alle diese Services kostenfrei verfügbar sind und Drive beispielweise großzügige 30 GB zur Verfügung stellt, verbreiteten sie sich entsprechend schnell.

Google hat schätzungsweise bis zu 21 Milliarden in ihre Services investiert und somit deutlich mehr als Amazon, bietet seine spezialisierten Services jedoch kostenlos an und finanziert diese über Werbeangebote.

**App Engine**

Googles App Engine ist ein PaaS Service und dient als Programmierumgebung und  Ausführungsumgebung für neu entwickelte Apps. Unterstützt werden Java und Python. Zum Testen kann die Anwendung auf einer lokalen Laufzeitumgebung gestartet werden, schließlich kann man eine fertige Version auf die Google Infrastruktur übertragen und ausführen lassen.

Zusätzlich zu den Funktionalitäten der Java Bibliotheken bietet die Plattform weitere Services, die über die Standardschnittstellen von Java angesprochen werden können und die Portabilität sowie die Benutzbarkeit des Codes erweitern.

* Zur Speicherung von Daten verwendet die Plattform den sogenannten DataStore, eine schemalose objektorientierte Datenbank. Angesprochen werden kann sie mit Hilfe von JDO und JPA.
* Des Weiteren können über die JavaMail Schnittstelle Funktionen zum Senden und Empfangen von Emails via Google-Mail  Konten implementiert werden.
* Zur Authentifizierung werden Google Konten verwendet, welche mit Hilfe eines rudimentären Rechte-Managements zwischen Administratoren und Nutzern der App unterschieden werden können.

Für Entwickler gibt es ein kostenloses Tageskontigent ans Nutzbarer CPU Leistung und Speicher, welches für die meisten kleineren Applikationen ausreichend ist. Erst bei größeren Projekte werden teurere Premiummodelle notwendig.

**Google Storage**

Der Speicherdienst funktioniert ähnlich dem S3 Service von Amazon und ermöglicht das Speichern von Web-Objekten in den Datenzentren von Google, die über REST abgerufen werden können. Auch hier werden Objekte in sogenannte Buckets gespeichert. Mit Hilfe des Kommandozeilenwerkzeugs GSUtil können Objekte hochgeladen und Buckets angelegt werden., sowie Zugriffsrechte verwalten.

**Google Cloud Print**

Durch den Cloud Print Service können sich netzwerkfähige, kompatible Drucker in der Cloud registrieren lassen und anschließend von jeder Applikation, die Google Cloud Print unterstützt, über das Internet angesprochen werden. So fallen die Installation von einzelnen Treibern und eventuelle Kompabilitätsprobleme weg. Drucker können mit anderen Google Konten geteilt werden und so den Zugriff gestatten oder gleich als Dienstleister auftreten.

