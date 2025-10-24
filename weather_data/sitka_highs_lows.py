import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extrai as temperaturas máximas e mínimas
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], r'%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plota as temperaturas máximas e mínimas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')

# Formata o gráfico
ax.set_title('Temperaturas Máxima e Mínima Diária, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatura (Fº)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
