# Beispiel-Applikation
Der folgende Code Aussschnitt zeigt eine komplettes Beispiel für eine simple Express.js Anwendung, welche mit Node.js ausgeführt werden könnte:
```javascript
let express = require(’express’);
let app = express();
app.post(’/’, function(req, res) { 
    res.send(’POST request’);
});
app.get(’/’, function(req, res) {
    res.send(’GET request’); 
});
app.put(’/’, function(req, res) { 
    res.send(’PUT request’);
});
app.delete(’/’, function(req, res) { 
    res.send(’DELETE request’);
});
app.listen(3000, function() { 
    console.log(’Server started at port 3000’);
});
```
