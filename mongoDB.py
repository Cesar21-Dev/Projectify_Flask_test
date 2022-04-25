from bson import ObjectId

# Funcion para insertar proyecto nuevo
def insertProjectMongoDB(nombre, mongoDB):
    newProject = {"name": nombre}
    mongoDB.insert_one(newProject)


# Funcion para insertar usuarios nuevos
def insertUser(public_id, username, password_salt, password_hash, admin, mongoDB):
    newProject = {
        "public_id": public_id,
        "username": username,
        "password_salt": password_salt,
        "password_hash": password_hash,
        "admin": admin,
    }
    mongoDB.insert_one(newProject)


# Funcion para consultar todos los proyectos
def getProjects(mongoDB):
    pj = list(mongoDB.find())
    data = []
    for i in range(0, len(pj)):
        pj[i]["_id"] = str(pj[i]["_id"])
        data.append(pj[i])
    print(data)
    return data


# Funcion para consulta con filtro de usuario o filtro de id publico
def getUsers(filtro, username, mongoDB):
    if username == True:
        return list(mongoDB.find({"username": filtro}))
    else:
        return list(mongoDB.find({"public_id": filtro}))


# Funcion para consulta preyectos con % de dedicacion reportados por el usuario
def getProjectUser(current_user, mongoDB):
    return mongoDB.find({"username": current_user})


# Funcion para validar si en la base de datos se encuentra reportado en la presente semana el projecto
# a el que el usuario quiere reportar.
def verificaciontDedicacion(week, username, project_name, mongoDB):
    return list(
        mongoDB.find(
            {
                "username": username,
                "project_name": project_name,
                "date": {"$regex": week},
            }
        )
    )


# Funcion para insertar nueva dedicación de un proyecto.
def insertProjectDedication(percentage, fecha, project_id, user, mongoDB):
    newProjectDedication = {
        "percentage": percentage,
        "date": fecha,
        "project_name": project_id,
        "username": user,
    }
    return mongoDB.insert_one(newProjectDedication)


# Funcion para actualizar porcentaje de dedicación de un precyecto.
def updateProject(newPercentage, id, mongoDB):
    newProjectDedication = {"_id": ObjectId(id)}
    print(list(mongoDB.find(newProjectDedication)))
    return mongoDB.find_one_and_update(
        newProjectDedication, {"$set": {"percentage": newPercentage}}
    )
