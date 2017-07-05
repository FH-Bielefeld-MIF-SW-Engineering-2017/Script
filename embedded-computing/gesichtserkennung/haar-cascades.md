# Haar Cascades
Paul Viola und Michael Jones entwickelten in ihren Paper "Rapid Object Detection Using a Boosted Cascade of Simple Features" 2001 eine Methode, um mit Hilfe einer Trainingsmenge an positiven (Bilder mit dem Objekt) und negativen Bildern (Bilder ohne Objekt) eines Objektes ein ähnliches Objekt auf einem Bild zu erkennen.[1.4,3-4]

## Das Prinzip
Benötigt werden eine große Menge an positiven und negativen normalisierten Graustufenbildern. Je mehr unterschiedliche Bilder man hat, desto größer ist auch die Genauigkeit der Erkennungsrate. Das Ziel ist es eine Cascade Function herauszuarbeiten, die ein ähnliches oder identisches Objekt auf einem beliebigen Bild erkennen kann. Folgender Flowchart erklärt das Grundprinzip:  
![](/assets/object-detection-flowchart.png)  
*Vorgehensweise für Objekterkennung in OpenCV.[1.4]*  

Im gezeigten Flowchart kann man erkennen, dass man am Anfang ein Set von Bildern hat. Anschließend wird eine Methode namens "Feature Extraction" angewendet. Die Feature Extraction sorgt dafür, dass aus den Bildern mit Hilfe von verschiedenen Haar Featuren (siehe Abbildung) ein Feature Vector extrahiert wird. Dabei werden die Haar Features in verschiedenen Skalierungen auf die Graustufenbilder angewandt. Ein Feature Vector (auf deutsch Merkmalsvektor) ist ein Vektor von Featuren, die ein bestimmtes Muster wiedergeben, das vom Programm als gemeinsames Muster bei einer Mehrheit von Bildern aus dem Bildset erkannt wurde.[1.4, 3]  
![](/assets/haar_features.jpg)  
*Verschiedene Haar Features.[3]*  

Existiert ein solcher Feature Vector kann vom Programm berechnet werden, welche Bilder aus dem Bilderset als positive oder negative Bilder zu klassifizieren sind. Dies erfolgt durch Prüfung der gesammelten Features im Feature Vector. Da man an Rechenzeit sparen möchte, werden nicht alle Features für jedes einzelne Bild durchgegangen, sondern man prüft die Features nacheinander. Sollte ein Feature als negativ erscheinen, wird das Bild als negativ bewertet und es wird zum nächsten Bild im Bildset übergegangen. Hier sieht man, dass das Klassifizieren den Klassifizierungsalgorithmus (Classification algorithm) entspricht und dass die positiven und negativen Bilder die Klassennamen (Class label) sind. Diese könnten beispielsweise "Gesicht" und "KeinGesicht" sein.[3]  
![](/assets/haar.png)  
*Anwendung von Haar Features als Beispiel.[3-4]*  

Als Beispiel in der Abbildung oben sieht man, dass ein Haar Feature im Gesicht erkannt wurde. Im ersten Feature (Bild mitte) wurde erkannt, dass die Region der Augen öfters dunkler ist, als die Region um die Nase und den Wangen. Im zweiten Feature wude erkannt, dass die Augen dunkler sind als die Nasenbrücke.[3]

## Haar-Cascade Umsetzung in OpenCV
Glücklicherweise nimmt OpenCV dabei einiges an Arbeit ab. Es ist für eine Gesichtserkennung in OpenCV nicht notwendig einen eigenen Haarcascade für den Algorithmus anzulernen. OpenCV implementiert im Framework den Algorithmus und hat verschiedene Default Haar Cascades im OpenCV Ordner. Sollte man ein eigenes Objekt erkennen wollen, so ist es notwendig vom Objekt ein eigenes Haar Cascade anzulernen.[1.5] Weiterhin sieht man auch anhand der Haar Features, dass auch hier die Kantenerkennung, die im Kapitel OpenCV kurz erwähnt wurde, eine Rolle spielt.
