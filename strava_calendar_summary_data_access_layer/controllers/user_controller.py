from ..models import User
from .base_controller import BaseController

USER_COLLECTION_NAME = u'Users'

class UserController(BaseController):
    def _get_table(self, db_conn):
        return db_conn.collection(USER_COLLECTION_NAME)

    def _from_dict(self, obj: User):
        return User.from_dict(obj.to_dict())

    def _to_dict(self, obj: User):
        return obj.to_dict()
