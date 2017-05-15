# Spezielle Gebiete zum Software Engineering Script

Dies ist das gemeinsam erstellte Modul Script zu den Themen, die im Sommersemester 2017 an der FH-Bielefeld im Modul behandelt wurden.

Anleitung:

* die Texte werden mit Mardown erstellt
* pro Kapitel wird eine Datei erstellt und nicht eine Datei pro Person
* pro Buch existiert eine Datei, in der die wichtigsten Eckdaten stehen und evtl. eine kleine Einleitung oder Zusammenfassung
* daraus ergibt sich folgende Struktur pro Buch:

  * buchname.md
  * buchname \(Ordner\)
  * buchname/kapitelnummer\_kapitelname.vorname\_nachname
  * Beispiel:
    * co-economy\_wertschoepfung\_im\_digitalen\_zeitalter.md
    * co-economy\_wertschoepfung\_im\_digitalen\_zeitalter \(Ordner\)
    * co-economy\_wertschoepfung\_im\_digitalen\_zeitalter/1\_connectedness.fabian\_lorenz.md
    * co-economy\_wertschoepfung\_im\_digitalen\_zeitalter/2\_colaboration.fabian\_lorenz.md
    * co-economy\_wertschoepfung\_im\_digitalen\_zeitalter/3\_cases.lutz\_winkelmann.md
    * ...
  * assets/bildname.png (o. *.jpg ...) (Bildordner)

* um das ganze einheitlich zu gestallten folgende Formatierung innerhalb der Kapitel:

  * Kapitelüberschrift in H1 \(z. B. \# 3 Cases\)
  * Unterkapitel in H2 \(z. B. \#\# 3.1 Die neue Sharing Economy\)
  * Abschnittsüberschriften in H3 \(z. B. \#\#\# Technologien und Innovationen\)
  * Bilder einfügen \(z. B. \!\[Alternativer Bildtext\] \(/assets/bildname.png\) \(Abbildung 1: Bildbeschriftung\))

* es wird nur noch mit Github gearbeitet und nicht mehr auf dem GitBook direkt

* jeder arbeitet auf einem eigenen Branch \(z. B. "florenz" und nicht master branch\)
* dieser wird per pull request an github geschickt und vom Admin gemerget bzw. mit Kommentar abgelehnt, falls etwas nicht passt
* auf gitbook kann man sich die aktuelle Version ansehen \(sobald der merge durchgeführt wurde\)

* um die Seitenzahl herauszufinden, falls jemand einen Markdown Editor verwendet, der das Dokument nicht als PDF anzeigen:

  * im Chrome-Browser rechte Maustaste
  * Drucken
  * nach PDF exportieren
