from google.oauth2.credentials import Credentials
import json


class GoogleCalendarCredentials:
    def __init__(self, user_id: str, credentials: Credentials):
        self.user_id = user_id
        self.credentials: Credentials = credentials

    @staticmethod
    def from_dict(source):
        return GoogleCalendarCredentials(source['user_id'], Credentials.from_authorized_user_info(source['credentials']))

    def to_dict(self):
        return {'user_id': self.user_id, 'credentials': json.loads(self.credentials.to_json())}
