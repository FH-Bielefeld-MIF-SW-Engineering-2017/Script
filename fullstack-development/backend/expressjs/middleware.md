# Was ist eine Middleware?
”Middlewarefunktionen sind Funktionen, die Zugriff auf das Anforderungsobjekt (req), das Antwortobjekt (res) und die nächste Middlewarefunktion im Anforderung/Antwort-Zyklus der Anwendung haben. Die nächste Middlewarefunktion wird im Allgemeinen durch die Variable next bezeichnet.“ [1](../quellen.md)

Es wird zwischen verschiedenen Middleware-Typen unterschieden:

## Middleware auf Anwendungsebene
Middlewares auf Anwendungsebene werden direkt an eine Instanz von Express gebunden. Der nachfolgende Ausschnitt gibt ein Beispiel [1](../quellen.md):
```javascript
let app = express();
app.get(’/’, function (req, res, next) { 
    res.send(’Hello World!’);
});
```

## Middleware auf Routerebene
Seit Express.js Version 4.x wurde eine Router-Klasse eingeführt. Im Wesentlichen handelt es sich dabei um eine abgespeckte Variante der Express-Klasse, es können auf die gleiche Weise Middlewares an ein Router-Objekt gebunden werden. Das Router-Objekt wird wiederum wie eine Middleware an das Express-Objekt gebunden. Dies birgt den wesentlichen Vorteil, dass so eine zusätzliche Abstraktionsschicht möglich ist. [1](../quellen.md)
```javascript
let express = require(’express’); 
let router = express.Router();
let app = express();
// routes
router.get(’/’, function (req, res, next) { 
    res.send(’Hello World!’);
});
// bind the routes to the app
app.use(’/route’, router);
```

## Middleware für die Fehlerbehandlung
Fehlerbehandlungen werden wie andere Middlewares an ein Express oder Router Objekt gebunden. Die Callback-Funktion enthält allerdings einen zusätzlichen Parameter ”err“. [1](../quellen.md)
```javascript
app.use(function(err, req, res, next) { 
    console.error ( err ) ;
    res.status(500).send(’Error!’);
});
```

## Integrierte Middleware
Seit Version 4.x besteht keine Abhängigkeite zu ”Connect“ mehr. Alle Middlewarefunktionen, die bislang in Express enthalten waren, wurden nun in separate Module ausgelagert. [1](../quellen.md)

## Middleware anderer Anbieter
Durch zusätzliche Module von Drittanbietern kann die Funktionalität von Express.js erweitert werden. Dies wird hier aber nicht naher erläutert. [1](../quellen.md)

Autor: Niklas Harting