import csv
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime as dt
# paandas -  tools for working with structured data, especially tabular data like data from CSV files


def analyze_data(df):
    #extract the date only (no time) and create a new column - 'date' is now a new column that's added to the DataFrame
    df['date'] = df['utc_timestamp'].dt.date
    #group by 'date' and calculate the mean for all numeric columns
    daily_averages = df.groupby('date').mean()
    print("\nTägliche Durchschnittswerte:")
    print(daily_averages['AT_temperature'])

    #plot daily averages
    plt.figure(figsize=(18, 6))
    plt.plot(daily_averages.index, daily_averages['AT_temperature'], label='AT Temperatur', color='blue')
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.title('Tägliche Durchschnittstemperatur (AT)')
    #plt.legend() displays the legend on the plot, which shows the labels for each line or data series - it will show a box "AT Temperatur"
    plt.legend()
    plt.grid(True)
    plt.show()


    #compare different countries - Germany, United Kingdom and Lithuania
    print("\nTägliche Durchschnittswerte (Temperaturen für DE, GB, LT):")
    print(daily_averages[['DE_temperature', 'GB_temperature', 'LT_temperature']])

    #calculate the mean for yearly temperatures and create a new column
    df['year'] = df['utc_timestamp'].dt.year
    yearly_averages = df.groupby('year')['AT_temperature'].mean()
    print("\nJährliche Durchschnittswerte:")
    print(yearly_averages)

    #plot yearly averages
    plt.figure(figsize=(12, 6))
    #daily_averages.index represents the x-axis values (dates); daily_averages['AT_temperature']represents the y-axis values (average temperature for Austria, "AT").
    plt.plot(yearly_averages.index, yearly_averages.values, color='green', alpha=0.7) #alpha is transparency of the plot line
    plt.xlabel('Jahr')
    plt.ylabel('Temperatur (°C)')
    plt.title('Jährliche Durchschnittstemperatur (AT)')
    plt.grid(True)
    plt.show()

    #daily temperatures at 11 AM
    df['hour'] = df['utc_timestamp'].dt.hour
    df['minute'] = df['utc_timestamp'].dt.minute
    temps_11_am = df[(df['hour'] == 11) & (df['minute'] == 0)].groupby('date')['AT_temperature'].mean()

    #plot daily temperatures at 11 AM
    plt.figure(figsize=(12, 6))
    plt.plot(temps_11_am.index, yearly_averages.values, label='Temperatur um 11:00 Uhr', color='cyan')
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperaturen um 11:00 Uhr (AT)')
    plt.legend()
    plt.grid(True)
    plt.show()
    #compare GB LT LV and NL

def plot_data(df):
    plt.figure(figsize=(12, 6))
    plt.plot(temps_11_am.index, yearly_averages.values, label='Temperatur um 11:00 Uhr', color='cyan')
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
    plt.title('Temperaturen um 11:00 Uhr (AT)')
    plt.legend()
    plt.grid(True)
    plt.show()


    plt.title("ABC")
    plt.xlabel("X")
    plt.ylabel("Y")
    x = 5
    y = 10
    plt.hist(x, y) #histogram
    plt.plot(x, y, color="red")
    plt.show()

    
    #histogram
    plt.figure(figsize=(12, 6))
    plt.hist(df['AT_temperature'], bins=30)
    plt.xlabel('Temperatur (°C)')
    plt.ylabel('Emmmmmm')
    plt.title('Histogramm der Temperaturen (AT)')
    plt.show()

    #compare
    daily_means = df.groupby('date').mean()
    plt.figure(figsize=(12, 6))

    plt.legend()
    plt.grid(True)
    plt.show()
    


def read_csv():
    file_path = r"C:\Users\DDXNB_Alien15\Downloads\08 Wetter Daten.csv"

    #df stands for DataFrame - a data structure in Pandas that looks like a table (rows and columns), 
    #similar to what you see in Excel or SQL tables
    df = pd.read_csv(file_path)

    #convert utc_timestamp to a datetime object
    df['utc_timestamp'] = pd.to_datetime(df['utc_timestamp'])

    analyze_data(df)

    plot_data(df)


#mean_temp = df['AT_temperature'].mean()

if __name__ == "__main__":
    read_csv()
