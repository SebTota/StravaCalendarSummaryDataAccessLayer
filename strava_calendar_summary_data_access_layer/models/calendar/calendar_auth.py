class CalendarAuth():
    def __init__(self, access_token, id_token, expiry_date, scope, token_type):
        self.access_token = access_token
        self.id_token = id_token
        self.expiry_date = int(expiry_date)
        self.scope = scope
        self.token_type = token_type

    @staticmethod
    def from_dict(source):
        return CalendarAuth(**source)

    def to_dict(self):
        return self.__dict__
