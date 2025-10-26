from pathlib import Path
import json

# Lê os dados como uma string e os converte em um objeto Python
path = Path('eq_data/data/eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examina todos os terremotos no conjunto de dados
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
