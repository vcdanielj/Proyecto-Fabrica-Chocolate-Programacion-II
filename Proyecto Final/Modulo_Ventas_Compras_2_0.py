
# MODULO DE VENTAS - COMPRAS

#DESCRIPCION DEL MODULO:
#Funciones del Modulo:
"""
1. Venta                      ->     venta():
    Se recibe como parametros:
    - producto y cantidad     -> Indica que se produce una venta

2. Compra                     ->     compra():
    Se recibe como parametros:
    - productos y cantidades  -> Indica que se produce una compra

3. Compra de Fabricación      ->     compraFabricacion():
    Se recibe como parametros:
    - productos y cantidades  -> Indica que se destinada a produccion
"""

from Modulo_Inventario_3_1 import inventario 
from Modulo_Validaciones_2_0 import *

#INICIO DEL MODULO

def inicializarComprasVentas():

    global ventas 
    global compras
    ventas = []
    compras = []

    rellenarTXT()

def reinicializarComprasVentas():
    global ventas 
    global compras

    ventas = []
    compras = []

    rellenarTXT()

formasDePago = {
    1: "bs",
    2: "usd"
}
def venta():
    while True:
        try:
            productosInventario = inventario("revision")
        
            if len(productosInventario) == 0:
                print("No hay productos en el inventario")
                return

            textoInput = "Indica el Producto que se Desea Vender\n"
            opcionesPorEscoger = {}
            presentaciones = {}
            for productos in productosInventario.keys():
                presentaciones[productos[0]] = productos[1]
            n = 1
            for productos in productosInventario.keys():
                textoInput += f"[{n}] {productos[0].title()}\n"
                opcionesPorEscoger[n] = productos[0]
                
                n += 1

                if n == (len(productosInventario.keys())+1):
                    textoInput += f"[{n}] Cancelar Venta\n"
                    opcionesPorEscoger[n] = "cancelar"
                

            opc = input(textoInput)

            opc = verificarEnteroRango(opc, n, "Indica un Valor Entero Válido: ")

            opcionEscogida = opcionesPorEscoger[opc]

            if opcionEscogida == "cancelar":
                return
            else:
                while True:
                    cantidadAVender = input("Ingresa la Cantidad de Producto que se Vende: ")

                    cantidadAVender = verificarRealPositivo(cantidadAVender, "Ingreso una Cantidad Valida: ")

                    cantidadInventario = inventario("consulta", {opcionEscogida: ["producto", presentaciones[opcionEscogida]]})
                    cantidadInventario = cantidadInventario[0]

                    if cantidadAVender > cantidadInventario:
                        print(f"Se superó la cantidad del Stock, solo existen {cantidadInventario} {presentaciones[opcionEscogida]} de {opcionEscogida} en el inventario")
                        
                        opc2 =input("""[1] Vender Cantidad Máxima
[2] Cambiar Cantidad
[3] Regresar
""")

                        opc2 = verificarEnteroRango(opc2, 3, "Ingresa un valor entero válido: ")

                        if opc2 == 1:
                            cantidadAVender = cantidadInventario
                        elif opc2 == 2:
                            continue
                        else:
                            break
                        
                    break
            
            opcFormaDePago = input("""[1] Bolívares
[2] Dólares
""")

            opcFormaDePago = verificarEnteroRango(opcFormaDePago, 2, "Ingresa un entero de entre las opciones: ")

            monto = input("Ingresa el monto total de la venta: ")
            monto = verificarRealPositivo(monto, "Ingresa un monto valido: ") 

            cedula = input("Ingresa la cédula del cliente: ")
            cedula = verificarRealPositivo(cedula, "Ingresa una cédula valida: ")       

            cliente = input("Ingresa el nombre del cliente: ")  
            cliente = verificarNombres(cliente, "Ingresa un nombre válido: ")  

            try:
                inventario("venta", {"producto": opcionEscogida, "presentacion": presentaciones[opcionEscogida], "cantidad": cantidadAVender})
                ventas.append({"producto": [opcionEscogida,cantidadAVender, presentaciones[opcionEscogida]], "cliente": [cliente, cedula], "monto": [monto, formasDePago[opcFormaDePago]]})

            except:
                print("Hubo un error durante la realización de la venta")
                return
            else: 
                print("\nVenta Concretada")
                rellenarTXT()

                opc3 = input("""
[1] Registrar Otra Venta
[2] Regresar
""")

                opc3 = verificarEnteroRango(opc3, 2, "Ingresa un entero valido de entre las opciones: ")

                if opc3 == 1:
                    continue
                elif opc3 == 2:
                    return

        except Exception as e:
            print("Hubo un error al realizar la venta")
            return


def compra():
    while True:
        try:
            producto = input("Indica el nombre del producto o materia prima que se compra: ")
            producto = verificarNombres(producto, "Indica un producto válido: ")

            cantidadCompra = input("Indica la cantidad que se compra: ")
            cantidadCompra = verificarRealPositivo(cantidadCompra, "Ingresa una cantidad valida: ")

            presentacion = input("Indique la presentación del producto que se compra: ")
            presentacion = verificarNombres(presentacion, "Indique una presentacion válida: ")

            opcFormaPago = input("""Ingresa la forma de pago: 
[1] Bolívares
[2] Dólares
""")

            opcFormaPago = verificarEnteroRango(opcFormaPago, 2, "Ingresa un entero válido de entre las opciones: ")

            monto = input("Ingrese el monto a cancelar: ")
            monto = verificarRealPositivo(monto, "Ingresa un monto valido: ")

            proveedor = input("Ingresa el nombre del proveedor: ")
            proveedor = verificarNombres(proveedor, "Ingresa un nombre de proveedor válido: ")

            inventario("compra", {producto:[cantidadCompra, presentacion]})
            compras.append({"producto": [producto,cantidadCompra, presentacion], "proveedor": proveedor, "monto": [monto, formasDePago[opcFormaPago]]})

            print("\nCompra Realizada con Exito")
            rellenarTXT()

            opc = input("""
[1] Registrar Otra Compra
[2] Regresar
""")
            opc = verificarEnteroRango(opc, 2, "Indica una entero valido de entre las opciones: ")

            if opc == 1: 
                continue
            else: 
                return

        except Exception as e:
            print("Error al registrar la compra")
            return

    



def compraFabricacion(nombreProducto):

    while True:
        try:
            producto = nombreProducto

            cantidadCompra = input("Indica la cantidad que se compra: ")
            cantidadCompra = verificarRealPositivo(cantidadCompra, "Ingresa una cantidad valida: ")

            presentacion = input("Indique la presentación del producto que se compra: ")
            presentacion = verificarNombres(presentacion, "Indique una presentacion válida: ")

            opcFormaPago = input("""Ingresa la forma de pago: 
[1] Bolívares
[2] Dólares
""")

            opcFormaPago = verificarEnteroRango(opcFormaPago, 2, "Ingresa un entero válido de entre las opciones: ")

            monto = input("Ingrese el monto a cancelar: ")
            monto = verificarRealPositivo(monto, "Ingresa un monto valido: ")

            proveedor = input("Ingresa el nombre del proveedor: ")
            proveedor = verificarNombres(proveedor, "Ingresa un nombre de proveedor válido: ")

            inventario("compra", {producto:[cantidadCompra, presentacion]})
            compras.append({"producto": [producto,cantidadCompra, presentacion], "proveedor": proveedor, "monto": [monto, formasDePago[opcFormaPago]]})
            rellenarTXT()
            print("\nCompra Realizada con Exito")

            opc = input("""
[1] Registrar Otra Compra
[2] Regresar
""")
            opc = verificarEnteroRango(opc, 2, "Indica una entero valido de entre las opciones: ")

            if opc == 1: 
                continue
            else: 
                return

        except Exception as e:
            print("Error al registrar la compra")
            return

def rellenarTXT():
    try:
        archivoTXT = open(".\Archivos\Compras y Ventas.txt", "w", encoding="utf-8")

        archivoTXT.write("---------------- COMPRAS Y VENTAS FÁBRICA DE CHOCOLATE ----------------\n")

        if len(compras) > 0:
            archivoTXT.write("\nCOMPRAS:\n")
            for Compra in compras:
                archivoTXT.write(f" • Compra: {Compra['producto'][1]} {Compra['producto'][2]} {Compra['producto'][0]}\n")
                archivoTXT.write(f"   Proveedor: {Compra['proveedor']}\n")
                archivoTXT.write(f"   Monto Total: {Compra['monto'][0]} {Compra['monto'][1]}\n")
            archivoTXT.write(f"\n   Egresos Totales: {balanceIngresoGasto()['egresoTotalBs']}Bs y {balanceIngresoGasto()['egresoTotalUsd']}Usd\n")

        if len(ventas) > 0:
            archivoTXT.write("\nVENTAS:\n")
            for Venta in ventas:
                archivoTXT.write(f" • Venta: {Venta['producto'][1]} {Venta['producto'][2]} {Venta['producto'][0]}\n")
                archivoTXT.write(f"   Cliente: {Venta['cliente'][1]} {Venta['cliente'][0]}\n")
                archivoTXT.write(f"   Monto Total: {Venta['monto'][0]} {Venta['monto'][1]}\n")
            
            archivoTXT.write(f"\n   Ingresos Totales: {balanceIngresoGasto()['ingresoTotalBs']}Bs y {balanceIngresoGasto()['ingresoTotalUsd']}Usd\n")

        if len(ventas) > 0 and len(compras) > 0:
            archivoTXT.write(f"\n\nBALANCE GENERAL: {balanceIngresoGasto()['balanceTotal'][0]}Bs y {balanceIngresoGasto()['balanceTotal'][1]}Usd\n")
            
        archivoTXT.close()
    except Exception as e:
        pass

def obtenerVentasCompras():
    try:
        return (ventas, compras)
    except:
        return ([], [])

def balanceIngresoGasto():
    try:
        ingresoTotalBs = 0
        ingresoTotalUsd = 0
        egresoTotalBs = 0
        egresoTotalUsd = 0
        for Venta in ventas:
            if Venta["monto"][1] == "bs":
                ingresoTotalBs += Venta["monto"][0]
            elif Venta["monto"][1] == "usd":
                ingresoTotalUsd += Venta["monto"][0]
        for Compra in compras:
            if Compra["monto"][1] == "bs":
                egresoTotalBs += Compra["monto"][0]
            if Compra["monto"][1] == "usd":
                egresoTotalUsd += Compra["monto"][0]

        balanceTotal = [ingresoTotalBs - egresoTotalBs, ingresoTotalUsd - egresoTotalUsd]

        balances = {
            "ingresoTotalBs": ingresoTotalBs,
            "ingresoTotalUsd": ingresoTotalUsd,
            "egresoTotalBs": egresoTotalBs,
            "egresoTotalUsd": egresoTotalUsd,
            "balanceTotal": balanceTotal
        }

        return balances
    except:
        return {}

