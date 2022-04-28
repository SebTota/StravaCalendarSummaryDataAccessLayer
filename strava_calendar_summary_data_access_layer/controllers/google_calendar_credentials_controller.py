from .base_controller import BaseController
from google.oauth2.credentials import Credentials

import json

COLLECTION_NAME = u'GoogleCalendarCredentials'


class GoogleCalendarCredentialsController(BaseController):
    def _get_table(self, db_conn):
        return db_conn.collection(COLLECTION_NAME)

    def _from_dict(self, obj) -> Credentials:
        return Credentials.from_authorized_user_info(obj.to_dict())

    def _to_dict(self, obj: Credentials) -> dict:
        return json.loads(obj.to_json())
