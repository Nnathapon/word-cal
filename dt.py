from datetime import datetime as d
import thcal as t
from ephem import Date
import ephem

# Get current date
tday = d.now()

# Print ISO week day (1: Monday, 2: Tuesday, ..., 7: Sunday)
weekday = tday.isocalendar()
print(ephem.localtime(ephem.previous_equinox(tday)))
print("iso week:", weekday.week, weekday.weekday)
print("ordinal:", tday.timetuple().tm_yday)
tup = t.solar(tday)
print("yy ddd:", tup[0], tup[1])
print("moon:", t.lunar(tday))
for i in range(2020, 2030):
    that = t.solar(d(year=i, month=1, day=1))
    print(i, that)
print(ephem.next_spring_equinox(tday))
# labour 42  ; 50
# newyear 287; 1
# equinoe 80
