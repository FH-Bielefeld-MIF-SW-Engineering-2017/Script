## Rest
### Protokollübersicht
Der Begriff des Representational State Transfer (REST) wurde von Roy T. Fielding in seiner Dissertation (2000) eingeführt [9](Quellen.md). Gemeint ist damit ein Programmierparadigma für verteilte Systeme. Darin wird die Struktur und das Verhalten des World Wide Webs abstrahiert. Mit Hilfe dieser Abstraktion ist es möglich einen Architekturstil zu schaffen, der die Anforderungen des modernen Webs besser darstellt. Strukturell basiert REST auf einer klassischen Client Server Architektur – der Server stellt einen Dienst bereit, der bei Bedarf vom Client aufgerufen werden kann. Die Ressourcen, die der Server bereitstellt, werden vom Client mittels einer URI (Uniform Resource Identifier) adressiert und abgerufen. Das zugrundeliegende Protokoll ist http [10](Quellen.md).

REST nutzt vier Operationen des http Protokolls um einem Client Zugriff auf die Ressourcen des Servers zu bieten: 

| Funktionalität | http-Verb | URI |
| ------------- | ------------- | ------------- |
| Ressource anlegen | POST | http://example.org/picture |
| Ressource aktualisieren | PUT | http://example.org/picture/123 |
| Ressource abfragen | GET | http://example.org/picture/123 |
| Ressource löschen | DELETE | http://example.org/picture/123 |

Einer der wichtigsten Eigenschaften des REST Protokolls ist die Zustandslosigkeit jeder Interaktion zwischen Client und Server. So speichert der Server keinerlei Zustandsinformationen zu einem Client, dieses hat zur Folge, dass bei jeder Interaktion alle nötigen Informationen zu der Anfrage übergeben werden müssen. Die Anfrage ist also in sich geschlossen. Diese Eigenschaft sorgt dafür, dass ein REST Service gut skalierbar ist, sodass Anfragen bei viel Last auf andere Server verteilt werden können [11](Quellen.md).
### Sicherheit
Ein normaler REST Service ohne weitere Absicherungen kann verwendet werden, wenn keine Authentifikation durch den User nötig ist. Falls diese doch erforderlich ist, kann das REST Protokoll durch die darunterliegenden Protokolle abgesichert werden. So kann zum Beispiel durch die Verwendung von HTTPS die gesamte Kommunikation des REST Protokolls abgesichert werden [12](Quellen.md).

### IoT Verwendung
Da Protokoll kann zwar tendenziell im IoT verwendet werden, allerdings fehlen einige hilfreiche Features wie zum Beispiel das bestehen lassen einer Verbindung. 
