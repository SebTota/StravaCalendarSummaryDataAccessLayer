from ..models import StravaCredentials
from .base_controller import BaseController

COLLECTION_NAME = u'StravaCredentials'


class StravaCredentialsController(BaseController):
    def _get_table(self, db_conn):
        return db_conn.collection(COLLECTION_NAME)

    def _from_dict(self, obj):
        return StravaCredentials.from_dict(obj.to_dict())

    def _to_dict(self, obj: StravaCredentials):
        return obj.to_dict()
