from datetime import timedelta, date


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


input_complete = False
while not input_complete:
    try:
        start_year = int(input("Start Year: "))
        start_month = int(input("Start Month: "))
        start_date = int(input("Start Date: "))
        end_year = int(input("end Year: "))
        end_month = int(input("end Month: "))
        end_date = int(input("end Date: "))
    except ValueError:
        print("\n~~~~~~~~~~~~~~~~~ERROR~~~~~~~~~~~~~~~~~")
        print("Try a number.")
        print("~~~~~~~~~~~~~~~~~ERROR~~~~~~~~~~~~~~~~~\n")
        continue
    else:
        start_dt = date(start_year, start_month, start_date)
        end_dt = date(end_year, end_month, end_date)
        input_complete = True
            
            
weekends = [6,7]
for dt in daterange(start_dt, end_dt):
    if dt.isoweekday() not in weekends:
        print(f'{dt.strftime("%Y-%m-%d")}, {dt.strftime("%A")}')
