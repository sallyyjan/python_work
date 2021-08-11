import csv
from datetime import datetime

import matplotlib.pyplot as plt

def find_column_numbers(*column_names, reader):
    header_row = next(reader)
    print(header_row)
    column_numbers = {}

    for name in column_names:
        column_number = header_row.index(name)
        column_numbers[name] = column_number
    
    print(column_numbers)
    return column_numbers


while True:
    filename = input("Enter the relative path of the dataset you want to " 
        "visulalize: ")
        
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            col_nums = find_column_numbers('NAME', 'DATE', 'TMAX', 'TMIN',
                reader=reader)
            
            # Get dates, and max and min temperatures
            highs, lows, dates = [], [], []
            for row in reader:
                date = datetime.strptime(row[col_nums['DATE']], '%Y-%m-%d')
                try:
                    high = int(row[col_nums['TMAX']])
                    low = int(row[col_nums['TMIN']])
                except ValueError:
                    print(f"Missing data for {date}")
                else:
                    highs.append(high)
                    lows.append(low)
                    dates.append(date)

    except FileNotFoundError:
        print(f"your file {filename} cannot be found.")
        continue

    # Plot the max and min temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
    ax.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    plt.title("Daily high and low temperatures - 2018\nSitka, AK", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()