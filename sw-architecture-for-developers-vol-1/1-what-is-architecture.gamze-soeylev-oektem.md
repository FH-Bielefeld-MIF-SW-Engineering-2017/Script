# Technische Führung
## Was ist Softwarearchitektur?
In diesem Teil werden wir sehen, was der Unterschied zwischen Softwareaarchitektur und Softwaredesign ist.

### Was ist Architektur?
Es ist nicht einfach, zu definieren, was Architektur ist. Es gibt zwei Begriffe: Architektur als Substantiv und als Verb.

#### Als Substantiv
Architektur kann als Struktur definiert werden. Es geht um die Dekomposition eines Produkts.

#### Als Verb
Architektur kann auch als Verb verstanden werden. In diesem Fall geht es darum zu verstehen, was man bauen muss und wie man es bauen muss. Hier liegt der Fokus also auf den Anforderungen.

### Architekturtypen
Wenn man verschiedene Menschen fragt, bekommt man viele verschiedene Antworten zum Softwarearchitekturtyp.
Es ist egal, was man baut (Softwaresystem, Netzwerk oder Datenbank), man braucht für eine erfolgreiche Lösung zwei Schritte. Zuerst muss man das Problem verstehen. Dann eine Vision zu erzeugen, die man mit jedem Beteiligten des Produktes kommunizieren kann. Es geht um Struktur und Vision, wenn man über Architektur spricht.

### Was ist Software-Architektur?
#### Applikationsarchitektur
Bei der Applikationsarchitektur geht es um die niedrigeren Stufen (lower levels) des Softwareentwurfs. Meistens gibt es nur eine Technologie (Java, Microsoft .Net, etc.). Die Bauteile beinhalten Programmiersprache, Bibliotheken, Frameworks, etc. Bei der Applikationsarchitektur geht es um die Software und die Organisation des Codes.

#### Systemarchitektur
In einem Softwaresystem gibt es meistens mehrere Applikationen. Diese müssen zusammenarbeiten. Die Mehrheit der Softwaresysteme kommunizieren mit der Aussenwelt, daher sind Interoperability und Integration mit den anderen Systeme sehr wichtig. Zusätzlich ist die Hardware auch wichtig. Die Bauteile beinhalten sowohl Software als auch Hardware (z.B. Programmiersprache, Frameworks, Servers, Infrastruktur). Systemarchitektur ist abstrakter als Applikationsarchitektur.

#### Softwararchitektur
Softwarearchitektur ist die Kombination der Applikation- und Systemarchitektur. Hier geht es um:
- Logging und Exception Handling
- Sicherheit
- Performance, scalability, availability
- Real-world constraint of the environment
- Interoperability/ Integrität,
- Operational, support and maintenance requirements
- ...
Wir müssen also einen allgemeinen Blick auf die Software werfen.

#### Enterprise-Architektur - Strategie statt Code
Bei der Enterprise-Architektur geht es nicht darum, wie Technologie funktioniert, sondern wie Technologie in der Organisation besser benutzt werden kann. Enterprise-Architektur guckt wie man Menschen, Prozesse und Technologien am besten organisiert und einsetzt, damit die Organisation besser und effizienter funktionieren kann.

### Architektur vs. Design
Was ist der Unterschied zwischen Design und Architektur? 
Design und Architektur sind sehr ähnlich. Jede Architektur ist Design, aber nicht jedes Design ist Architektur. Wichtige Entscheidungen im Design-Prozess, also Entscheidungen die man nicht leicht rückgängig machen kann, sind Architektur - alles andere ist Design. Als Architektur gelten:
- Die Systemform (z.B. client-server, web-based etc.)
- Die Struktur des Softwaresystems (z.B. Komponenten, Interaktionen)
- Die Wahl der Technologien (z.B. Programmiersprachen)
- ...

### Ist Softwarearchitektur wichtig?
Guter Code ist nicht immer genug für gute Software. Ein kleines bisschen Architektur hilft um Problemen vorzubeugen.

#### Ein Mangel an Softwarearchitektur verursacht Probleme
Ohne Softwarearchitektur kann man keine gute Softwarestruktur haben. Ohne gute Softwarearchitektur kann unsere Software häufig zu langsam, unsicher, störungsanfällig, schwer zu warten etc. sein.

#### Vorteile von Softwarearchitektur
- Ein klare Roadmap für das Team
- Bessere Koordinierung
- Ein Framework für Risikoidentifizierung
- Eine Struktur um Lösungen gegenüber verschiedenen Zielgruppen zu kommunizieren

#### Braucht jedes Softwareprojekt Softwarearchitektur?
Ja. Nur muss man sich entscheiden, wieviel Softwarearchitektur man braucht. Es hängt von der Grösse und Komplexität des Projekts und der Grösse und Erfahrung des Teams ab.

## Die Rolle der Softwarearchitektur
Softwarearchitekt ist eine Rolle, kein Titel.

#### Architectural Drivers
Ein wichtiger Teil der Rolle als Softwarearchitekt besteht darin, die Geschäftsziele zu verstehen und Anforderungen und Begrenzungen der Umgebung zu managen.

#### Software designen
Beim Softwaredesign geht es darum zu verstehen, wie die Probleme (bzgl. Anforderungen und Begrenzungen) gelöst werden können. Der wichtigste Teil ist die richtige Technologie zu wählen.

#### Technische Risiken
Der beste Entwurf und die beste Technologie bedeuten nicht unbedingt Erfolg. Viele Firmen wählen eine Technologie, um Kosten zu sparen. Eigentlich muss man sich fragen, ob die Technologie macht, was sie machen soll.
Eine Architektur funktioniert, wenn die nicht-funktionalen Anforderungen erfüllt sind. Eine der wichtigsten Probleme von Software ist, dass sie komplex und abstrakt ist. Daher ist es schwer, sich Software vorzustellen. Wenn möglich, sollte man Architektur testen. Insgesamt geht es darum, technische Risiken vorzeitig zu identifizieren und zu managen.

#### Architekturevolution
Architektur sollte sich während des Entwicklungszyklusses weiterentwickeln. Deswegen braucht man kontinuierliche technische Führung für die Architektur.

#### Coding
Manche Firmen wollen nicht, dass ihre Softwarearchitekten Code schreiben. Aber dies ist keine gute Entscheidung. Nur wenn das Projekt sehr gross ist, kann der Architekt keinen Beitrag beim Coding leisten.

#### Qualitätssicherung
Qualitätssicherung ist die wichtigste Aufgabe von Softwarearchitekten. Allerdings wird diese Aufgabe in den meisten Projekten vernachlässigt.

#### Zusammenarbeiten oder scheitern
An einem Softwareprojekt sind viele Personen mit unterschiedlichen Interessen beteiligt. Jede dieser Personen beteiligt sich in gewisser Weise an der Entwicklugn der Softwarearchitektur. Als Softwarearchitekt muss man mit allen, an einem Projekt beteiligten Personen, zusammenarbeiten.

### Sollten Softwarearchitekten Code schreiben?
Softwarearchitekten sollten definitiv Code schreiben.

#### Code schreiben
Der Architekt muss nicht der beste Coder im Team sein. Aber er sollte Code schreiben können. Wenn Softwarearchitekten sich am Code schreiben beteiligen, hilft dies die Lücke zwischen Entwicklung und Architektur zu schliessen.

#### Prototypen, Frameworks und Foundations
Wenn ein Architekt nicht die Möglichkeit hat, Code zu schreiben kann er Prototypen entwickeln. Das hilft dabei eine bessere Kommunikation mit dem Team zu entwickeln und um zu sehen, ob die Architektur funktionieren wird. Ausserdem kann er Frameworks und Foundations für das Team kreieren.

#### Experimentieren und auf dem neuesten Stand bleiben
Der Architekt sollte in seiner Freizeit seine Code-Skills weiterentwickeln und versuchen technologisch auf dem neuesten Stand zu bleiben.

## Softwarearchitekten sollten Baumeister sein
Wenn wir uns anschauen, woher das Wort Architekt kommt, sehen wir, dass es auf Latein Baumeister bedeutet. Baumeister mussten sich beweisen, bevor sie Baumeister werden konnten: Sie mussten zuerst alle anderen Jobs auf dem Bau machen, bevor sie Baumeister wurden. Aber nachdem sie Baumeister wurden hatten sie keine Zeit um diese Arbeiten weiterzumachen. Es gibt viele Parallelen zwischen Baumeistern und Softwarearchitekten.

Man sollte vorsichtig sein, wenn man bei der Entwicklung des Codes hilft. Die Entwickler im Projekt nehmen Personen nicht ernst, wenn sie nicht Softwareentwickler im Projekt sind. Sie können sich auf den Schlips getreten fühlen.

Allerdings gibt es auch Unterschiede zwischen Baumeistern und Softwarearchitekten. Zum Beispiel gibt es bei Softwarearchitekten kein Ausbildungsmodell und im Gegensatz zu den Baumeistern müssen die Architekten in verschiedenen Projekten mit verschiedenen Teams arbeiten. Wir brauchen eigentlich ein Ausbildungssystem für Softwarearchitekten, weil jedes Softwareprojekt einen eigenen Architekten braucht.
