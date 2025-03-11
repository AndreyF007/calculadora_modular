"""
Módulo de operaciones matemáticas básicas.
Este módulo proporciona funciones para realizar operaciones matemáticas básicas
como suma, resta, multiplicación, división y potencia. También incluye una función
para imprimir un mensaje de salida del programa.
"""

def sumar(a, b):
    """Suma dos números.
    Args:
        a (float): El primer número.
        b (float): El segundo número.
    Returns:
        float: La suma de a y b.
    """
    return a + b
def restar(a, b):
    """Resta el segundo número del primero.
    Args:
        a (float): El primer número.
        b (float): El segundo número.
    Returns:
        float: La diferencia entre a y b.
    """
    return a - b
def multiplicar(a, b):
    """Multiplica dos números.
    Args:
        a (float): El primer número.
        b (float): El segundo número.
    Returns:
        float: El producto de a y b.
    """
    return a * b
def dividir(a, b):
    """Divide el primer número por el segundo.
    Args:
        a (float): El primer número.
        b (float): El segundo número.
    Returns:
        float: El cociente de a y b.
    """
    return a / b
def potencia(a, b):
    """Eleva el primer número a la potencia del segundo número.
    Args:
        a (float): El primer número.
        b (float): El exponente.
    Returns:
        float: El resultado de a elevado a la potencia de b.
    """
    return a ** b
def salir():
    """
    Imprime un mensaje de salida del programa.
    """
    print("Saliendo del programa.")
