# Importar la librería JSON
import json
import requests

# Definir la URL de la API
url = 'https://rodrik.mx/api/listado_deptos_desarrollo.php?id=6'

# Hacer una solicitud HTTP a la API
response = requests.get(url)

# Convertir la respuesta a un objeto JSON
data = json.loads(response.text)

# Imprimir los datos
# print(data)

for i in range(len(data)):
    #Cambiar if i == i:
    if data[i]['id'] == 29:
        print(f"{i} - {data[i]['id']}")
        print(data[i]['depto'])
        print(data[i]['tipo'])
        print(f"{data[i]['suptotal']} m2")
        print(f"{data[i]['valortotal']} MXN")
        print(f"{data[i]['HIPOTECARIO']} MXN")
        print(f"{data[i]['FINANCIERO 1']} MXN")
        print(f"{data[i]['FINANCIERO 2']} MXN")
        print(f"{data[i]['CONTADO']} MXN")
        print(f"ESTATUS: {data[i]['estatus']}\n")