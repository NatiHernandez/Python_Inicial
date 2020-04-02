from tkinter import *
from tkinter import messagebox
import  random, mysql.connector
from tkinter import ttk

root = Tk()
tabla = Label(root, text="Ingrese sus datos", background = "magenta3", bd = 7, foreground = "white", width = 72 )
tabla.grid(row=0, column=0, sticky=NW , columnspan=10)

titulo = Label(root, text = "Título")
ruta= Label(root, text = "Ruta")
descripcion= Label(root, text = "Descripción")

titulo.grid(row = 1, column = 3, sticky = W)
ruta.grid(row = 2, column = 3, sticky = W)
descripcion.grid(row = 3, column = 3, sticky = W)


e1, e2, e3 = Entry(root), Entry(root), Entry(root)

idLabel = Label(root, text = "ID")
idLabel.grid( row = 3, column = 5, sticky = E)
idEntry = Entry(root)


idEntry.grid(row = 3, column = 6, sticky = W)

def sorpresa():
    color = random.choice(["gold", "green3", "orangeRed2","snow4", "yellow", "blue", "magenta",  "cyan", "azure", "plum4"])
    colorTitulo = random.choice(["black", "red", "brown", "grey", "orange"])
    colorBoton = random.choice(["pink", "white"])
    root.configure(background  = color)
    tabla.configure(background  = colorTitulo)
    titulo.configure(background = color)
    ruta.configure(background = color)
    descripcion.configure(background = color)
    idLabel.configure(background = color)
    e4.configure(background = colorBoton)
    e5.configure(background = colorBoton)
    e6.configure(background = colorBoton)
    e7.configure(background = colorBoton)
    e8.configure(background = colorBoton)
    e9.configure(background = colorBoton)
    if colorTitulo == "black":
        tabla.configure(foreground = "red")
    else:
        tabla.configure(foreground = "black")

def crearBase():
    try:
        mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )
        micursor = mibase.cursor()
        micursor.execute("CREATE DATABASE IF NOT EXISTS mi_plantilla0")

        mibase = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="mi_plantilla0"
            )
        micursor = mibase.cursor()
        micursor.execute("CREATE TABLE IF NOT EXISTS producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta varchar(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
        messagebox.showinfo(message="Base de datos creada", title="Mensaje")
    except:
        messagebox.showinfo(message="No se ha podido cargar la base de datos", title="Mensaje")


def escribir():
    mibase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mi_plantilla0"
        )
    micursor = mibase.cursor()
    dato1 = e1.get()
    dato2 = e2.get()
    dato3 = e3.get()
    patron = re.compile("^[A-Za-z]+(?:[ -][A-Za-z]+)*$")    
    sql = "INSERT INTO producto (titulo, ruta, descripcion) VALUES (%s, %s, %s)"
    if patron.match(dato1) != None:
        datos = (dato1, dato2, dato3)
        micursor.execute(sql, datos)
        mibase.commit()
        print(datos)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
    else:
        messagebox.showinfo(message="Título inválido.\nIntroduzca otro título", title="Mensaje")

def consultar():
    mibase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mi_plantilla0"
        )
    micursor = mibase.cursor()
    sql = "SELECT * FROM producto"
    micursor.execute(sql)
    resultado = micursor.fetchall()
    for x in resultado:
        print(x)


def borrar():
    mibase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mi_plantilla0"
    )
    micursor = mibase.cursor()
    valor_id = idEntry.get()
    sql = "DELETE FROM producto WHERE id = %s"
    dato = (valor_id,)
    print(valor_id)
    micursor.execute(sql, dato)
    mibase.commit()
    idEntry.delete(0, END)
    if micursor.rowcount == 0:
        messagebox.showinfo(message="Introduzca un ID", title="Mensaje")
    else:
        messagebox.showinfo(message="Se eliminó correctamente", title="Mensaje")

def modificar():
    try:
        mibase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="mi_plantilla0"
        )
        valor_id = idEntry.get()
        micursor = mibase.cursor()
        sql = "UPDATE producto " \
                    "SET titulo = '%s', ruta= '%s', descripcion= '%s' " \
                    "WHERE id = %s;" % (e1.get(), e2.get(), e3.get(), valor_id)
        micursor.execute(sql)
        mibase.commit()
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        idEntry.delete(0, END)
        messagebox.showinfo(message="Se modificó correctamente", title="Mensaje")
    except:
        messagebox.showinfo(message="Debe introducir un ID y completar todos los campos", title="Mensaje")


e4 = Button(root, text="Alta", width = 10, command = escribir) 
e5 = Button(root, text="Sorpresa", width = 10, command = sorpresa) 
e6 = Button(root, text="Crear Base",width = 10, command = crearBase) 
e7 = Button(root, text="Consultar", width = 10, command = consultar) 
e8 = Button(root, text="Borrar", width = 10, command = borrar) 
e9 = Button(root, text="Modificar", width = 10, command = modificar) 

def botones (e, r, c, p):
    e.grid(row=r, column=c, pady = p)

botones(e1, 1, 4, 4)
botones(e2, 2, 4, 4)
botones(e3, 3, 4, 4)
botones(e4, 4, 4, 5)
botones(e5, 4, 5, 5)
botones(e6, 4, 3, 5)
botones(e7, 6, 3, 5)
botones(e8, 6, 5, 5)
botones(e9, 6, 4, 5)

mainloop()
