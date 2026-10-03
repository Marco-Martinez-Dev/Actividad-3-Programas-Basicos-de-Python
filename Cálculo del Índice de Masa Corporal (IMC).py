"""
Programa: Cálculo de IMC
Descripción: Solicita el peso y la altura de una persona para calcular su Índice de Masa Corporal.
"""

# Importaciones (ninguna necesaria)

# Constantes (ninguna necesaria)

# Funciones
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Parámetros:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Retorna:
        float: El valor del IMC.
    """
    return peso / (altura ** 2)


# Bloque principal
if __name__ == "__main__":
    print("--- CÁLCULO DEL IMC ---")

    # Entrada de datos
    peso = float(input("Ingresa tu peso en kilogramos (kg): "))
    altura = float(input("Ingresa tu altura en metros (m): "))

    # Proceso
    imc = calcular_imc(peso, altura)

    # Salida
    print(f"\nTu Índice de Masa Corporal (IMC) es: {imc:.2f}")