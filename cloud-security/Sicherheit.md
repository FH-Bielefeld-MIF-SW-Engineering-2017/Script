# Sicherheit
Autor: André Kaleja

Der größte Vorteil durch Clouds ist das hohe Performanz/Kosten Verhältnis. Grade kleine bis mittelständische IT Betriebe, können von den großen Recheneinheiten profitieren, ohne dabei selber in den Bau und den Kauf dieser Datenzentren investieren zu müssen. Der Wunsch nach einer kritischen cyber-physischen Infrastruktur löst einige Sicherheitsbedenken aus, da riesige Mengen an sensiblen Daten übertragen und in großen Datencentern verarbeitet werden müssen. Außerdem kann es vorkommen, dass diese sensiblen Daten an Vermittler ohne volle Zugriffsrechte, weitergegeben werden müssen. [9 Part V S.357]

Viele Sicherheitsprobleme konzentrieren sich auf die neuen Eigenschaften der Cloudentwicklung. Allerdings stellt ihre einzigartige und innovative Natur die Industrie und Entwickler vor immer neue Herausforderungen. [10 Kap 5 S. 37] Auch wenn die Virtualisierung keine Technologie ist, die aus der Cloud hervorkam, sondern eine eigenständige Komponente darstellt, wird ihr durch die Cloud immer mehr Aufmerksamkeit zu teil. Sie ist inzwischen eine der Haupteigenschaften einer Cloud und von extremer Wichtigkeit. Allerdings ermöglicht die Virtualisierung VM (Virtual Machine) zu VM Attacken, aufgrund der VMM (Virtual Machine Management) Schwachstellen.  [10 Kap 5 S. 37]

Laut dem National Institute of Technology (NIST) sind die Bereiche Sicherheit, Interoperabilität und Portabilität die größten Barrieren für den Einsatz von Clouds. Da es bisher nur sehr wenige Standards für Clouds gibt, sind Kunden abhängig von einem Anbieter. Zusätzlich gibt es noch keine Möglichkeit, die in einer Cloud gespeicherten Daten auf eine Cloud eines anderen Anbieters zu übertragen. Diesem Problem könnte man mit sogenannten „Interclouds“ (eine Art Netzwerk von Clouds) entgegenwirken. Interclouds vereinen Interoperabilität, universelles und Utility Computing, sowie Datenspeicherung miteinander. Sie würden die Anbieterabhängigkeiten beseitigen und die freie Datenübertragung zwischen Clouds ermöglichen. Da Clouds via Internet erreicht werden, erben sie alle bekannten Sicherheitsprobleme des Internets. Zusätzlich sind auch neuartige Sicherheitsprobleme durch die Cloud entstanden. [10 Kap. 1.2 S. 5]

Die Tatsache, dass ein Netzwerk und auch seine physischen Bestandteile geteilt werden, ist einer der Hauptgründe, weswegen viele potenzielle Cloud Kunden noch zögern. Sind Clouds und ihre Dienste nicht richtig überprüfbar und nachvollziehbar, sinkt das Vertrauen zwischen Kunde und Anbieter. Das Outsourcen der IT Pflichten an Third Party Cloud Anbieter ist ein Problem, dass noch überwunden werden muss. [10 Kap 5 S. 37] Das Datenoutsourcing bringt viele Vorteile, allerdings wirft es auch einige Datenschutz und Sicherheitsbedenken auf. Tatsächlich sind diese Daten gar nicht mehr unter der direkten Kontrolle des Inhabers, dadurch sind ihre Vertraulichkeit und Integrität einem großen Risiko ausgesetzt. Solche outgesourcten Daten müssen nicht nur vor externen Nutzern, sondern auch vor böswilligen Insidern geschützt sein. In den meisten Fällen sollten externe Server nur für die Erreichbarkeit und das Speichern der Daten sorgen und keine Berechtigungen besitzen, die Daten zu lesen. Solch ein effektiver, praktischer Datenschutz ist sehr komplex und benötigt dementsprechend ein effektives Design. Dieses sollte den Dateninhabern die Möglichkeit liefern, selbst die Anforderungen an den Datenschutz spezifizieren zu können. [9 Kap. 14.1 S.361]

Aufgrund der noch nicht ausgereiften Sicherheit, zögern die meisten Menschen, ihr ganzes Business auf Clouds abzulegen. Das bremst den Fortschritt der Clouds, da sich Forschung und Industrie mehr darauf konzentrieren müssen Sicherheitsprobleme zu beheben, anstatt das Potential der Clouds zu erforschen. Die meisten Menschen sind einfach noch nicht bereit dazu, ihre sensiblen Daten in der Cloud zu speichern. Daraus geht unweigerlich hervor, wie wichtig die Sicherheit ist. [10 Kap. 1.2 S. 5]

Durch große Risiken wie Datenverluste, Datenenthüllungen und die dadurch entstehenden finanziellen Verluste, steht viel auf dem Spiel. Clouds bieten einige ansprechende Features und Vorteile, aber solange die Sicherheitsrisiken nicht besser verstanden sind, werden sich die wichtigsten Firmen und Kunden zurückhalten. Clouds sind daher risikoreich für alle Beteiligten: Kunden, Firmen und Investoren.  [10 Kap. 1.2 S. 5]

Um schneller auf diesem Gebiet voranzukommen, sollten sich Studien und Untersuchungen nicht mehr nur noch auf vereinzelte Probleme beziehen. Es muss die komplette Breite der Cloud Sicherheitsprobleme betrachtet und analysiert werden, um das Vertrauen in Clouds stärken zu können. [10 Kap 5 S. 37]

 ![](/assets/Herausforderungen.png)
 
Abbildung 1: Herausforderungen und Probleme von Clouds und ihre Relevanz entsprechend der International Data Corporation (IDC) und zugehörige Ergebnisse der Cloud User Survey [10 Fig. 1 Kap 1.2 S. 6]

## Interessante verwandte Arbeiten

In der Industrie aber auch in der Literatur genießt das Thema Cloud Sicherheit immer mehr Beliebtheit. Einige verschiedenste internationale Konferenzen haben sich ausschließlich darauf konzentriert. Darunter fallen Organisationen wie die Association for Computer Machinery (ACM) Workshop on Cloud Computing Security, die International Conference on Cloud Security Management und die einzige europäische Konferenz, Secure Cloud, die bereits drei Auflagen veröffentlicht hat. Das steigende Interesse beschränkt sich längst nicht mehr auf wissenschaftliche Veröffentlichungen oder Konferenzen, inzwischen befassen sich auch internationale Magazine und Zeitschriften mit diesem Thema. Die Untersuchung in (12) z.B. befasst sich mit Sicherheits- und Datenschutzangelegenheiten von Cloud Anbietern. Die Sicherheit wurde in Hinblick auf Erreichbarkeit, Vertraulichkeit, Datenintegrität, Kontrolle und Prüfungseigenschaften diskutiert. Beim Datenschutz lag der Fokus auf veralteten Datenschutz Vorgängen, die Informationen nicht mehr vor Regierungen oder third-parties beschützen können. Außerdem wurden die multi-location Probleme von Clouds besprochen. Es ist eine Grundvoraussetzung, zu wissen in welchem Land sich die Daten befinden. [10 Kap 2 S. 7]

In der Untersuchung (13) standen erneut die Aspekte Vertraulichkeit, Datenschutz, Integrität und Erreichbarkeit unter Betrachtung. Als Lösungsansatz dieser Untersuchung wurde eine vertrauenswürdige third-party Lösung vorgeschlagen, um Sicherheitsbedrohungen auf Vertraulichkeit, Integrität, Authentizität und Erreichbarkeit auszumerzen. Der Ansatz kombiniert Public Key Infrastructure (PKI), das Lightweight Directory Access Protocol (LDAP) und Single Sign-On (SSO). Die Prämisse der Untersuchung war es darzulegen, dass die Vorteile der Cloud den Defiziten überlegen sind. [10 Kap 2 S. 7]

Eine andere Studie zielte auf die Sicherheitsprobleme der Cloud Modelle ab. (20). Jedes Modell wurde einzeln betrachtet, um dabei die signifikantesten Schwachstellen, Bedrohungen und Risiken zu finden. Es ist auffällig, dass das Software as a Service (SaaS) Modell die Mehrheit an Problemen hervorbrachte. [10 Kap 2 S. 7]

Die Sicherheit und Datenschutz Themen wurden erneut in (14) diskutiert. Vertraulichkeit, Integrität, Verantwortung und Datenschutz wurden als die signifikantesten Attribute identifiziert. Zu jeder Eigenschaft wurden Sicherheitsprobleme, mit zugehörigen Verteidigungslösungen, beschrieben. [10 Kap 2 S. 7]

In (15) sind einige Sicherheitsherausforderungen als Schlüsselthemen spezifiziert. Diese Themen beziehen sich auf Ressourcenvergabe, Systemüberwachung und Protokollierung, Computer forensic, Virtualisierungen, Multi Vermietungen, Authentifizierung und Autorisierung, Erreichbarkeit und Cloud Standards. Die Untersuchung konzentrierte sich danach auf die Service Level Agreements (SLAs). [10 Kap 2 S. 7]


## Wichtige Konzepte der Cloud Sicherheit

Da Clouds auf Virtualisierungstechniken basieren, ist es wichtig diese zu identifizieren und beschreiben und zu wissen, welche Elemente das Rückgrat der Virtualisierung bilden. Nutzer können auf speziell für die Cloud entwickelte Applikationen zugreifen. Daher ist es umso wichtiger, dass bei der Software besonders auf die Sicherheit geachtet wird. [Kap 3.4 ab S. 11] Die wichtigsten Cloud Sicherheitskonzepte sind: Virtualisierung, multi-tenancy, Cloud Software, Daten Outsourcing, Datenspeichersicherheit und Standardisierung und Vertrauen. Diese werden näher beschrieben in [10 Kap 3.4 ab S. 11]

## Generelle und Coud Spezifische Probleme

Unter das Wort Sicherheitsproblem fallen viele Probleme wie Schwachstellen, Bedrohungen, Lücken, Angriffe und Risiken. Bedrohungen sind Situationen, die Schwachstellen ausnutzen. Schwachstellen sind Defekte oder Schwächen eines Systems, wie bei einer Lücke. Der Angriff beschreibt die Tat, welche eine vorhandene Bedrohung auszunutzt. Ein Risiko beschreibt die Wahrscheinlichkeit, dass jemand eine Schwachstelle ausnutzt. Die meisten Personen verstehen den Unterschied zwischen generellen und cloud spezifischen Problemen nicht. [10 Kap 3.5 S. 13-14] Clouds basieren stark auf den Möglichkeiten, die durch verschiedene Core Technologien, wie Web Applikationen, die Cloud Dienst Modelle, Virtualisierungen und kryptografischen Mechanismen, bereitgestellt werden. Ein Cloud spezifisches Sicherheitsproblem kommt im Wesentlichen aus einer Core Technologie. Sie haben ihre Wurzeln in einem der fünf essentiellen Charakteristiken, welche von NIST vorgeschlagen wurden. Die fünf Charakteristiken sind On-demand self-service, Broad network access, ressource pooling, rapid elasticity und measured service. Um einen besseren Überblick über die Sicherheitsprobleme zu bekommen, sollte man versuchen sie zu kategorisieren. Die Studie [59] teilt Sicherheitsprobleme in drei Hauptbereiche ein: Sicherheitskategorien, Sicherheitsdimensionen und Sicherheit in Dienstleistungsmodellen. Sicherheitskategorien variieren vom Cloud Kunden zum Anbieter und Sicherheitsdimensionen enthalten Domains, Risiken und Bedrohungen. [10 Kap 3.5 S. 13-14]

## Cloud-Modelle und ihre Sicherheit

Die immer steigende Bandbreite treibt die Entwicklung des Web 2.0 und damit einhergehende neue Klassen an Diensten voran. Cloud Systeme bestehen aus einer three-Model Architecture. Diese drei Stufen sind Infrastructure as a Service (IaaS), Platform as a Service (PaaS) und Software as a Service (SaaS). [10 Kap 3.1 S. 8]

IaaS beschäftigt sich mit der Investition der Geschäftsleute in die IT Infrastruktur. Anstatt große Mengen in Hardware und technisches Personal zu stecken, stellt IaaS virtuelle Server zur gebrauchten Zeit bereit. Amazon Web Services (AWS) ist ein passendes reales Beispiel für solch einen Anbieter, dabei zahlt der Kunde nur das was er auch braucht. Das IaaS Model stellt eine grundlegende Sicherheit, durch Perimeter Firewalls und Auto Balancing, bereit. Der Anbieter sollte aber die Sicherheit des Virtual Maschine Managers (VMM) gewährleisten. [10 Kap 3.1 S. 8]

PaaS liefert Kunden die Möglichkeit ihre eigenen Cloud Applikationen, durch bereitgestellte Plattformen und Frameworks, zu entwickeln. Im Gegensatz zu SaaS liefert PaaS mehr Flexibilität in Sachen Sicherheit, da kundenfertige Features bereitgestellt sind. Allerdings können durch unsicher integrierte Integrated Development Environments (IDEs) und Application Programming Interfaces (APIs) mehr Sicherheitslücken entstehen. [10 Kap 3.1 S. 8]

SaaS erlaubt Applikationen auf Clouds zu hosten, um Anforderungesressourcen in Form von Diensten via Internet zu liefern. In diesem Modell tauchen die meisten Sicherheitsprobleme auf, die in den meisten Fällen die Datenspeicherung betreffen. Cloud Anbieter müssen sicherstellen, dass Nutzer keine Möglichkeiten haben, die Daten anderer Nutzer zu verstehen oder Zugriff zu bekommen. [10 Kap 3.1 S. 9]

Diese drei Modelle bilden den Grundstein von Clouds. Allerdings fließen sie immer mehr zu einer Art Anything as a Service (XaaS) zusammen, weil sie virtuell unendlich sein können und daher alles und jeden in Form von Diensten unterstützen können. [10 Kap 3.1 S. 9]

## Sicherheit der Datenzentren

Clouds sind Computersysteme in speziell designten Räumen, um die massive Anzahl an Servern und Netzwerken unterzubringen. Diese Räume werden in Hinsicht auf geologische und umwelttechnische Aspekte wie Ort, Temperatur, Luftfeuchtigkeit und Erdbeben gebaut. Auch politische, regierungstechnische und energiesparende Aspekte spielen eine große Rolle. [10 Kap 3.2 S. 9]

## Sicherheitsprobleme identifiziert von Organisationen

Cloud Sicherheit interessiert nicht nur Entwickler sondern auch Unternehmen. Die folgenden Arbeiten waren bahnbrechend für die Cloud Sicherheit (16).[10 Kap 4.1 S. 15]

TheGartner veröffentlichte das Dokument mit dem Namen „Assessing the Security Risks of Cloud Computing“ (17). Das Dokument beschreibt sieben Sicherheitsrisiken mit denen sich Kunden auseinandersetzen sollten, bevor sie sich einem Anbieter gegenüber verpflichten. Die sieben Risiken sind Nutzerzugriff, Einhaltung gesetzlicher Vorschriften, Datenstandort, Datentrennung, Wiederherstellung, Nachforschungsunterstützung und Langzeitfähigkeit. [10 Kap 4.1 S. 15]

Die European Network and Information Security Agency (ENISA) ist verantwortlich für Cyber Sicherheitsprobleme in der EU und veröffentlichte das Dokument „Cloud Computing: Benefits, Risks and Recommendations“. (18) Acht Cloud spezifische Risiken werden hier als Top Risiken definiert, auch aus Sicht der Kunden. Sie sind Regierungsausfall, Ausschaltsperre, Isolationsfehler, Übereinstimmungsrisiken, Management Schnittstellen Gefährdung, Datenschutz, unsichere unvollständige Datenlöschung und böswillige Insider. [10 Kap 4.1 S. 15]

Die Cloud Security Alliance (CSA) veröffentlichte das Dokument „Top Threats to Cloud Computing“.(19) Es beschreibt Top Bedrohungen, echte Beispiele und Abhilfemaßnahmen. Die folgende Tabelle zeigt die Bedrohungen und die betroffenen Service Modelle. [10 Kap 4.1 S. 15]

 ![](/assets/TopBedrohungen.png)
 
Tabelle 1: Top Bedrohungen des Cloud Computing beschrieben von der CSA [10 Table 1 Kap 4.1 S. 15]

 ![](/assets/Hauptcharakteristiken.png)
 
Tabelle 2: Zusammenfassung der Hauptcharakteristiken von Cloud Entwicklungsmodellen, Zuständigkeit (Organisation O, Third-Party (TP) or both (B)), Management (O, TP or B), Standort (Off-site, On-site or B), Kosten (Low, Medium, High) und Sicherheit (Low, Medium, High), VPC steht für Virtual Private Cloud [10 Table 2 Kap 4.1 S. 16]

## Einleitung in die Überwachung

Das Netzwerkmanagement entwickelt sich stetig weiter und ist inzwischen riesig und komplex. Es gibt hunderte an Software und Hardware Produkten, die Administratoren helfen, Netzwerke zu überwachen und zu steuern. Zusätzlich gibt es auch hunderte an Tools, die die volle Kontrolle über Netzwerke garantieren. Die Netzwerküberwachung ist sehr strategisch. Sicherheit, Performanz, Verlässlichkeit und viele Klassen an Diensten müssen 24/7 überwacht werden.[11 Kap 22.1 S. 565] Es spielt längst nicht mehr nur noch die Überwachung eine Rolle. Zusätzlich optimiert man den Datenfluss und den Datenzugriff in einer sich ständig ändernden Umgebung. Dienste und Tools sind zahlreich vorhanden und variieren je nach Umgebung in der sie analysieren. Fehlermeldungen und ungewöhnliche Ereignisse können dem Admin durch E-Mails, SMS, Warnungen oder Alarmen mitgeteilt werden. Die Netzwerküberwachung macht nur Sinn, wenn man auch die richtigen Dinge überwacht. Dazu zählen z.B. die SLA Metriken und Sicherheitsbedingungen. Normalerweise werden Bandbreite, Verbrauch, Applikationsperformanz, Serverperformanz und Datenverkehr untersucht. [11 Kap 22.1 S. 565]

Netzwerküberwachungssysteme können inzwischen Switches, Router, Server, Desktops, backbone devices, Netzwerkpunkte, Telefone und mehr überwachen. Sie zeichnen automatisch Geräteaktivitäten auf. Die Funktionen unterscheiden die Geräte anhand von IP Adressen, Diensten, Arten (Switch, Router, etc.) und dem physischen Standort. Es ist ein offensichtlicher Vorteil, in Echtzeit zu wissen was genau passiert. [11 Kap 22.1 S. 566]

## Überwachung und Kontrolle in der Cloud

Das Messen, Überwachen und Analysieren ändert sich, sobald die Umgebung und Dienste outgesourced werden. Cloud Computing ist anders als die bisherigen angebotenen Dienste. Das liegt daran, dass Eigenschaften wie Betrieb, Elastizität, gemessene Dienste und universeller Zugriff komplexer sind. Ohne geeignete Metriken ist das Hosten von IT Diensten auf öffentlichen, privaten oder hybriden Clouds problematisch. Vereinheitlichte Sichtbarkeit, Kontrolle und Verständnis der kompletten Cloud Infrastruktur sind unerlässlich für die Überwachung der Cloud. [11 Kap 22.2 S. 567] Es gibt zwei Seiten der Cloudüberwachung. Zum einen die Überwachung der Kern Infrastruktur, zum anderen das Überwachen der kompletten Dienste und ihrer Metriken, um die gewünschte Qualität beizubehalten. Die Überwachung der Kern Infrastruktur kann durch Cloud Ebenen abgegrenzt werden. Hier können allerdings Konflikte zwischen den Interessen von Kunde und Anbieter entstehen. Die Überwachung der Dienste kann mithilfe von Metriken stattfinden. Ein Problem an dieser Überwachung ist, dass Cloud Anbieter ungenaue und irreführende Reports dieser Metriken angeben. [11 Kap 22.2 S. 567]

## Überwachung und Kontrolle der Cloud Ebenen

Laut der CSA kann Cloud Computing in die folgenden sieben Ebenen eingeteilt werden: Facility(F), Network(N), Hardware(H), OS(O), Middleware(M), Application(A) und User(U). Die folgende Abbildung veranschaulicht diese Ebenen: [11 Kap 22.2.1 S. 567]

 ![](/assets/CloudEbenen.png)
 
Abbildung 2: Cloud Ebenen, Implementierungsmodelle, Anbieter- vs. Kundenkontrolle [11 Fig 22.1 Kap 22.2.1 S. 568]

Die Kunden können abhängig von dem Implementierungsmodell, die Cloud bis zu einem gewissen Grad überwachen und kontrollieren. 

In SaaS gibt es eine Nutzerebene, die von Cloud Kunden überwacht und kontrolliert werden soll. Die anderen Ebenen werden komplett vom Anbieter gehandhabt. [11 Kap 22.2.1 S. 568]

In PaaS gibt es eine Nutzer-, Applikations- und Middleware Ebene für den Kunden. In Diesem Modell, kann darüber verhandelt werden, wer die Middleware Ebene kontrolliert und überwacht. Die anderen Ebenen werden wieder vom Anbieter überwacht. [11 Kap 22.2.1 S. 569]

In IaaS gibt es eine Nutzer-, Applikations-, Middleware und OS Ebene für den Kunden. In Diesem Modell kann darüber verhandelt werden, wer für die OS Ebene zuständig ist. Die anderen Ebenen werden wieder vom Anbieter überwacht. [11 Kap 22.2.1 S. 569]

## Ausblick auf zukünftige Möglichkeiten der Sicherheit in Clouds

Im Folgenden werden kurz drei Möglichkeiten der zukünftigen Sicherheit in Clouds beschrieben.

### Datenverschlüsselung

Eine mögliche Lösung wäre es, die Daten die auf dem Server gespeichert werden sollen, zu verschlüsseln. Selbst wenn der Server bereits kompromittiert ist, schützt die Verschlüsselung die Daten vor Enthüllungen. Es gibt bereits Methoden, die externen Servern ermöglichen, Befehle und Queries mit verschlüsselten Daten, auszuführen. [9 Kap. 14.2 S.362]

### Fragmentation zum Schutz vertraulicher Daten

Komplette Datensets zu verschlüsseln bringt aber auch Nachteile mit sich. Es ist nicht immer möglich, Queries und Zustände effizient auf diesen verschlüsselten Datensets auszuführen. Neueste Ansätze liefern eine Möglichkeit, die Datenvertraulichkeit mithilfe von Fragmentationen zu schützen und somit die Verschlüsselungen zu limitieren. [9 Kap. 14.3 S.371]

### Datenintegrität schützen

Es ist auch wichtig, Mechanismen zu entwickeln, die die Integrität und Authentizität der Daten schützt. Nutzer und Organisationen sind immer abhängiger von Daten, die für den täglichen Betrieb gebraucht werden. Ein externer Server muss also garantieren können, dass die gespeicherten Daten in keiner Art und Weise verändert werden. Außerdem muss der Server richtige Antworten auf Queries liefern. [Kap. 14.4 S.379-380] Die Integrität kann auf den folgenden verschiedenen Ebenen gewährleistet werden: Tabellen, Attribute, Tupel und Zellen. Tabellen und Attribute können nur verifiziert werden, wenn der Kunde die komplette Tabelle oder Zeile erhält. Verifizierungen auf der Zellenebene leiden stark unter einem Verifizierungs-Overhead. Um die Integrität der Daten zu wahren, wird empfohlen mit digitalen Signaturen zu arbeiten. Dabei signiert der Inhaber jedes Tupel mit seinem privaten Schlüssel und die Signatur wird mit dem Tupel verkettet. Diese Verkettungen werden dann verschlüsselt. Bei Erhalt der verketteten Tupel, kann der Empfänger überprüfen ob die Signatur mit den Tupels, unautorisierte Veränderungen beinhaltet. Ein Nachteil dieser Methode ist, dass die Verifizierungskosten für den Klienten linear mit der Menge an Tupeln steigen. [9 Kap. 14.4.1 S.380]

