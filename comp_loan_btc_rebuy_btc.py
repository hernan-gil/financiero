# Reimportar bibliotecas necesarias tras el reinicio del estado
import pandas as pd

# Parámetros iniciales del escenario
precio_inicial_btc = 400_000_000  # Precio inicial de 1 BTC en COP
colateral_btc = 0.7  # Colateral en BTC
ltv = 0.5  # Loan-to-Value máximo (50%)
tasa_ea = 0.22  # Tasa de interés efectiva anual (22%)
plazo_años = 5  # Plazo en años
crecimiento_btc_anual = 0.1  # Crecimiento anual del precio de BTC (10%)

# Cálculos iniciales
colateral_cop = colateral_btc * precio_inicial_btc  # Valor del colateral en COP
prestamo_inicial = colateral_cop * ltv  # Préstamo inicial (50% del colateral)
saldo_anterior = prestamo_inicial  # Saldo inicial del préstamo

# Simulaciones para los dos escenarios
datos_esc1 = []  # Escenario 1: Sueldo anual
datos_esc2 = []  # Escenario 2: Reinversión en BTC

# Variables para el escenario 2
btc_comprado = prestamo_inicial / precio_inicial_btc  # BTC comprados con el préstamo
valor_total_btc = colateral_cop  # Valor inicial del portafolio en BTC

for año in range(1, plazo_años + 1):
    # Escenario 1: Sueldo anual
    intereses_anuales = saldo_anterior * tasa_ea  # Intereses del año
    saldo_actual = saldo_anterior + intereses_anuales  # Saldo refinanciado
    disponible_retiro = prestamo_inicial - intereses_anuales  # Sueldo neto disponible
    datos_esc1.append({
        "Año": año,
        "Saldo Inicial (COP)": saldo_anterior,
        "Intereses Anuales (COP)": intereses_anuales,
        "Saldo Refinanciado (COP)": saldo_actual,
        "Disponible para Retiro Anual (COP)": disponible_retiro
    })
    saldo_anterior = saldo_actual  # Actualizar saldo para el siguiente año

    # Escenario 2: Reinversión en BTC
    precio_actual_btc = precio_inicial_btc * (1 + crecimiento_btc_anual) ** año  # Precio de BTC actual
    valor_total_btc = (colateral_btc + btc_comprado) * precio_actual_btc  # Valor total del portafolio en BTC
    datos_esc2.append({
        "Año": año,
        "Precio BTC (COP)": precio_actual_btc,
        "Valor Portafolio (COP)": valor_total_btc
    })

# Crear DataFrames para mostrar las tablas
tabla_esc1 = pd.DataFrame(datos_esc1)
tabla_esc2 = pd.DataFrame(datos_esc2)

tabla_esc1, tabla_esc2
