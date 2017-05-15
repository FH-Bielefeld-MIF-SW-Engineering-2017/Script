# Valet Key Pattern

Das Valet Key Pattern wird bei Server-Client-Systemen angewendet, um Clients den direkten, aber eingeschränkten, Zugriff auf dedizierte Ressourcen zu ermöglichen. Das soll den Datenumsatz der Serverapplikation reduzieren, ohne die Datensicherheit zu gefährden. Das Pattern ist besonders bei Applikationen nützlich, die Cloud-basierte Speichersysteme nutzen, da so Kosten minimiert und die Skalierbarkeit und Performanz des Gesamtsystems maximiert werden können.

## Kontext und Problemstellung

Bei Server-Client-Systemen ist typischerweise die Server-Applikation dafür zuständig Daten zwischen Clients und dem eigenen Datenspeicher hin- und herzutransferieren. Dieses Vorgehen bindet jedoch wertvolle Ressourcen, wie Rechenzeit, Arbeitsspeicher und Bandbreite. Dabei sind Datenspeicher eigentlich in der Lage den Datenaustausch mit dem Client direkt zu regeln, ohne die Applikation zu belasten.

Dafür braucht ein Client Zugriff auf die Sicherheitsschlüssel des Datenspeichers. Sobald der Client diesen Zugriff hat, hat die Applikation jedoch keine Handhabe mehr über den Datenaustausch zwischen Client und Datenspeicher; sie kann also nicht mehr als Gatekeeper agieren. Dieser direkte und damit unkontrollierte Zugriff ist bei verteilten Systemen, die nicht-vertrauenswürdige Clients ausschließen können müssen, kritisch und deshalb nicht gangbar. Applikationen müssen stets in der Lage sein den direkten Datenzugriff durch den Client granular zu steuern und ggf. zu verwähren, um Datensicherheit zu garantieren und gleichzeitig die eigenen Ressourcen zu schonen.

## Lösungsansatz

Es bedarf der dedizierten Zugriffskontrolle auf den Datenspeicher. Letzterer kann die Authentifizierung und Authorisierung der Clients aber nicht selber durchführen. Eine typische Lösung für dieses Problem ist es, dem Client, durch die Verwendung von Schlüsseln oder Tokens, nur eingeschränkten Speicherzugriff zu geben. Diesen Schlüssel nennt man Valet Key, welcher dem Client temporären Zugriff ausschließlich auf benötigte Speicherbereiche gewährt. Die Ausstellung der Valet Keys zur Laufzeit durch die Applikation ist dabei schnell und einfach, wordurch die Auslastung von Applikation und Server durch Datentransferprozessen effektiv gesenkt wird.

Nach der Ausstellung eines Tokens benutzt der Client diesen, um auf eine dedizierte Ressource zuzugreifen; und zwar nur für einen beschränkten Zeitraum und mit restriktiven Zugriffsrechten \(vgl. Abbildung\). Zum einen kann so nur auf bestimmte Speicherbereiche zugegriffen werden \(Tabellen, Tabellenzeilen, Container, Container-Elemente\). Zum anderen verliert der Token nach einer bestimmten Zeit seine Gültigkeit und dem Client wird der Ressourcenzugriff wieder verwehrt. Zusätzlich kann die Applikation die Gültigkeit vorzeitig beenden, wenn z.B. der Client den erfolgreichen Abschluss eines Datentransfers gemeldet hat.

![](/images/valet-key-pattern.png)

## Probleme und Überlegungen

Wenn es um die Implementierung des Patterns geht, sind folgende Aspekte zu berücksichtigen:

* Verwaltung des Gültigkeitsstatus' und -zeitraums: Für den Fall, dass ein Sicherheitsschlüssel durchgesickert ist und die Gefahr der boshaften Verwendung besteht, gibt es verschiedene Gegenmaßnahmen. Der Schlüssel kann als ungültig makiert, die Server-Rechte angepasst oder der korrespondierende Server-seitige Schlüssel deaktiviert werden. Präventiv kann bereits bei der Schlüsselgenerierung die Gültigkeitsdauer möglichst kurz gesetzt werden; dabei darf sie aber nicht so kurz gewählt werden, dass der Client nicht genügend Zeit zur kompletten Datenübertragung hätte.
* Kontrolle des Zugrifflevels: Der Sicherheitsschlüssel sollte dem Nutzer ausschließlich den Ressourcenzugriff ermöglichen, der für die aktuelle Operation notwendig ist. Soll der Nutzer nichts hochladen dürfen, genügt einfacher Leserzugriff. Soll er lediglich Daten hochladen, genügt ausschließlich Schreibzugriff in einen bestimmten leeren Bereich.
* Lenken des Benutzerverhaltens: Die granulare Ressourcenkontrolle ist durch die Funktionalitäten der Applikationsdienste und des Datenspeichers beschränkt, weshalb die Client-Operationen nur eingeschränkt lenkbar sind. So hat man keine Handhabe über die Anzahl der Uploads oder die Dateigrößen, wodurch große unerwartete Kosten entstehen können. Um die Anzahl der Uploads zu kontrollieren, unterstützen Datenspeicher jedoch oft die Möglichkeit erfolgreichen Uploads zu melden, was die Applikation zur Überwachung nutzen kann.
* Validierung und optionale Zensierung hochgeladener Daten: Ein boshafter Nutzer kann kompromitierte Daten hochladen oder ein authorisierter Nutzer lädt versehentlich defekte oder manipulierte Daten hoch. Deshalb müssen alle Uploads validiert und überprüft werden.
* Alle Operationen können durch Protokollfunktionen der Schlüsselbasierten Mechanismen protokolliert werden, was für die Prozessoptimierung oder Rechnungsstellung gegenüber dem Nutzer verwendet werden kann.
* Sichere Übermittlung des Schlüssels durch Einbettung in die URL, automatischen Download und der ausschließlichen Übermittlung via HTTPS. 
* Sensitive Daten bei der Übermittlung schützen durch die verpflichtende Verwendung von SSL oder TLS.

## Anwendungsszenarien

Nützlich bei folgenden Anwendungen:

* Minimierung der Ressourcenlast und Maximierung der Performanz und Skalierbarkeit, da die Schlüsselerzeugung typischerweise eine einfache kryptografische Operation ist.
* Minimierung der Operationskosten, da der direkte Datenzugriff die Netzwerklast reduzieren kann.
* Wenn Clients regelmäßig Daten hochladen, besonder bei großen Speichern oder großen Dateien.
* Wenn die Applikation nur limitierte Hardwareressourcen zur Verfügung hat.
* Wenn Daten dezentral gespeichert sind und die Applikation häufig vermitteln muss.

Nicht nützlich bei folgenden Anwendungen:

* Wenn die Applikation Daten bearbeiten oder validieren muss, bevor sie an den Client gesendet werden können.
* Wenn das Design der Applikation die Implemtierung des Patterns schwierig macht; das Valet Key Pattern sollte bei der initialen Architektur berücksichtigt werden.
* Wenn die Anzahl der Up- und Downloads genau überwacht werden muss und der Datenspeicher über keinen Mitteilungsmechanismus verfügt.
* Wenn die Größe der Uploads begrenzt werden muss. Alternativ kann nach dem Upload die Dateigröße kontrolliert werden oder zyklisch während des Uploads.