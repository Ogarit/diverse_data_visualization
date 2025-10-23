import plotly.express as px
from die import Die

# Cria um D6
die = Die()

# Realiza alguns testes e armazena os resultados em uma lista
results = [die.roll() for _ in range(1_000)]

# Analisa os resultados
poss_results = range(1, die.num_sides+1)
frequencies = [results.count(value) for value in poss_results]

# Visualiza os resultados
title = "Resultados da Rolagem de um D6 1.000 Vezes"
labels = {'x': 'Resultado', 'y': 'Frequência do Resultado'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()
