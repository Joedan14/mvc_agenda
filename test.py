from model.contacto import Contacto #importa la clase de la direccion model contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

'''
contactos = [] #Lista vacia
citas = []
c1=Contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga 5 Col Carranza')
c2=Contacto(2,'Parque','464-456-4578','jem@gmail.com','Colon')
c3=Contacto(3,'Veronica','464-123-7589','dge.45@hotmail.com','Hidalgo 4 col RdP')

t1 =Cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Informacion')
t2 = Cita(2,2,'Plaza','15-03-2020','12:00','Salir')


contactos.append(c1) #append sirve para agregar un objeto a la lista, uno solo
contactos.append(c2)
citas.append(t1)
citas.append(t2)'''

'''t=input('Dame un nombre: ')

for c in contactos:
    if t.lower() == c.nombre.lower(): #es una operacion para strings para convertirlos a minusculas
        print('Si esta')
        break
else:
    print('No esta')'''

'''# Contactos
m = Model()
m.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga 5 Col Carranza')
m.agregar_contacto(2,'Gerardo','464-456-4578','jem@gmail.com','Colon')

s = m.leer_contacto(1)
print(s.nombre, s.tel, s.correo, s.dir)

#m.actualizar_contacto(1, 'Sara Juarez', '123-456-78910', 'gem@hotmail.com', 'Calle Torreon')
m.actualizar_contacto(1, n_nombre = 'Hugo Belman')
s = m.leer_todos_contactos()
for c in s:
    print(c.nombre, c.tel)

s = m.leer_contactos_letra('a')
for c in s:
    print(c.nombre, c.tel)

v = View()
s = m.leer_todos_contacto()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto()
'''

cont = Controller()
cont.start()




'''f = m.borrar_contacto(1)
if f:
    v.borrar_contacto(1)
else:
    v.contacto_no_existe(1)'''

'''s = m.leer_contacto(2)
print(s.nombre, s.tel, s.correo, s.dir)'''

'''
s = m.borrar_contacto(1)
print(s)
s = m.borrar_contacto(1)
print(s)

# Citas
n = Model()
n.agregar_cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Informacion')
n.agregar_cita(2,2,'Plaza','15-03-2020','12:00','Salir')

ss = n.leer_cita(1)
print(ss.lugar, ss.fecha, ss.hora, ss.asunto)

ss.actualizar_cita(2, 2, 'DICIS', '16-03-2020','10:00','Estudiar')
ss = n.leer_cita(2)
print(ss.lugar, ss.fecha, ss.hora, ss.asunto)

ss = n.borrar_cita(1)
print(ss)
ss = n.borrar_cita(1)
print(ss)

'''