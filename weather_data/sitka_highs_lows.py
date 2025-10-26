from datetime import datetime
from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
sitka = csv.DictReader(lines)

# Extrai as temperaturas máximas e mínimas
dates, tmax_list, tmin_list = [], [], []
for row in sitka:
    current_date = datetime.strptime(row['DATE'], r'%Y-%m-%d')
    try:
        tmax = int(row['TMAX'])
        tmin = int(row['TMIN'])
    except ValueError:
        print(f'Dados ausentes para o {current_date}')
    else:
        dates.append(current_date)
        tmax_list.append(tmax)
        tmin_list.append(tmin)

# Plota as temperaturas máximas e mínimas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, tmax_list, color='red', alpha=0.5)
ax.plot(dates, tmin_list, color='blue', alpha=0.5)
ax.fill_between(dates, tmax_list, tmin_list, facecolor='blue', alpha=0.1)

# Formata o gráfico
ax.set_title('Temperaturas Máxima e Mínima Diária, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (Fº)', fontsize=16)
ax.set_ylim(10, 140)
ax.tick_params(labelsize=16)

fig.autofmt_xdate()

plt.show()
