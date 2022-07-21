from django.utils import timezone
import calendar


class Day:
    def __init__(self, year, month, day, is_past) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.past = is_past


class Calendar(calendar.Calendar):
    def __init__(self, year, month) -> None:
        super().__init__(firstweekday=6)
        self.year = year
        self.month = month
        self.day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        self.months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]

    def get_days(self):
        m2c = self.monthdays2calendar(self.year, self.month)
        day = []
        now = timezone.now()
        today = now.day
        month = now.month
        is_past = False

        for week in m2c:
            for date, _ in week:
                if month == self.month:
                    is_past = date < today

                d = Day(year=self.year, month=self.month, day=date, is_past=is_past)
                day.append(d)
        return day

    def get_month(self):
        return self.months[self.month - 1]
