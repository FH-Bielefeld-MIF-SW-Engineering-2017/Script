# Scheduler Agent Supervisor Pattern

Das Pattern dient dazu Aufgaben und Abfolgen von Aufgaben in der Cloud auszuführen und zu Koordinieren.

Cloud bedeutet dabei, dass mehrere Systeme am Ausführen von Aufgaben beteiligt werden.
Aufgaben sind dabei Prozesse die auf andern Systemen ausgeführt werden. Die Aufgaben werden
nicht direkt innerhalb der Komponenten des Patterns eingebettet sondern durch z.B. URLs in externen System aufgerufen.

Durch den Einsatz des Patterns soll insbesondere im Fehlerfall, beim Absturz des Supervisors
oder beim Fehlschalgen einzelner Aktionen, ein definierter Zustand wiederhergestellt werden (Self-Healing).

Das Pattern beinhaltet 3 Zuständigkeiten (Actors):
- Scheduler
- Agent
- Supervisor

Durch den **Scheduler** wird die Reihenfolge der Ausführung der Aufgaben festgelegt. Weiterhin wird der derzeige Zustand der Aufgabe festgehalten,
welche Teilschritte ausgeführt wurden und in welchem Zustand sich die derzeitige Teilaufgabe befindet. Der Supervisor speichert den Zustand der aktuellen Ausführung in
einer Datenbank dem "State-Store".

Dieser State-Store bietet ein Protokoll über den Zustand der der aktuellen Aufgabe, er bietet aber auch die Möglkichkeit die Ausfürhrung bestimmter Aufgaben nach einem Absturz
oder Neustart fortzusetzen.

Der **Agent** koordiniert den Aufruf der konkreten Aufgabe. Er Prüft den Zustand einer Aufgabe und kann den Scheduler anweisen bestimmte Aktionen erneut auszuführen.
Er entspricht im wesentlichen dem Proxy-Pattern mit der Erweiterung von Timeouts und kommunikation mit einem bekannten Scheduler. Der Agent ist möglich generisch zu halten
er sollte keine Kentniss des aktuellen Geschäftsvorgangs haben.

Der **Supervisor** benutzt den Agent um den Status einer Teilaufgabe abzufragen und dem Scheduler zugänglich zu machen.

Im Kontext von Cloud-Anwendungen ist die Koordinierung der Aufgaben besonders wichtig, insbesondere ist es wichtig, dass Aufgaben nicht mehrfach Ausgeführt werden. Um dies Sicherzustellen muss zusätzlich
zum Scheduler Agent Supervisor Pattern auf das Leader Election Pattern zurückgegriffen werden. Pro Aufgabe muss ein Scheduler ausgemacht werden der für diese spezifische Aufgabe verantwortlich ist.

Um korrekte Ergebnisse der ausgeführten Aktionen zu erhalten sollten diese Indempotent sein. Sollte dies nicht möglich sein muss ein Mechanismus für Transaktionen (Ein Rollback im Fehlerfall muss gewährleistet sein) innerhalb der Aufgaben oder der Aktoren integriert sein.