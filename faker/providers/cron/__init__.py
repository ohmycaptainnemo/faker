from .. import BaseProvider
from .models import Minute, Hour, DayOfMonth, Month, DayOfWeek


class Provider(BaseProvider):
    minute: Minute = Minute()
    hour: Hour = Hour()
    day_of_month: DayOfMonth = DayOfMonth()
    month: Month = Month()
    day_of_week: DayOfWeek = DayOfWeek()

    def create_full_cron_expression(self) -> str:
        return (
            f"{Provider.minute.create_random_minute()} {Provider.hour.create_random_hour()} "
            f"{Provider.day_of_month.create_random_day_of_month()} "
            f"{Provider.month.create_random_month()} "
            f"{Provider.day_of_week.create_random_day_of_week()}"
        )
