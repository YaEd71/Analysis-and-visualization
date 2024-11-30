import yfinance as yf
import numpy as np


def fetch_stock_data(ticker, period='1mo'):
    """Получает данные об акциях для указанного тикера из Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        return data
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")
        return None


def add_moving_average(data, window_size=5):
    """Добавляет скользящее среднее к данным"""
    if data is None:
        return None
    try:
        data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
        return data
    except Exception as e:
        print(f"Ошибка при расчете скользящего среднего: {e}")
        return data


def calculate_average_price(data):
    """Вычисляет и выводит среднюю цену закрытия за период"""
    if data is None:
        print("Нет данных для расчета средней цены.")
        return None

    try:
        average_price = np.mean(data['Close'])
        print(f"Средняя цена закрытия за период: ${average_price:.2f}")
        return average_price
    except Exception as e:
        print(f"Ошибка при расчете средней цены: {e}")
        return None
