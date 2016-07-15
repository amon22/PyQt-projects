def weather():
    import pyowm

    data = {}

    owm = pyowm.OWM("00d400860e6a288e5682427bfd178b29")

    forecast = owm.daily_forecast("Budapest,hu")
    today_weather = forecast.get_forecast().get(0)
    temp = today_weather.get_temperature("celsius")

    data["status"] = today_weather.get_detailed_status()
    data["icon"] = today_weather.get_weather_icon_name()
    data["temp"] = (temp["min"] + temp["max"]) / 2

    return data

if __name__ == "__main__":
    raw = weather()

    for i in raw.keys():
        print i + " : " + str(raw[i])
