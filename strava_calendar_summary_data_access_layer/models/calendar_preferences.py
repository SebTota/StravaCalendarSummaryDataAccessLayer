class CalendarPreferences:
    def __init__(self, title_template: str, description_template: str, end_of_week: str):
        self.title_template = title_template
        self.end_of_week = end_of_week

    @staticmethod
    def from_dict(source: dict):
        return CalendarPreferences(**source)

    def to_dict(self):
        return self.__dict__