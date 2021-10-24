import requests
import json

endPoint = 'https://data.covid19.go.id/public/api/update.json'


def dataCovid():
    response = requests.get(endPoint)
    data = json.loads(response.text)
    return str(data)


print(dataCovid())
