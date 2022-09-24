
# MODULO DE PLANIFICACIÓN DE FABRICACION

#DESCRIPCION DEL MODULO:
#Se recibe como parámetros:
"""
1. Un en forma de string:
    - inicio      -> Indica que se inicializa el almacenamiento vacio 
"""

#Returns:
"""
1. Para la acción de consulta:
    Al tomar como parametro a: {"nombre":["producto", "presentacion"], "nombre":["materia prima", "unidades"]} en el registro
    se retornara una lista ordenada donde cada elemento de la lista contendrá la cantidad de producto o materia prima que exista en el inventario con esa presentación
    Ej: inventario("consulta", {"leche": ["materia prima", "litros"], "chocolate blanco": ["producto", "tabletas"]}) -> Retornara: [0.0, 0.0] 
        donde el primer elemento de la lista es la cantidad de leche el litros y el segundo elemento es la cantidad de chocolate blanco en tabletas
"""

#Funcionamiento del modulo:
"""
1. Inicializar el inventario

2. Recibir como parámetro la acción a realizar

3. Describir una función que actualice el diccionario según la acción del parámetro
   En caso de producirse una compra: se agregan al inventario las materias primas compradas
   En caso de producirse una venta: se retiran del inventario los productos comerciales vendidos
   En caso de producirse una produccion: se retira del inventario la materia prima utilizada y 
                                         se agrega al inventario los productos comerciales producidos

4. Crear funcion que permita consultar la cantidad de producto existente en el inventario
"""

#Lista de posibles datos inválidos y de manejo de errores:
"""
    Aquí ira una lista con la descripción de los posibles errores y tracebacks que puede dar el modulo 

    - Ingreso de una cantidad inválida de parámetros a la hora de llamar la función
    - Inclusión de una acción no incluida en el parámetro (inicio, reinicio, compra, venta, produccion, consulta, revision)
    - Consulta o actualización del inventario antes de su inicialización 
    - Ingreso de formato o tipo de dato inválido en los parámetros
"""

from Modulo_Inventario_3_1 import inventario
from Modulo_Validaciones_2_0 import *
from time import sleep
from random import random

#INICIO DEL MODULO

def planificarFabricacion(receta):
    while True:
        try:
            nombreReceta = receta[1]
            Receta = receta[0]
            
            cantidadProducto = input("Ingresa la cantidad de producto que se desea fabricar: ")
            cantidadProducto = verificarRealPositivo(cantidadProducto, "Indica un valor válido")

            proporcion = cantidadProducto / float(Receta["cantidad generada"])

            print("\nHaciendo Revisión de Inventario...\n")

            sleep(1)

            for k, v in Receta["materia prima"].items():
                cantidadMPNecesitada = v[0] * proporcion
                cantidadInventario = inventario("consulta", {k: ["materia prima", v[1]]}) 
                cantidadInventario = cantidadInventario[0]
                cantidadFaltante = cantidadMPNecesitada - cantidadInventario

                if cantidadInventario <= 0:
                    if k == "cacao" or k == "Cacao":
                        print(f"No hay {k} en el inventario")
                        opc = input(f"""[1] Comprar {cantidadMPNecesitada} {v[1]} de {k}
[2] Esperar Producción de Cacao
[3] Cancelar Fabricación
""")

                        opc = verificarEnteroRango(opc, 3, "Ingresa un entero válido (1-3): ")

                        if opc == 1:
                            inventario("compra", {k:[cantidadMPNecesitada, v[1]]})
                        elif opc == 2:
                            print("Cultivando y Cosechando los Granos de Cacao")
                            sleep(1)
                            print("Desgranando los Granos de Cacao")
                            sleep(1)
                            print("Fermentando los Granos de Cacao")
                            sleep(1)
                            print("Secando los Granos de Cacao")
                            sleep(1)
                            print("Torrefaccionando los Granos Cacao")
                            sleep(1)
                            print("Moliendo los Granos de Cacao")
                            sleep(1)
                            print("Refinando el Cacao")
                            sleep(1)
                            print("Templando el Cacao")

                            print(f"{2 * cantidadFaltante} {v[1]} de Cacao han Sido Despachados al Inventario")
                            inventario("compra", {k:[cantidadFaltante*2, v[1]]})

                        elif opc == 3:
                            return
                    else:
                        print(f"No hay {k} en el inventario")
                        opc = input(f"""[1] Comprar {cantidadMPNecesitada} {v[1]} de {k}
[2] Cancelar Fabricación
""")                  
                        opc = verificarEnteroRango(opc, 2, "Ingresa un entero válido (1-2): ")

                        if opc == 1:
                            inventario("compra", {k:[cantidadMPNecesitada, v[1]]})
                        elif opc == 2:
                            return

                elif cantidadInventario - cantidadMPNecesitada < 1:
                    if k != "cacao":
                        cantidadFaltante = cantidadMPNecesitada - cantidadInventario
                        print(f"Hace falta {round(cantidadFaltante, 2)} {v[1]} de {k} en el inventario")
                        opc = input(f"""[1] Comprar {round(cantidadFaltante, 2)} {v[1]} de {k}
[2] Cancelar Fabricación
""")

                        opc = verificarEnteroRango(opc, 2, "Ingresa un entero válido (1-2)")
                        
                        if opc == 1:
                            inventario("compra", {k:[cantidadFaltante, v[1]]})
                        elif opc == 2:
                            return
                    else:
                        cantidadFaltante = cantidadMPNecesitada - cantidadInventario
                        print(f"Hace falta {round(cantidadFaltante, 2)} {v[1]} de {k} en el inventario")
                        opc = input(f"""[1] Comprar {round(cantidadFaltante, 2)} {v[1]} de {k}
[2] Esperar Producción de Cacao
[3] Cancelar Fabricación
""")                  
                        
                        opc = verificarEnteroRango(opc, 3, "Intenta con un entero Válido (1-3): ")
                        
                        if opc == 1:
                            inventario("compra", {k:[cantidadFaltante, v[1]]})
                        elif opc == 2:
                            print("Cultivando y Cosechando los Granos de Cacao")
                            sleep(1)
                            print("Desgranando los Granos de Cacao")
                            sleep(1)
                            print("Fermentando los Granos de Cacao")
                            sleep(1)
                            print("Secando los Granos de Cacao")
                            sleep(1)
                            print("Torrefaccionando los Granos Cacao")
                            sleep(1)
                            print("Moliendo los Granos de Cacao")
                            sleep(1)
                            print("Refinando el Cacao")
                            sleep(1)
                            print("Templando el Cacao")
                            sleep(1)

                            print(f"{2 * cantidadFaltante} {v[1]} de Cacao han Sido Despachados al Inventario")
                            inventario("compra", {k:[cantidadFaltante*2, v[1]]})
                        elif opc == 3:
                            return
            

            sleep(0.5)

            print("\nSeleccionando Materias Primas\n")

            sleep(0.5)

            print("Materia Prima Recolectada\n")
            print("Alistando Personal")
            sleep(0.2)


            while True:
                try:
                    tiempoEstimado = input("Ingresa el Tiempo Estimado en Horas: ")
                    tiempoEstimado = verificarRealPositivo(tiempoEstimado, "Indica un valo Válido: ")

                    if tiempoEstimado < 1:
                        raise Exception("El tiempo estimado no puede ser tan corto o menor a 1 hora")
                    elif tiempoEstimado > 5000:
                        raise Exception("El tiempo estimado no puede ser tan largo")

                    break

                except Exception as e:
                    print(e)

                
            print("Preparativos Listos")
            print("Empezando produccion")

            sleep(1)

            print(f'Moldeando y Dando Forma de {Receta["presentacion"]}')

            sleep(2)

            print("Producto Listo")

            sleep(0.6)

            tiempoTardado = round(2*(random()+0.25)*tiempoEstimado)

            sleep(0.6)

            print("Empaquetando y Despachando a Inventario")

            materiasPrimas = {}
            for k, v in Receta["materia prima"].items():
                materiasPrimas[k] = [v[0]*proporcion, v[1]]

            inventario("produccion", {"producto":nombreReceta, "presentacion": Receta["presentacion"], "cantidad": cantidadProducto, "materia prima usada": materiasPrimas})
            
            print(f"El producto se demoro {tiempoTardado} horas en fabricarse")
            if tiempoTardado < tiempoEstimado:
                print(f"\nSe despacho el producto con un adelanto de {tiempoEstimado-tiempoTardado} horas")
            else:
                print(f"\nSe despacho el producto con un atraso de {tiempoTardado - tiempoEstimado} horas")

            sleep(1.6)

            print("Proceso de Fabricación Completado Correctamente")

            break
        except Exception as e:
            print(e)


# TESTS

# Test de Datos Válidos


# - Test 1

