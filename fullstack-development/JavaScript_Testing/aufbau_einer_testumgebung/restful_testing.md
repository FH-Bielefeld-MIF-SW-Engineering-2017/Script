## 3.7 RESTful API Test
Mit den in den vorherigen Kapiteln vorgestellten Technologien lassen sich ebenfalls RESTful API Tests durchführen. Es ist sinnvoll für jede API Methode einen Test zu schreiben. Es können ebenfalls schnelle native Tests mit beispielsweise Postman durchgeführt werden, in denen ein simulierter Request abgeschickt wird und das Ergebnis als JSON dargestellt wird, jedoch bieten diese nicht den Umfang, welcher mit Unit Tests möglich ist. So kann beispielsweise bei Negativ und Positiv Tests, auf bestimmtes Verhalten geprüft werden. Ebenfalls ist es sehr aufwendig, bei Veränderungen der Applikation die Requests neu in Postman umzusetzen. [25](../Quellen.md)
```javascript
describe('/GET model', function() {
      it('should return all the models', (done) => {
        chai.request(server)
            .get('/model')
            .end((err, res) => {
                res.should.have.status(200);
                res.body.should.be.a('array');
              done();
            });
      });
    });
```
In diesem mit Mocha und Chai erstelltem Testbeispiel wird zuallerst ein Request aufgebaut, indem die Route und der anzusprechende Server mitgeteilt wird. Wenn eine Response ankommt, wird diese analysiert. In diesem Fall wird der Status der Antwort und der Datentyp des Bodys überprüft. Hierbei wird ein Array erwartet, da diese Route eine Liste aller Models zurückliefern sollte. [25](../Quellen.md)
