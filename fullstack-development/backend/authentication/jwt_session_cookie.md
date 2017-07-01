# JWT vs. Session Cookie

## JSON Web Token (JWT)
Die Token-Based Authentication ist **Stateless**. Das bedeutet, dass auf dem Server keine Information gespeichert werden, sondern nur das JSON Web Token beim Client gespeichert wird. [9](../quellen.md)   
Beim einer Authentifizierung wird auf dem Server ein neues JWT erstellt und zurück an den Client geschickt. Dieser speichert das JWT im Local Storage. Bei jeder weiteren Anfrage sendet der Client nun das JWT mit, welches dann auf dem Server verifiziert wird. [9](../quellen.md)

![Token-Based_Authentication](/assets/authentication_jwt.png)
*Token-Based Authentication [9](../quellen.md)*

Bei einem Logout des User, wird das JWT dann einfach beim Client gelöscht und es ist keine weitere Interaktion mit dem Server notwending. [9](../quellen.md)

## Session Cookie
Die Cookie-Based Authentication ist im Gegensatz zur Token-Based Authentication **Stateful**. Es müssen also sowohl auf dem Server sowie beim Client Daten gespeichert werden. Der Server speichert in einer Datenbank alle aktivien Sessions und auf der Client Seite wird ein Cookie mit der Session ID gespeichert. [9](../quellen.md)  
Beim einer Authentifizierung wird dann also auf dem Server eine neue Session ID erstellt, welche in der Datenbank gespeichert wird und in einem Cookie zurück an der Client geschickt wird. Bei jeder weiteren Anfrage zum Server wird nun der Cookie mitgeschickt und es wird überprüft, ob die Session ID aus dem Cookie mit einer Session ID aus der Datenbank übereinstimmt. [9](../quellen.md)

![Cookie-Based_Authentication](/assets/authentication_cookie.png)
*Cookie-Based Authentication [9](../quellen.md)*

Wenn sich der User nun ausloggt, muss auf dem Client der Cookie und auf dem Server die Session ID aus der Datenbank gelöscht werden. [9](../quellen.md)

Autor: Niklas Harting
