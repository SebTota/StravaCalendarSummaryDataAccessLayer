from .strava_event_type import StravaEventType

class StravaEvent():
    def __init__(self, object_type: str, id: int, event_type: StravaEventType, updates: dict, athlete_id: int, event_time: int):
        self.object_type = object_type  # 'activity' or 'athlete'
        self.id = id  # the activity id in Strava
        self.event_type = event_type
        self.updates = updates
        self.athlete_id = athlete_id
        self.event_time = event_time

    @staticmethod
    def from_dict(source):
        return StravaEvent(**source)

    def to_dict(self):
        return self.__dict__
