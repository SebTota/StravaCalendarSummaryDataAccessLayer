class CalendarEvent:
    def __init__(self, strava_event_id: str, calendar_event_id: str, calendar_template: str):
        self.strava_event_id = strava_event_id
        self.calendar_event_id = calendar_event_id
        self.calendar_template = calendar_template

    @staticmethod
    def from_dict(source):
        return CalendarEvent(**source)

    def to_dict(self):
        return self.__dict__
