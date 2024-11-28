# utils/data.py
import datetime

def formatar_data(data):
    return data.strftime("%d/%m/%Y")

def obter_data_atual():
    return datetime.date.today()