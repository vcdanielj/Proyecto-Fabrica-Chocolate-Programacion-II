
def verificarEnteroRango(valor, valorTope, textoInput):
    valorTope += 1
    while True:
        try:
            if int(valor) not in range(1, valorTope):
                raise Exception()
            
            return int(valor)
        except (ValueError, TypeError):
            print("El valor ingresado no es un Entero Válido")
            valor = input(textoInput)
        except:
            print("El Valor Escogido no es una Opción Válida")
            valor = input(textoInput)

            
def verificarRealPositivo(valor, textoInput):
    while True:
        try:
            if float(valor) < 0:
                raise Exception("El valor Ingresado no es Un Real Positivo Válido")
            
            return float(valor)

        except (ValueError, TypeError):
            print("No se ha ingresado un Real Positivo Válido")
            valor = input(textoInput)
        except Exception as e:
            print(e)
            valor = input(textoInput)

def verificarEnteroPositivo(valor, textoInput):
    while True:
        try:
            if int(valor) < 0:
                raise Exception("El valor Ingresado no es Un Real Positivo Válido")
            
            return int(valor)

        except (ValueError, TypeError):
            print("No se ha ingresado un Real Positivo Válido")
            valor = input(textoInput)
        except Exception as e:
            print(e)
            valor = input(textoInput)


def verificarNombres(valor, textoInput):
    while True:
        try:
            if valor == "":
                print("El valor de la cadena no puede quedar vacío")
                valor = input(textoInput)
                continue

            for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "/"]:
                if i in valor:
                    raise Exception()
            return valor

        except:
            print("No se Pueden Incluir Reales ni Caracteres Especiales en el Nombre")
            valor = input(textoInput)


def verificarCompatibilidad(valor1, valor2):
    equivalenciasUnidades = [
        ["kilogramos", "Kilogramos", "KILOGRAMOS", "KG", "kg", "Kg", "Kilogramo", "kilogramos"], 
        ["gramos", "Gramos", "GRAMOS", "G", "GR", "gr", "Gr", "Gramo", "gramo"],
        ["litros", "Litros", "LITROS", "L", "l", "litro", "Litro"],
        ["Unidades", "Unidad", "unidades", "unidad", "UNIDADES"],
        ["mililitros", "Mililitros", "MILILITROS", "ML", "ml", "Ml", "Mililitro", "mililitro"]
        ]

    for valor in equivalenciasUnidades:
        if valor1 in valor and valor2 in valor:
            return True
    
    return False

def equivalidar(valor1, valor2):
    if valor1 in ["kilogramos", "Kilogramos", "KILOGRAMOS", "KG", "kg", "Kg", "Kilogramo", "kilogramos"] and valor2 in ["gramos", "Gramos", "GRAMOS", "G", "GR", "gr", "Gr", "Gramo", "gramo"]:
        return True
    
    elif valor2 in ["kilogramos", "Kilogramos", "KILOGRAMOS", "KG", "kg", "Kg", "Kilogramo", "kilogramos"] and valor1 in ["gramos", "Gramos", "GRAMOS", "G", "GR", "gr", "Gr", "Gramo", "gramo"]:
        return True
    
    elif valor1 in ["litros", "Litros", "LITROS", "L", "l", "litro", "Litro"] and valor2 in ["mililitros", "Mililitros", "MILILITROS", "ML", "ml", "Ml", "Mililitro", "mililitro"]:
        return True

    elif valor2 in ["litros", "Litros", "LITROS", "L", "l", "litro", "Litro"] and valor1 in ["mililitros", "Mililitros", "MILILITROS", "ML", "ml", "Ml", "Mililitro", "mililitro"]:
        return True

    

def verificarTipoDeDato(valor, tipoDeDato):
    pass









