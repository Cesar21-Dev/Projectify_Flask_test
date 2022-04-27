from flask import Flask, make_response, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import jwt
import datetime
from functools import wraps
from functions import insert, update
import mongoDB

app = Flask(__name__)
cors = CORS(app)

app.config["SECRET_KEY"] = "thisissecret"
app.config["CORS_HEADERS"] = "Content-Type"
app.config[
    "MONGO_URI"
] = "mongodb+srv://MongoDB21:FH4wQnyRy4JaidST@cluster0.jz3of.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


mongo = PyMongo(app)

db = mongo.db.client.get_database("projectify_mongo")
projectsMongoDB = db.projectify_projects
usersMongoDB = db.projectify_users
reportMongoDB = db.projectify_report

# ruta para registro de usuario nuevo.
@app.route("/register", methods=["POST"])
def insertUser():
    public_id = str(uuid.uuid4())
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")

    mongoDB.insertUser(
        public_id,
        request.json["name"],
        request.json["password"],
        hashed_password,
        False,
        usersMongoDB,
    )

    return "Usuaio Guardado"


# Definición de funcion de requerimiento de token.
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])

            mongoDBUser = mongoDB.getUsers(data["public_id"], False, usersMongoDB)
            current_user = mongoDBUser
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token is invalid Exp!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid Error!"}), 401
        except:
            return jsonify({"message": "Token is invalid!"}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# Ruta para login de usuario
@app.route("/login")
def login():
    auth = request.authorization
    users = mongoDB.getUsers(auth.username, True, usersMongoDB)
    if not auth or not auth.username or not auth.password:
        return make_response(
            "Could not verify Blank",
            401,
            {"WWW-Authenticate": 'Basic realm="Login required!"'},
        )

    if not users:
        return make_response(
            "Could not verify User",
            401,
            {"WWW-Authenticate": 'Basic realm="Login required!"'},
        )

    if check_password_hash(users[0]["password_hash"], auth.password):
        token = jwt.encode(
            {
                "public_id": users[0]["public_id"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            },
            app.config["SECRET_KEY"],
        )
        return jsonify({"token": token.decode("UTF-8")})

    return make_response(
        "Could not verify password salt and hash no coinciden",
        401,
        {"WWW-Authenticate": 'Basic realm="Login required!"'},
    )


# Ruta para visualziar todos los proyectos en la empresa.
@app.route("/")
@token_required
def allProjects(current_user):
    Projects = mongoDB.getProjects(projectsMongoDB)
    return jsonify(Projects)


# Consulta de proyectos segun usuario logeado.
@app.route("/projectsuser")
@token_required
def getProjectxUser(current_user):
    mysqlProj = mongoDB.getProjectUser(current_user[0]["username"], reportMongoDB)
    return jsonify(mysqlProj)


@app.route("/xx")
@token_required
def test(current_user):
    currentWeek = datetime.datetime.now().strftime("W%V")
    report_o = mongoDB.verificaciontDedicacion(
        "W13",
        "Cesar21",
        "Dashboard energetico de planta de alimentos",
        reportMongoDB,
    )
    return "ok"


# Ruta para ingresar o Actualizar proyecto y porcentaje de dedicación.
@app.route("/insert_update_dedicacion", methods=["POST"])
@token_required
@cross_origin()
def functionCreateUpdateDedication(current_user):

    if "_id" in request.json:
        output = update(
            request.json["percentage"],
            request.json["_id"],
            request.json["date"],
            reportMongoDB,
        )
    else:
        timeweek = datetime.datetime.now().strftime("%Y-W%V-%w")
        output = insert(
            timeweek,
            current_user[0]["username"],
            request.json["project_name"],
            request.json["percentage"],
            reportMongoDB,
        )
    return jsonify(output)


@app.route("/inicio")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
