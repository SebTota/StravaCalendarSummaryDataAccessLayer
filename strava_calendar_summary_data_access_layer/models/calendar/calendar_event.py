class CalendarEvent:
    def __init__(self, strava_event_id: str, calendar_event_id: str, title_template: str, description_template: str):
        self.strava_event_id = strava_event_id
        self.calendar_event_id = calendar_event_id
        self.title_template = title_template
        self.description_template = description_template

    @staticmethod
    def from_dict(source):
        return CalendarEvent(**source)

    def to_dict(self):
        return self.__dict__
