"""
Programa: Cálculo del Salario Neto
Descripción: Calcula el impuesto acumulado y el salario neto de un empleado según las deducciones.
"""

# Importaciones (ninguna necesaria)

# Constantes (ninguna necesaria)

# Funciones
def calcular_impuesto(salario_bruto, porcentaje_impuesto):
    """
    Calcula el monto correspondiente a impuestos.

    Parámetros:
        salario_bruto (float): Salario mensual sin deducciones.
        porcentaje_impuesto (float): Porcentaje de impuestos a retener.

    Retorna:
        float: Monto a descontar por impuestos.
    """
    return salario_bruto * (porcentaje_impuesto / 100)


def calcular_salario_neto(salario_bruto, impuesto, deducciones):
    """
    Calcula el salario neto final.

    Parámetros:
        salario_bruto (float): Salario bruto mensual.
        impuesto (float): Monto total de impuestos.
        deducciones (float): Deducciones adicionales.

    Retorna:
        float: El salario neto final a percibir.
    """
    return salario_bruto - impuesto - deducciones


# Bloque principal
if __name__ == "__main__":
    print("--- CÁLCULO DE SALARIO NETO ---")

    # Entrada de datos
    salario_bruto = float(input("Ingresa el salario bruto mensual ($): "))
    porcentaje_impuesto = float(input("Ingresa el porcentaje de impuestos (%): "))
    deducciones = float(input("Ingresa las deducciones adicionales ($): "))

    # Proceso
    impuesto = calcular_impuesto(salario_bruto, porcentaje_impuesto)
    salario_neto = calcular_salario_neto(salario_bruto, impuesto, deducciones)

    # Salida
    print("\n--- DESGLOSE DE NÓMINA ---")
    print(f"Salario Bruto:      ${salario_bruto:,.2f}")
    print(f"Impuestos ({porcentaje_impuesto:.1f}%):  -${impuesto:,.2f}")
    print(f"Deducciones:        -${deducciones:,.2f}")
    print("-" * 32)
    print(f"Salario Neto:       ${salario_neto:,.2f}")