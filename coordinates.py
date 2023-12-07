from typing import NamedTuple

from geopy.geocoders import Nominatim


class Coordinates(NamedTuple):
    longitude: float
    latitude: float


def get_coordinates() -> Coordinates:
    # Создаем объект geopy для использования сервиса геокодирования Nominatim
    geolocator = Nominatim(user_agent="my_geocoder")

    # Получаем местоположение пользователя (можно использовать любой адрес)
    location_input = input('Введите ваше место в формате(Город, улица): ')
    location = geolocator.geocode(location_input)

    if location:
        # Выводим полученные координаты
        return Coordinates(location.longitude, location.latitude)
    else:
        print("Не удалось получить координаты")



