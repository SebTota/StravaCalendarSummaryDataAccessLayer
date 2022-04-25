from .strava import StravaAuth
from oauth2client import client


class User:
    def __init__(self, id: str, strava_auth: StravaAuth, calendar_auth: client):
        self.id = id
        self.strava_auth = strava_auth
        self.calendar_auth = calendar_auth

    @staticmethod
    def from_dict(source):
        strava_auth = StravaAuth.from_dict(source['strava_auth']) if 'strava_auth' in source else None
        calendar_auth = client.from_json(source['calendar_auth']) if 'calendar_auth' in source else None
        return User(source['id'], strava_auth, calendar_auth)

    def to_dict(self):
        d = {}
        d['id'] = self.id
        d['strava_auth'] = self.strava_auth.to_dict() if self.strava_auth is not None else None
        d['calendar_auth'] = self.calendar_auth.to_json() if self.calendar_auth is not None else None
        return d
