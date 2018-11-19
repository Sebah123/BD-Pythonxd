import mysql.connector
db = mysql.connector.connect(host='localhost',user='root',passwd='',database='bdsteam')
cursor = db.cursor()

"""
////////////////////////////////////////////////////////////////////////////////////////////////////////////
def inicio():
    while True:
        print("-------------------------------")
        print("Bienvenido/a a nuestro software")
        print("-------------------------------")
        print("a)Iniciar sesión")
        print("b)Crear usuario")
        print("c)Salir del sistema")

        opc = input("Ingrese opcion: ")
        if opc == "a":
            nick = input("Nombre de usuario: ")
            clave = input("Contraseña: ")
            sql = "SELECT COUNT(*) FROM administrador WHERE nom_usuario = '" + nick + "' AND pass = SHA2('" + clave + "',0)"

inicio()
//////////////////////////////////////////////////////////////////////////////////////////////////////////////
"""


nick = input("Nombre de usuario: ")
clave = input("Contraseña: ")
sql = "SELECT COUNT(*) FROM administrador WHERE nom_usuario = '" +nick+ "' AND pass = SHA2('" +clave+ "',0)"
cursor.execute(sql)
rs = cursor.fetchall()
##for fila in rs:
##    print(fila[1])
valor = rs[0][0]

def login():
    if valor == 1:
        print("Ingresado Correctamente")
    else:
        print("Error, ingrese correctamente sus datos")
login()


"""
while(valor == 1):
    print("")
    print("---------------------")
    print("bienvenido")
    print("seleccione una opcion")
    print("1.- comentarios")
    print("2.- crear comentario")
    opc = input("opcion: ")
    print("---------------------")
    if (opc == "1"):
        cursor.execute("SELECT usuario.nickname, comentario.fecha, comentario.texto "
                       "FROM comentario INNER JOIN usuario "
                       "ON comentario.usuario_id_fk = usuario.id "
                        "WHERE usuario.email = '"+correo+"'")
        rs = cursor.fetchall()
        for fila in rs:
            print(fila[0], fila[1], fila[2])
    elif(opc == "2"):
        texto = input("ingrese su comentario: ")
        cursor.execute("INSERT INTO comentario VAlUES(NULL, (SELECT id FROM usuario WHERE email = '"+correo+"'), NOW(), '"+texto+"')")

"""

def menu():
    while (valor == 1):
        print("")
        print("----------------")
        print("----------------")
        print("Bienvenido/a")
        print("Seleccione una opción")
        print("----------------")
        print("----------------")
        print("a)Actualizar datos")
        print("b)Borrar datos")
        print("c)Insertar datos")
        print("d)Visualizar datos")
        print("e)Salir del Sistema")
        print("-----------------")

        opcion = input("Opcion --> ")

        if opcion == "a":
            pass
        elif opcion == "b":
            pass
        elif opcion == "c":
            while(True):
                print("--------------")
                print("--------------")
                print("Insertar datos")
                print("--------------")
                print("a)Insertar juegos")
                print("b)Volver al menú")
                op = input("Ingrese una opcion")
                if op != "a" or op == "b":
                    break
                elif op == "a":

                    texto = print("Ingrese juegos en el siguiente orden :")
                    nombre = input("Nombre:")
                    descripcion = input("Descripcion:")
                    categoria = input("Categoría:")
                    precio = int(input("Precio:"))

                    cursor.execute("INSERT INTO juego VALUES(NULL,'"+nombre+"','"+descripcion+"','"+categoria+"',"+str(precio)+" )")
                    db.commit() #SIEMPRE SE UTILIZA, MENOS EN UN SELECT, IMPORTANTE
                    print("Juego creado")

                    menu()
        elif opcion == "d":
            while(True):
                print("----------------")
                print("Vizualizar Datos")
                print("----------------")
                print("----------------")
                print("a)Ver todos los juegos con su respectivos datos")
                print("b)Ver por nombre")
                print("c)Ver por precio")
                print("d)Volver al menú")

                opcion1 = input("Ingrese la opcion -->")

                if opcion1 != "a" or opcion1 != "b" or opcion1 != "c":
                    break
                if opcion1 == "d":
                    break

                if opcion1 == "a":
                    cursor.execute("SELECT * FROM juego")
                    print()
                menu()

        else:
            break


menu()