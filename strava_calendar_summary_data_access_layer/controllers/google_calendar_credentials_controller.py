from .base_controller import BaseController
from ..models import GoogleCalendarCredentials

COLLECTION_NAME = u'GoogleCalendarCredentials'


class GoogleCalendarCredentialsController(BaseController):
    def _get_table(self, db_conn):
        return db_conn.collection(COLLECTION_NAME)

    def _from_dict(self, obj) -> GoogleCalendarCredentials:
        return GoogleCalendarCredentials.from_dict(obj.to_dict())

    def _to_dict(self, obj: GoogleCalendarCredentials) -> dict:
        return obj.to_dict()
