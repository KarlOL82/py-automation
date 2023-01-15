import schedule
import time

import requests


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '2064755452',
        'message': 'Good Morning!',
        'key': 'textbelt',
    })
    print(resp.json())

schedule.every().day.at('06:15').do(send_message)
# schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)