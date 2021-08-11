import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get dates, and max and min temperatures
    highs, lows, dates = [], [], []
    for row in reader:
        highs.append(int(row[5]))
        lows.append(int(row[6]))
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

# Plot the max and min temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=1, alpha=0.5)
ax.plot(dates, lows, c='blue', linewidth=1, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2018\nSitka, AK", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
