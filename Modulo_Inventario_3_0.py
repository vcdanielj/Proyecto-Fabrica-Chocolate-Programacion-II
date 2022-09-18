
# MODULO DE "NOMBRE DEL MODULO"

#DESCRIPCION DEL MODULO:
#Se recibe como parámetros:
"""
1. Una accion (compra, venta, produccion) en forma de string:
    - inicio      -> Indica que se inicializa el almacenamiento vacio 
    - reinicio    -> Indica que se reinicializa el almacenamiento
    - compra      -> Indica que se compra nueva materia prima y por lo tanto debe ser agregada al inventario                                  
    - venta       -> Indica que se vende un producto comercial y por lo tanto debe ser retirado del inventario
    - produccion  -> Indica que se fabrica un objeto (Se consummen materias primas y se obtienen productos comerciales)
    - consulta    -> Indica que se quiere examinar la cantidad de producto existente en el inventario
2. Un registro en forma de diccionario:
    - para compra: {"producto1": [cant1, "unidad"], "productoN": [cantN, "unidadN"]}
    - para venta: {{"producto":"", "presentacion":"", cantidad: n}  
    - para producción: {"producto":"", "presentacion":"", "cantidad": n, "materia prima usada": {"producto1": [cant1, unidad1], "productoN": [cantN, unidadN]}}
    - para consulta: {"nombre":["producto", "presentacion"], "nombre":["materia prima", "unidades"]}  
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

#Formato del almacenamiento:
"""
    almacenamiento = {
        ("producto 1", "presentacion 1"): cantidad 1,
        ("producto 1", "presentacion 2"): cantidad 2,
        ("producto 2", "presentacion 1"): cantidad 3,
        ("producto N", "presentacion X"): cantidad N,
    }
"""    


#INICIO DEL MODULO

def inventario(accion: str, registro: dict = {}):
    try:

        def inicializarAlmacenamiento():
            global almacenamiento
            
            almacenamiento = {}
            
        def comprar(registro: dict):

            """ Aquí se va iterando la clave y el valor dentro del diccionario que se le pasa como valor """
            
            for producto, valor in registro.items():
                try:
                   
                    """ En esta parte se verifica si el producto existe en el inventario,
                    de existir se le suma la cantidad que lo representa valor[0] a las unidades 
                    existentes en el inventario que se representa como valor[1].  """

                    almacenamiento[(producto, valor[1])] += valor[0]
                    
                except:
                    
                    """ Si no exite el producto en el inventario la cantidad que es valor[0]
                    pasa a agregarse como valor al inventario. """

                    almacenamiento[(producto, valor[1])] = valor[0]


        def vender(registro: dict):
            
            """ De la estructura para ventas que es: {producto:"", presentacion:"", cantidad: n}.
            Se asignan a las variables: producto, presentacion, cantidadProducto los valores que hay en las claves
            producto, presentación y cantidad del diccionario de registro.  """
            
            producto = registro["producto"]
            presentacion = registro["presentacion"]
            cantidadProducto = registro["cantidad"]
            
            try:
                
                """ En este apartado se busca actualizar el inventario restandole la cantidad de producto
                que desea comprar el usuario final a la presentacion"""

                almacenamiento[(producto, presentacion)] -= cantidadProducto

            except:
                
                """ Esto pasara si el usuario ingresa o intenta adquirir un producto que no aparecen en el inventario """
                
                print("Error: Este producto no existe en el inventario")


        def producir(registro: dict):

            """ De la estructura para producir que es: {"producto":"", "presentacion":"", "cantidad": n, "materia prima usada": {"producto1": [cant1, unidad1], "productoN": [cantN, unidadN]}}.
            Se asignan a las variables: producto, presentacion, cantidadProducto los valores que hay en las claves
            producto, presentación y cantidad del diccionario de registro.  """

            producto = registro["producto"]
            presentacion = registro["presentacion"]
            cantidadProducto = registro["cantidad"]
            
            try:

                """ Como en la clave "materia prima" hay un diccionario que contine como claves productos y como valor una lista
                se itera con la variables de ciclo (materiaPrima, valor) dentro del diccionario que hay en "materia prima" y se trata de restar
                las unidades que es valor[1] con las cantidades que es valor[0]   """

                for materiaPrima, valor in registro["materia prima usada"].items():
                    almacenamiento[(materiaPrima, valor[1])] -= valor[0]
            except:
                print(f"{materiaPrima} {valor}: Esta materia prima no existe en el inventario")
            else:

                """ Entrara a este apartado en caso tal de que se haya fabricado correctamente el producto """

                try:
    
                    """ Si en el producto que se acabo de producir ya había sido registrado previamente: """
                    almacenamiento[(producto, presentacion)] += cantidadProducto

                except:

                    """ Si en el producto que se acabo de producir no había sido registrado previamente: """
                    almacenamiento[(producto, presentacion)] = cantidadProducto


        def consultar(registro: dict) -> list: 
            
            """Con la estructura de consulta que  es dada por:  {"nombre":["producto", "presentacion"], "nombre":["materia prima", "unidades"]}
            se quiere verificar si hay cierto elemento existente dentro del inventario que es la variable de ciclo producto
            y con el valor[1] se accede a las cantidades de las presentaciones es decir, por ejemplo:5 galletas, 10 litros de leche... sin los nombres solo
            las cantidades en bruto"""
            
            valores = []

            for producto, valor in registro.items():
                try:
                    valores.append(almacenamiento[(producto, valor[1])])

                except:
                    """De no exitir alguna cantidad de presentación se dice que es 0 su cantidad y se guarda en la lista valores"""
                    valores.append(0.0)
            
            return valores


        """Apartado donde se llaman las a las funciones segun la accion dada en el parametro"""
        if accion == "inicio" or accion == "reinicio":
            inicializarAlmacenamiento()

        elif accion == "compra":
            comprar(registro)

        elif accion == "venta":
            vender(registro)

        elif accion == "produccion":
            producir(registro)

        elif accion == "consulta":
            return consultar(registro)
        
        elif accion == "revision":
            return almacenamiento

        else: 
            return "Ninguna accion valida dada"


        """Apartado Creacion Archivo TXT"""

        """Se resetea el archivo para que quede en blanco"""
        inventarioTXT = open(".\Archivos\inventario.txt", "w", encoding="utf-8")

        """Se rellena el archivo con todos los elementos de la variable almacenamiento"""
        inventarioTXT.write("------------------ INVENTARIO FÁBRICA DE CHOCOLATE ------------------\n\n")

        for k, v in almacenamiento.items():
            linea = f"{k[0]}: {v} {k[1]}\n"

            inventarioTXT.write(linea)
        
        inventarioTXT.close()

    except Exception as e:

        """ Si hay un problema esto devolvera el tipo de problema que se presento para luego validarse en el llamamiento de la funcion """
        print(e)
        return e

# TESTS

# Test de Datos Válidos


# - Test 1

inventario("inicio")
inventario("compra", {"leche":[50, "litros"]})
inventario("compra", {"leche":[10, "litros"]})
inventario("compra", {"huevos":[100, "unidades"]})
inventario("compra", {"cacao":[10, "kilogramos"]})
inventario("venta", {"producto": "cacao", "presentacion": "kilogramos", "cantidad": 6})
inventario("produccion", {"producto":"galletas de chocolate", "presentacion": "paquetes de 3 unidades", "cantidad": 10, "materia prima usada": {"leche": [2,"litros"], "huevos": [10, "unidades"], "cacao": [1, "kilogramos"]}})

if inventario("consulta", {"galletas de chocolate":["producto", "paquetes de 3 unidades"], "leche": ["materia prima", "litros"], "huevos": ["materia prima", "unidades"], "cacao": ["materia prima", "kilogramos"]}) == [10.0, 58.0, 90.0, 3.0]:
    print("Test 1 pasado")
else:
    print("Test 1 no pasado")
    

# - Test 2

inventario("reinicio")
inventario("compra", {"avellana":[5, "kilogramos"], "almendras":[10, "kilogramos"]})
inventario("compra", {"mani":[10, "kilogramos"]})
inventario("compra", {"cacao":[25, "kilogramos"]})
inventario("compra", {"azucar":[15, "kilogramos"]})

inventario("produccion", {"producto":"chocolate de mani", "presentacion": "tableta", "cantidad": 10, "materia prima usada": {"avellana": [3,"kilogramos"], "mani": [6, "kilogramos"], "cacao": [3, "kilogramos"]}})
inventario("produccion", {"producto":"chocolate almendrado", "presentacion": "tableta", "cantidad": 25, "materia prima usada": {"almendras": [8,"kilogramos"], "avellana": [1, "kilogramos"], "cacao": [7, "kilogramos"]}})

inventario("venta", {"producto": "chocolate de mani", "presentacion": "tableta", "cantidad": 6})
inventario("venta", {"producto": "chocolate almendrado", "presentacion": "tableta", "cantidad": 6})

if inventario("consulta", {"chocolate de mani":["producto", "tableta"], "chocolate almendrado":["producto", "tableta"]}) == [4.0, 19.0]:
    print("Test 2 pasado")
else:
    print("Test 2 no pasado")


# - Test 3

if inventario("consulta", {"leche": ["materia prima", "litros"], "chocolate blanco": ["producto", "tableta"]}) == [0.0, 0.0]:
    print("Test 3 pasado")
else:
    print("Test 3 no pasado")


# - Test 4

#       -> En el archivo Main.py 