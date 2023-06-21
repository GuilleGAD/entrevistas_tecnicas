"""
Definir una funcion max() que tome como arumento dos numeros y 
devuelva el mayor de ellos.
"""

def custom_max(n1: int, n2: int):
    """Dados dos numeros de entrada retornar el maximo de ambos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar

    Returns:
        int: Mayor de ambos
    """
    if n2>n1:
        return n2
    elif n1>n2:
        return n1
    else:
        raise Exception("No hay una especificación de que hacer cuando sean iguales")
    raise Exception("Algo salió mal")

print("custom max:", custom_max(1234,42))

def max_de_tres(n1: int, n2: int, n3: int):
    """Toma tres números como argumentos y devuelve el mayor de ellos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar
        n3 (int): Tercer numero a comparar

    Returns:
        int: Mayor de los tres
        
    a>b>c => por transitividad
    b>c
    a>c
    """
    
    n = custom_max(n1,n2)
    
    return custom_max(n,n3)

print("max de tres:", max_de_tres(123,54,34))

def sum(lista: list[int]):
    """Escribir una función sum que sume todos los números de la lista

    Args:
        lista (list[int]): Lista de numeros

    Returns:
        int: Resultado de la suma
    """
    resultado = 0
    
    for i in lista:
        resultado = resultado + i

    return resultado

print("sum list:", sum([1,2,3,4,-5]))

def multip(lista: list[int]):
    """Escribir una función multip que multiplique todos los números de la lista

    Args:
        lista (list[int]): Lista de numeros

    Returns:
        int: Resultado de la multiplicación
    """
    resultado = 1
    
    for i in lista:
        if type(i)== int:
            resultado = resultado * i
        else:        
            raise Exception("algo salió mal")
    
    return resultado

print("multip list:", multip([1,2,3,-4]))

def inversa(cadena: str):
    """Definir una funcion que calcule la inversión de una cadena

    Args:
        cadena (str): Cadena de entrada

    Returns:
        _type_: Cadena de salida
    """
    salida = ""
    
    for x in cadena:
        salida = x + salida
    
    return salida

print("Inversa String:", inversa("estoy probando"))

def es_palindromo(cadena: str):
    """Una funcion que devuelve True en caso de que la cadena sea Palindromo

    Args:
        cadena (str): Cadena de entrada

    Returns:
        Boolean: True en caso de ser palindromo, False caso contrario
    """
    
    return inversa(cadena)==cadena

print("Palindromo String", es_palindromo("radara"))

def superposicion(list1: list, list2: list):
    """
    Definir una funcion que tome dos listas y devuelva True si tiene al menos 1 miembro
    en común o devuelva False en caso contrario. Escribir la función usando bucle anidado

    Args:
        list1 (list): Primera lista de entrada
        list2 (list): Segunda lista de entrada

    Returns:
        Boolean: True en caso de de tener 1 miembro en comun, Fase caso contario.
    """
    
    for x in list1:
        for y in list2:
            if x == y:
                return True
            
    """sin for anidado
    for x in list1:
        if y in list2:
        return True
    return False   
    """
    
    return False

print("Superposición:", superposicion([1,2,"a",4,5],[6,7,8,9,"a"]))

def generar_n_caracteres(i: int, car: str):
    """Definir una funcion que tome un entero n y un carcater y devuelva el
    caracter multiplicado por n. Ej.: generar_n_caracteres(5,"x") devuelve "xxxxx"

    Args:
        i (int): Numero de cantidad de veces que se tiene que repetir el caracter
        car (str): Caracter de entrada
        
    Returns:
        String: Caracter multiplicado i veces
    """
    """resultado = ""
    for n in range(0,i):
        resultado = resultado + car
    
    return resultado"""
    
    return car * i

print("Generar n caracteres:", generar_n_caracteres(5 ,"x"))

def procedimiento(lista: list[int]):
    """Definir un procedimiento que tome una lista de numeros enteros e imprima un
    histograma en la pantalla. Ej.: procedimiento([4,9,7]) debería imprimir:
    ****
    *********
    *******

    Args:
        lista (list[int]): Lista de enteros

    """
    for x in lista:
        print("*" * x)

print("Histograma procedimiento:")
procedimiento([4,9,7])