from datetime import datetime
from pathlib import Path
import csv
import matplotlib.pyplot as plt

# Preparando o arquivo csv
path = Path('weather_data/data/san_francisco_2021_full.csv')
lines = path.read_text().splitlines()
san_francisco = csv.DictReader(lines)

# Extrai as temperatura máxima e mínima
dates, tmax_list, tmin_list = [], [], []
for row in san_francisco:
    current_date = datetime.strptime(row['DATE'], r'%Y-%m-%d')
    tmax = int(row['TMAX'])
    tmin = int(row['TMIN'])
    dates.append(current_date)
    tmax_list.append(tmax)
    tmin_list.append(tmin)

# Gerando a figura do gráfico
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# Plotando o gráfico de linhas com a temperatura máxima e mínima
ax.plot(dates, tmax_list, color='red', alpha=0.5)
ax.plot(dates, tmin_list, color='blue', alpha=0.5)
ax.fill_between(dates, tmax_list, tmin_list, facecolor='blue', alpha=0.1)

# Estilizando o gráfico
title = 'Temperaturas máximas e mínimas, San Francisco, CA, 2021'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (Fº)')
ax.set_ylim(10, 140)
ax.tick_params(labelsize=16)

fig.autofmt_xdate()

plt.show()
