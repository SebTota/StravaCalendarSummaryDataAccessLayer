from abc import ABC, abstractmethod
from google.cloud import firestore


class BaseController(ABC):
    def __init__(self):
        self.db_conn = firestore.Client()

    def get_by_id(self, id: str):
        table = self._get_table(self.db_conn)
        doc_ref = table.document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return self._from_dict(doc)
        else:
            return None

    def insert(self, id: str, obj: object):
        table = self._get_table(self.db_conn)
        doc_ref = table.document(str(id))
        doc_ref.set(self._to_dict(obj))

    def update(self, id: str, obj: object):
        table = self._get_table(self.db_conn)
        doc_ref = table.document(str(id))
        doc_ref.update(self._to_dict(obj))

    def delete(self, id):
        table = self._get_table(self.db_conn)
        doc_ref = table.document(str(id))
        doc_ref.delete()

    @abstractmethod
    def _from_dict(self, obj):
        pass

    @abstractmethod
    def _to_dict(self, obj):
        pass

    @abstractmethod
    def _get_table(self, db_conn):
        pass