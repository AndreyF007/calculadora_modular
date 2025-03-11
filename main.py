from calculador.operaciones import *
from calculador.menu import menu
def main():
    """
    Función principal de la calculadora.

    Esta función muestra un menú de opciones para realizar operaciones matemáticas
    básicas como suma, resta, multiplicación, división y potencia. Solicita al usuario
    que ingrese una opción y dos números, y luego realiza la operación seleccionada.
    La función continúa ejecutándose hasta que el usuario elige salir.

    Raises:
        ValueError: Si se ingresa un valor no numérico.
        ZeroDivisionError: Si se intenta dividir por cero.
    """
    while True:
        print("Calculadora".center(50))
        menu()
        try:
            elegir_opciones = int(input("Ingresa una opción disponible: "))
            if elegir_opciones < 1 or elegir_opciones > 6:
                print("La opcion ingresada no está disponible. Intentalo de nuevo.")
                continue
            if elegir_opciones == 6:
                salir()
                break
            num1 = float(input("ingresa el primer valor: "))
            num2 = float(input("Ingresa el segúndo valor: "))
            if elegir_opciones == 1:
                resultado_suma = sumar(num1, num2)
                print(F"El resultado de la suma es {resultado_suma}")
            elif elegir_opciones == 2:
                resultado_resta = restar(num1, num2)
                print(F"El resultado de la resta es de: {resultado_resta}")
            elif elegir_opciones == 3:
                resultado_multiplar = multiplicar(num1, num2)
                print(F"El resultado de la multiplicación es: {resultado_multiplar}")
            elif elegir_opciones == 4:
                resultado_division = dividir(num1, num2)
                print(F"El resultado de la división es de: {resultado_division}")
            elif elegir_opciones == 5:
                resultado_potencia = potencia(num1, num2)
                print(F"El resultado de la potencia es de: {resultado_potencia}")
        except ValueError:
            print("Error: Se ha ingresado un valor incorrecto. Intentalo de nuevo.")
        except ZeroDivisionError:
            print("Error: No se permite la división por cero. Intentalo de nuevo.")



if __name__ == "__main__":
    main()
