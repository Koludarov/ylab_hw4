from typing import Union
from heroes import Superman, SuperHero, ShootingHero
from massmesdia import TV, Newspaper
from places import Kostroma, Tokyo, Earth, Jupiter


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    Newspaper.create_news(place, hero.name)
    TV().planets(Earth)
    TV().planets(Jupiter)
    TV.create_news(place, hero.name)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(ShootingHero('Chack Norris', False), Tokyo())
