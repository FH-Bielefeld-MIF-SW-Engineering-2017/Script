## Probleme
Ein großes Problem für das gesamte Internet sind DDoS-Angriffe (Distributed Denial of Service), wobei schlecht gesicherte
Geräte, die am Internet hängen, in ein großes Botnetz übernommen werden und gleichzeitig ein oder mehrere Ziele angreifen.

Eine mögliche Form des DoS-Angriffs ist hierbei das so genannte "SYN-Flooding", bei dem viele TCP-Verbindungsaufbauanfragen
an den Zielserver geschickt werden, ohne auf die Antworten des Servers zu reagieren. Da bei einem TCP-Verbindungsaufbau
ein Drei-Wege-Handshake stattfindet, bei dem zuerst ein Client ein TCP-SYN-Paket an den Server schickt, welcher mit einem
SYN-ACK-Paket antwortet und ein Bestätigungspaket (ACK-Paket) vom Client erwartet. Der Server wartet eine gewisse Zeit
auf das Bestätigungspaket vom Client und speichert deshalb die Anfragendaten des Clients solange ab, bis entweder die
Timout-Zeit abgelaufen ist oder der Client geantwortet hat. Da Server nur begrenzte Puffer für neue TCP-Verbindungen haben,
können diese schnell voll werden, wenn Clients viele TCP-Verbindungsaufbauanfragen senden, aber nicht die Bestätigungsnachricht
senden, wenn der Server diese anfordert. So muss der Server für jede neue Verbindung warten, bis die eingestellte Timeout-Zeit
abgelaufen ist, bis die Anfrage wieder aus dem Puffer entfernt werden kann. Ist der Puffer voll, kann der Server keine neuen
Verbindungen aufbauen und ist somit für andere Clients nicht mehr erreichbar. [5](quellen.md)

![TCP-Handshake](img/TCP-Handshake.png)

Eine weitere Form von DoS-Angriffen ist der so genannte "Smurf-Angriff", bei dem von einem Angreifer sehr viele ICMP-Nachrichten mit
Ping-Request an die Boradcast-Adresse des Netzwerks geschickt werden. Als Absenderadresse wird der Zielrechner angegeben, der angegriffen werden soll.
Alle Rechner in dem Netzwerk empfangen die Ping-Pakete und antworten mit Request-Paketen, die an den Zielrechner geschickt werden.
Dadurch erzeugt der Anreifer, der selbst nur wenige Pakete verschickt, ein so großes Datenaufkommen, dass der Zielrechner
überlastet werden kann. [5](quellen.md)

Mit steigender Geräteanzahl und Leistungsfähigkeit der Geräte nimmt auch die mögliche Bandbreite für DDoS-Angriffe zu.
Ein großes Problem ist, dass Hersteller
bei der Entwicklung von Produkten nicht gut genug auf die Sicherheit achten. Viele Konsumenten achten bei dem Kauf von neuen
Geräten weniger auf die Sicherheit und mehr auf die Leistungsfähigkeit und Features des Produktes. Somit haben Hersteller
andere Prioritäten bei der Entwicklung und Herstellung neuer Produkte, da sie mit sichereren Geräten nicht mehr verkaufen.

Ein weiteres Problem ist, dass viele Hersteller, die früher nichts mit der Entwicklung von Elektronik und Software zu tun
hatten (und so auch wenig Erfahrung haben), plötzlich bei dem Trend "IoT" mitmachen wollen und ihre Produkte nun mit
einer Internetanbindung ausstatten, ohne grundlegende Sicherheitsmaßnahmen zu bedenken. So implementieren viele Hersteller
zum Beispiel keinen Updatemechanismus über den wichtige Sicherheitspatches eingespielt werden können. Auch die
unverschlüsselte Übertragung von Daten ist ein großes Risiko. Angreifer können Logindaten einfach abgreifen und Geräte damit
für ihre Zwecke einspannen. [4](quellen.md)
