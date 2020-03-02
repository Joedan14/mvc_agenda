class View:
    def mostrar_contacto(self, contacto):
        print('**** Datos del contacto *****')
        print('Nombre:', contacto.nombre)
        print('Telefono:', contacto.tel)
        print('Correo:', contacto.correo)
        print('Direccion:', contacto.dir)
        print('******************************')

    def mostrar_contactos(self, contactos)
        print('****** Conctactos *********')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('*******************************************************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha agregado a la base de datos!')
    
    def borrar_contacto(self,contacto):
        print(contacto, 'Se ha borrado de la base de datos')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'Se ha modificado correctamente a:' contacto_n.nombre)

    def contacto_ya_existe(self, contacto):
        print(contacto.id_contacto, 'YA EXISTE EN LA BASE DE DATOS')

    def contacto_no_existe(self, id_contacto):
        print(contacto.id_contacto, 'NO EXISTE EN LA BASE DE DATOS')

    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Good Bye')

    

    # Vistas de citas
    def mostrar_cita(self, cita):
        print('**** Datos de cita *****')
        print('ID:', id_cita)
        print('Contacto:', id_contacto)
        print('Lugar:', cita.lugar)
        print('Fecha:', cita.fecha)
        print('Hora:', cita.hora)
        print('Asunto:', cita.asunto)
        print('******************************')

    def mostrar_citas(self, citas)
        print('****** Citas *********')
        for c in citas:
            print(c.id_cita, c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('*******************************************************************')

    def agregar_cita(self, cita):
        print(cita.fecha, cita.asunto, 'Se ha agregado a la base de datos!')

    def borrar_cita(self,cita):
        print(cita.fecha, cita.asunto, 'Se ha borrado de la base de datos')

    def modificar_cita(self, cita_o, cita_n):
        print(cita_o.fecha, cita_o.asunto, 'Se ha modificado correctamente')

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'YA EXISTE EN LA BASE DE DATOS')

    def cita_no_existe(self, id_cita):
        print(cita.id_cita, 'NO EXISTE EN LA BASE DE DATOS')

    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Good Bye')



    #General Views
    def start(self):
        print('Esto es unejemplo sencillo de MVC')

    def end(self):
        print('Hasta la vista!')

    def menu(self):
        print('1. Agregar contacto')
        print('2. Buscar contacto')
        print('3. Acuatlizarf contacto')
        print('4. Borrrar contacto')
        print('5. ')