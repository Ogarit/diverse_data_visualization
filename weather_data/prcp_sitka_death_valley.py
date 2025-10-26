from datetime import datetime
from pathlib import Path
import csv
import matplotlib.pyplot as plt


def csv_reader(file):
    """Retorna o arquivo csv como uma lista pronta para ser trabalhada."""
    path = Path(file)
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)

    return reader


def data_prep(data, i_date, i_prcp):
    dates, prcp_list = [], []
    for row in data:
        current_date = datetime.strptime(row[i_date], r'%Y-%m-%d')
        try:
            prcp = float(row[i_prcp])
        except ValueError:
            print(f'Dados ausentes para {current_date}')
        else:
            dates.append(current_date)
            prcp_list.append(prcp)

    return dates, prcp_list


sitka = csv_reader('weather_data/data/sitka_weather_2021_full.csv')
next(sitka)
death_valley = csv_reader('weather_data/data/death_valley_2021_full.csv')
next(death_valley)

# Extrai as temperaturas máximas e mínimas
dates_sitka, prcp_sitka = data_prep(sitka, 2, 5)
dates_death_valley, prcp_death_valley = data_prep(death_valley, 2, 3)

# Plota as temperaturas máximas e mínimas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates_sitka, prcp_sitka, color='blue')
ax.bar(dates_death_valley, prcp_death_valley, color='red')

# Formata o gráfico
title = 'Precipitação Sitka x Death Valley'
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Índice Pluviométrico', fontsize=16)
ax.tick_params(labelsize=16)
ax.legend(['Sitka', 'Death Valley'])

fig.autofmt_xdate()
fig.tight_layout()

plt.show()
