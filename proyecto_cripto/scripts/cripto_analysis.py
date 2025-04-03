# cripto_analysis.py

# Importación de librerías
import requests
import pandas as pd

# Definición de constantes
API_KEY = "tu_api_key_aqui"
SYMBOL = "BTC"
CURRENCY = "USD"
LIMIT = 1000

# Función para obtener datos históricos
def obtener_datos_historicos(api_key, symbol, currency, limit):
    url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym={symbol}&tsym={currency}&limit={limit}&api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["Data"]["Data"]
    else:
        raise Exception(f"Error al obtener los datos: {response.status_code}")

# Función para crear un DataFrame
def crear_dataframe(datos):
    df = pd.DataFrame(datos)
    df["time"] = pd.to_datetime(df["time"], unit="s")
    return df

# Ejecución principal
if __name__ == "__main__":
    # Obtener datos históricos
    datos = obtener_datos_historicos(API_KEY, SYMBOL, CURRENCY, LIMIT)
    
    # Crear DataFrame
    df = crear_dataframe(datos)
    
    # Guardar datos en CSV
    df.to_csv("data/historical_btc.csv", index=False)
    
    print("Datos guardados exitosamente en 'data/historical_btc.csv'")