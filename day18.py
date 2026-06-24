import requests
url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/teams?_limit=60"

r = requests.get(url=url)
if r.status_code==200:
    print(r.json())

    