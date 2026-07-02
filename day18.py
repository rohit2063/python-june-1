import requests
url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/teams?_limit=60"

r = requests.get(url=url)
if r.status_code==200:
    response = r.json()
    print(type(response))
    print(response.keys())
    result = response['data']
    print(type(result))
    final_data = result
    print(final_data)
    for i in final_data:
         print(i['name'], i['abbr'],)

# url = "https://markets.onlinekhabar.com/smtm/stock_live/sector-performance"

# r = requests.get(url=url)
# if r.status_code==200:
#     data = r.json()
#     print(type(data))
#     print(data.keys())
#     result = data['response']
#     print(type(result))
#     positive = []
#     negative = []
#     for item in result:
#         if item['points_change']<0:
#             negative.append(item['indices'])
#         else:
#             positive.append(item['indices'])

#         print("positive--->",len(positive))
#         print("Negative--->",len(negative))