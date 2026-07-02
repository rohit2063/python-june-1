import requests
from day19 import send_message_to_viber
url = "https://api.msn.com/weatherfalcon/weather/current?apikey=j5i4gDqHL6nGYwx5wi5kRhXjtf2c5qgFX9fzfk0TOo&activityId=6a3f924d-ee86-46ac-ab11-42e8a6497597&ocid=msftweather&cm=en-us&it=web&user=m-06A85E6A634A64AC035C491F620E6552&scn=ANON&latLongList=27.712102378458727%2C85.31295776367188%7C27.416728703489333%2C85.03332138061523%7C28.180375627281535%2C85.33870697021484%7C28.15510328142808%2C85.98226547241212%7C27.27492399849851%2C84.47490692138673%7C27.110173039671658%2C84.462890625%7C28.852642640228687%2C85.29733657836915%7C27.313823989274546%2C86.50051116943361%7C28.212298017096376%2C83.9872169494629%7C27.94103350326715%2C86.8246078491211%7C28.642389157900524%2C84.10188674926759%7C29.3286113604602%2C85.23313522338869%7C27.70799908345649%2C83.4569549560547%7C27.145464565009377%2C83.52939605712892%7C28.65895989119463%2C87.12604522705078&locale=en-us&units=F&appId=9e21380c-ff19-4c78-b4ea-19558e93a5d3&wrapOData=false&includenowcasting=true&usemscloudcover=true"

r = requests.get(url=url)
print(r)
if r.status_code==200:
     # print(r.json())
     data = r.json()
     print(type(data))
     print(data.keys())
     result = data['responses']
     print(type(result))
     final_data = result
     # print(final_data)
     for i in final_data:
        data = (f"The temperature of {i['source']['location']['Name']} is {i['weather'][0]['current']['temp']}.")
        send_message_to_viber(data)
