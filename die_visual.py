import plotly.express as px
from die import Die

# Cria um D6
die = Die()

# Realiza alguns testes e armazena os resultados em uma lista
results = []
for roll_num in range(1_000):
    result = die.roll()
    results.append(result)

# Analisa os resultados
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados~
title = "Resultados da Rolagem de um D6 1.000 vezes"
labels = {'x': 'Resultado', 'y': 'Frequência do Resultado'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
