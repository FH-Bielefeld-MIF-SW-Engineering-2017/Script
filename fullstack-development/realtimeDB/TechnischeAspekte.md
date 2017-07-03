# Technische Aspekte

Die Echtzeit-Verbreitung der Ereignisse bzw. der aktualisierten Daten findet im Idealfall durch [WebSockets](./../KommunikationInVerteiltenSystemen/WebSocket.md) statt. Als Ersatz bei älteren Client-Anwendungen kann auch das sog. _long polling_ ausreichen.  
_Echtzeit_ in Zusammenhang mit der Kommunikation über das Internet bedeutet: "so schnell wie technisch möglich". Latenzen und Paketverluste können während der Kommunikation auftreten. Bei sehr zeitkritischen Anwendungen kann es notwendig sein, Zeitstempel der Datenbank mit den Nachrichten zu schicken, damit die Client-Anwendungen die Nachrichten besser einordnen und darauf reagieren können.  


Um eine Datenbank zu einer Realtime Datenbank zu erweitern bedarf, es mindestens zwei weiterer Komponenten:  
- Backend-Server mit Unterstützung für WebSockets
- Publish/Subscribe Server


![](/assets/realtime_extension.png)
Abbildung: Veranschaulichung Erweiterung einer beliebigen Datenbank um eine Echtzeit-Komponente


Ereignisse in der Datenbank werden von dem Publish/Subscribe Server erkannt und über die WebSockets propagiert. Ein Publish/Subscribe Server, ist ein Server, der zwischen dem Backend-Server und der Datenbank sitzt und alle Veränderungen der Datenbank entgegennimmt und zum Abonnieren über ein WebSocket zur Verfügung stellt. Als Beispiel für einen Publish/Subscribe Server sei hier Redis genannt. Aber anstatt eine beliebige SQL- oder noSQL-Datenbank um diese durchaus komplexen Komponenten zu erweitern und so zu konfigurieren, dass diese auch gut skalieren, können vorgefertigte Dienste genutzt werden, die nicht nur diese Komponenten zur Verfügung stellen, sondern auch Bibliotheken für diverse Web-Technologien, wodurch die Implementierung der Echtzeit-Komponente für die eigene Anwendung deutlich erleichtert wird.  
Ein durchaus bekannter Dienst, der diese Komponenten bündelt und als _eine_ Realtime Datenbank vermarktet, ist _Firebase Database_.

