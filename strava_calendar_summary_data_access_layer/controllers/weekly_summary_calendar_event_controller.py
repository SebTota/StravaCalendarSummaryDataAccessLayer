from ..models import CalendarSummaryEvent
from .base_controller import BaseController

USER_COLLECTION_NAME = u'Users'
DAILY_SUMMARY_CALENDAR_EVENTS_COLLECTION_NAME = u'WeeklySummaryCalendarEvents'


class WeeklySummaryCalendarEventsController(BaseController):
    def __init__(self, user_id: str):
        super().__init__()
        self._strava_events_controller_user_id = user_id

    def _get_table(self, db_conn):
        return db_conn.collection(USER_COLLECTION_NAME).document(self._strava_events_controller_user_id)\
            .collection(DAILY_SUMMARY_CALENDAR_EVENTS_COLLECTION_NAME)

    def _from_dict(self, obj):
        return CalendarSummaryEvent.from_dict(obj.to_dict())

    def _to_dict(self, obj: CalendarSummaryEvent):
        return obj.to_dict()
