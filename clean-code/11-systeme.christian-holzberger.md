#  11 Systeme

Die Erstellung von Software ist nicht nur auf das schreiben von Code beschränkt. Die organisation des Codes ist von der Anwendung getrennt. Einzelne Bestandteile des Codes werden in einem System benutzt um bestimmte Ziele zu erreichen. Es ist nicht erwünscht, dass jeder Teil des Codes so wenig wie möglich über die Umgebung in der er eingesezt wird "weiß".

## Abhängigkeiten

Die organisation der Funktionseinheiten sollte ohne Rücksicht auf die konkrete Umsetzung, ohne zu viel "Level of Detail" erreicht werden. z.B. ist es nicht gut wenn eine Klasse Ihre Abhängigkeiten (Datenbankverbindung, etc.) selber erzeugt.

### Seperation of Main

Eine Möglichkeit um Abhänigkeiten zu Isolieren ist es, alle Komponenten innerhalb der Main Methode zu Inistialisieren und dann den jeweiligen abhängigen Klassen als Konstruktor-Argument mitzugeben. 

Hierbei verläßt man sich darauf, dass die Main-Methode keinen Fehler bei der Initalisierung macht und die Abhängkleiten über die Laufzeit des Programms gültig bleiben.

### Factories

Um den Zeitpunkt der Erstellung weiterhin der jeweiligen Klasse zu überlassen, können Factories eingesetzt werden. Factories stellen Methoden bereit die bestimmte Abhängkeiten zum Anfragezeitpunkt erzeugen. 

Dabei bleibt der konkrete Vorgang der erzeugung vor dem Aufrufer versteckt.

### Dependency Injection (DI)

Das Dependency Injection Pattern geht mit dem Inversion of Control (IoC) Pattern einher. Die benötigten Resourcen werden ausserhalb der Klassen erstellt und durch einen Mechanismus in die Klasse injeziert. Die Klasse findet die benötigte Abhängigkeit in einer Ihrer Instanzvariablen vor, ohne die Abhängigkeit selber zu Initalisieren. Diese Vorgehensweise gibt jegliche Kontrolle an den DI-Mechanismus ab, daher spricht man von Inversion of Control. Die Anwendung steuert alle Logik die benötigt ist um Abhängigkeiten bereitzustellen.

## Wenn Systeme wachsen

Die beschreibene Art Abhängigkeiten zu Injezieren funktionieren gut wenn es sich um Domain-Speziische-Objekte handelt. Alle Objekte sind hier am erreichen eines (Geschäfts-)Ziels beteiligt. Es gibt allerdings auch Funktionalität die über die "Domain" hinweg eingesetzt werden muss (z.B. Persistenz). Diese Anforderung führt dazu, dass bestimmte Teile des Codes immer wieder verwendet werden. Diese Art der Anforderung wird "Cross-Cutting Concern" genannt.

Um Cross-Cutting Concerns abzubilden sollte man sich einer form der Aspektortierten Programmierung (AOSP) bedien.

### Proxies

Das Proxy-Pattern beitet beschränkte Möglichkeit bestimmte Aspekte eines Systems zu Kapseln. Die Persistenz eines POJO (Plain Old Java Object) kann durch einen MySQLProxy erreicht werden. Diese  Proxy kümmert sich lediglich darum das Objekt in einer Datenbank abzulegen und reicht alle sonstigen Anfragen direkt an das Objekt weiter.

Der Aspekt der Persistenz wurde dann in das Proxy-Object verlagert. 

Proxies müssen explizit eigesetzt werden und können nicht zentral gesteuert werden. Sie machen es schwer die Qualität des Codes herzustellen oder zu erhalten.

### Aspect Oriented Programming

Durch den einsatz von AOP Frameworks kann ein System deklarativ erweitert werden. Die Cross-Cutting Concerns können zentral gesteuert werden und an bestimmte Objekte gebunden werden (z.B. bestimmte Objekt werden immer in die Datenbank geschreiben). Diese Frameworks gibt es in verschiedener Qualität.

## Weitere Methoden

Im folgenden werden weitere Wege beschreiben die man beim erstellen komplexer Systeme beachten sollte.

### Optimize Decision Making

Entscheidungen sollten zu dem Zeitpunkt getroffen werden an dem sie für das System relevant werden. Frühzeitig getroffene Entscheidungen führen zu einem suboptimalen System, da das Problem noch nicht vollständig erkannt ist.

### Use Standard when they add Demostratable Value

Standards sollten dann eingesetzt werden wenn sie dem System einen echten nutzen hinzufügen. Viel Technologie wird bei Ihrem erscheinen gehyped und bietet wenig nutzen. Die Archtitektur macher Standards entwickelt sich eher von echten Anwendungsfällen weg.

### Domain Specific Languages 

Programimersprachen bieten viele Features. Sie bieten viele verscheidene Anwendungsmöglichkeiten und Frameworks. Allerdings bietet diese Flexibilität auch Nachteile. Das erstellen einer Sprache die nur für den jeweiligen, konkreten, Anwendungsfall geeigneit ist bietet Vorteile bei der Zusammenarbeit mit fachgebietsspeziefischen Experten. Diese müssen sich nicht in eine große Programmiersprache einarbeiten sondern haben eine kleine Sprache in der spezifische Befehle für genau eine Domäne hinterlegt sind.