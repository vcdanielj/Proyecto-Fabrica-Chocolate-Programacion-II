
# MODULO DE "NOMBRE DEL MODULO"

#Notas:
"""Desarrollar todo el modulo dentro de una sola función que englobe al modulo."""
"""No habra inputs dentro de la función, en cambio todo los datos necesarios se pedirán a través de parámetros"""
"""Especificar el tipo de dato del tipo de dato del parametro y el tipo de dato a retornar."""
"""Dentro de una función puede haber otras funciones definidas"""
"""Para hacer los test se puede llamar a la función desde afuera y darle datos válidos o inválidos a los parametros"""



def nombreDelModulo(parametro1: int, parametro2: str, parametro3: list) -> dict:

    print(f"El parametro 1: {parametro1} debe ser un entero")
    print(f"El parametro 2: {parametro2} debe ser un string")
    print(f"El parametro 3: {parametro3} debe ser una lista")

    valorDeRetorno = {"\nprimer parametro": parametro1, "segundo parametro": parametro2, "tercer parametro": parametro3}

    print(f"El valor de retorno: {valorDeRetorno} debe ser un diccionario\n")

    return valorDeRetorno



# Tests

#   Datos Válidos 

print(nombreDelModulo(1, "primera prueba", [1, 1, 1]))
print(nombreDelModulo(2, "segunda prueba", [2, 2, 2]))
print(nombreDelModulo(3, "tercera prueba", [3, 3, 3]))
print(nombreDelModulo(4, "cuarta prueba", [4, 4, 4]))


#   Datos inválidos (para manejo de errores)

print(nombreDelModulo("Primera prueba inválida", 1, {5:1}))
print(nombreDelModulo("Segunda prueba inválida", False, 2))