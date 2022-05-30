from .end_of_week_type import EndOfWeekType

DEFAULT_END_OF_WEEK = EndOfWeekType.SUNDAY
DEFAULT_EVENT_TITLE_TEMPLATE = '{distance_miles} {type}'
DEFAULT_EVENT_DESCRIPTION_TEMPLATE = 'Name: {name}\n' \
                         'Distance: {distance_miles}\n' \
                         'Duration: {duration}\n' \
                         'Pace: {pace_min_per_mile}'
DEFAULT_SUMMARY_TITLE_TEMPLATE = 'Total Distance: {distance_miles}'
DEFAULT_SUMMARY_DESCRIPTION_TEMPLATE = 'Total Distance: {distance_miles}\n' \
                           'Total Duration: {duration}\n' \
                           'Total Elevation Gain: {elevation_gain_feet}\n' \
                           'Average Pace: {avg_pace_min_per_mile}'


class CalendarPreferences:
    def __init__(self, per_run_summary_enabled: bool = True, per_run_title_template: str = DEFAULT_EVENT_TITLE_TEMPLATE,
                 per_run_description_template: str = DEFAULT_EVENT_DESCRIPTION_TEMPLATE,
                 daily_run_summary_enabled: bool = True, daily_run_title_template: str = DEFAULT_SUMMARY_TITLE_TEMPLATE,
                 daily_run_description_template: str = DEFAULT_SUMMARY_DESCRIPTION_TEMPLATE,
                 weekly_run_summary_enabled: bool = True,
                 weekly_run_title_template: str = DEFAULT_SUMMARY_TITLE_TEMPLATE,
                 weekly_run_description_template: str = DEFAULT_SUMMARY_DESCRIPTION_TEMPLATE,
                 end_of_week: EndOfWeekType = DEFAULT_END_OF_WEEK):
        self.per_run_summary_enabled = per_run_summary_enabled
        self.per_run_description_template = per_run_description_template
        self.per_run_title_template = per_run_title_template

        self.daily_run_summary_enabled = daily_run_summary_enabled
        self.daily_run_description_template = daily_run_description_template
        self.daily_run_title_template = daily_run_title_template

        self.weekly_run_summary_enabled = weekly_run_summary_enabled
        self.weekly_run_description_template = weekly_run_description_template
        self.weekly_run_title_template = weekly_run_title_template
        self.end_of_week = end_of_week

    @staticmethod
    def from_dict(source):
        per_run_summary_enabled = source['per_run_summary_enabled'] if 'per_run_summary_enabled' in source else True
        daily_run_summary_enabled = source[
            'daily_run_summary_enabled'] if 'daily_run_summary_enabled' in source else True
        weekly_run_summary_enabled = source[
            'weekly_run_summary_enabled'] if 'weekly_run_summary_enabled' in source else True

        per_run_description_template = source['per_run_description_template'] if 'per_run_description_template' in source else None
        daily_run_description_template = source[
            'daily_run_description_template'] if 'daily_run_description_template' in source else None
        weekly_run_description_template = source[
            'weekly_run_description_template'] if 'weekly_run_description_template' in source else None

        per_run_title_template = source['per_run_title_template'] if 'per_run_title_template' in source else None
        daily_run_title_template = source['daily_run_title_template'] if 'daily_run_title_template' in source else None
        weekly_run_title_template = source[
            'weekly_run_title_template'] if 'weekly_run_title_template' in source else None

        end_of_week = EndOfWeekType.from_str(source['end_of_week']) if 'end_of_week' in source else DEFAULT_END_OF_WEEK

        return CalendarPreferences(per_run_summary_enabled, per_run_title_template, per_run_description_template,
                                   daily_run_summary_enabled, daily_run_title_template,
                                   daily_run_description_template,
                                   weekly_run_summary_enabled, weekly_run_title_template,
                                   weekly_run_description_template, end_of_week)

    def to_dict(self):
        d = {
            'per_run_summary_enabled': self.per_run_summary_enabled if self.per_run_summary_enabled is not None else True,
            'daily_run_summary_enabled': self.daily_run_summary_enabled if self.daily_run_summary_enabled is not None else True,
            'weekly_run_summary_enabled': self.weekly_run_summary_enabled if self.weekly_run_summary_enabled is not None else True}

        if self.per_run_description_template is not None:
            d['per_run_description_template'] = self.per_run_description_template
        if self.daily_run_description_template is not None:
            d['daily_run_description_template'] = self.daily_run_description_template
        if self.weekly_run_description_template is not None:
            d['weekly_run_description_template'] = self.weekly_run_description_template

        if self.per_run_title_template is not None:
            d['per_run_title_template'] = self.per_run_title_template
        if self.daily_run_title_template is not None:
            d['daily_run_title_template'] = self.daily_run_title_template
        if self.weekly_run_title_template is not None:
            d['weekly_run_title_template'] = self.weekly_run_title_template

        d['end_of_week'] = self.end_of_week.value if self.end_of_week is not None else DEFAULT_END_OF_WEEK

        return d
