## wat-intro-set.png
```
python -m IPython
```
```
import wat
wat / {42}
```


## wat-datetime-now.png

- terminal 90x27
- `title wat`
- `python`
```python
import wat
wat.str / datetime.datetime.now()
```

```python
wat_out = "\x1b[0;34m──────────────────────────────────────────────────────────────────────────────────────────\x1b[0m\n\x1b[1;34mstr:\x1b[0m \x1b[0;32m2024-07-31 21:30:28.163527\x1b[0m\n\x1b[1;34mrepr:\x1b[0m \x1b[1mdatetime.datetime(2024, 7, 31, 21, 30, 28, 163527)\x1b[0m\n\x1b[1;34mtype:\x1b[0m \x1b[0;33mdatetime.datetime\x1b[0m\n\x1b[1;34mparents:\x1b[0m \x1b[0;33mdatetime.date\x1b[0m\n\n\x1b[1mPublic attributes:\x1b[0m\n  \x1b[1;33mday\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m31\x1b[0m\x1b[0m\n  \x1b[1;33mfold\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m0\x1b[0m\x1b[0m\n  \x1b[1;33mhour\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m21\x1b[0m\x1b[0m\n  \x1b[1;33mmax\x1b[0;33m: \x1b[0;33mdatetime.datetime\x1b[0m = \x1b[0;32m9999-12-31 23:59:59.999999\x1b[0m\x1b[0m\n  \x1b[1;33mmicrosecond\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m163527\x1b[0m\x1b[0m\n  \x1b[1;33mmin\x1b[0;33m: \x1b[0;33mdatetime.datetime\x1b[0m = \x1b[0;32m0001-01-01 00:00:00\x1b[0m\x1b[0m\n  \x1b[1;33mminute\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m30\x1b[0m\x1b[0m\n  \x1b[1;33mmonth\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m7\x1b[0m\x1b[0m\n  \x1b[1;33mresolution\x1b[0;33m: \x1b[0;33mdatetime.timedelta\x1b[0m = \x1b[0;32m0:00:00.000001\x1b[0m\x1b[0m\n  \x1b[1;33msecond\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m28\x1b[0m\x1b[0m\n  \x1b[1;33mtzinfo\x1b[0;33m: \x1b[0;33mNoneType\x1b[0m = \x1b[0;35mNone\x1b[0m\x1b[0m\n  \x1b[1;33myear\x1b[0;33m: \x1b[0;33mint\x1b[0m = \x1b[0;31m2024\x1b[0m\x1b[0m\n\n  \x1b[0;34mdef \x1b[1;32mastimezone\x1b[0;32m(…)\x1b[0m \x1b[2;37m# tz -> convert to local time in new timezone tz\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mcombine\x1b[0;32m(…)\x1b[0m \x1b[2;37m# date, time -> datetime with same date and time fields\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mctime\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return ctime() style string.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mdate\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return date object with same year, month and day.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mdst\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return self.tzinfo.dst(self).\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mfromisocalendar\x1b[0;32m(…)\x1b[0m \x1b[2;37m# int, int, int -> Construct a date from the ISO year, week number and weekday.…\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mfromisoformat\x1b[0;32m(…)\x1b[0m \x1b[2;37m# string -> datetime from a string in most ISO 8601 formats\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mfromordinal\x1b[0;32m(…)\x1b[0m \x1b[2;37m# int -> date corresponding to a proleptic Gregorian ordinal.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mfromtimestamp\x1b[0;32m(…)\x1b[0m \x1b[2;37m# timestamp[, tz] -> tz's local time from POSIX timestamp.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32misocalendar\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return a named tuple containing ISO year, week number, and weekday.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32misoformat\x1b[0;32m(…)\x1b[0m \x1b[2;37m# [sep] -> string in ISO 8601 format, YYYY-MM-DDT[HH[:MM[:SS[.mmm[uuu]]]]][+HH:MM].…\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32misoweekday\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return the day of the week represented by the date.…\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mnow\x1b[0;32m(tz=None)\x1b[0m \x1b[2;37m# Returns new datetime object representing current time local to tz.…\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mreplace\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return datetime with new specified fields.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mstrftime\x1b[0;32m(…)\x1b[0m \x1b[2;37m# format -> strftime() style string.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mstrptime\x1b[0;32m(…)\x1b[0m \x1b[2;37m# string, format -> new datetime parsed from a string (like time.strptime()).\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtime\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return time object with same time but with tzinfo=None.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtimestamp\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return POSIX timestamp as float.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtimetuple\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return time tuple, compatible with time.localtime().\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtimetz\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return time object with same time and tzinfo.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtoday\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtoordinal\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return proleptic Gregorian ordinal.  January 1 of year 1 is day 1.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mtzname\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return self.tzinfo.tzname(self).\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mutcfromtimestamp\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Construct a naive UTC datetime from a POSIX timestamp.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mutcnow\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return a new datetime representing UTC day and time.\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mutcoffset\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return self.tzinfo.utcoffset(self).\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mutctimetuple\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return UTC time tuple, compatible with time.localtime().\x1b[0m\x1b[0m\n  \x1b[0;34mdef \x1b[1;32mweekday\x1b[0;32m(…)\x1b[0m \x1b[2;37m# Return the day of the week represented by the date.…\x1b[0m\x1b[0m\n\x1b[0;34m──────────────────────────────────────────────────────────────────────────────────────────\x1b[0m"
RESET ='\033[0m'
STYLE_BRIGHT = '\033[1m'
STYLE_DIM = '\033[2m'
STYLE_RED = '\033[0;31m'
STYLE_BRIGHT_RED = '\033[1;31m'
STYLE_GREEN = '\033[0;32m'
STYLE_BRIGHT_GREEN = '\033[1;32m'
STYLE_YELLOW = '\033[0;33m'
STYLE_BRIGHT_YELLOW = '\033[1;33m'
STYLE_BLUE = '\033[0;34m'
STYLE_BRIGHT_BLUE = '\033[1;34m'
STYLE_MAGENTA = '\033[0;35m'
STYLE_CYAN = '\033[0;36m'
STYLE_WHITE = '\033[0;37m'
STYLE_GRAY = '\033[2;37m'

output = '\n'.join([
    f'>>> {STYLE_BRIGHT_GREEN}import {STYLE_BRIGHT_BLUE}wat{RESET}',
    f'>>> {STYLE_BRIGHT_GREEN}import {STYLE_BRIGHT_BLUE}datetime{RESET}',
    f'>>> wat / datetime.datetime.now()',
    wat_out,
])
print(output)
```
