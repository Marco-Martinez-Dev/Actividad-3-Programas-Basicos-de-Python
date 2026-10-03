"""
Programa: Cálculo del área de un rectángulo
Descripción: Solicita la base y la altura de un rectángulo para calcular su área total.
"""

# Importaciones (ninguna necesaria en este caso)

# Constantes (ninguna necesaria)

# Funciones
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Parámetros:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Retorna:
        float: El área calculada del rectángulo.
    """
    return base * altura


# Bloque principal
if __name__ == "__main__":
    print("--- CÁLCULO DEL ÁREA DE UN RECTÁNGULO ---")

    # Entrada de datos
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))

    # Proceso
    area = calcular_area_rectangulo(base, altura)

    # Salida
    print(f"\nEl área del rectángulo es: {area:.2f}")