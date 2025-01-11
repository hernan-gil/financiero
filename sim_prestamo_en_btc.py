import pandas as pd

# Datos iniciales
precio_btc = 400_000_000  # Precio de 1 BTC en COP
colateral = 0.5 * precio_btc  # Valor del colateral (0.5 BTC)
ltv = 0.5  # Loan-to-Value máximo (50%)
tasa_ea = 0.35  # Tasa de interés efectiva anual (35%)
plazo_años = 5  # Plazo del préstamo en años
sueldo_anual_requerido = 60_000_000  # Sueldo requerido al año en COP

# Cálculos iniciales
prestamo_inicial = colateral * ltv  # Préstamo máximo
saldo_anterior = prestamo_inicial

# Tabla de simulación
datos = []

for año in range(1, plazo_años + 1):
    intereses_anuales = saldo_anterior * tasa_ea  # Intereses del año
    saldo_actual = saldo_anterior + intereses_anuales  # Saldo refinanciado
    disponible_retiro = prestamo_inicial - intereses_anuales  # Sueldo neto después de intereses
    
    # Añadir datos a la tabla
    datos.append({
        "Año": año,
        "Saldo Inicial (COP)": saldo_anterior,
        "Intereses Anuales (COP)": intereses_anuales,
        "Saldo Refinanciado (COP)": saldo_actual,
        "Disponible para Retiro Anual (COP)": disponible_retiro
    })
    
    # Actualizar saldo para el siguiente año
    saldo_anterior = saldo_actual

# Crear DataFrame para mostrar la tabla
tabla_simulacion = pd.DataFrame(datos)
tabla_simulacion
