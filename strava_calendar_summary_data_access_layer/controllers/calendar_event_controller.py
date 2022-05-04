from ..models import User
from .base_controller import BaseController

from google.cloud import firestore


USER_COLLECTION_NAME = u'Users'
STRAVA_EVENTS_COLLECTION_NAME = u'CalendarEvents'


class CalendarEventController(BaseController):
    def __init__(self, user_id: str):
        super().__init__()
        self._strava_events_controller_user_id = user_id

    def _get_table(self, db_conn):
        return db_conn.collection(USER_COLLECTION_NAME).document(self._strava_events_controller_user_id)\
            .collection(STRAVA_EVENTS_COLLECTION_NAME)

    def _from_dict(self, obj):
        return User.from_dict(obj.to_dict())

    def _to_dict(self, obj: User):
        return obj.to_dict()
