from .strava import StravaCredentials
from .calendar import CalendarPreferences, CalendarSummaryEvent

from google.oauth2.credentials import Credentials
import json


class User:
    def __init__(self, user_id: str, first_name: str, last_name: str,
                 strava_credentials: StravaCredentials = None,
                 calendar_credentials: Credentials = None,
                 calendar_id: str = None,
                 calendar_preferences: CalendarPreferences = CalendarPreferences(),
                 daily_summary_calendar_event: CalendarSummaryEvent = None,
                 weekly_summary_calendar_event: CalendarSummaryEvent = None):
        self.user_id: str = user_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.strava_credentials: StravaCredentials = strava_credentials
        self.calendar_credentials: Credentials = calendar_credentials
        self.calendar_id: str = calendar_id  # The id of the calendar belonging to the app if one is already created
        self.calendar_preferences: CalendarPreferences = calendar_preferences
        self.daily_summary_calendar_event = daily_summary_calendar_event
        self.weekly_summary_calendar_event = weekly_summary_calendar_event

    @staticmethod
    def from_dict(source):
        user_id = source['user_id']
        first_name = source['first_name']
        last_name = source['last_name']

        strava_credentials = StravaCredentials.from_dict(source['strava_credentials']) \
            if 'strava_credentials' in source else None

        calendar_credentials = Credentials.from_authorized_user_info(
            source['calendar_credentials']) if 'calendar_credentials' in source else None

        calendar_id = source['calendar_id'] if 'calendar_id' in source else None

        calendar_preferences = CalendarPreferences.from_dict(source['calendar_preferences']) \
            if 'calendar_preferences' in source else CalendarPreferences()

        daily_summary_calendar_event = CalendarSummaryEvent.from_dict(source['daily_summary_calendar_event']) \
            if 'daily_summary_calendar_event' in source else None

        weekly_summary_calendar_event = CalendarSummaryEvent.from_dict(source['weekly_summary_calendar_event']) \
            if 'weekly_summary_calendar_event' in source else None

        return User(user_id, first_name, last_name, strava_credentials,
                    calendar_credentials, calendar_id, calendar_preferences, daily_summary_calendar_event,
                    weekly_summary_calendar_event)

    def to_dict(self):
        d = {'user_id': self.user_id, 'first_name': self.first_name, 'last_name': self.last_name}
        if self.strava_credentials:
            d['strava_credentials'] = self.strava_credentials.to_dict()
        if self.calendar_credentials:
            d['calendar_credentials'] = json.loads(self.calendar_credentials.to_json())
        if self.calendar_id:
            d['calendar_id'] = self.calendar_id
        if self.calendar_preferences:
            d['calendar_preferences'] = self.calendar_preferences.to_dict()
        if self.daily_summary_calendar_event:
            d['daily_summary_calendar_event'] = self.daily_summary_calendar_event.to_dict()
        if self.weekly_summary_calendar_event:
            d['weekly_summary_calendar_event'] = self.weekly_summary_calendar_event.to_dict()
        return d
