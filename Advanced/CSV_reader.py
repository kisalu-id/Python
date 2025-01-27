import csv
import matplotlib.pyplot  as plt
import pandas as pd
from datetime import datetime

# paandas -  tools for working with structured data, especially tabular data like data from CSV files

def plot_data(df):
    plt.title("ABC")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.hist(x, y) #histogram
    plt.plot(x, y, color="red")



def analyze_data(df):
    #extract the date only (no time) and create a new column
    df['date'] = df['utc_timestamp'].dt.date
    
    #group by 'date' and calculate the mean for all numeric columns
    daily_averages = df.groupby('date').mean()
    print(daily_averages)

    #calculate the mean for yearly temperatures 
    df['year'] = df['utc_timestamp'].dt.year
    yearly_averages = df.groupby('year')['AT_temperature'].mean()

    #daily temperatures at 11 AM


def read_csv():
    file_path = '08 Wetterdaten.csv'

    #df stands for DataFrame - a data structure in Pandas that looks like a table (rows and columns), 
    #similar to what you see in Excel or SQL tables
    df = pd.read_csv(file_path)

    #convert utc_timestamp to a datetime object
    df['utc_timestamp'] = pd.to_datetime(df['utc_timestamp'])

    plot_data(df)

    analyze_data(df)




#mean_temp = df['AT_temperature'].mean()

if __name__ == "__main__":
    read_csv()
