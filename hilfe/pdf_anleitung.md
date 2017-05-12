# PDF Anleitung

## Linux:

#### Installation:

**Nodejs** wird benötigt \([https://wiki.ubuntuusers.de/Node.js/](https://wiki.ubuntuusers.de/Node.js/)\)

`sudo ln -s /usr/bin/nodejs /usr/bin/node` \(Symlink wird nicht bei allen Distributionen benötigt\)

**Gitbook Package** Installation:

`(sudo) npm install gitbook-cli -g`

`(sudo) npm install gitbook-pdf -g`

**Phantomjs** könnte evtl. Fehler bei der Installation ausgeben deswegen ggf. nachinstallieren \([https://gist.github.com/julionc/7476620](https://gist.github.com/julionc/7476620)\)

der **Ebook-Converter von Calibre** wird dafür verwendet \([https://wiki.ubuntuusers.de/Calibre/](https://wiki.ubuntuusers.de/Calibre/)\)

#### Verwendung:

`gitbook pdf '/pfad zu dem Dateien' '/Speicherpfad der PDF/mybook.pdf'` \(" ' " nur bei Leerzeichen im Pfad nötig\)

z. B. `gitbook pdf /Gitbook/Library/fh-bielefeld-mif-sw-engineerin/script /Gitbook/Library/fh-bielefeld-mif-sw-engineerin/script/mybook.pdf`

