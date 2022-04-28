class StravaCredentials:
    def __init__(self, access_token: str, refresh_token: str, expiry_date: int):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expiry_date = expiry_date

    @staticmethod
    def from_dict(source):
        return StravaCredentials(**source)

    def to_dict(self):
        return self.__dict__
