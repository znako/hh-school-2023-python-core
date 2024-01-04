from log_time_decorator import log_time


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.market_wines_map, self.market_beers_map = {}, {}
        for i in range(max(len_wines := len(wines if wines is not None else []),
                           len_beers := len(beers if beers is not None else []))):
            if i < len_wines:
                self.market_wines_map[wines[i].title] = wines[i]
            if i < len_beers:
                self.market_beers_map[beers[i].title] = beers[i]

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
        return sorted(list(self.market_wines_map.keys()) + list(self.market_beers_map.keys()))

    @log_time
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        return [x for x in (list(self.market_wines_map.values()) + list(self.market_beers_map.values())) if x.production_date >= from_date and x.production_date <= to_date]
