#PROGRAMA PRINCIPAL PROYECTO FABRICA DE CHOCOLATE

"""A Este Programa se le Harán Las Importaciones de Cada Modulo"""
from Modulo_Inventario_3_0 import inventario




# Test de Inventario

inventario("inicio")
inventario("compra", {"manteca de cacao":[25, "kilogramos"]})
inventario("compra", {"leche":[10, "litros"]})
inventario("compra", {"azucar":[100, "kilogramos"]})
inventario("compra", {"pasta de cacao":[10, "kilogramos"]})

inventario("produccion", {"producto":"chocolate blanco", "presentacion": "tabletas", "cantidad": 40, "materia prima usada": {"manteca de cacao": [10, "kilogramos"], "azucar": [7, "kilogramos"]}})
inventario("produccion", {"producto":"chocolate con leche", "presentacion": "tabletas", "cantidad": 10, "materia prima usada": {"pasta de cacao": [2,"kilogramos"], "azucar": [4, "kilogramos"], "leche": [1, "litros"]}})

inventario("venta", {"producto": "chocolate blanco", "presentacion": "tabletas", "cantidad": 5})
inventario("venta", {"producto": "chocolate con leche", "presentacion": "tabletas", "cantidad": 6})
inventario("venta", {"producto": "chocolate blanco", "presentacion": "tabletas", "cantidad": 3})
inventario("venta", {"producto": "chocolate blanco", "presentacion": "tabletas", "cantidad": 4})

if inventario("consulta", {"chocolate blanco":["producto", "tabletas"], "chocolate con leche":["producto", "tabletas"], "leche": ["materia prima", "litros"], "azucar": ["materia prima", "kilogramos"]}) == [28.0, 4.0, 9.0, 89.0]:
    print("Test 4 pasado")
else:
    print("Test 4 no pasado")

    