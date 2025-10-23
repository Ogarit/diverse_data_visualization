import plotly.express as px
from die import Die

# Cria três D6
die1 = Die()
die2 = Die()
die3 = Die()

# Realiza alguns testes e armazena os resultados em uma lista
results = [die1.roll()+die2.roll()+die3.roll() for _ in range(1_000_000)]

# Analisa os resultados
max_results = die1.num_sides + die2.num_sides + die3.num_sides
poss_results = range(1, max_results+1)
frequencies = [results.count(value) for value in poss_results]

# Visualiza os resultados
title = "Resultados da Rolagem de três D6 1.000.000 de Vezes"
labels = {'x': 'Resultado', 'y': 'Frequência do Resultado'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Personaliza ainda mais o gráfico
fig.update_layout(xaxis_dtick=1)

fig.show()
