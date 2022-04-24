class StravaEvent():
    def __init__(self, object_type: str, object_id: str, aspect_type: str, updates: dict, owner_id: int, event_time: str):
        self.object_type = object_type  # 'activity' or 'athlete'
        self.object_id = object_id  # the activity id in Strava
        self.aspect_type = aspect_type
        self.updates = updates
        self.owner_id = owner_id
        self.event_time = event_time

    @staticmethod
    def from_dict(source):
        return StravaEvent(**source)

    def to_dict(self):
        return self.__dict__
