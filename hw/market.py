from log_time_decorator import log_time


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.market_wines_map = {wine.title: wine for wine in wines}
        self.market_beers_map = {beer.title: beer for beer in beers}

    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.market_wines_map or title in self.market_beers_map

    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        return sorted(filter(lambda x: x.title is not None, list(self.market_wines_map.values()) + list(self.market_beers_map.values())), key=lambda x: x.title)

    @log_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        products = [x for x in (list(self.market_wines_map.values()) + list(self.market_beers_map.values()))]
        if from_date is not None:
            products = list(filter(lambda x: x.production_date is not None and x.production_date >= from_date, products))
        if to_date is not None:
            products = list(filter(lambda x: x.production_date is not None and x.production_date <= to_date, products))
        return products
