from datetime import datetime

from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
red_and_white = Market(
    wines=[
        Wine("AbrauDurso", datetime(2024, 1, 1)),
        Wine("Sovetskoe", datetime(2024, 1, 3)),
    ],
    beers=[
        Beer("ZHIGULEVSKOE", datetime(2024, 1, 2)),
        Beer("OHOTA KREPKOE", datetime(2024, 1, 4)),
    ]
)

print(red_and_white.has_drink_with_title('AbrauDurso'))
print(red_and_white.has_drink_with_title('AbrauDursoASF'))
print(red_and_white.get_drinks_sorted_by_title())
print(red_and_white.get_drinks_by_production_date(from_date=datetime(2024, 1, 2), to_date=datetime(2024, 1, 4)))
