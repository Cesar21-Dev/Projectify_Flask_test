# Projectify Test

Es una API RESTful desarrollada utilizando el Framework Flask y base dadato MongoDB, que tiene como objetivo que los usuarios pueda reportar el tiempo de dedicación de los proyectos que esten ejecutando.  La elaboración de este proyecto es un test para optar por el cargo  de  ***Python Backend Developer*.**

Acontinuación se indica las funcionalidades de la Api:

- El usuario debe realizar logging para ingresar a las funcionalidades de la API:
	- Visualizar todos los proyectos de la empresa.
	- Realizar el reporte de porcentaje de dedicación de los proyectos (Solo se puede realizar una vez por semana por actividad).
	- EL usuario puede visualizar todos los reporte de dedicación realizados por el.
	- El usuario puede realizar la modificación de este porcentaje si se ecuentra en el mismo mes calendario cuando realizo el reporte.

#### **Desarrollo:**

Base de datos:

Ae creo una base de datos en MongoDB Atlas con el nombre ***Projectify_mongo.***, dentro de esta se crearo 3 colletions:

- projectify_projects: En esta  se encuetran todos los proyectos de la empresa tiene los argumentos ** _Id y name.**
- projectify_report:  En esta se encuentran los  reporte realizados por los usuarios, tiene los argumentos _Id, percentage, date, project_name y username.
- projectify_users: En esta se encuentra los usuarios registrados, tiene los argumentos  _id, public_id, username, password_salt, password_hash y admin.

#### Run Test:

Para realizar las pruebas se adjunta link postman con los request
https://web.postman.co/workspace/My-Workspace~019093d4-f143-4f1d-8770-4ce26c11bb7f/request/19471109-5636d234-9ae2-415b-9af2-fe567e5b53c9
