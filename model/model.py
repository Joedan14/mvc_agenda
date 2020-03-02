from .contacto import Contacto #se coloca punto antes de contacto porque se importa de la misma carpeta
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id_contacto(self, id_contacto): #detectar id similares
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    def esta_id_cita(self, id_cita): #detectar id similares
        for c in self.cita:
            if c.id_cita == id_cita:
                return True, c
        return False, 0


    #Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.esta_id_contacto(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, dir) #Pasa los parametros
            self.contactos.append(c)#lo agrega a la lista
            return True, c
        return False, 0 #pass puede que se incluyan cosas ahi

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        return e, c
    
    def leer_todos_contactos(self):
        return self.contactos

    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id(id_contacto)
        if e:
            if n_nombre !='':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_dir != '':
                c.dir = n_dir
            return True
        return False

    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

    def leer_contactos_letra(self, letra):
        #lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
        lista = []
        for c in self.contactos:
            if c.nombre[0].lower() == letra.lower():
            #if c.nombre.lower().startswith(letra):
                lista.append(c)
        return lista




    #Citas medthods
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.esta_id(id_cita)[0]: #devuelve una tupla con dos elementos
            c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto) #Pasa los parametros
            self.citas.append(c)#lo agrega a la lista
            return True, c
        return False, 0 #pass puede que se incluyan cosas ahi

    def leer_cita(self, id_cita):
        e, c = self.esta_id(id_cita)
        return e, c

    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, c = self.esta_id(id_cita)
        if e:
            c.lugar = n_lugar
            c.fecha = n_fecha
            c.hora = n_hora
            c.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, c = self.esta_id(id_cita)
        if e:
            self.citas.remove(c)
            return True, c
        return False, 0
    
    def leer_citas_fecha(self, fecha):
        lista = [c for c in self.citas if c.fecha == fecha]
        #lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
        lista = []
        for c in self.citas:
            if c.fecha == fecha:
                lista.append(c)
        return lista

    m.borrar_contacto(1)
    1 = m.leer_todas_citas()
    for c in 1:
        print(c.fecha, c.fecha, c.asunto)