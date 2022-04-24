from enum import Enum

class StravaEventUpdateType(Enum):
    TITLE = 'title'  # title of the activity
    TYPE = 'type'  # type of activity
    PRIVATE = 'private'  # visibility of activity
    AUTHORIZED = 'authorized'  # OPTIONAL - will show {'authorized': 'false'} on de-authorization event
