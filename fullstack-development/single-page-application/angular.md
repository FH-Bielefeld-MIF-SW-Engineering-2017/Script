# Angular

Angular \(auch Angular2 oder Angular2+ genannt\) ist ein open-source, auf JavaScript / Typescript basiertes Softwareframework, zur Entwicklung von Single Page Applications und der Nachfolger von AngularJS. Die Community-getriebene Entwicklung, bestehend aus verschiedenen Einzelpersonen und Unternehmen, wird vom Angular Team bei Google angeführt.

#### Grundlegende Architektur

Eine Angular-Applikation ist modular aufgebaut \(siehe Abbildung 1: Angular Architektur\). Ein wesentlicher Bestandteil sind die sogenannten Komponenten, diese beinhalten die in JavaScript oder Typescript geschriebene Logik, die wiederum mit einem HTML Template und optional einer \(S\)CSS Datei verknüpft wird. Das besondere hierbei ist das sogenannte 2-way-databinding, wodurch Variablen und Funktionen innerhalb der Komponente direkt mit den Elementen im HTML Markup verknüpft werden und Änderungen sofort wechselseitig übertragen und verarbeitet werden. Eine Komponente ist vergleichbar mit einer klassischen HTML Seite einer nicht Single Page Application. _\(Angular 2017a\)_

Globale Funktionalitäten werden wiederum in Service Modulen geschrieben, welche beim Start der SPA einmal als Singleton initialisiert werden und deren Funktionen und Variablen fortan von jeder Komponenten verwendet werden können.

![](/assets/overview2.png)

_Abbildung 1: Angular Architektur \(Angular 2017a\)_

#### Module

Die Module werden als Angular Module oder NgModule bezeichnet. Jede Applikation besteht aus mindestens einem Modul, dem sogenannten root module, in der Regel **AppModule **genannt.

```
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
@NgModule({
  imports:      [ BrowserModule ],
  providers:    [ Logger ],
  declarations: [ AppComponent ],
  exports:      [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
```

_Code-Ausschnitt 1: AppModule _

In diesem Modul werden alle anderen notwendigen Module geladen, dazu gehören die Module bzw.Bibliotheken die Angular selber stellt, weitere Software die z.B. über NPM hinzugefügt wurde, sowie die eigens geschriebenen Komponenten und Services der Applikation \(siehe Code-Ausschnitt 1: AppModule\).

* **@NgModule** ist ein Decorator, der alle Module der Applikation als ein MetaData-Objekt zusammenfasst.
* **Imports **listet alle Module, deren exportierte Klassen und Funktionalitäten in den Komponenten gebraucht werden \(z.B. das RoutingModule, dessen Funktionen zum navigieren zwischen Komponenten nötig ist\)
* **Providers **listet die Service Module, die initial instanziiert werden und in allen anderen Modulen aufgerufen werden können
* **Declarations **listet die View-Klassen der Applikation, die vom User geschriebenen Komponenten, Direktiven und Pipes.
* **Exports **listet Deklarationen, die in den Templates anderer Module aufgerufen werden können
* **bootstrap **definiert die root Komponente, der Ausgangspunkt der Applikation und somit die erste geladene Sicht, über die auf die weiteren Komponenten zugegriffen werden kann.

Beim Starten wird die SPA über das root module gebaut und aufgerufen, welches die SPA anschließend dem Browser präsentiert. Dies geschieht nach gegebenen Konventionen in einer übergeordneten Datei, wie der "main.ts" \(siehe Code-Ausschnitt 2: main.ts Beispiel\).

```
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule);
```

_Code-Ausschnitt 2: main.ts Beispiel_

### Komponenten

Eine Komponente kontrolliert eine View innerhalb der SPA und ist daher mit einem HTML Template verknüpft. Eine Komponente kann dabei auf Funktionen der zuvor im root module deklarierten und importierten Module zugreifen, sowie eigenen Attribute und Funktionen definieren \(siehe Code-Ausschnitt 3: Beispielkomponente\).

```
@Component({
    selector: 'app-search',
    templateUrl: './search.component.html',
    styleUrls: ['./search.component.css']
})

export class SearchComponent implements OnInit {

  searchString: String = "";
  results: String[] = [];

  constructor(private _searchService: SearchService,private route: ActivatedRoute) { }

  ngOnInit() {
    //stuff happens when components gets initiated
  }

   startSearch() {
    //...
  }
}
```

_Code-Ausschnitt 3: Beispielkomponente_

In einem Konstruktor werden Services für den lokalen Zugriff innerhalb der Komponente übergeben, mit Interfaces wie OnInit können wiederum die Funktionalitäten der Komponenten erweitert werden.

#### MetaData

![](/assets/template-metadata-component.png)  
_Abbildung 2: MetaData-Verknüpfung zwischen Template und Komponente \(Angular 2017a\)_

Dem **@Component** Decorator können verschiedene Attribute mitgegeben werden, unter anderem ein Verweis auf eine HTML und eine CSS Datei. Der **selector **ist der HTML-Tag, über den die Komponenten innerhalb einer anderen Komponente aufgerufen werden könnte. Erst diese Angaben machen aus der Klasse SearchComponent eine Komponente im Angular Kontext.

#### Input und Output Attribute

Komponenten können andere Komponenten innerhalb ihres Templates  aufrufen und so in einer Eltern-Kind-Beziehung zueinanderstehen. Beim Aufruf des Kindes über einen selector können Input-Attribute übergeben werden. Gelichzeitig können Output-Events des Kindes an Funktionen der Eltern-Komponenten gebunden werden \(siehe Code-Ausschnitt\). _\(Angular 2017b\)_

```
<result-app [result]="resultElement" (deleteResult)="deleteR($event)">
</result-app>
```

_Code-Ausschnitt 4: Aufruf einer Kind-Komponete im Template_

In der Kind-Komponente werden diese Attribute mit einem @Input oder @Output deklariert. Ein Output-Event wird manuell innerhalb einer Funktion getriggert und kann ein oder mehrere Objekte mitgeben \(siehe Code-Ausschnitt\).

```
@Input()  result: Result;
@Output() deleteResult = new EventEmitter<Result>();
```

_Code-Ausschnitt 5: Input und Output Parameter einer Kind-Komponente_

Im Falle der beiden Code-Ausschnitte wird zuerst die Variable resultElement der Eltern-Komponente dem Kind mitgegeben, welche es in der eigenen Variable result speichert. Wenn das Kind das Event deleteResult wirft, gibt es ein Objekt vom Typ Result mit, welches wiederum die deleteR Funktion in der Eltern-Komponente aufruft.

#### Lifecycle Hooks

| Hook | Beschreibung / Wann |
| :--- | :--- |
| ngChanges\(\) | Wird noch vor OnInit das erste Mal aufgerufen und weiterhin immer dann, wenn eine 2-way gebundene Variabel geändert wird |
| ngOnInit\(\) | Wird initial einmalig aufgerufen |
| ngDoCheck\(\) | Erkennt Änderungen die Angular selber nicht erkennt, wird in Intervallen aufgerufen oder manuell getriggert |
| ngAfterContentInit\(\) | Einmalig nach dem ersten DoCheck\(\), wenn alle externen Inhalte in die View geladen wurden |
| ngAfterContentChecked\(\) | Nach ContentInit und jedem erneuten DoCheck\(\) |
| ngAfterViewInit\(\) | Einmalig nach dem ersten ContentChecked, wenn die eigene View der Komponente sowie deren Kinder gecheckt wurden |
| ngAfterViewChecked\(\) | Nach AfterViewInit und jedem erneuten AfterContentChecked\(\) |
| ngOnDestroy\(\) | Bevor Komponente zerstört wird, um Observables zu unsubscriben und ein Speicherleck zu vermeiden |

_Tabelle 1: Lyfecycle Hooks einer Komponente_

![](/assets/hooks-in-sequence.png)

_Abbildung 3: Reihenfolge der Lifecycle Hooks \(Angular 2017c\)_

### Template

Das Template kann entweder in einer separaten Datei definiert werden oder direkt als Attribut des Decorators, in Form eines Strings, in die Komponente geschrieben werden.

```
<md-input-container>
   <input mdInput [(ngModel)]="searchString" [placeholder]="'SEARCH.SEARCH' | translate" [type]="text" [mdAutocomplete]="auto">
</md-input-container>
{{searchString}}
<result-app *ngFor="let searchresult of results" [result]="searchresult"></result-app>
```

_Code-Ausschnitt 6: Auszug aus HTML Template mit data-binding_

**result-app** ist in diesem Fall der selector einer anderen Komponente, die in einer Schleife mehrfach aufgerufen und in der View generiert wird \(siehe Code-Ausschnitt 6: Auszug aus HTML Template mit data-binding\). Das in Klammern stehende **\[result\] ** ist wiederum eine Input-Variable innerhalb der result-Komponente.

Result-App ist in diesem Fall eine Kind-Komponenten von der SearchComponent und wird innerhalb des Template der Eltern-Komponenten aufgerufen. Dieses Verhalten ist hierarchisch organisiert \(siehe Abbildung 4: Hierachie der Komponenten\)

![](/assets/component-tree.png)  
_Abbildung 4: Hierachie der Komponenten \(Angular 2017a\)_

#### Structural Directives

Strukturelle Direktiven werden genutzt um den DOM zu manipulieren, Elemente hinzuzufügen oder zu entfernen. Folgende Elemente sind die, die am häufigsten verwendet werden.

**\*ngIf** wird an eine Boolean-Variable oder ein Statement gebunden, das entweder true oder false ist. Das Element und alle Kind-Elemente werden entsprechend dem DOM hinzugefügt oder entfernt.

```
<div *ngIf="isActive"></div>
```

_Code-Ausschnitt 7: \*ngIf Beispielcode_

**\*ngFor** wird verwendet um über eine Liste oder Array zu iterieren und entsprechende Elemente im DOM auszugeben. Das HTML-Element an dem die Liste hängt wird entsprechend häufig erzeugt. Optional kann der Index des Elementes an eine Variable gebunden werden.

```
<div *ngFor="let result of results;let i=index;">{{result.titel}} {{i}}</div>
```

_Code-Ausschnitt 8: \*ngFor Beispielcode_

**\*ngSwitch** entspricht der Logik seines JavaScript Pendants und fügt jenes Element dem DOM hinzu, welches dem Switch-Statement entspricht.

```
<div [ngSwitch]="result.price">
  <div *ngSwitchCase="50">Ist okay.</div>
  <div *ngSwitchCase="100">Viel zu teuer!</div>
</div>
```

_Code-Ausschnitt 9: \*ngSwitch Beispielcode_

#### Attribute Directives

Diese Direktiven funktionieren als klassische HTML-Attribute, die Variablen aus der Komponente mit den Attributen verknüpfen und so das Verhalten des HTML-Elements beeinflussen. Neben ngModel \(welches im folgenden Kapitel genauer beschrieben wird\) wird auf 2 relevante Direktiven eingegangen. _\(Angular 2017b\)_

**ngClass **fügt ein komplettes Set an potenziellen Klassen hinzu, indem eine Liste aus Schlüssel-Wert Paaren bestimmt welche Klassen aktuell aktiv sein sollten für das jeweilige Element.

```
<div [ngClass]="currentClasses">This div is initially saveable, unchanged, and special</div>
```

_Code-Ausschnitt 10: ngClass Beispielcode_

**ngStyle **funktioniert nach der gleichen Methode, verschiedene Styles können wiederum durch weitere Variablen beeinflusst werden, die beim Setzen der Schlüssel-Wert Paare abgerufen werden.

```
<div [ngStyle]="currentStyles"> </div>
```

```
this.currentStyles = {
    'font-style':  this.canSave      ? 'italic' : 'normal',
    'font-weight': !this.isUnchanged ? 'bold'   : 'normal',
    'font-size':   this.isSpecial    ? '24px'   : '12px'
  };
```

_Code-Ausschnitt 11: ngStyle Beispielcode_

### Data binding

Durch das data-binding werden Elemente und Ereignisse aus DOM und Komponente verknüpft. Dies kann in eine oder in beide Richtung geschehen \(siehe Abbildung 5: Data Binding\).

![](/assets/databinding.png)  
_Abbildung 5: Data Binding \(Angular 2017a\)_

**1-Way-Data-Binding**

```
<li>{{object.attribute}}</li>
<result-app [result]="result"></result-app>
<li (click)="search(seachstring)"></li>
```

_Code-Ausschnitt 12: 1-Way-Data-Binding Beispielcode_

* **geschweifte Klammern** werden dafür genutzt um den Wert einer Variable direkt im HTML anzuzeigen
* **\[Attribute\]** eines HTML Elements in eckigen Klammern werden Werte einer Variable aus der Komponente zugeschrieben, z.B. _\[class\]="klassenvariable"_
* **\(event\)** wiederum kann eine Funktion innerhalb der Komponenten aufrufen und ggf. Variablen übergeben, alternativ kann auch die Funktion direkt in das HTML geschrieben werden z.B. _\(click\)="variable='false'"_

**2-Way-Data-Binding**

Über **\[\(ngModel\)\]** können Variablen z.B. mit einem Input-Feld verknüpft werden, die Variable ändert sich entsprechend im Template als auch in der Komponente, wenn der Nutzer eine Eingabe macht. Zusätzlich kann über das **ngModelChange**-Event eine Funktion an die Änderung des gebundenen Objektes gehängt werden.

Angular verarbeitet alle data-bindings pro **JavaScript-Event-Circle** und traversiert dabei von der root Komponenten bis hinunter zum letzten Kind. Das 2-way-data-binding ist daher auch besonders für die Verknüpfung von Eltern und Kind-Komponenten wichtig, wo Objekte als Referenzen übergeben werden können. Sollte ein übergebenes Objekt in der Kind-Komponente verändert werden, gilt dies auch für das Objekt in der Eltern-Komponente \(siehe auch Abbildung 6: Eltern-Kind-Data-Binding\).

![](/assets/parent-child-binding.png)  
_Abbildung 6: Eltern-Kind-Data-Binding \(Angular 2017a\)_

### Pipes

Pipes transformieren einen gegebenen Input und werden direkt im Template mit dem Pipe Operator "\|" aufgerufen. Dieser kann direkt hinter einem Value Aufruf stehen oder hinter einer strukturellen Direktive, wie einem \*ngFor. Die Pipe kann dabei beispielsweise als Filter fungieren \(siehe Code-Ausschnitt\). _\(Angular 2017d\)_

```
<div>Value Aufruf: {{title | uppercase}}</div>
<div>Value Aufruf: {{title | uppercase | lowercase}}</div>
<div *ngFor="let Offer of Offers | filterList: filterBy">
```

_Code-Ausschnitt 13: Pipes Operator Beispielcode_

Hinter dem Pipe Operator wird der Name der Pipe genannt, wobei auch mehrere Pipes hintereinander gereiht werden können. Zusätzlich kann durch Doppelpunkte die zu übergebenen Parameter definiert werden. Falls dies nicht geschieht, wird die Variable vor dem Operator übergeben.

#### Built-in

| Pipe | Format | Beschreibung |
| :--- | :--- | :--- |
| DatePipe | date\_expression \| date\[:format\] | Formatiert eine Datumseingabe in ein gewünschtes Format |
| LowerCasePipe | value \| lowercase | Setzt alle Zeichen eines String auf Kleinbuchstaben |
| UpperCasePipe | value \| uppercase | Setzt alle Zeichen eines String auf Großbuchstaben |
| CurrencyPipe | number\_expression \| currency:currencyCode:symbolDisplay:digitInfo | Wandelt Zahl in spezifische Währung um, currencyCode: EUR / USD, symbolDisplay true oder false ob man € oder EUR sehen möchte, digitInfo Anzahl der Dezimalstellen |
| PercentPipe | number\_expression \| percent:digitInfo | Wandelt Zahl in Prozentangabe um |

_Tabelle 2: Built-In Pipes_

#### Eigene Pipes

Eigens geschriebene Klassen können mit @Pipe zu einer Pipe deklariert werden. Dabei wird der Name definiert, der später hinter dem Pipe Operator angegeben wird, und optional, ob die Pipe pure oder impure ist. Standardmäßig werden Pipes als pure definiert.

```
@Pipe({
  name: 'filterResults',
  pure: true
})
export class SortListPipe implements PipeTransform {

  transform(array: Array<any>, filterby: string): Array<any> {
  }
}
```

_Code-Ausschnitt 14: Eigene Pipe Komponente_

Aufgerufen wird eine Methode, die das PipeTransform-Interface implementiert, welche beliebig viele Input-Parameter \(mindestens einen\) verarbeiten kann. Hier kann zum Beispiel ein Array übergeben werden, dessen Objekte nach einem bestimmten Wert gefiltert werden sollen. Anschließend wird das neue Array zurück gegebenen und in der View der Komponente dargestellt.

**Pure** Pipes werden lediglich aufgerufen, wenn sich der triviale Inputparameter ändert \(String, Boolean, Integer etc\) oder ein komplett neues Objekt oder Array eingespeist wird. Die Pipe wird jedoch nicht getriggert, sollte ein Attribut eines Objektes geändert oder einem Array ein Element hinzugefügt werden.

**Impure **Pipes hingegen reagieren auf jede Veränderung, weswegen sie grade bei komplexeren Aufgaben und größeren Inputs die Performance negativ beeinflussen können.

### Services

Services sind Klassen, die an sich nichts Angular-Spezifisches beinhalten \(siehe Code-Ausschnitt 15: Beispiel des Search Service\). Es ist jedoch guter Stil alle nicht trivialen Aufgaben in diese Service-Klassen auszulagern und ihre Funktionen innerhalb der Komponenten zu nutzen, statt die komplette Logik in die Komponenten zu schreiben.

```
@Injectable()
export class SearchService {

  constructor(private http: Http, private _router: Router) { }

    searchOffer(params:any) {
        //....
    }
}
```

_Code-Ausschnitt 15: Beispiel des Search Service_

### Dependency injection

Mit der dependency injection wird eine neue Instanz einer Klasse erzeugt, mit samt allen ihren Abhängigkeiten. Dies sind in der Regel Services. Alle zu injizierenden Klassen werden dem Konstruktor einer Komponente als Parameter übergeben.  
Wenn Angular eine Komponenten aufruft werden zuerst ihre Abhängigkeiten überprüft, ein Injektor hält in einem Container alle bereits initialisierten Klassen bereit \(siehe Abbildung 7: Injektor\). Sollte eine benötigte Klasse noch nicht in diesem Container vorhanden sein, wird eine neue Instanz erstellt.

![](/assets/injector-injects.png)  
_Abbildung 7: Injektor \(Angular 2017a\)_

Um eine neue Instanz zu erstellen, muss zuvor ein Provider für die Klasse definiert worden sein. Ein Provider kann einen Service erstellen oder zurückgeben. Dieser kann, wie bereits zuvor erwähnt, im root moduleangegeben werden oder als MetaData im @Component Decorator. Wenn der Provider im root moduledefiniert ist, werden alle Komponenten auf die gleiche Instanz zugreifen.

### Server Kommunikation

Angular bietet unter der **@angular/http** Bibliothek sein eigenes HTTP Modul, welches optional über das root module in eine SPA integriert werden kann. Dabei werden die Methoden GET, POST, PUT und DELETE zur Verfügung gestellt, sowie Möglichkeiten Header, Options und Body eines Requests zu definieren. _\(Angular 2017e\)_

```
searchOfferExt(params:any) {
      return this.http.get(Path + "/api/offer")
            .map((r: Response) => r.json() as Offer[]);
}
```

_Code-Ausschnitt 16: GET-Request aus Service Funktion_

Als Rückgabewert wird ein sogenannter Observable erwartet. In diesem Beispiel wird innerhalb der Funktion eines Services die Antwort des Servers bereits auf einen bestimmten Datentypen gemaped.

#### Observable

Ein Observable ist ein Fluss an Daten auf den man subscriben kann, um fortan über mögliche Events informiert zu werden. Klassisch wird auf den Erfolg oder Misserfolg einer Datenübertragung reagiert. Der Aufruf dieser Funktion ist asynchron.

```
this._searchService.searchOfferExt(params).subscribe(
     data => {
          this.resultOffers = data;
          },
     error => {
          console.log("Error during search");
          }

 });
```

_Code-Ausschnitt 17: Subscription auf Methode des Services und Observable_

### Routing

Der Router in Angular erlaubt das Navigieren von einer View zu einer anderen, basierend auf den Aktionen des Nutzers. Der Trigger liegt dabei innerhalb der Komponente der aktuellen View, die den Nutzer auf eine neue Route weiterleitet und dabei optional auch Parameter mitgeben kann. Der Router kann jedoch auch klassisch eine URL auslesen und so die Route erkennen, die der Nutzer nehmen möchte, und eine entsprechende View generieren. _\(Angular 2017f\)_

Der Router ist nicht Teil der @angular/core Bibliothek, sondern besitzt sein eigenes Package **@angular/router** und kann optional dem root module einer Applikation hinzugefügt werden. Der **Router Service** bietet die entsprechenden Funktionen, um aus einer Komponente heraus zu navigieren.

#### Aufbau

Eine SPA besteht nur aus einer einzigen Seite, physisch ist dies die **index.html**, die auf dem Server liegt. Über einen base-Tag wird diese als Ausgangspunkt für den Router deklariert.

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>SPA-Example</title>
  <base href="/">
  </head>
<body>
  <app-root>Loading...</app-root>
</body>
</html>
```

_Code-Ausschnitt 18: Index-Seite der SPA_

Im app-root-Tag wird schließlich die komplette SPA geladen und die oberste View aufgebaut, dieses ist nach gegebenen Konventionen die App-Komponente "app.component", die dem root module zum bootrapen übergeben wurde.

#### Routing Module

Die Struktur der Applikation wird dem Router über ein separat geschriebenes Routing-Modul mitgeteilt \(siehe Code-Ausschnitt 19: Ausgelagertes Routing Modul\). Dieses wird anschließend in das root modul eingefügt, optional kann dieser Teil auch direkt in das root module geschrieben werden.

```
const routes: Routes = [
{
    path: '',
    redirectTo: '/main/start',
    pathMatch: 'full'
  },
  { path: 'login', component: LoginComponent },
  {
    path: 'main',
    component: MainComponent,
    canActivate: [LoginService],
    children: [
      { path: 'start',     component: StartpageComponent },
      { path: 'search/:input',     component: SearchComponent },
      {
        path: '',
        redirectTo: '/main/start',
        pathMatch: 'full'
      },
    ]
  },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class RoutingModule { }
```

_Code-Ausschnitt 19: Ausgelagertes Routing Modul_

* Jede **Route **stellt dabei einen Endpunkt dar, zu dem navigiert werden kann und zu dem eine entsprechende URL innerhalb der SPA existiert. Routen können verschachtelt werden, sodass manche Views nur über andere erreichbar sind. 
* Durch **redirectTo **können z.B. bei keiner oder Falscheingabe einer Route, ein allgemeiner Fallback-Startpunkt für den Nutzer festgelegt werden. Dazu ist zusätzlich das **pathMatch **Attribut notwendig.
* Mit Hilfe von **canActivate **können zusätzlich Services eingesponnen werden, die über eine bestimmte Methode zurückgeben, ob der Nutzer zu einer bestimmten Route navigieren darf.
* Über einen Doppelpunkt werden die **Parameter **definiert, die eine Route bzw. die Komponente dahinter erwartet.
* Es ist auch möglich **Wildcards **über Pfadangaben wie "\*\*" zu erteilen oder andere Formen eines RegEx Statements zu verwenden.

#### Router Outlet

Das Router-Outlet ist ein HTML-Tag, welches sich typischerweise im Template der obersten Komponente wiederfindet. Es kann jedoch an beliebiger Stelle eingebracht werden. In diesem Element werden die Views geladen, zu denen der Nutzer traversieren möchte.

```
<router-outlet></router-outlet>
```

_Code-Ausschnitt 20: Router Outlet_

#### Navigation

Um einen Navigationspunkt festzulegen kann entweder die RouteLink-Direktive verwendet werden oder die Funktion des Router Service innerhalb einer Komponente verwendet werden. Dabei können auch entsprechende Parameter gesetzt werden.

```
<a routerLink="/main/search" routerLinkActive="active">Search</a>
```

```
this._routerService.navigate(['/main/search', searchString]);
```

_Code-Ausschnitt 21: Navigation mit Router_

#### Status

Der Status des Routers kann über das Attribut **RouterState **aus jeder Komponente heraus abgerufen werden. Nach jeder erfolgreichen Navigation baut der Router dabei einen Baum aus **ActivatedRoute **Objekten auf, der den aktuellen Status des Routers darstellt. Die Activatedroute Objekte bieten dem Nutzer Methoden zum traversieren über den Baum.

#### Parameter Subscription

Eine Komponente kann auf seine eigene Route subscriben, wodurch bei jeder erfolgreichen Navigation die Parameter auf der Route erneut übergeben werden und diese anschließend verarbeitet werden können.  
Die Komponente selber wird nicht zerstört, wenn der Router auf eine andere View navigiert, daher ist eine initiale Subscription, die für den kompletten Lifecycle bestehen bleibt, notwendig.

```
constructor(private route: ActivatedRoute) { }

    ngOnInit() {
        this.subscription = this.route.params.subscribe((params: Params) => {
            this.searchString = params['input'];
        });
    }
```

_Code-Ausschnitt 22: Parameteraufruf_

