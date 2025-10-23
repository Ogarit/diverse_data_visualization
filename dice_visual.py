import plotly.express as px
from die import Die

# Cria dois dados D6
die1 = Die()
die2 = Die()

# Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(1_000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
max_results = die1.num_sides + die2.num_sides
poss_results = range(1, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
title = "Resultados da Rolagem de dois dados D6 1.000 Vezes"
labels = {'x': 'Resultado', 'y': 'Frequência do Resultado'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
