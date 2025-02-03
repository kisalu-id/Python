import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt
# paandas -  tools for working with structured data, especially tabular data like data from CSV files


def plot_daily_averages(df):
    #extract the date only (no time) and create a new column - 'date' is now a new column that's added to the DataFrame
    df['date'] = df['utc_timestamp'].dt.date
    #group by 'date' and calculate the mean for all numeric columns
    daily_averages = df.groupby('date').mean()

    print("\nTägliche Durchschnittswerte (AT, gerundet):")
    #print(daily_averages[['AT_temperature']].round(2).to_string(index=True))
    print(daily_averages[['AT_temperature']].round(2).to_string(formatters={'AT_temperature': '{:,.2f}'.format}, index_names=False))
    #plot daily averages
    plt.figure(figsize=(18, 6))
    smoothed_data = daily_averages['AT_temperature'].rolling(7).mean()
    plt.plot(daily_averages.index, smoothed_data, label='AT Temperatur', color='blue', alpha=0.7, linestyle='-')
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.title('Tägliche Durchschnittstemperatur (AT)')
    #plt.legend() displays the legend on the plot, which shows the labels for each line or data series - it will show a box "AT Temperatur"
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

    return daily_averages


def compare_different_countries(daily_averages):
    #compare different countries - Germany, United Kingdom and Lithuania
    print("\nTägliche Durchschnittswerte (gerundet, °C):")
    print(daily_averages[['DE_temperature', 'GB_temperature', 'LT_temperature']].round(2).to_string(index=True))

    plt.figure(figsize=(14, 6))
    plt.plot(daily_averages.index, daily_averages['DE_temperature'], label='Deutschland (DE)', color='red', alpha=0.8, linestyle='-', linewidth=0.5)
    plt.plot(daily_averages.index, daily_averages['GB_temperature'], label='Vereinigtes Königreich (GB)', color='blue', alpha=0.8, linestyle='-', linewidth=0.5)
    plt.plot(daily_averages.index, daily_averages['LT_temperature'], label='Litauen (LT)', color='green', alpha=0.8, linestyle='-', linewidth=0.5)

    plt.xlabel("Datum")
    plt.ylabel("Temperatur (°C)")
    plt.title("Tägliche Durchschnittstemperaturen (DE, GB, LT)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()


def mean_for_yearly_temperatures(df):
    #calculate the mean for yearly temperatures and create a new column
    df['year'] = df['utc_timestamp'].dt.year
    yearly_averages = df.groupby('year')['AT_temperature'].mean()
    print("\nJährliche Durchschnittswerte:")
    print(yearly_averages.round(2).to_string(index=True))

    #plot yearly averages
    plt.figure(figsize=(12, 6))
    #daily_averages.index represents the x-axis values (dates); daily_averages['AT_temperature']represents the y-axis values (average temperature for Austria, "AT").
    plt.plot(yearly_averages.index, yearly_averages.values, color='green', linewidth=1.5, alpha=0.7, marker='o', markersize=5) #alpha is transparency of the plot line
    plt.xlabel('Jahr')
    plt.ylabel('Temperatur (°C)')
    plt.title('Jährliche Durchschnittstemperatur (AT)')
    plt.grid(True)
    plt.show()


def daily_temperatures_11_AM(df):
    #daily temperatures at 11 AM
    df['hour'] = df['utc_timestamp'].dt.hour
    df['minute'] = df['utc_timestamp'].dt.minute
    temps_11_am = df[(df['hour'] == 11) & (df['minute'] == 0)].groupby('date')['AT_temperature'].mean()

    #plot daily temperatures at 11 AM
    plt.figure(figsize=(12, 6))
    plt.plot(temps_11_am.index, temps_11_am.values, label='Temperatur um 11:00 Uhr', color='cyan', linewidth=0.6)
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperaturen um 11:00 Uhr (AT)')
    plt.legend()
    plt.grid(True)
    plt.show()


def histogram_temperature_distribution_Germany_in_last_5_years(df):
    last_5_years = df[df['utc_timestamp'].dt.year >= df['utc_timestamp'].dt.year.max() - 4]
    plt.figure(figsize=(12, 6))
    plt.hist(last_5_years['DE_temperature'], bins=40, color='orange', alpha=0.7, edgecolor='black', density=True)
    plt.xlabel("Temperatur (°C)")
    plt.ylabel("Häufigkeit")
    plt.title("Temperaturverteilung in Deutschland (DE) - Letzte 5 Jahre")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()



def read_csv():
    file_path = r"C:\...\08 Wetter Daten.csv"
    
    #df stands for DataFrame - a data structure in Pandas that looks like a table (rows and columns), 
    #similar to what you see in Excel or SQL tables
    df = pd.read_csv(file_path)

    #convert utc_timestamp to a datetime object
    df['utc_timestamp'] = pd.to_datetime(df['utc_timestamp'])

    daily_averages = plot_daily_averages(df)

    compare_different_countries(daily_averages)

    mean_for_yearly_temperatures(df)

    daily_temperatures_11_AM(df)

    histogram_temperature_distribution_Germany_in_last_5_years(df)



if __name__ == "__main__":
    read_csv()
