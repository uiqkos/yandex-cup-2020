import os
import sys


def get_alarm(alarm_count, period, alarm_limit, *alarms):
    result = []
    for alarm in alarms:
        result += [
            alarm + step * period
            for step in range(alarm_limit)
            if alarm + step * period not in result
        ]

    return list(sorted(result))[alarm_limit - 1]

print(sys.argv)

if len(sys.argv) == 1:
    alarm_count_, period_, alarm_limit_ = [int(num) for num in input().split()]
    alarms_ = [int(num) for num in input().split()]
    print(get_alarm(alarm_count_, period_, alarm_limit_, *alarms_))
else:
    print(get_alarm(*[int(arg) for arg in sys.argv[1:]]))
