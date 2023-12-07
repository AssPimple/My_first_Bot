from coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import ApiServiceError, CantGet


def main():
    try:
        coordinates = get_coordinates()
    except CantGet:
        print('Не удалось получить координаты')
        exit(1)
    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print(f'Не удалось получить погоду {coordinates}')
        exit(1)
    print(format_weather(weather))


if __name__ == "__main__":
    main()
