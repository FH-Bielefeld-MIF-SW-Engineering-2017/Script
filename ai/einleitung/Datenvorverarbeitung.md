## Datenvorbereitung

In den meisten Fällen (abhängig von der Datenquelle) sind rohe Textdaten nicht gut formatiert, nicht standardisiert und nicht strukturiert.
Mithilfe  von diversen Techniken aus dem Bereich des _text-preprocessing_ sollen die Daten in definierte Sequenzen aus linguistischen Komponenten umgewandelt werden,
welche eine standardisierte Struktur und Notation haben. <sup id="fn1_1">[[1]](#fn1)

### Methodenübersicht

Nachfolgend werden einige wohlbekannte Methoden mit einer kurzen Beschreibung aufgelistet. Die Verwendung dieser Methoden, sowie deren Reihenfolge,
ist von der Anwendung bzw. der Domäne abhängig: <sup id="fn1_2">[[1]](#fn1)

**Text Bereinigung:** Oftmals beinhalten rohe Textdaten unbekannte und/oder unnötige Token und Zeichen, welche für weitere Verarbeitungen entfernt
werden sollten. Beispielsweise sind HTML-Tags oder bestimmte Daten von XML- oder JSON-Strukturen nicht Notwendig.

**Text Tokenisierung:** Üblicherweise werden Textdaten für weitere Verarbeitungsschritte in Token (Einheiten der Wortebene, z. B. Wörter, Sätze oder Absätze) extrahiert.
Beispielsweise ist eine sehr einfache Variante einen Text auf Basis der Leerzeichen zu Tokenisieren. In Abhängigkeit von der Domäne, kann dieser
Prozess komplexer sein.

**Entfernung von Speziellen Zeichen:** Einige Zeichen sind für weitere Verarbeitungsschritte hinderlich. Beispielsweise sind Satzzeichen oder
Sonderzeichen in vielen Anwendungen zu entfernen. Die Domäne muss berücksichtigt werden: Eventuell könnten Smilies, bestehend aus speziellen zeichen,
für die Anwendung von Bedeutung sein.

**Kontraktionen erweitern:** Mit Kontraktion ist die Zusammenziehung zweier oder mehr Wörter zu einem Wort gemeint (Bspw.: "you will" -> "you'll").
Die Erweiterung von Kontraktionen in ihre Wortbestandteile kann in vielen Anwendung Notwendig sein. Sprachen haben üblicherweise Listen von Kontraktionen,
welche angewendet werden können.

**Umwandlung von Groß- und Kleinbuchstaben:** Die Umwandlung von Zeichen in Groß- oder Kleinbuchstaben macht viele Anwendung einfacher: Beispielsweise
das matchen von Wörtern. Die Umwandlung von Textdaten in Groß- oder Kleinbuchstaben ist üblicherweise eines der ersten Schritte in der Datenvorverarbeitung.

**Entfernung von Stoppwörtern:** Stoppwörter sind Wörter, welche in der Anwendung nur eine kleine oder keine Bedeutung haben.
Es gibt keine universelle Liste von Stoppwörtern, jede Sprache und Domäne hat ihre eigenen Listen. Typische Stoppwörter der Englischen Sprache sind
beispielsweise _a, the, me_ und so weiter.

**Wortkorrektur:** Die Korrektur von Wörtern gehört zu den größten Herausforderungen im Bereich der Datenvorverarbeitung von Textdaten.
Zu der Korrektur von Wörtern gehören u. a. das Verbessern von falsch geschriebenen Wörtern und Zeichen Wiederholungen. Oftmals ist das Verbessern
kontraproduktiv: In Abhängigkeit von der Domäne können Zeichen Wiederholungen beispielsweise einen intensiven emotionalen Ausdruck unterstreichen (finallllyyyyyy), welche
für eine weitere Verarbeitung von bedeutung sein könnten.

**Stammformreduktion:** Stammformreduktion (Stemming) ist das Zurückführen von verschiedene morphologische Varianten eines Wortes auf den Wortstamm ("having" -> "have").
Stammformreduktionen werden für eine verbesserte Verarbeitung von Textdaten angewendet.

**Lemmatisierung:** Mithilfe von Lemmatisierungs Verfahren werden Wörter auf ihre Grundform zurückgeführt ("better" -> "good").

### Verwendete Methoden für Twitter Datensätze

Die nachfolgenden Methoden wurden für das Projekt angewendet:

1. Text Bereinigung: Tweets können HTML-Tags beinhalten um u. a. Wörter hervorzuheben. Mit der wohlbekannten Python Web-Scraping Library _Beautifulsoup_ werden für dieses Projekt
sämtliche relevanten Inhalte ausgelesen und HTML-Tags ausgelassen.
2. Text Tokenisierung: Tweets beinhalten viele Domänen spezifische Zeichenketten, welche als Tokens eine Bedeutung haben, bspw.: Smilies, @-Mentions, Hashtags, und so weiter.
Das _Natural Language Toolkit (NLTK)_ beinhaltet u. a. eine Tokenisierungs Funktion für Tweets, welche im Rahmen dieses Projekts verwendet wird.
3. Kontraktionen erweitern: Für die Sentimentanalyse ist die Erweiterung von Kontraktionen von Bedeutung, um u. a. Negierungen als einzelne Tokens 
hervorzuheben ("won't" -> "will not").
4. Entfernung von Speziellen Zeichen: Mithilfe des Attributs _string.punctuation_ werden in der Python Anwendung alle Token Entfernt, welche aus
einer Interpunktion bestehen.
5. Entfernung von Stoppwörtern: Das bereits erwähnte NLTK beinhaltet eine Liste von Stoppwörtern der Englischen Sprache. Sämtliche TOkens, welche
aus einem dieser Stoppwörter bestehen, werden entfernt.
6. Stammformreduktion: Für dieses Projekt wird eine Stammformreduktion anstatt Lemmatisierung verwendet. Der Grund ist, dass die Grundformen von Wörtern
die emotionalen Ausdrücke abschwächen könnten. In der Sentiment Analyse ist dies jedoch von Bedeutung.

___

<b id="fn1"></b>1. Sarkar, D.: Text Analytics with Python. Apress (Herausgeber) (2016) [↩](#fn1_1)[↩](#fn1_2)
