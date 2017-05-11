# Cache-Aside Pattern

Das Cache-Aside Pattern beschreibt ein Verfahren, nach dem häufig benötigte Daten für den schnellen Zugriff in einem Cache
zwischengespeichert und bei Bedarf aktualisiert werden.
Der Ablauf ist wie folgt: Das System greift zuerst auf den Cache zu und prüft, ob die gewünschten Daten im Cache vorhanden
sind. Ist dies nicht der Fall, so werden die Daten aus dem eigentlichen Speicher (Datebank, etc.) geladen und im Cache für
weitere Zugriffe gespeichert.
Werden Änderungen an den Daten durchgeführt, so werden die Änderungen im Speicher übernommen und der entsprechende Cache-Eintrag
wird als ungültig markiert, damit bei einem weiteren Zugriff die Daten neu aus dem Speicher geladen werden.

Beim Umsetzen diese Patterns sollte eine Gültigkeitsdauer der Daten im Cache festgelegt werden. Daten, die eine längere Zeit
nicht abgerufen wurden, müssen aus dem Cache entfernt werden, um Platz für Daten zu schaffen, die häufiger benötigt werden.
Diese Gültigkeitsdauer sollte nicht zu kurz gewählt werden, sonst werden die Daten ständig neu aus dem Datenspeicher geladen.
Bei der Wahl der Gültigkeitsdauer sollte aber auch die Zeit, die benötigt wird, um ein bestimmtes Datum aus einem Datenspeicher
zu holen, beachtet werden. So sollte zum Beispiel ein Datum, dass in einer externen Datenbank liegt, die sehr langsam ist, länger
im Cache verbleiben als ein Datum, dass in einer Datenbank auf demselben Server liegt und somit schneller geladen werden kann.
Ein sehr wichtiger Punkt ist, dass Daten im Datenspeicher durch eine externe Anwendung geändert werden können und die Kopie
der Daten im Cache damit nicht mehr gültig ist. Die Anwendung, die den Cache verwendet, merkt die Änderung erst beim erneuten Laden
der Daten aus dem Datenspeicher.
Verwenden mehrere Anwendungen die gleichen Daten, so sollte man sich die Verwendung von geteilten Caches überlegen, bei der
meherere Anwendungen gemeinsam auf einen Cache zugreifen. Beim Start der Anwendung kann außerdem der Cache mit Daten
gefüllt werden, die wahrscheinlich während des Startens benötigt werden.

Das Cache-Aside-Pattern sollte eingesetzt werden, wenn der Bedarf von bestimmten Daten nicht vorhersagbar ist und quasi
zufällig ist.
Für statische Daten oder für Session-Daten in Client-Server-Anwendungen sollte das Pattern nicht eingesetzt werden.
