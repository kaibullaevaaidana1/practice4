import sys
from datetime import datetime, timedelta, timezone
import re


def parse_datetime_tz(s):
    date_part, tz_part = s.strip().split()
    year, month, day = map(int, date_part.split('-'))

    m = re.match(r'UTC([+-])(\d{2}):(\d{2})', tz_part)
    sign, hours, minutes = m.groups()
    offset_minutes = int(hours) * 60 + int(minutes)
    if sign == '-':
        offset_minutes = -offset_minutes
    tz = timezone(timedelta(minutes=offset_minutes))

    dt = datetime(year, month, day, 0, 0, 0, tzinfo=tz)
    return dt


def main():
    dt1 = parse_datetime_tz(sys.stdin.readline())
    dt2 = parse_datetime_tz(sys.stdin.readline())

    dt1_utc = dt1.astimezone(timezone.utc)
    dt2_utc = dt2.astimezone(timezone.utc)

    delta_seconds = abs((dt1_utc - dt2_utc).total_seconds())

    full_days = int(delta_seconds // 86400)
    sys.stdout.write(str(full_days) + "\n")


if __name__ == "__main__":
    main()