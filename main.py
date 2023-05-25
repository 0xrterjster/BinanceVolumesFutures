import requests
import time

prev_volumes = {}


def get_data_and_send_message():
    global prev_volumes
    time_url = 'https://api.binance.com/api/v3/ticker/24hr'
    time_response = requests.get(time_url)
    time_data = time_response.json()
    for elem in time_data:
        symbol = elem['symbol']
        volume = float(elem['volume'])
        if symbol in prev_volumes:
            prev_volume = prev_volumes[symbol]
            if volume > prev_volume:
                diff = volume - prev_volume
                volume_change = (volume - prev_volume) / prev_volume * 100
                if volume_change >= 0.25 and volume_change < 5:
                    message = f"❗{symbol} vol up {volume_change:.2f}% \nDiff: {diff:.2f} $"
                    print(message)
                elif volume_change >= 5 and volume_change < 8:
                    message = f"‼️{symbol} vol up {volume_change:.2f}% \nDiff: {diff:.2f} $"
                    print(message)
                elif volume_change >= 8:
                    message = f"🛑🛑{symbol} vol up {volume_change:.2f}% \nDiff: {diff:.2f} $"
                    print(message)
        prev_volumes[symbol] = volume


while True:
    get_data_and_send_message()
    time.sleep(15)