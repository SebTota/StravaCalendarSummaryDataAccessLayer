import datetime

class CalendarSummaryEvent:
    def __init__(self, calendar_event_id: str, start_datetime: datetime.datetime, end_datetime: datetime.datetime):
        """
        A DB model to store the calendar event id of a calendar summary event
        :param calendar_event_id: the event id
        :param start_datetime: summary event start datetime
        :param end_datetime: summary event end datetime
        """
        self.calendar_event_id: str = calendar_event_id
        self.start_datetime: datetime.datetime = start_datetime
        self.end_datetime: datetime.datetime = end_datetime

    @staticmethod
    def from_dict(source):
        return CalendarSummaryEvent(**source)

    def to_dict(self):
        return self.__dict__
