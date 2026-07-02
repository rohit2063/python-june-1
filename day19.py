import requests
import json
token ="56c069fd467285a7-62b4b07391e94a04-a1ffe9e46170aa4a"
user_id ="ftFhfafVqi2UyoOEBm/6zA=="
viber_url = "https://chatapi.viber.com/pa/post"

payload = {
    "auth_token":token, 
    "from":user_id, 
    "type":"text", 
    "text":"Hello world!" 
}

def send_message_to_viber(message):
    payload["text"] = message
    r = requests.post(url=viber_url, data=json.dumps(payload))
    print(r)

# send_message_to_viber()


def get_stock_index():
 url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

 r = requests.get(url=url)
 if r.status_code==200:
    data = r.json()
    print(type(data))
    print(data.keys())
    result = data['response']
    print(type(result))
    positive = []
    negative = []
    for item in result:
        if item['points_change']<0:
            send_message_to_viber(f'{item['indices']}-ve')
            negative.append(item['indices'])
        else:
            send_message_to_viber(f'{item['indices']}')
            positive.append(item['indices'])

        print("positive--->",len(positive))
        print("Negative--->",len(negative))