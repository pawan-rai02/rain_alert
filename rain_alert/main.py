import requests
from twilio.rest import Client

api_key = "120be7b702b28b24a33bf9466ac7a030"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "ACff222434bf8de6ad846b2377da941ba2"
auth_token = "f3d1255da657583ded0bb811028ff685"

weather_params = {
    "lat": 28.6094802,
    "lon": 77.3576435,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body='its going to rain today, Remember to bring an umbrella ☔',
        from_="+13123865915",
        to="+918528978449"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body='Its a clear day, no need for an umbrella ☔',
        from_="+13123865915",
        to="+918528978449"
    )
    print(message.status)

