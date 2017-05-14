# Asynchronous Messaging Primer

Der Nachrichtenaustausch ist einer der Schlüsselfunktionen von verteilten Systemen. Dieser ermöglicht es Applikationen und Diensten miteinander zu Kommunizieren und zu kooperieren und hilft dabei skalierbare und belastbare Systeme zu entwerfen. (vgl. S. 166)

## Queue-Grundlagen

Innerhalb von Cloud-Technologien ist der Nachrichtenaustausch häufig in Form von Queues (Warteschlagen) implementiert. Diese unterstützen meist folgende drei Operationen: Ein Absender kann eine Nachricht in die Queue legen, ein Empfänger kann diese Nachricht untersuchen oder sie aus der Queue entnehmen. (vgl. S. 166)

### Senden und Empfangen von Nachrichten mithilfe einer Queue

Eine Queue kann man sich tatsächlich wie eine Warteschlange vorstellen. Der Absender hängt hinten an die Warteschlange neue Nachrichten an, die der Empfänger von der anderen Seite abarbeitet (FIFO-Prinzip). Versucht ein Empfänger aus einer leeren Queue eine Nachricht zu entnehmen, so wird diese Operation geblockt. Häufig ist es den Empfängern auch möglich zu Prüfen ob Nachrichten zur Verfügung stehen, sodass das Blocken umgangen werden kann. (vgl. S 166)

Die Infrastruktur der Queue muss dafür sorgetragen, dass eine einmal hineingelegte Nachricht nicht verloren geht. (vgl. S. 166)

Queus sind ideal für das asynchrone Arbeiten zweier oder mehrerer Dienste. Nach dem Ablegen einer Nachricht in einer Queue, kann sich der Absender anderen Aufgaben widmen. Zusätzlich werden Queues häufig in Verbindung mit mehreren Sendern und Empfängern eingesetzt.

### Grundlegende Message-Queue-Patterns

**One-way messaging** ist die einfachste Form der Implementierung. Absender legen Nachrichten in eine Queue die anschließend von  Empfängern bearbeitet werden. Es findet keine Überprüfung statt, ob die Nachrichten tatsächlich irgendwann von einem Empfänger bearbeitet werden. (Vgl. S. 168)

Beim **request/response messaging** erwartet der Absender eine Rückmeldung des Empfängers, dass die Nachricht verarbeitet wurde. Die Antwort der Empfänger wird in eine Absender-Spezifische Queue gelegt (jeder Absender hat eine eigene Queue für die Antworten). Erfolgt innerhalb einer bestimmten Zeit keine Antwort, kann ein Empfänger entsprechende Maßnahmen einleiten (z.B. erneutes Senden der Nachrichten). (Vgl. S. 168)

![ResponseMessaging](../assets/Response-Messaging.png) Abbildung 1: Request/Response Messaging [[Cloud Design Patterns, S. 168]](https://www.google.de/url?sa=t&rct=j&q=&esrc=s&source=web&cd=7&ved=0ahUKEwjBp_bjh-rTAhWIZVAKHR05CSYQFghMMAY&url=https%3A%2F%2Fdownload.microsoft.com%2Fdownload%2FB%2FB%2F6%2FBB69622C-AB5D-4D5F-9A12-B81B952C1169%2FCloudDesignPatternsBook-PDF.pdf&usg=AFQjCNGfN9eRS1NDFxLihCC4R3k-mvGmvg&sig2=yScohHzNzZ06OrbI6Lr51Q&cad=rja "Cloud Design Patterns").

**Broadcast messaging** wird eingesetzt wenn mehrere Empfänger die gleiche Nachricht erhalten sollen. Der Absender legt seine Nachrichten in eine Haupt-Queue, von der diese Nachrichten dann in Empfängerspezifische Queues umkopiert werden. 

![Broadcast](../assets/Broadcast.png) Abbildung 2: Broadcast Messaging [[Cloud Design Patterns, S. 169]](https://www.google.de/url?sa=t&rct=j&q=&esrc=s&source=web&cd=7&ved=0ahUKEwjBp_bjh-rTAhWIZVAKHR05CSYQFghMMAY&url=https%3A%2F%2Fdownload.microsoft.com%2Fdownload%2FB%2FB%2F6%2FBB69622C-AB5D-4D5F-9A12-B81B952C1169%2FCloudDesignPatternsBook-PDF.pdf&usg=AFQjCNGfN9eRS1NDFxLihCC4R3k-mvGmvg&sig2=yScohHzNzZ06OrbI6Lr51Q&cad=rja "Cloud Design Patterns").


### Scenarien für asynchronen Nachrichtenaustausch (Auswahl)

**Decoupling workloads:** Das Trennen des Aufrufens einer Aktion von dessen tatsächlicher Durchführung (Beispiel: Ein Anwender ruft eine Aktion über eine Website auf, dessen Durchführung erfolgt jedoch auf einem Application-Server). (Vgl. S. 169)

**Temporal decoupling: **Sender und Empfänger können zu unterschiedlichen Zeiten arbeiten. Ein Empfänger kann Nachrichten auch verarbeiten, wenn der Sender nicht zur Verfügung steht. (Vgl. S. 169)

**Load balancing: **Es kommen verschiedene Empfänger auf mehreren Servern zum Einsatz. Die Architektur ist durch das hinzufügen weiterer Server skalierbar . (Vgl. S. 169)

**Load leveling: **Beim Erhalten vieler Nachrichten zur gleichen Zeit wird das System nicht direkt in die Höchstleistung getrieben. Der Queue-Mechanismus sorgt für ein langsames Steigen der Anfragen, sodass dem System die Möglichkeit geboten wird, sich den Gegebenheiten Anzupassen. (Vgl. S. 170)

**Cross-platform integration: **Das Zusammenspiel verschiedener Software-Systeme kann über eine Queue erleichtert werden. Eine Queue kann so implementiert werden, dass die Interaktion vollkommen System- und Sprachenunabhängig ist. Es bedarf lediglich einer Definition von Schnittstellen und des Formats der Nachrichten. (Vgl. S. 170)

### Überlegungen zur Implementierung von asynchronem Nachrichtenaustausch (Auswahl)

**Message ordering:** Die Reihenfolge der Nachrichten kann in machen Software-Systemen eine Rolle spielen. Nicht in allen Queues wird eine bestimmte Abarbeitungs-Reihenfolge garantiert. Das "Priority Queue Pattern" realisiert einen Mechanismus der das Abarbeiten bestimmter Nachrichten vor anderen umsetzt (Priorisierung). (Vgl. S. 171)

**Message grouping:** Typischerweise sollen Nachrichten innerhalb einer Queue unabhängig sein. In manchen Fällen lassen sich die Abhängigkeiten allerdings nicht vollkommen eliminieren. In diesem Fall sorgt "Message Grouping" für das Abarbeiten zusammengehöriger Nachrichten durch den gleichen Empfänger. (Vgl. S. 171)

**Idempotency:** (Idempotenz) beschreibt, dass die mehrfache Durchführung einer Operation mit den gleichen Daten immer zum gleichen Ergebnis führt. Im Bezug auf den Nachrichtenaustausch ist gemeint, dass auch wenn eine Nachricht fehlerhafterweise mehr als einmal empfangen und bearbeitet wird, die mehrfache Ausführung keine Auswirkungen auf das System hat. (Vgl. S. 171)

### Verwandte Entwurfsmuster und Empfehlungen (Auswahl)

**Autoscaling Guidance:** Sobald die Anzahl der Nachrichten innerhalb der Queue eine bestimmte Schwelle unter- oder überschreitet, kann es sinnvoll sein einen Teil der Empfänger ab- bzw. hinzuzuschalten. (Vgl. S. 172)

**Circuit Breaker Pattern:** Wenn ein Empfänger oder Sender sich wiederholt nicht mit der Queue verbinden kann, ist es Sinnvoll weitere Versuche zu unterbinden, bis der Fehler gefunden respektive behoben wurde. Dieser Mechanismus wird mit dem "Circuit Breaker Pattern" realisiert. (Vgl. S. 172)

**Scheduler Agent Supervisor Pattern:** Der Nachrichtenaustausch ist häufig Teil eines größeren Workflows. Das Scheduler Agent Supervisor Pattern beschreibt, wie der Nachrichtenaustausch genutzt werden kann um Aktionen innerhalb von verteilten Systemen zu koordinieren, sowie andere verteilte Ressourcen sinnvoll zu nutzen. (Vgl. S. 173)