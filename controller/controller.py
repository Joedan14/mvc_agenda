from model.model import Model
from view.view import View

class Controller:
    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    #Contacto controllers
   
    
    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    

    def insertar_contactos(self, id_contacto, nombre, tel, correo, dir):
        self.view.agregar_contacto()
        self.view.agregar_contacto()
        self.view.agregar_contacto()


    #Cita controllers
   
    
    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)
    

    def insertar_citas(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        self.view.agregar_cita()
        self.view.agregar_cita()
        self.view.agregar_cita()



    def start(self):
        #Display a welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga 5 Col Carranza')
        self.insertar_contactos(2,'Parque','464-456-4578','jem@gmail.com','Colon')
        self.insertar_contactos(3,'Veronica','464-123-7589','dge.45@hotmail.com','Hidalgo 4 col RdP')

        self.insertar_citas(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Informacion')
        self.insertar_citas(2,2,'Plaza','15-03-2020','12:00','Salir')
        self.insertar_citas(3,3,'Medico','05-03-2020','11:00','Consulta medica')

        #Show all contacts in DB
        self.leer_todos_contactos()
        self.leer_contactos_letra('a')

    def menu(self):
        #Display menu
        self.view.menu()
        o = input('Selecciona una opcion (1-10)')
        if o == '1':
            def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
                    b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
                    if b:
                        self.view.agregar_contacto(c)
                    else:
                        self.view.contacto_ya_existe(c)
        elif o == '2':
            def leer_contacto(self, id_contacto):
                e, c = self.model.leer_contacto(id_contacto)
                if e:
                    self.view.mostrar_contacto(c)
                else:
                    self.view.contacto_no_existe(id_contacto)
        elif o == '3':
            def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo='', n_dir=''):
                e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
                if e:
                    self.view.actualizar_contacto(id_contacto)
                else:
                    self.view.contacto_no_existe(id_contacto)
        elif o == '4':
            def borrar_contacto(self, id_contacto):
                e, c = self.model.borrar_contacto(id_contacto)
                if e:
                    self.view.borrar_contacto(c)
                else:
                    self.view.contacto_no_existe(id_contacto)
        elif o == '5':
            def leer_contactos_letra(self, letra):
                c = self.model.leer_contactos_letra(letra)
                self.view.mostrar_contactos(c)
        elif o == '6':
            def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
                b, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                if b:
                    self.view.agregar_cita(c)
                else:
                    self.view.contacto_ya_existe(c)
        elif o == '7':
            def leer_cita(self, id_cita):
                e, c = self.model.leer_cita(id_cita)
                if e:
                    self.view.mostrar_cita(c)
                else:
                    self.view.cita_no_existe(id_cita)
        elif o == '8':
            def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
                e = self.model.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
                if e:
                    self.view.actualizar_cita(id_cita)
                else:
                    self.view.cita_no_existe(id_cita)
        elif o == '9':
            def borrar_cita(self, id_cita):
                e, c = self.model.borrar_cita(id_cita)
                if e:
                    self.view.borrar_cita(c)
                else:
                    self.view.cita_no_existe(id_cita)
        elif o == '10':
            def leer_citas_fecha(self, fecha):
                c = self.model.leer_citas_fecha(fecha)
                self.view.mostrar_citas(c)
            self.view.end()
        else:
            self.view.opcion_no_valida()