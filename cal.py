import calendar


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
        for week in m2c:
            for date, _ in week:
                day.append(date)
        return day

    def get_month(self):
        return self.months[self.month - 1]
