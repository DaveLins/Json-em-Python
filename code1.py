import json

carros_json = '{"marca": "honda", "modelo": "HRV","cor": "prata"}'

carros = json.loads(carros_json)

for a, b in carros.items():
    
    print(a, b)