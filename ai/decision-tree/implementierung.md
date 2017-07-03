# Implementierung

Das Projekt verwendet für die Implementierung der Klassifizierungs Algorithmen die _Scikit-learn_ Library<sup id="fn1_1">[[1]](#fn1)</sup>, welche eine  wohl bekannte und beliebte Python Library für Data Mining Algorithmen ist. Scikit-learn wird von Google unterstützt und befindet sich unter aktiver Entwicklung.

## Decision Tree Beispiel mit Scikit-learn
Für das kommende Beispiel werden die folgenden, beispielhaften, Trainingsdaten verwendet. Die einzelnen Zeilen stehen jeweils für ein Fall bzw. _Sample_. Es existieren zwei Features. Jedes Sample hat für jedes Feature einen Wert und ist einer Klasse zugewiesen.

| Samples       | Feature 1     | Feature 2  | Klasse |
| ------------- |:-------------:| ----------:|-------:|
| Sample 1      | 0             | 0          | 0      |
| Sample 2      | 1             | 1          | 1      |

Der nachfolgende Code-Abschnitt implementiert einen Decision Tree mit dem Gini-Index als Splitkriterium. Der Code-Abschnitt zeigt das Trainieren des Decision Trees mit den bereits aufgeführten Trainingsdaten. Variable x ist die _samples x features_ Matrix und y ist ein Array mit den zugewiesenen Klassen. Beispielsweise ist y[0] = 0 die Klasse des Samples x[0] mit den Features x[0][0] = 0 und x[0][1] = 0.
> from sklearn import tree  
x = [[0, 0],  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 1]]  
y = [0, 1]
clf = tree.DecisionTreeClassifier(criterion='gini')  
clf = clf.fit(x, y)

Mit dem nächsten Code-Abschnitt wird für ein drittes Sample die Klasse mit dem trainierten Decision Tree vorhergesagt.
> result = clf.predict([[1, 1]])  
print(result)  
-> Ausgabe: [1]

## Decision Tree für Sentimentanalyse
Im Bezug auf das Projekt wird für die Variable x (_samples x features_ Matrix) der Output des Kapitels _Datenvorverarbeitung_ vorgestellten Verfahrens verwendet. Variable y (Klassenbezeichnungen) sind die Klassifizierungen der Trainingsdaten.
> from sklearn import tree  
vectorizer = _<Der vectorizer ist der Output der Datenvorverarbeitung>_  
df = pd.read_csv("training_data.csv", usecols=["ItemID", "Sentiment", "SentimentSource", "SentimentText"])  
y = df.Sentiment  
x = vectorizer.fit_transform(df.SentimentText)  
clf = tree.DecisionTreeClassifier(criterion='gini')  
clf.fit(x, y)

___

<b id="fn1"></b>1. Scikit-learn Homepage. http://scikit-learn.org/stable/ (2017)
