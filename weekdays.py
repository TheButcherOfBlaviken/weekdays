from datetime import timedelta, date


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


start_dt = date(2021, 12, 1)
end_dt = date(2021, 12, 31)

weekends = [6,7]
for dt in daterange(start_dt, end_dt):
    if dt.isoweekday() not in weekends:
        print(f'{dt.strftime("%Y-%m-%d")}, {dt.strftime("%A")}')
