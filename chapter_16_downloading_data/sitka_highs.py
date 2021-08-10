import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Get dates and max temperatures
    highs, dates = [], []
    for row in reader:
        highs.append(int(row[5]))
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

# Plot the max temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=1)

# Format plot
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
