import schedule
import requests


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '2064755452',
        'message': 'Good Morning!',
        'key': 'textbelt',
    })
    print(resp.json())