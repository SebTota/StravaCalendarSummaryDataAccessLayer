from .strava import StravaCredentials
from .calendar import CalendarPreferences

from google.oauth2.credentials import Credentials
import json


class User:
    def __init__(self, user_id: str, strava_credentials: StravaCredentials = None,
                 calendar_credentials: Credentials = None, calendar_id: str = None,
                 calendar_preferences: CalendarPreferences = None):
        self.user_id = user_id
        self.strava_credentials = strava_credentials  # The credentials for authenticating user Strava API Calls
        self.calendar_credentials = calendar_credentials  # The credentials for authenticating user Calendar API Calls
        self.calendar_id = calendar_id  # The id of the calendar belonging to the app if one is already created
        self.calendar_preferences = calendar_preferences

    @staticmethod
    def from_dict(source):
        user_id = source['user_id']
        strava_credentials = StravaCredentials.from_dict(source['strava_credentials']) \
            if 'strava_credentials' in source else None
        calendar_credentials = Credentials.from_authorized_user_info(
            source['calendar_credentials']) if 'calendar_credentials' in source else None
        calendar_id = source['calendar_id'] if 'calendar_id' in source else None
        calendar_preferences = CalendarPreferences.from_dict(source['calendar_preferences']) \
            if 'calendar_preferences' in source else None
        return User(user_id, strava_credentials, calendar_credentials, calendar_id, calendar_preferences)

    def to_dict(self):
        d = {'user_id': self.user_id}
        if self.strava_credentials:
            d['strava_credentials'] = self.strava_credentials.to_dict()
        if self.calendar_credentials:
            d['calendar_credentials'] = json.loads(self.calendar_credentials.to_json())
        if self.calendar_id:
            d['calendar_id'] = self.calendar_id
        if self.calendar_preferences:
            d['calendar_preferences'] = self.calendar_preferences.to_dict()
        return d
