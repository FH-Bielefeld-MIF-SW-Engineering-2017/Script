**Was ist Autoscaling?**

Autoscaling ist ein dynamischer Prozess der Ressourcen so ver-/ bzw. einteilt, dass eine Applikation die Anforderungen an Performance und die SLAs (service level aggreements) erfüllt. Häufig ist er ein automatisierter Prozess, der kontinuierlich die Performance überprüft und entscheided, ob Ressourcen hinzu oder entfernt werden sollen. Autoscaling bestimmt sämtliche Ressourcen, nicht nur Rechenressourcen.

**Scaling Arten**

 *Vertikales Skalieren* umfasst das Umstrukturieren der Lösungen durch den Einsatz verschiedener Hardware. In einer Cloud stellt veritkales Skalieren bessere Ressourcen zur Verfügung und überträgt das System auf diese. Durch vertikales Skalieren wird ein System häufig zeitweise nicht erreichbar sein.

 *Horizontales Skalieren* setzt das System auf zusätzliche Ressourcen auf, dabei kann das System ohne Unterbrechung weiterlaufen. Elemente die das System mit einbeziehen, können auf diesen zusätzlichen Ressourcen verfügbar gemacht werden und je nach Bedarf wieder runtergefahren werden. Viele Cloud Systeme nutzen diese Art des Skalierens.
 
 **Implementierung einer Autoskalierungsstrategy**
 
 Umfasst typischerweise die folgenden Prozesse und Komponenten:
 
 - Einfangen der Schlüssel Performance und Sckalierungsfaktoren wie z.B. Antwortzeiten, Warteschlangenlänge, Speichernutzung, etc
 - Überwachungskomponenten
 - Entscheidungslogik die anhand der überwachten Skalierungsfaktoren entscheid ob skaliert wird oder nicht. Hierbei spielt die Zeit eine wichtige Rolle.
 - Ausführungskomponenten die für Aufgaben verantwortlich sind. Sie nutzen typischerweise Tools und Skripte für:
     - Versorgung mit Ressourcen
     - Rekonfigurierung des Systems
 - Testen und Validieren der Strategy

Immer häufiger werden Cloud Systeme mit einem Build-in tooling ausgestattet, um bei der Implementierung des Autoscalings zu helfen. 

**Gesichtspunkte für das Implementieren von Autoscaling**

Autoscaling bietet keine sofortige Lösung, einfach nur Ressourcen oder mehr Instanzen eines Prozesses hinzufügen garantiert keine Performancesteigerung. Folgende Punkte sollten in Betracht gezogen werden:

- Das System sollte horizontal Skalierbar sein. Vermeiden von Instanzähnlichkeiten, keine Codelösungen, die immer in einer spezifischen Instanz eines Prozesses laufen. Anfragen derselben Quelle werden nicht immer der selben Instanz zugeteilt. Autoscaling kann zusätzliche Instanzen eines Dienstes hinzufügen! 
- Langanhaltende Aufgaben sollten horizontale und vertikale Skalierung unterstützen. Ohne entsprechende Beachtung könnten Instanzen von Prozessen nicht sauber heruntergefahren werden oder sogar Daten verlieren. Idealerweise wird bei solch langanhaltenden Aufgaben die Abwicklung in kleinere Stücke aufgeteilt. Das "Pipes and Filters Pattern" zeigt ein Beispiel für die Umsetzung. 
- Beinhaltet die Lösung mehrere Elemente wie Web Rollen, Arbeiter Rollen und andere Ressourcen, dann sollten diese Elemente als Einheit skaliert werden. Es ist wichtig, die Beziehung der Elemente zu verstehen und sie in Gruppen aufzuteilen.
- Um exzessives horizontales Skalieren zu vermeiden, sollten man dem Autoscaling Grenzen setzen. Autoscaling ist nicht der beste Mechanismus um plötzlichem Arbeitsaufwand entgegenzuwirken, da es Zeit braucht um Instanzen zu starten oder Ressourcen hinzuzufügen. (Throttling Pattern)
- Überwachen und Aufzeichnen von Details jedes Autoscaling Prozesses. Mithilfe dieser Informationen kann die Effektivität der Strategy gemessen werden.

**Autoscaling in einer Windows Azure Lösung**

- Das *Windows Azure Autoscaling* unterstützt die üblichen Skalierungsszenarien und man kann mit hilfe des Windows Azure Management Portal Lösungen konfigurieren.
- Die *Microsoft Enterprise Library Autoscaling Application Block* ermöglicht eine Skalierungslösung basierend auf spezifischen Regeln und Performancedaten. Dieser Ansatz ist flexibler und komplexer, braucht aber Code um Performancedaten zu bekommen.
- Die *Microsoft Windwos Azure Monitioring Services Management Library* stellt den Zugang zu den *Windows Azure Monitoring Service* Operationen bereit. Sie beinhaltet eine vereinheitlichte API für das Abrufen und Konfigurieren von Metriken, Warnungen und Autoscaling Regeln der Windows Azure Dienste.

**Benutzen von Windows Azure Autoscaling**

Es gibt die folgenden zwei Möglichkeiten um Windows Azure für das Autoscaling zu konfigurieren:
- basierend auf Metriken wie die durchschnittliche CPU Leistung der letzten Stunde oder das Backloggen von Elementen in einer Mitteilungswarteschlange. Die Parameter des Windows Azure Autoscaling können der Skalierung des Systems angepasst werden. Autoscaling ist kein sofortiger Prozess, es braucht Zeit um auf Metriken zu reagieren. Windows Azure setzt Regeln, die z.B. nur eine Skalierung in einem 5 Minuten Intervall zulässt.
- zeitbasierte Autoskalierung um sicherzustellen, dass Instanzen auch verfügbar sind wenn sie gebraucht werden.

**Verwandte Muster und Richtlinien**

Bei der Verwendung von Autoscaling sind außerdem die Muster "Throttling Pattern", "Competing Consumers Pattern" und die Richtlinien "Instrumentation and Telemetry Guidance" relevant.
