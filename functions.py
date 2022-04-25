import datetime
import mongoDB

# Función para insertar nuevo proyecto con porcentaje de dedicación.
def insert(fecha, username, project_name, percentage, mongo_DB):
    currentWeek = datetime.datetime.now().strftime("W%V")
    verificacionWeek = mongoDB.verificaciontDedicacion(
        currentWeek, username, project_name, mongo_DB
    )
    print(verificacionWeek)
    if len(verificacionWeek) < 1:
        mongoDB.insertProjectDedication(
            percentage,
            fecha,
            project_name,
            username,
            mongo_DB,
        )
        return {"mensaje": "Dedicacion de proyecto guardado"}
    else:
        return {
            "mensaje": "No se puede anexar dos reportes de dedicacion en la misma semana"
        }


# Función para actualizar el porcentaje de dedicación.
def update(newPercentage, id, fecha, mongo_DB):

    a = fecha.replace("W", "")
    b = a.split("-")

    mesBitacora = datetime.date.fromisocalendar(
        int(b[0]), int(b[1]), int(b[2])
    ).strftime("%m")
    mesActual = datetime.datetime.now().strftime("%m")

    if mesBitacora == mesActual:
        mongoDB.updateProject(newPercentage, id, mongo_DB)
        return {"mensaje": "OK - Porcentaje de dedicacion del proyecto actualizado"}
    else:
        return {
            "mensaje": "No se puede actualziar Porcentaje se encuentra fuera del mes"
        }
