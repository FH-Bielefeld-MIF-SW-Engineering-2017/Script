# Implementierungen

Der Algorithmus Support-Vector-Machine ist in vielen verschiedenen Sprachen verfügbar. Viele greifen intern auf die Bibliothek [libSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) zurück und müssen dadurch nur ein Interface bereit stellen.

### PHP
In php steht ein Interface zu [libSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) zur Verfügung.
Es existiert eine [Dokumentation](http://php.net/manual/de/book.svm.php), die die Installation und Nutzung erklärt.
Dort wurde auch folgendes Beispiel entnommen:

```php
<?php
$data = array(
    array(-1, 1 => 0.43, 3 => 0.12, 9284 => 0.2),
    array(1, 1 => 0.22, 5 => 0.01, 94 => 0.11),
);

$svm = new SVM();
$model = $svm->train($data);

$data = array(1 => 0.43, 3 => 0.12, 9284 => 0.2);
$result = $model->predict($data);
var_dump($result);
$model->save('model.svm');
?>
```

### Python (sklearn)
Das bekannte Machine-Learning-Framework *sklearn* nutzt ebenfalls [libSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/).
Das folgende Beispiel, sowie andere Varianten des SVM-Algorithmus sind zu finden unter der [sklearn SVM Dokumentation](http://scikit-learn.org/stable/modules/svm.html).

```python
from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
clf.predict([[2., 2.]])
```

### Java (weka)

In Java steht SVM über das *weka*-Framework zur Verfügung. Die Dokumentation des Algorithmus, der intern ebenfalls [libSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/) nutzt, ist [hier](https://weka.wikispaces.com/LibSVM#Reference%20(Weka)) zu finden.


### NodeJS

Für NodeJS lässt sich der Support-Vector-Machine Algorithmus über den Packet Manager *npm* installieren.
Die Dokumentation des Paketes und das hier aufgeführte Beispiel ist unter [diesem Link](https://www.npmjs.com/package/node-svm) verfügbar.
Die Implementierung nutzt intern ebenfalls libSVM.

```javascript
var svm = require('node-svm');
var xor_data = [
    [[0, 0], 0],
    [[0, 1], 1],
    [[1, 0], 1],
    [[1, 1], 0]
];
var clf = new svm.CSVC();
clf.train(xor_data).done(function () {
    // predict things 
    xor_data.forEach(function(ex){
        var prediction = clf.predictSync(ex[0]);
        console.log('%d XOR %d => %d', ex[0][0], ex[0][1], prediction);
    });
});
 ```
 
 ### MatLab
 MatLab ist bei vielen mathematischen Anwendungen ein beliebtes Programm. Besonders zum Visualisieren von Funktionen ist es hervorragend geeignet.
 Eine Implementierung des SVM-Algorithmus ist ebenfalls enthalten: 
 [fitcsvm](https://de.mathworks.com/help/stats/fitcsvm.html) .
 Mit MatLab lassen sich nicht nur die Datenpunkte als Grafik plotten, sondern auch die Trennebenen, die der SVM-Algorithmus findet, visualisieren.