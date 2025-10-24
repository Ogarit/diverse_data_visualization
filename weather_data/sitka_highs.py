from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extrai as temperaturas máximas
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

# Plota as temperaturas máximas
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Formata o gráfico
ax.set_title('Temperaturas Máxima Diária, Julho de 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperatura (Fº)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
