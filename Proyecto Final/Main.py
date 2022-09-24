#PROGRAMA PRINCIPAL PROYECTO FABRICA DE CHOCOLATE

"""A Este Programa se le Harán Las Importaciones de Cada Modulo"""

#IMPORTACIONES
from Modulo_Inventario_3_1 import inventario
from Modulo_Configuracion_Recetas_2_1 import configurarRecetas
from Modulo_Planificacion_Fabricacion_2_0 import planificarFabricacion
from Modulo_Ventas_Compras_2_0 import *
from Modulo_Validaciones_2_0 import *

#FUNCIONES
try:
    def obtenerAccionReceta():

        opc1 =input("""
[1] Añadir Receta
[2] Eliminar Receta
[3] Reiniciar Recetario
[4] Modificar Receta
[5] Regresar
""")

        opc1 = verificarEnteroRango(opc1, 5, "Ingresa un Entero Válido (1-5): ")

        if opc1 == 1:
            configurarRecetas("adicion")
        elif opc1 == 2:
            configurarRecetas("eliminacion")
        elif opc1 == 3:
            configurarRecetas("reinicio")
        elif opc1 == 4:
            configurarRecetas("modificacion")
        elif opc1 == 5: 
            return

    def inicializarFabricacion():
        while True:
            try:
                if len(configurarRecetas("revision").keys()) > 0:
                    textoInput = "Ingresa la Receta del Producto a Fabricar\n"
                    opcionesPorElegir = {}
                    n = 1
                    for receta in configurarRecetas("revision").keys():
                        textoInput += f"{[n]} {receta.title()}\n"
                        opcionesPorElegir[n] = receta
                        n += 1

                        if n == (len(configurarRecetas("revision")) + 1):
                            textoInput += f"{[n]} Otra Nueva\n"
                            opcionesPorElegir[n] = "otra"

                            textoInput += f"{[n+1]} Cancelar\n"
                            opcionesPorElegir[n+1] = "cancelar"

                else:
                    raise Exception("No hay Recetas para Empezar con la Fabricación, Agrega Nuevas")


                opc = input(textoInput)

                opc = verificarEnteroRango(opc, n+1, textoInput)


                if opcionesPorElegir[opc] == "cancelar":
                    break
                elif opcionesPorElegir[opc] == "otra":
                    configurarRecetas("adicion")
                elif opcionesPorElegir[opc] not in configurarRecetas("revision").keys():
                    raise Exception("Opcion Escogida Invalida")
                else:
                    recetaElegida = configurarRecetas("revision")[opcionesPorElegir[opc]]
                    planificarFabricacion([recetaElegida, opcionesPorElegir[opc]])
                break
            except Exception as e:
                print(e)
                break



    def iniciarSistema():
        configurarRecetas("reinicio")
        inventario("reinicio")
        reinicializarComprasVentas()
        
        menuPrincipal()

    def menuPrincipal():
        while True:
            opc1 = input("""
[1] Configurar Recetas
[2] Realizar Compra
[3] Realizar Venta
[4] Realizar Producción
[5] Guardar y Terminar
[6] Salir sin Guardar
""")
            opc1 = verificarEnteroRango(opc1, 6, "Ingresa un Entero Válido (1-6): ")

            if opc1 == 1:
                obtenerAccionReceta()
            elif opc1 == 2:
                compra()
            elif opc1 == 3:
                venta()

            elif opc1 == 4:
                inicializarFabricacion()
            
            elif opc1 == 5:
                while True:
                    
                    path = input("Ingresa el Nombre del Archivo de Guardado: ")

                    try:
                        path = f".\Archivos\ArchivosDeGuardado\{path}.txt"
                    except:
                        print("El archivo no se encuentra en la ubicación de la ejecución del programa no se encuentra en el lugar correcto o se modifico la ruta de las carpetas o el nombre")
                        print("Intentalo de nuevo luego de haber solucionado el error")
                        break
                    try:
                        archivoGuardadoTXT = open(path, "x")
                        textoVariableInventario = str(inventario("revision"))
                        archivoGuardadoTXT.write(textoVariableInventario)

                        textoVariableRecetario = str(configurarRecetas("revision"))
                        archivoGuardadoTXT.write(f"\n{textoVariableRecetario}")

                        archivoGuardadoTXT.close()
            
                        break
                    except:
                        print("Este nombre de archivo ya existe")
                        opc2 = int(input("""[1] Reemplazar 
[2] Cambiar Nombre
[3] Cancelar
"""))

                        if opc2 == 1:
                            
                            archivoGuardadoTXT = open(path, "w")
                            textoVariableInventario = str(inventario("revision"))
                            archivoGuardadoTXT.write(textoVariableInventario)

                            textoVariableRecetario = str(configurarRecetas("revision"))
                            archivoGuardadoTXT.write(f"\n{textoVariableRecetario}")

                            archivoGuardadoTXT.close()

                            quit()
                        
                        elif opc2 == 3:
                            return

                quit()

            elif opc1 == 6:
                quit()


    def reusarSistema():
        while True:
            try:
                path = input("Ingresa el Nombre del Archivo de Guardado: ")

                if ".txt" in path:
                    path = f".\Archivos\ArchivosDeGuardado\{path}"
                else:
                    path = f".\Archivos\ArchivosDeGuardado\{path}.txt"
                
                try:
                    archivoGuardadoTXT = open(path, "r")
                except Exception as e:
                    print("El Archivo no se pudo Ubicar")
                    opc1 = input("""[1] Cancelar Inicio
[2] Cambiar Nombre
""")

                    opc1 = verificarEnteroRango(opc1, 2, """[1] Cancelar Inicio\n[2] Cambiar Nombre\n""")

                    if opc1 == 1:
                        quit()
                    elif opc1 == 2:
                        continue
                

            
                lineas = archivoGuardadoTXT.readlines()

                if len(lineas) < 2:
                    print("Archivo Inválido\n")
                    continue

                linea1 = lineas[0]
                linea2 = lineas[1]

                inventario("inicio", str(linea1))
                configurarRecetas("inicio", str(linea2))
                inicializarComprasVentas()
                break
            except Exception as e:
                print(e)
        
        menuPrincipal()


    #DESARROLLO
    print("\n-------------------------------- SISTEMA FABRICA DE CHOCOLATE --------------------------------")

    while True:
        try:
            opc = input("""
[1] INICIAR NUEVO SISTEMA
[2] INICIAR SISTEMA GUARDADO
""")

            opc = verificarEnteroRango(opc, 2, """\nElige una Opción Válida:\n[1] INICIAR NUEVO SISTEMA\n[2] INICIAR SISTEMA GUARDADO\n""")

            if opc == 1:
                iniciarSistema()
            elif opc == 2:
                reusarSistema()

            break
        except Exception as e:
            print(e)
except KeyboardInterrupt:
    quit()
except Exception:
    quit()
