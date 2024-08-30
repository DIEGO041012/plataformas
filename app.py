from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase  
from user import User  # Importa la clase User

# Conexión a la base de datos
db = dbase.dbConnection()

app = Flask(__name__)

# Ruta de inicio: Mostrar todos los usuarios
@app.route('/')
def home():
    users = db['users']
    usersReceived = users.find()
    return render_template('index.html', users=usersReceived)

# Ruta para agregar un nuevo usuario (POST)
@app.route('/users', methods=['POST'])
def addUser():
    users = db['users']
    
    # Recoger datos del formulario
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    plataforma = request.form.get('plataforma')
    perfil = request.form.get('perfil')
    pin = request.form.get('pin')
    fecha_inicio = request.form.get('fecha_inicio')
    fecha_final = request.form.get('fecha_final')

    # Validar que todos los campos estén presentes
    if nombre and email and plataforma and perfil and pin and fecha_inicio and fecha_final:
        user = User(nombre, email, plataforma, perfil, pin, fecha_inicio, fecha_final)
        users.insert_one(user.toDBCollection())
        return redirect(url_for('home'))
    else:
        return notFound()

# Ruta para eliminar un usuario (DELETE)
@app.route('/delete/<string:user_name>')
def delete(user_name):
    users = db['users']
    users.delete_one({'nombre': user_name})
    return redirect(url_for('home'))

# Ruta para editar un usuario (PUT)
@app.route('/edit/<string:user_name>', methods=['POST'])
def edit(user_name):
    users = db['users']
    
    # Recoger datos del formulario
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    plataforma = request.form.get('plataforma')
    perfil = request.form.get('perfil')
    pin = request.form.get('pin')
    fecha_inicio = request.form.get('fecha_inicio')
    fecha_final = request.form.get('fecha_final')

    # Validar que todos los campos estén presentes
    if nombre and email and plataforma and perfil and pin and fecha_inicio and fecha_final:
        users.update_one(
            {'nombre': user_name}, 
            {'$set': {
                'nombre': nombre,
                'email': email,
                'plataforma': plataforma,
                'perfil': perfil,
                'pin': pin,
                'fecha_inicio': fecha_inicio,
                'fecha_final': fecha_final
            }}
        )
        return redirect(url_for('home'))
    else:
        return notFound()

# Manejador de errores 404
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=4000)
