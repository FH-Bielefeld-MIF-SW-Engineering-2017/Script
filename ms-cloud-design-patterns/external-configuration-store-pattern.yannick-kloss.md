# External Configuration Store Pattern

## Definition
Mit dem _External Configuration Store Pattern_ werden Konfigurationsinformationen an einer zentralen Stelle verwaltet. Diese werden von allen Anwendungen und den Instanzen von Anwendungen verwendet. Dieses Pattern soll für ein vereinfachtes Management und ein bessere Steuerung der Konfigurationen beitragen.

## Probleme mit herkömmlichen Lösungen
Eine vielzahl von Anwendungen haben Konfigurationsinformationen in Dateien gespeichert, welche in Laufzeitumgebungen einer Cloud ausgeführt werden. Bei manchen Anwendungen lassen sich diese verändern und die Anwendung reagiert sofort darauf. In anderen Fällen müssen diese jedoch neu gestartet werden, was die Anwendung in dieser zeit unerreichbar macht und zusätzlichen Administrationsaufwand erfordert. Ein weiteres Problem ist, wenn in einer Cloud alle Instanzen einer Anwendung geupdated werden und diese während dem Vorgang unterschiedliche Konfigurationen verwenden. Die Authentifizierung von Benutzern muss berücksichtigt werden.  
In vielen Anwendungsfällen ist es von Vorteil, wenn Konfigurationen von einer zentralen Stelle für Anwendungen gemeinsam genutzt werden. 

## Das Pattern
Das _External Configuration Store Pattern_ sieht es vor, dass Konfigurationsinformationen an einer externen, zentralisierten, Stelle von einem nicht-flüchtigen Speichertyp gespeichert werden. Über definierte Schnittstellen können Konfigurationen gelesen und verändert werden. In einem typischen Cloud Szenario könnte der Speicher beispielsweise ein Cloud-basierter Speicherservice sein. Die Schnittstellen müssen konsistent und einfach zu verwenden sein. Die Konfigurationsinformationen sollten in einem strukturierten Format wiedergegeben werden.  
Je nach Typ des Speichers kann es von Vorteil sein, wenn die Softwarekomponente, welche für Konfigurationsspeicher zuständig ist, die Konfigurationsinformationen in einen lokalen Cache einliest um die Performance zu erhöhen.

[![](https://docs.microsoft.com/en-us/azure/architecture/patterns/_images/external-configuration-store-overview.png "Überblick des External Configuration Store pattern with optionalem lokalen Cache.")](https://docs.microsoft.com/en-us/azure/architecture/patterns/_images/external-configuration-store-overview.png)  
Überblick des External Configuration Store pattern mit optionalem lokalen Cache. \(Quelle: [https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store](https://docs.microsoft.com/en-us/azure/architecture/patterns/external-configuration-store)\)

## Wann das Pattern verwendet werden kann 
* Wenn sich Anwendungen und Instanzen einer Anwendung Konfigurationsinformationen teilen oder wenn Standardeinstellungen auf mehreren Anwendungen und Instanzen einer Anwendung erzwungen werden müssen
* Wenn das Standard Konfigurationssystem nicht alle geforderten Konfigurationseinstellungen unterstützt
* Wenn ein ergänzender Speicher für einige Konfigurationen benötigt wird
* Wenn ein vereinfachter Mechanismus für die Administration von mehreren Anwendungen benötigt wird



