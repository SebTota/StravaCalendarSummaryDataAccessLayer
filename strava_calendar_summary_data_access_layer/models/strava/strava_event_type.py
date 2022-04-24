from enum import Enum

class StravaEventType(Enum):
    CREATE = 'create'
    UPDATE = 'update'
    DELETE = 'delete'
