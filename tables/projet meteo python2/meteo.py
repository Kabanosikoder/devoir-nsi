# 1. Introduction
# Dans ce premier TP, nous allons revoir quelques basiques Python que sont les listes et les dictionnaires.
# Nous allons nous exercer sur des données importées depuis un fichier CSV contenant des relevés MétéoFrance.

# 2. Import d’un fichier CSV en Python
import csv
import pandas as pd
def load_csv(filename):
    """Load the CSV file and preprocess the data using pandas."""
    df = pd.read_csv(filename, sep=';', encoding='utf-8')
    df = df[(df['ff'] != 'mq') & (df['t'] != 'mq') & (df['u'] != 'mq') & (df['rr1'] != 'mq')]
    df = df.assign(
        vitesse_vent=df['ff'].astype(float) * 3.6,  # Convert m/s to km/h
        temperature=df['t'].astype(float) - 273.15,  # Convert Kelvin to Celsius
        humidite=df['u'].astype(int),
        precipitations=df['rr1'].astype(float)
    )
    return df

def temperature_min(df):
    """Return the minimum temperature recorded."""
    return df['temperature'].min()

def max_wind_speed_station(df):
    """Return the station ID with the highest wind speed."""
    return df.loc[df['vitesse_vent'].idxmax(), 'numer_sta']

def average_humidity(df):
    """Return the average humidity."""
    return df['humidite'].mean()

def average_precipitation_60000_69999(df):
    """Return the average precipitation for stations with ID in range 60000-69999."""
    filtered = df[(df['numer_sta'].astype(int) >= 60000) & (df['numer_sta'].astype(int) <= 69999)]
    return filtered['precipitations'].mean() if not filtered.empty else 0

def merge_weather_data(df_2009, df_2019):
    """Merge weather records from 2009 and 2019, keeping only common stations."""
    merged = pd.merge(
        df_2009[['numer_sta', 'temperature']].rename(columns={'temperature': 't2009'}),
        df_2019[['numer_sta', 'temperature']].rename(columns={'temperature': 't2019'}),
        on='numer_sta'
    )
    return merged

def hotter_year(merged_data):
    """Determine whether February 2009 or February 2019 was hotter on average."""
    avg_2009 = merged_data['t2009'].mean()
    avg_2019 = merged_data['t2019'].mean()
    return "2019" if avg_2019 > avg_2009 else "2009"

# Les valeurs ne sont pas correctes parce que les fichiers on changer
if __name__ == "__main__":
    # Load data (replace filenames with actual file paths)
    records_2019 = load_csv("projet meteo python2/february_2019.csv")
    records_2009 = load_csv("projet meteo python2/february_2009.csv")

    # Question 1
    print("Question 1: Modifications appliquées pour les champs requis.")

    # Question 2
    temp_min = temperature_min(records_2019)
    print(f"Question 2: Température minimale en février 2019: {temp_min:.2f}°C")

    # Question 3
    max_wind_id = max_wind_speed_station(records_2019)
    print(f"Question 3: ID de la station avec la vitesse de vent maximale en février 2019: {max_wind_id}")

    # Question 4
    avg_humidity = average_humidity(records_2019)
    print(f"Question 4: Humidité moyenne en février 2019: {avg_humidity:.1f}%")

    # Question 5
    avg_precipitation = average_precipitation_60000_69999(records_2019)
    print(f"Question 5: Précipitations moyennes entre 60000 et 69999 en février 2019: {avg_precipitation:.1f}mm")

    # Questions 9 et 10
    merged_data = merge_weather_data(records_2009, records_2019)
    hotter = hotter_year(merged_data)
    print(f"Question 9 et 10: Le mois le plus chaud entre février 2009 et 2019: Février {hotter}")