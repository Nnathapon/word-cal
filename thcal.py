import datetime as d
import math
from ephem import previous_spring_equinox as eq
from ephem import previous_new_moon as nm
from ephem import Date
from ephem import now
from ephem import localtime as loc

year = str(d.datetime.now().year)
datelist = {
    "newyear": year + "-1-1",
    "laborday": year + "-5-1",
    "chatr": year + "-5-5",
    "kingbirth": "1952-7-28 10:45",
    "queenbirth": "1978-6-3",
    "motherday": "1932-9-12",
    "fatherday": "1927-12-5 8:45",
    "piyaday": "1910-10-23",
    "conday": "1932-12-10",
    "14oct": "1973-10-14",
    "6oct": "1976-10-6",
    "navaminday": "2016-10-13 8:52",
    "qingming": eq(now()) + 15,
}


def jd(date):
    # Ensure correct format
    if not isinstance(date, d.datetime):
        raise TypeError('Invalid type for parameter "date" - expecting datetime')
    elif date.year < 1801 or date.year > 2099:
        raise ValueError("Datetime must be between year 1801 and 2099")

    # Perform the calculation
    julian_datetime = (
        367 * date.year
        - int((7 * (date.year + int((date.month + 9) / 12.0))) / 4.0)
        + int((275 * date.month) / 9.0)
        + date.day
        + 1721013.5
        + (date.hour + date.minute / 60.0 + date.second / math.pow(60, 2)) / 24.0
        - 0.5 * math.copysign(1, 100 * date.year + date.month - 190002.5)
        + 0.5
    )

    return julian_datetime


def atikmas(ad):
    return (ad - 78 - 0.45222) % 2.7118886 < 1


def dt(date=d.datetime.now()):
    ju = jd(date)
    h = ju - 1954167
    return (h + 0.192) % 29.530588


def sideAtikmas(ad):
    y = ad - 2000
    c = -1.17181e-9 * y - 1.22811e-9 * y**2
    return (ad + 0.1945238 + c) % 2.7118913122 < 1


def tropAtikmas(ad):
    y = ad - 2000
    c = -3.98347e-9 * y - 4.00987e-9 * y**2
    return (ad + 2.4143931 + c) % 2.7154255542 < 1


def suvanpum(ad):
    return (ad - 638 + 2.0) % 2.7154123 < 1


def solar(date):
    equinox = eq(date)
    ah = loc(equinox).replace(hour=0, minute=0, second=0)

    if Date(date) < eq(date.replace(month=4)):
        cpt = date.year - 1971
    else:
        cpt = date.year - 1970
    return cpt, (date - ah).days + 1


def lunar(date):
    newmoon = nm(date)
    return Date(date) - newmoon


def fromsolar(date):
    return Date(eq(now() + 365) + date)


"""
for i in range(2000, 2050):

    if atikmas(i):
        print(i, i + 543)


# print(dt(d.datetime(2024, 3, 21)))
for i in range(1, 367):
    q = d.datetime.fromordinal(i).replace(year=2024, second=i % 60)
    print(q, solar(q))
"""
