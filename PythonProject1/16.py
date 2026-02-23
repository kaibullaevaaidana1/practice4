import sys
from datetime import datetime, timedelta


def parse_time(line):
    # Split into datetime part and timezone part
    date_part, time_part, tz_part = line.strip().split()

    # Parse naive datetime
    dt = datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")

    # Parse timezone offset
    sign = 1 if tz_part[3] == '+' else -1
    hours = int(tz_part[4:6])
    minutes = int(tz_part[7:9])

    offset = timedelta(hours=hours, minutes=minutes)

    # Convert to UTC
    dt_utc = dt - sign * offset

    return dt_utc


def main():
    start_line = sys.stdin.readline()
    end_line = sys.stdin.readline()

    start_utc = parse_time(start_line)
    end_utc = parse_time(end_line)

    duration = int((end_utc - start_utc).total_seconds())

    print(duration)


if __name__ == "__main__":
    main()