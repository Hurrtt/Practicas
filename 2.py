#Instrucciones:
    
#Crea un diccionario que represente los productos, donde las claves son los nombres de los productos y los valores son la cantidad en inventario.
#Permite al usuario:
#•    Consultar la cantidad de un producto específico.
#•    Agregar un nuevo producto al inventario.
#•    Actualizar la cantidad de un producto existente.
#•    Eliminar un producto del inventario.
#Calcula el total de productos en el inventario.
global inventario 
inventario = {}
global stock
stock = None
global nombre
nombre = None

def agregar_producto():
    global inventario
    nombre = input("Ingrese el nombre del nuevo producto: ")
    stock = int(input("Ingrese la cantidad de stock: "))
    inventario [nombre] = stock
    
def actualizar_stock():
    global inventario
    nombre = input("Ingrese el nombre del producto: ")
    nuevo_stock = int(input("Ingrese el nuevo stock: "))
    inventario[nombre] = nuevo_stock

def eliminar_prodcutos():
    global inventario
    nombre = input("Ingrese el nombre del producto que desea eliminar: ")
    del inventario[nombre]
def menu():
    global stock
    opc = ""
    while opc != "5":
        print("--Bienvenido al sistema de inventarios--")
        opc = input(("1-Agregar productos \n2-Consultar stock de un producto \n3-Actualizar stock \n4-Eliminar producto \n5-Salir"))
        if opc == "1":
            agregar_producto()
        elif opc == "2":
            consulta = input("Nombre del producto que desea consultar: ")
            print("El stock es de: ",inventario.get(consulta,stock))
        elif opc == "3":
            actualizar_stock()
        elif opc == "4":
            eliminar_prodcutos()
menu()



