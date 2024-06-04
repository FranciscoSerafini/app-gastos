import requests
from fastapi import HTTPException
from requests.exceptions import RequestException

def get_dollar_blue_value():
    try:
        response = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarblue')
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
        data = response.json()
        return data['venta']
    except RequestException as e:
        raise HTTPException(status_code=503, detail="Error fetching dollar blue value")

