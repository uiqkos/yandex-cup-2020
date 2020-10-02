import subprocess
import sys
import random


def compare_results(testable, tester, alarm_count, period, limit, *alarms):
    #\"{str(alarm_count)} {str(period)} {str(limit)} {' '.join([str(alarm) for alarm in alarms])}\"
    print(f"python {tester} {alarm_count} {period} {limit} {' '.join([str(alarm) for alarm in alarms])}")
    tester_result_process = subprocess.Popen(f"python {tester} {alarm_count} {period} {limit} {' '.join([str(alarm) for alarm in alarms])}", stdout=subprocess.PIPE)
    testable_result_process = subprocess.Popen(f"python {testable} {alarm_count} {period} {limit} {' '.join([str(alarm) for alarm in alarms])}", stdout=subprocess.PIPE)

    # testable_result_process = subprocess.Popen(f"python {testable} < ")
    # tester_result_process = subprocess.Popen(f"echo \"{str(alarm_count)} {str(period)} {str(limit)} {' '.join([str(alarm) for alarm in alarms])}\" | python {tester}")

    testable_output, testable_error = testable_result_process.communicate()
    tester_output, tester_error = tester_result_process.communicate()

    if tester_output != tester_output:
        print('Args: ', alarm_count, period, limit, alarms)
        print('Testable result: ', testable_output)
        print('Tester result: ', tester_output)


def generate_tests(
        test_count, min_alarm_count, max_alarm_count,
        min_period, max_period, min_limit, max_limit,
        min_start_time, max_start_time
    ):
    for i in range(test_count):
        alarm_count = random.randint(min_alarm_count, max_alarm_count)
        period = random.randint(min_period, max_period)
        limit = random.randint(min_limit, max_limit)
        alarms = [random.randint(min_start_time, max_start_time) for j in range(alarm_count)]
        yield alarm_count, period, limit, *alarms


args = sys.argv[1:]

testable, tester, \
min_alarm_count, max_alarm_count, \
min_period, max_period, \
min_limit, max_limit, \
min_start_time, max_start_time = 'C:\\Users\\uiqko\\PycharmProjects\\yandex-cup-2020\\tester\\Alarms.py', 'C:\\Users\\uiqko\\PycharmProjects\\yandex-cup-2020\\tester\\Alarms.py', 1, 100, 1, 100, 1, 100, 1, 100

for test in generate_tests(100, min_alarm_count, max_alarm_count, min_period, max_period, min_limit, max_limit, min_start_time, max_start_time):
    compare_results(testable, tester, *test)