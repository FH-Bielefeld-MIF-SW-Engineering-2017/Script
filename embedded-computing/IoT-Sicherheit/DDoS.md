## Distributed Denial of Service (DDoS)
Ein großes Problem für das gesamte Internet sind DDoS-Angriffe (Distributed Denial of Service), wobei schlecht gesicherte
Geräte, die am Internet hängen, in ein großes Botnetz übernommen werden und gleichzeitig ein oder mehrere Ziele angreifen.

Eine mögliche Form des DoS-Angriffs ist hierbei das so genannte "SYN-Flooding", bei dem viele TCP-Verbindungsaufbauanfragen
an den Zielserver geschickt werden, ohne auf die Antworten des Servers zu reagieren. Da bei einem TCP-Verbindungsaufbau
ein Drei-Wege-Handshake stattfindet, bei dem zuerst ein Client ein TCP-SYN-Paket an den Server schickt, welcher mit einem
SYN-ACK-Paket antwortet und ein Bestätigungspaket (ACK-Paket) vom Client erwartet. Der Server wartet eine gewisse Zeit
auf das Bestätigungspaket vom Client und speichert deshalb die Anfragedaten des Clients in einem Puffer solange ab, bis entweder die
Timout-Zeit abgelaufen ist oder der Client geantwortet hat. Da die Puffer nur begrzent groß sind,
können diese schnell voll laufen, wenn Clients viele TCP-Verbindungsaufbauanfragen senden, aber nicht die Bestätigungsnachricht
senden, wenn der Server diese anfordert. So muss der Server für jede neue Verbindung warten, bis die eingestellte Timeout-Zeit
abgelaufen ist, bis die Anfrage wieder aus dem Puffer entfernt werden kann. Ist der Puffer voll, kann der Server keine neuen
Verbindungen aufbauen und ist somit für andere Clients nicht mehr erreichbar. [5](quellen.md)

![TCP-Handshake](/assets/TCP-Verbindungsaufbau.png)
*TCP-Verbindungsaufbau*

Eine weitere Form von DoS-Angriffen ist der so genannte "Smurf-Angriff", bei dem von einem Angreifer sehr viele ICMP-Nachrichten mit
Ping-Request an die Broadcast-Adresse des Netzwerks geschickt werden. Als Absenderadresse wird der Zielrechner angegeben, der angegriffen werden soll.
Alle Rechner in dem Netzwerk empfangen die Ping-Pakete und antworten mit Request-Paketen, die an den Zielrechner geschickt werden.
Dadurch erzeugt der Anreifer, der selbst nur wenige Pakete verschickt, ein so großes Datenaufkommen, dass der Zielrechner
überlastet werden kann. [5](quellen.md)
