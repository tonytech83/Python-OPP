from project.month_mapper import months_mapper


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, month, year = [int(x) for x in date.split('.')]
        month_name = months_mapper[month]

        return cls(name, id, year, month_name, age_restriction)

    def __return_status(self):
        return 'rented' if self.is_rented else 'not rented'

    def __repr__(self):
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year})' \
               f' has age restriction {self.age_restriction}. Status: {self.__return_status()}'
