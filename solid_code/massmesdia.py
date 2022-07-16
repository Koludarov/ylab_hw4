from abc import ABC, abstractmethod


class Media(ABC):
    @staticmethod
    @abstractmethod
    def create_news(place, name):
        pass


class TV(Media):
    def __init__(self):
        self.name = 'Fox news'

    @staticmethod
    def create_news(place, name):
        place_name = getattr(place, 'name', 'place')
        print(f'{name} saved the {place_name}!')

    def planets(self, planet):
        planet_coordinates = getattr(planet, 'coordinates', 'place')
        print(f'{self.name} notifies {planet_coordinates}')


class Newspaper(Media):
    def __init__(self):
        self.name = 'Times'

    @staticmethod
    def create_news(place, name):
        place_name = getattr(place, 'name', 'place')
        print(f'On the cover of our newspaper today:')
        print(f'{name} rescues the {place_name}!'.upper())
