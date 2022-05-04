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

