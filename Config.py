USE_ROUNDED_COORDS = True
OPENWEATHER_API = 'b7a373f28cc135946df37a744fb88f17'
OPENWEATHER_URL_TEMPLATE = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + OPENWEATHER_API + '&lan=ru&'
        'units=metric'
)
