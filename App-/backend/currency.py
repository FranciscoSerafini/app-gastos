import requests
from fastapi import HTTPException

def get_dollar_blue_value():
    try:
        response = requests.get('https://api-dolar-argentina.herokuapp.com/api/dolarblue')
        data = response.json()
        return data['venta']
    except Exception as e:
        raise HTTPException(status_code=503, detail="Error fetching dollar blue value")
