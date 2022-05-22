from .end_of_week_type import EndOfWeekType

DEFAULT_END_OF_WEEK = EndOfWeekType.SUNDAY


class CalendarPreferences:
    def __init__(self, per_run_summary_enabled: bool, per_run_title_template: str, per_run_summary_template: str,
                 daily_run_summary_enabled: bool, daily_run_title_template: str, daily_run_summary_template: str,
                 weekly_run_summary_enabled: bool, weekly_run_title_template: str, weekly_run_summary_template: str,
                 end_of_week: EndOfWeekType):
        self.per_run_summary_enabled = per_run_summary_enabled
        self.per_run_summary_template = per_run_summary_template
        self.per_run_title_template = per_run_title_template

        self.daily_run_summary_enabled = daily_run_summary_enabled
        self.daily_run_summary_template = daily_run_summary_template
        self.daily_run_title_template = daily_run_title_template

        self.weekly_run_summary_enabled = weekly_run_summary_enabled
        self.weekly_run_summary_template = weekly_run_summary_template
        self.weekly_run_title_template = weekly_run_title_template
        self.end_of_week = end_of_week

    @staticmethod
    def from_dict(source):
        per_run_summary_enabled = source['per_run_summary_enabled'] if 'per_run_summary_enabled' in source else False
        daily_run_summary_enabled = source[
            'daily_run_summary_enabled'] if 'daily_run_summary_enabled' in source else False
        weekly_run_summary_enabled = source[
            'weekly_run_summary_enabled'] if 'weekly_run_summary_enabled' in source else False

        per_run_summary_template = source['per_run_summary_template'] if 'per_run_summary_template' in source else None
        daily_run_summary_template = source[
            'daily_run_summary_template'] if 'daily_run_summary_template' in source else None
        weekly_run_summary_template = source[
            'weekly_run_summary_template'] if 'weekly_run_summary_template' in source else None

        per_run_title_template = source['per_run_title_template'] if 'per_run_title_template' in source else None
        daily_run_title_template = source['daily_run_title_template'] if 'daily_run_title_template' in source else None
        weekly_run_title_template = source[
            'weekly_run_title_template'] if 'weekly_run_title_template' in source else None

        end_of_week = EndOfWeekType.from_str(source['end_of_week']) if 'end_of_week' in source else DEFAULT_END_OF_WEEK

        return CalendarPreferences(per_run_summary_enabled, per_run_title_template, per_run_summary_template,
                                   daily_run_summary_enabled, daily_run_title_template,
                                   daily_run_summary_template,
                                   weekly_run_summary_enabled, weekly_run_title_template,
                                   weekly_run_summary_template, end_of_week)

    def to_dict(self):
        d = {
            'per_run_summary_enabled': self.per_run_summary_enabled if 'per_run_summary_enabled' is not None else False,
            'daily_run_summary_enabled': self.daily_run_summary_enabled if 'daily_run_summary_enabled' is not None else False,
            'weekly_run_summary_enabled': self.weekly_run_summary_enabled if 'weekly_run_summary_enabled' is not None else False}

        if 'per_run_summary_template' is not None:
            d['per_run_summary_template'] = self.per_run_summary_template
        if 'daily_run_summary_template' is not None:
            d['daily_run_summary_template'] = self.daily_run_summary_template
        if 'weekly_run_summary_template' is not None:
            d['weekly_run_summary_template'] = self.weekly_run_summary_template

        if 'per_run_title_template' is not None:
            d['per_run_title_template'] = self.per_run_title_template
        if 'daily_run_title_template' is not None:
            d['daily_run_title_template'] = self.daily_run_title_template
        if 'weekly_run_title_template' is not None:
            d['weekly_run_title_template'] = self.weekly_run_title_template

        d['end_of_week'] = self.end_of_week.value if self.end_of_week is not None else DEFAULT_END_OF_WEEK

        return d
