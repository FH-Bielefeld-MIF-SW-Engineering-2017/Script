# Scheduler Agent Supervisor Pattern

Das Pattern dient dazu Aufgaben in der Cloud auszuführen und zu Koordinieren. 
Cloud bedeutet dabei, dass mehrere Systeme am ausführen von Aufgaben beteiligt werden.
Durch den Einsatz des Patterns soll vorallem im Fehlerfall, beim Absturz des Supervisors 
oder beim Fehlschalgen einzelner Aktionen, ein definierter Zustand wiederhergestellt wird (Self-Healing). 

Eine Aufgabe wird definiert durch eine Remote URL, einen Timeout. ... tbd

Das Pattern beinhaltet 3 Zuständigkeiten: 
- Scheduler
- Agent 
- Supervisor 

Durch den Scheduler wird die Reihenfolge der Ausführung der Aufgaben festgelegt. Weiterhin wird der derzeige Zustand der Aufgabe festgehalten, 
welche Teilschritte ausgeführt wurden und in welchem Zustand sich die derzeitige Teilaufgabe befindet. Der Superviros speichert den Zustand der aktuellen Ausführung in 
einer Datenbank dem "State-Store".
... was passiert beim Absturz

Der Agent koordiniert den Aufruf der konkreten Aufgabe. Er Prüft den Zustand einer Aufgabe und kann den Scheduler anweisen bestimmte Aktionen erneut auszuführen. 
Er entspricht im wesentlichen dem Proxy-Pattern mit der Erweiterung von Timeouts und kommunikation mit einem bekannten Scheduler. Der Agent ist möglich generisch zu halten 
er sollte keine Kentniss des aktuellen Geschäftsvorgangs haben.

Der Supervisor benutzt den Agent um den Status einer Teilaufgabe abzufragen und dem Scheduler zugänglich zu machen. 

Im Kontext von Cloud-Anwendungen ist die Koordinierung der Aufgaben besonders wichtig, insbesondere ist es wichtig, dass Aufgaben nicht mehrfach Ausgeführt werden. Um dies Sicherzustellen muss zusätzlich 
zum Scheduler Agent Supervisor Pattern auf das Leader Election Pattern zurückgegriffen werden. Pro Aufgabe muss ein Scheduler ausgemacht werden der für diese spezifische Aufgabe verantwortlich ist.
