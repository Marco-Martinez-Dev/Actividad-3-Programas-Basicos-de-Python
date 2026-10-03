"""
Programa: Calculadora de promedios
Descripción: Solicita tres números al usuario y calcula su promedio aritmético.
"""

# Importaciones (ninguna necesaria)

# Constantes
TOTAL_NUMEROS = 3

# Funciones
def calcular_promedio(num1, num2, num3):
    """
    Calcula el promedio de tres números.

    Parámetros:
        num1 (float): Primer número.
        num2 (float): Segundo número.
        num3 (float): Tercer número.

    Retorna:
        float: El promedio de los tres números.
    """
    suma = num1 + num2 + num3
    return suma / TOTAL_NUMEROS


# Bloque principal
if __name__ == "__main__":
    print("--- CÁLCULO DEL PROMEDIO ---")

    # Entrada de datos
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    # Proceso
    promedio = calcular_promedio(num1, num2, num3)

    # Salida
    print(f"\nTu promedio es: {promedio:.2f}")