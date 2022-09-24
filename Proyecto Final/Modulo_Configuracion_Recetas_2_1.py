
# MODULO DE CONFIGURACION RECETAS

#DESCRIPCION DEL MODULO:
#Se recibe como parámetros:
"""
1. Una accion (inicio, reinicio, adicion, eliminacion, modificacion, consulta, revision) en forma de string:
    - inicio        -> Indica que se inicializa el recetario vacio 
    - reinicio      -> Indica que se reinicializa el recetario
    - adicion       -> Indica que se quiere agregar una nueva receta al recetario                            
    - eliminacion   -> Indica que se quiere eliminar una receta del recetario
    - modificacion  -> Indica que se quiere modificar una receta del recetario
    - consulta      -> Indica que se quiere examinar la receta de un producto en específico
    - revision      -> Indica que se requiere el recetario completo
2. Un nombre de un producto en forma de string:
    solo se requerira este parametro para la accion de consulta como: "nombre del producto"
"""

#Returns:
"""
1. Para la acción de consulta:
    Al tomar como parametro a: "nombre de la receta" en el registro
    se retornara un diccionario donde cada clave sera el nombre de una materia prima y cada valor sera una lista con primer item la cantidad de materia prima 
    que es necesaria y el segundo item sera la unidad del primer item
    Ej: configurarRecetas("consulta", {"trufas de chocolate"}) -> Retornara: {"cantidad producto": cantidad generada, "materia prima 1": cantidad, "materia prima 2": cantidad} 
"""

#Funcionamiento del modulo:
"""
1. Inicializar el Recetario

2. Recibir como parámetro la acción a realizar

3. Describir una función que actualice el recetario según la acción del parámetro

4. Crear funcion que permita consultar la receta de un producto en específico
"""

#Lista de posibles datos inválidos y de manejo de errores:
"""
    Aquí ira una lista con la descripción de los posibles errores y tracebacks que puede dar el modulo 

    - Ingreso de una cantidad inválida de parámetros a la hora de llamar la función
    - Inclusión de una acción no incluida en el parámetro (inicio, reinicio, adicion, eliminacion, modificacion, consulta, revision)
    - Consulta o actualización del recetario antes de su inicialización 
    - Ingreso de formato o tipo de dato inválido en los parámetros
"""

#Formato del recetario:
"""
    recetario = {
        "producto 1": {
            "cantidad generada": cantidad,
            "presentacion": "presentacion producto",
            "materia prima": {
                "materia prima 1": [cantidad, "unidad materia prima"],
                "materia prima 2": [cantidad, "unidad materia prima"],
                "materia prima 3": [cantidad, "unidad materia prima"]
            }
        },

        "producto 2": {
            "cantidad generada": cantidad,
            "presentacion": "presentacion producto",
            "materia prima": {
                "materia prima 1": [cantidad, "unidad materia prima"],
                "materia prima 2": [cantidad, "unidad materia prima"],
                "materia prima 3": [cantidad, "unidad materia prima"]
            }
        }
    }
"""    


#INICIO DEL MODULO

from Modulo_Validaciones_2_0 import *


def configurarRecetas(accion: str, producto: str = ""):
    try:
        def inicializarRecetas(data):
            global recetario
            recetario = eval(data)

            rellenarTXT()

        def reinicializarRecetas():
            global recetario

            recetario = {}

        def rellenarTXT():
                
            """Apartado Creacion Archivo TXT"""

            """Se resetea el archivo para que quede en blanco"""
            recetarioTXT = open(".\Archivos\Recetario.txt", "w", encoding="utf-8")

            """Se rellena el archivo con todos los elementos de la variable almacenamiento"""
            recetarioTXT.write("------------------ RECETARIO FÁBRICA DE CHOCOLATE ------------------\n\n")
            
            for k, v in recetario.items():
                receta = f"\n{k.upper()}\n"
                for k2, v2 in v.items():

                    if k2 == "cantidad generada":
                        receta += f"{k2.title()}: {v2}\n"
                    elif k2 == "presentacion":
                        receta += f"{k2.title()}: {v2}\n"
                    elif k2 == "materia prima":
                        receta += "Ingredientes:\n" 
                        for k3, v3 in v2.items():
                            receta += f" • {k3.title()}: {v3[0]} {v3[1]}\n"
                    elif k2 == "elaboracion":
                        receta += f"Elaboración:\n"
                        for i, v in enumerate(v2):
                            receta += f" • Paso {i+1}: {v}\n"

                recetarioTXT.write(receta)
            
            recetarioTXT.close()


        def añadir():

                while True:
                    while True:
                        try:
                            opc = input("""Elige la Forma en la que Desea Agregar la Receta: 
[1] A través de la consola
[2] Cancelar
""")                      
                            opc = verificarEnteroRango(opc, 2, "Ingresa un entero válido (1-2): ")
                            
                            break
                        
                        except Exception as e:
                            print(e)
                    if opc == 1:
                        while True:
                            try:
                                nombre = input("Ingresa el Nombre del Producto a Agregar: ")
                                nombre = verificarNombres(nombre, "Ingresa un Nombre de Producto Válido: ")
                                recetario[nombre] = {}
                                recetario[nombre]["presentacion"] = ""
                                recetario[nombre]["cantidad generada"] = 0
                                recetario[nombre]["materia prima"] = {}

                                break
                            except Exception as e:
                                print(e)
                        
                        while True:
                            try:
                                cantidadGenerada = input("Ingresa La Cantidad del Producto que Crea la Receta: ")
                                cantidadGenerada = verificarEnteroPositivo(cantidadGenerada, "Ingresa un Entero Válido para la Cantidad Generada")
                                recetario[nombre]["cantidad generada"] = cantidadGenerada
                                break
                            except Exception as e:
                                print(e)
                        
                        while True:
                            try:
                                presentacion = input("Ingresa la Presentacion del Producto: ")
                                recetario[nombre]["presentacion"] = presentacion
                                break
                            except Exception as e:
                                print(e)

                        n = 0
                        c = 0
                        k = 0
                        while c != 1:
                            while True:
                                try:
                                    if n == 0:
                                        materiaPrima = input("Ingresa el Nombre de la Materia Prima Necesaria: ")
                                        materiaPrima = verificarNombres(materiaPrima, "Ingresa un nombre valido para Materia Prima: ")
                                        n = 1
                                        break
                                    elif k == 1:
                                        opc2 = input("""[1] Agregar Materia Prima
[2] Terminar Receta
""")                                    
                                        opc2 = verificarEnteroRango(opc2, 2, "Ingresa un entero válido (1-2)")    
                                        if opc2 == 1:
                                            n = 0
                                            continue

                                        elif opc2 == 2:
                                            c = 1
                                            rellenarTXT()
                                            break

                                    else:
                                        opc2 = int(input("""[1] Agregar Materia Prima
[2] Agregar Elaboración
[3] Terminar Receta
"""))

                                        opc2 = verificarEnteroRango(opc2, 3, "Ingresa un entero válido de entre las opciones: ")

                                        if opc2 == 1:
                                            n = 0
                                            continue

                                        elif opc2 == 2:
                                            recetario[nombre]["elaboracion"] = []
                                            elaboracion = input("Ingresa el Paso 1: ")
                                            recetario[nombre]["elaboracion"].append(elaboracion)

                                            while True:
                                                opc3 = input("""[1] Añadir Otro Paso
[2] Terminar Elaboración
""")
                                                
                                                opc3 = verificarEnteroRango(opc3, 2, "Ingresa un entero válido de entre las opciones: ")
                                                if opc3 == 1:
                                                    paso = len(recetario[nombre]["elaboracion"]) + 1
                                                    paso = f"Ingreso el paso {paso}: "

                                                    elaboracion = input(paso)
                                                    recetario[nombre]["elaboracion"].append(elaboracion)
                                                if opc3 == 2:
                                                    break

                                            k = 1
                                            continue
                                        elif opc2 == 3:
                                            c = 1
                                            rellenarTXT()
                                            print("\nReceta Añadida Correctamente")
                                            break

                                        break

                                except Exception as e:
                                    print(e)
                            
                            if c == 1:
                                break

                            while True:
                                try:
                                    cantidad = input("Ingresa la Cantidad de Materia Prima Necesaria: ")
                                    cantidad = verificarRealPositivo(cantidad, "Ingresa un valor válido: ")

                                    break

                                except Exception as e:
                                    print("Cantidad de Materia Prima Inválida, Ingresa un Real Válido")
                            while True:
                                try:
                                    unidades = input("Ingresa las Unidades de la Cantidad de Materia Prima: ")
                                    unidades = verificarNombres(unidades, "Ingresa el nombre de las unidades valido: ")
                                    recetario[nombre]["materia prima"][materiaPrima] = [cantidad, unidades]

                                    break

                                except Exception as e:
                                    print(e)
                            
                            n += 1

                        while True:
                            try:
                                
                                opc2 = input("""
[1] Regresar
[2] Registrar otra Receta
""")
                                
                                opc2 = verificarEnteroRango(opc2, 2, "Ingresa un valor entero valido de entre las opciones: ")

                                if opc2 == 1:
                                    return
                                elif opc2 == 2:
                                    break

                            except Exception as e:
                                print(e)


                    elif opc == 2:
                        break


        def eliminar():
            while True:
                try:
                    while True:
                        try:
                            
                            textoInput = "Elige la Receta a Eliminar: \n"
                            opcionesPorEscoger = {}   
                            n = 1

                            if len(recetario) < 1:
                                print("No se puede eliminar ya que no hay recetas en el recetario")
                                opc = input("""[1] Agregar Recetas
[2] Regresar
""")

                                opc = verificarEnteroRango(opc, 2, "Ingresa un Entero Valido de entre las opciones: ")

                                if opc == 1:
                                    añadir()
                                elif opc == 2:
                                    return
                            for opcion in recetario.keys():
                                textoInput += f"[{n}] {opcion}\n" 
                                opcionesPorEscoger[n] = opcion
                                n += 1
                                if n == (len(recetario) + 1):
                                    textoInput += f"[{n}] cancelar\n"
                                    opcionesPorEscoger[n] = "cancelar"

                            opc = int(input(textoInput))
                            opcionEscogida = opcionesPorEscoger[opc]

                            if opcionEscogida != "cancelar":
                                recetario.pop(opcionEscogida)
                                print("\nReceta Eliminada Correctamente\n")
                            else:
                                return

                            rellenarTXT()

                            break
                        
                        except Exception as e:
                            print(e)

                    while True:
                        try:
                            opc2 = input("""[1] Eliminar Otra Receta
[2] Regresar
""")

                            opc2 = verificarEnteroRango(opc2, 2, "Ingresa un Entero Valido de Entre las Opciones: ")

                            if opc2 == 1:
                                break
                            elif opc2 == 2:
                                return
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
                

        def modificar():
            while True:
                while True:
                    try:
                        textoInput = "Elige la Receta a Modificar: \n"
                        opcionesPorEscoger = {}   
                        n = 1

                        if len(recetario) < 1:
                            print("No se puede modificar nada ya que no hay recetas en el recetario")
                            opc5 = input("""[1] Agregar Recetas: 
[2] Regresar
""")

                            opc5 = verificarEnteroRango(opc5, 2, """[1] Agregar Recetas: \n[2] Regresar \n""")

                            if opc5 == 1:
                                añadir()
                            elif opc5 == 2:
                                return

                        for opcion in recetario.keys():
                            textoInput += f"[{n}] {opcion}\n" 
                            opcionesPorEscoger[n] = opcion
                            n += 1
                            if n == (len(recetario) + 1):
                                textoInput += f"[{n}] cancelar\n"
                                opcionesPorEscoger[n] = "cancelar"

                        opc = int(input(textoInput))
                        opcionEscogida = opcionesPorEscoger[opc]

                        if opcionEscogida != "cancelar":
                            opc2 = input("""Indica Que Apartado Quieres Modificar
[1] Nombre
[2] Cantidad Generada
[3] Presentacion
[4] Ingredientes
[5] Elaboración
[6] Cancelar
""")

                            opc2 = verificarEnteroRango(opc2, 6, "Indica el Apartado a Modificar con un Entero Válido (1-6): ")

                            if opc2 == 1:
                                nombre = input("Ingresa el nuevo nombre de la receta: ")
                                nombre = verificarNombres(nombre, "Ingresa el nuevo nombre de la receta: ")

                                recetario[nombre] = recetario[opcionEscogida]
                                recetario.pop(opcionEscogida) 

                                print("\nNombre Modificado con Exito")

                            
                            elif opc2 == 2:
                                cantidadGenerada = input("Ingresa la nueva cantidad que crea de la receta: ")
                                cantidadGenerada = verificarEnteroPositivo(cantidadGenerada, "Ingresa la nueva cantidad que crea de la receta: ")

                                recetario[opcionEscogida]["cantidad generada"] = cantidadGenerada

                                print("\nCantidad Generada Modificada con Exito")

                            elif opc2 == 3:
                                presentacion = input("Ingresa la nueva presentacion de la receta: ")

                                recetario[opcionEscogida]["presentacion"] = presentacion

                                print("\nPresentacion Modificada con Exito")

                            elif opc2 == 4:
                                n1 = 1
                                opcionesPorEscogerMP = {}
                                textoInputMP = "Ingresa Cual Ingrediente se Quiere Modificar: \n"
                                for elemento in recetario[opcionEscogida]["materia prima"].keys():
                                    textoInputMP += f"[{n1}] {elemento}\n"
                                    opcionesPorEscogerMP[n1] = elemento
                                    n1 += 1
                                    
                                    if n1 == (len(recetario[opcionEscogida]["materia prima"]) + 1):
                                        textoInputMP += f"[{n1}] cancelar\n"
                                        opcionesPorEscogerMP[n1] = "cancelar"

                                opcionEscogidaMP = int(input(textoInputMP))

                                opcionEscogidaMP = opcionesPorEscogerMP[opcionEscogidaMP]

                                if opcionEscogidaMP != "cancelar":
                                
                                    nombreMP = input("Ingresa el nuevo nombre del ingrediente: ")
                                    cantidadMP = input("Ingresa la nueva cantidad del ingrediente: ")
                                    unidadMP = input("Ingresa la nueva unidad de cantidad del ingrediente: ")

                                    recetario[opcionEscogida]["materia prima"][nombreMP] = [cantidadMP, unidadMP]

                                    if nombreMP != opcionEscogidaMP: 
                                        recetario[opcionEscogida]["materia prima"].pop(opcionEscogidaMP) 

                                    print("\nIngrediente Modificado con Exito\n")

                                else:   
                                    break

                            elif opc2 == 5:
                                n2 = 1
                                opcionesPorEscogerP = {}

                                if "elaboracion" in recetario[opcionEscogida] :
                                    
                                    if not recetario[opcionEscogida]["elaboracion"]:
                                        raise Exception("No se puede modificar nada más ya que no hay pasos en la receta")

                                    textoInputP = "Ingresa Cual Paso de Elaboracion se Quiere Modificar: \n"
                                    for elemento in recetario[opcionEscogida]["elaboracion"]:
                                        textoInputP += f"[{n2}] {elemento}\n"
                                        opcionesPorEscogerP[n2] = elemento
                                        n2 += 1
                                        
                                        if n1 == (len(recetario[opcionEscogida]["elaboracion"]) + 1):
                                            textoInputMP += f"[{n2}] cancelar\n"
                                            opcionesPorEscogerP[n2] = "cancelar"

                                    opcionEscogidaPn = int(input(textoInputP))

                                    opcionEscogidaP = opcionesPorEscogerP[opcionEscogidaPn]

                                    if opcionEscogidaP != "cancelar":
                                    
                                        paso = input("Ingresa el nuevo paso a realizar: ")

                                        for index, value in enumerate(recetario[opcionEscogida]["elaboracion"]):
                                            if value == opcionEscogidaP:
                                                recetario[opcionEscogida]["elaboracion"][index] = paso

                                        print("\nElaboracion Modificada con Exito\n")

                                    else:   
                                        break
                                else:
                                    print("Esta Receta no Incluye Elaboracion\n")
                                    
                                    opc3 = input("""[1] Añadir Elaboración
[2] Cancelar
""")

                                    opc3 = verificarEnteroRango(opc3, 2, "Ingresa un Entero Valido de Entre las Opciones: ")

                                    if opc3 == 1:
                                        recetario[opcionEscogida]["elaboracion"] = []
                                        elaboracion = input("Ingresa el Paso 1: ")
                                        recetario[opcionEscogida]["elaboracion"].append(elaboracion)

                                        while True:
                                            opc4 = input("""[1] Añadir Otro Paso
[2] Terminar Elaboración
""")

                                            opc4 = verificarEnteroRango(opc4, 2, "Ingresa un Entero Valido de Entre las Opciones: ")
                                            
                                            if opc4 == 1:
                                                paso = len(recetario[opcionEscogida]["elaboracion"]) + 1
                                                paso = f"Ingreso el paso {paso}: "

                                                elaboracion = input(paso)
                                                recetario[opcionEscogida]["elaboracion"].append(elaboracion)

                                                print("\nElaboracion Añadida a la Receta Modificada Correctamente\n")
                                            if opc4 == 2:
                                                break
                
                                    break
                                
                            elif opc2 == 6:
                                break

                            rellenarTXT()
                        else: 
                            return
                        
                        opc1 = input("""[1] Seguir Modificando Recetas
[2] Regresar
""")

                        opc1 = verificarEnteroRango(opc1, 2, """Ingresar una opcion Valida:\n[1] Seguir Modificando Recetas\n[2] Regresar\n""")

                        if opc1 == 2:
                            return
                    except Exception as e:
                        print(e)
                

        def consultar(producto): 
            if producto in recetario:
                return recetario[producto]
            else:
                return False

        """Apartado donde se llaman las a las funciones segun la accion dada en el parametro"""
        if accion == "inicio":
            inicializarRecetas(producto)

        if accion == "reinicio":
            reinicializarRecetas()

        elif accion == "adicion":
            añadir()

        elif accion == "eliminacion":
            eliminar()

        elif accion == "modificacion":
            modificar()

        elif accion == "consulta":
            return consultar(producto)
        
        elif accion == "revision":
            return recetario
        
        else: 
            return "Ninguna accion valida dada"


        rellenarTXT()
    
    except Exception as e:

        """ Si hay un problema esto devolvera el tipo de problema que se presento para luego validarse en el llamamiento de la funcion """
        print(e)
        return e
    

# TESTS

# Test de Datos Válidos

# - Test 1

"""
configurarRecetas("inicio")
print("\n\nEjecutando Test de Adición")
configurarRecetas("adicion")


print("\n\nEjecutando Test de Modificación")
configurarRecetas("modificacion")
print("\n\nEjecutando Test de Eliminación")
configurarRecetas("eliminacion")

print("\n\nEjecutando Test de Consulta")
print(configurarRecetas("consulta", "producto 1"))
"""
