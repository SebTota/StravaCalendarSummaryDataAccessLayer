from enum import Enum


class EndOfWeekType(Enum):
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    @classmethod
    def from_str(cls, label):
        if label == 'Saturday':
            return cls.SATURDAY
        elif label == 'Sunday':
            return cls.SUNDAY
        else:
            raise NotImplementedError

    def get_weekday_num_val(self):
        if self.name == EndOfWeekType.SATURDAY.name:
            return 5
        elif self.name == EndOfWeekType.SUNDAY.name:
            return 6
