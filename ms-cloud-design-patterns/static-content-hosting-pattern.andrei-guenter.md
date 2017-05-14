# Static Content Hosting Pattern

Im Folgenden wird das Static Content Hosting Pattern beschrieben, welches dazu dient Ressourcen effizienter zu verwalten, wenn statische Elemente von Servern zur Verfügung gestellt werden.

## Problemstellung

Web-Applikationen beinhalten im Normalfall einige Elemente mit statischem Inhalt. Dieser statische Inhalt kann in Form von HTML-Seiten und anderen Ressourcen, wie Bildern oder Dokumenten vorliegen. Clients können entweder über den Aufruf der HTML-Seite oder über einen direkten Download auf diese statischen Elemente zugreifen. Dies führt dazu, dass der Webserver Anfragen zum Bereitstellen statischer Inhalte verarbeiten muss und somit Rechenzeit nutzt, um die Inhalte zu instanziieren. Diese Rechenzeit lässt sich minimieren, indem statische Inhalte ausgelagert werden.

## Abhilfe

In vielen cloudbasierten Systemen ist es möglich die zur Laufzeit erstellten statischen Instanzen zu minimieren, indem statische Instanzen auf einem Speicherdienst zum Abruf bereitgestellt werden. Die Kosten für Speicherdienste sind im Gegensatz zu den Kosten für Rechenzeit auf cloudbasierten Systemen wesentlich geringer. Das folgende Schaubild bietet einen Überblick in das Konzept des Static Content Hosting Pattern:

![](https://github.com/FH-Bielefeld-MIF-SW-Engineering-2017/Script/tree/master/assets/StaticContentHostingPatternOverview.png)

## Herausforderungen und Überlegungen

Beim Implementieren dieses Design-Patterns ist folgendes zu beachten:

* Der gehostete Speicherdienst muss einen HTTP Endpunkt auflösen können, damit Benutzer auf den statischen Inhalt zugreifen können. Und Einige Speichergeräte unterstützen HTTPS, falls statische Ressourcen SSL erfordern.
* Für eine maximale Performance und Verfügbarkeit sollte ein "Content Delivery Network" in Betracht gezogen werden. Dieses nutzt eine Zwischenspeicherung der Inhalte an mehreren Datenzentren und ist dadurch allerdings mit zusätzlichen Kosten verbunden.
* Durch das Duplizieren der Daten an verschiedenen Datenzentren kann sich die IP-Adresse ändern, die URL bleibt jedoch erhalten.
* Die Komplexität der Applikation steigt, da Daten gestreut vorzufinden sind und damit ist auch ein erhöhter Aufwand für das Verwalten der Daten verbunden.
* Speicherdienste 
* Die Rechte für den öffentlichen Zugriff in "Storage Container" müssen korrekt verwaltet werden um bspw. unbefugte Uploads zu verhindern. Um anonyme Zugriffe zu verhindern sollte ein Valet Key oder ein Valet Token genutzt werden: [Valet Key Pattern](valet-key-pattern.marvin-schirrmacher.md).

## Wann sollte das Pattern genutzt werden?

Das Pattern ist ideal geeignet, um:

* Kosten für das Hosting von Webseiten und Applikationen mit statischen Inhalten zu minimieren.
* Kosten für das Hosting von Webseiten zu minimieren, wenn diese ausschließlich aus statischen Inhalten bestehen.
* statische Inhalte für Applikationen bereitzustellen, welche auf anderen Hosts \(oder "on-premises"\) betrieben werden.
* Inhalte an mehreren geographisch verteilten Standorten mit Hilfe eines "Content Delivery Networks" zu speichern.
* Kosten und Nutzung der Bandbreite zu überwachen, da sich Host- und Laufzeitkosten von Speicherkosten der statischen Inhalte trennen lassen.

Das Pattern ist nicht geeignet, wenn:

* Applikationen die statischen Inhalte manipulieren, bevor die Inhalte an Clients ausgeliefert werden. Beispielsweise wenn Applikationen einen Zeitstempel auf ein Dokument aufsetzen, direkt bevor es heruntergeladen wird.
* nur sehr wenig statischer Inhalt zu verwalten ist.



