class User:
    def __init__(self, nombre=None, email=None, plataforma=None, perfil=None, pin=None, fecha_inicio=None, fecha_final=None):
        self.nombre = nombre
        self.email = email
        self.plataforma = plataforma
        self.perfil = perfil
        self.pin = pin
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final

    def toDBCollection(self):
        return {
            'nombre': self.nombre,
            'email': self.email,
            'plataforma': self.plataforma,
            'perfil': self.perfil,
            'pin': self.pin,
            'fecha_inicio': self.fecha_inicio,
            'fecha_final': self.fecha_final
        }
