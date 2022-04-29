# Projectify Test

Es una API RESTful desarrollada utilizando el Framework Flask y base de dadatos MongoDB, que tiene como objetivo que los usuarios puedan reportar el porcentaje de dedicación semanal de los proyectos que esten ejecutando.  La elaboración de este proyecto es un test para optar por el cargo  de  ***Python Backend Developer*.**

Acontinuación se indica las funcionalidades de la Api:

- El usuario debe realizar logging para ingresar a las funcionalidades de la API las cuales son:
	- Visualizar todos los proyectos de la empresa.
	- Realizar el reporte de porcentaje de dedicación de los proyectos (Solo se puede realizar una vez por semana y por actividad).
	- EL usuario puede visualizar todos los reporte de dedicación realizados por el.
	- El usuario puede realizar la modificación de este porcentaje si se ecuentra en el mismo mes calendario cuando realizó el reporte.

#### **Desarrollo de la solución:**
>Estructura de la aplicación:

- **app.py**: Script principal.
- **funtions.py**: Funciones de insertar y atualizar reporte de dedicación.
- **mongoDB.py**: Funciones de consulta hacia la base de datos mongoDB Atlas.

> Base de datos:

Se creo una base de datos en MongoDB Atlas con el nombre ***Projectify_mongo.***, dentro de esta se crearo 3 colletions:

- projectify_projects: Se encuetra todos los proyectos de la empresa, tiene los argumentos ** _Id y name.**
- projectify_report: Se encuentra los  reporte realizados por los usuarios, tiene los argumentos _Id, percentage, date, project_name y username.
- projectify_users: Se encuentra los usuarios registrados, tiene los argumentos  _id, public_id, username, password_salt, password_hash y admin.

#### Run Test:

Para ejecutar la aplicacion se puede realziar de dos formas:

1. Crea un entorno virtual e instalar los requermientos que se visualizan en el archvio requirements.txt.

2. la aplicación se enciuentra hosteada en la plataforma Heroku a continuzación se adjuntan los url.

Para realizar las pruebas se adjunta json de postman con los request, puede descarga el archivo Leanware.postman_collection (1).json, e importarlo en su postman. 

1. Loging: En esta ruta podemos logear el usuario y este nos devolvera un token, el cual se debe utiliza rpara disfurtar de las funcioanlidades de la api. https://projectifytest.herokuapp.com/login.

2. Register:  En esta ruta permite registar un nuevo usuario.
https://projectifytest.herokuapp.com/register

3. All_Projects: Esta es la ruta inical o por defecto, el cual nos devuelve el listado de los  proyectos en la empresa.
https://projectifytest.herokuapp.com/

Headers:
Content-Type --> application/json
x-access-token --> token de longing actual.

4. Projects_User: Nos regresa el listado de projecto con reporte de dedicación segun el usuario actualmente logeado.
https://projectifytest.herokuapp.com/projectsuser

Headers:
Content-Type --> application/json
x-access-token --> token de longing actual.

5. Insert_Project_Dedication: Esta ruta permite añadir un nuevo reorte de dedicación requeire los siguientes parametros:

Headers:
Content-Type --> application/json
x-access-token --> token de longing actual.

Body raw JSON.
{"percentage":Val, "project_name":"strings"}

https://projectifytest.herokuapp.com/insert_update_dedicacion

6. Update_Project_Dedication: Esta ruta permite actualizar el porcentaje de reporte de dedicación

Headers:
Content-Type --> application/json
x-access-token --> token de longing actual.

Body raw JSON.
{"_id":"String", "date":"String","percentage":Val, "project_name":"string"}

https://projectifytest.herokuapp.com/insert_update_dedicacion
