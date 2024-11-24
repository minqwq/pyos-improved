import requests
import datetime

Api_key = '2154faddb71353e0e8e2b62421209689' # Please lessly use this program, this key is only 1000 requests/day max
base_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city/state name: ')

request_url = f"{base_url}?appid={Api_key}&q={city}"
response = requests.get(request_url)

if response.status_code==200:
    data = response.json()
    weather = data['weather'][0]['description']
    country = data["sys"]['country']
    humidity = data["main"]['humidity']
    unix_sunrise_pre = data["sys"]["sunrise"]
    unix_sunset_pre = data["sys"]["sunset"]
    unix_sunrise_rc = datetime.datetime.fromtimestamp(unix_sunrise_pre)
    unix_sunset_rc = datetime.datetime.fromtimestamp(unix_sunset_pre)
    unix_sunrise = unix_sunrise_rc.strftime("%b %a %d %H:%M:%S %Y")
    unix_sunset = unix_sunset_rc.strftime("%b %a %d %H:%M:%S %Y")
    temperature = round(data['main']['temp']- 273.15,2 ) # for celsius
    print('Weather:', weather)
    print('Temperature:', temperature)
    print("Humidity:" + str(humidity))
    print("Sunrise:" + unix_sunrise)
    print("Sunset:" + unix_sunrise)
    if country == "CN":
        print("\033[41m", end="")
    print("\nCountry:" + country)
else:
    print("An error occured... ")

                                    
