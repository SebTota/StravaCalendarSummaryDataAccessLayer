from .end_of_week_type import EndOfWeekType


class CalendarPreferences:
    def __init__(self, title_template: str, description_template: str, end_of_week: EndOfWeekType):
        self.title_template: str = title_template
        self.description_template: str = description_template
        self.end_of_week: EndOfWeekType = end_of_week

    @staticmethod
    def from_dict(source: dict):
        title_template = source['title_template']
        description_template = source['description_template']
        end_of_week = EndOfWeekType.from_str(source['end_of_week'])
        return CalendarPreferences(title_template, description_template, end_of_week)

    def to_dict(self):
        d = {'title_template': self.title_template,
             'description_template': self.description_template,
             'end_of_week': self.end_of_week.value}
        return d
