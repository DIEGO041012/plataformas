from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://dlondonov1994:Luna041012**@turin.uke1hni.mongodb.net/?retryWrites=true&w=majority&appName=turin'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["plataformas"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
