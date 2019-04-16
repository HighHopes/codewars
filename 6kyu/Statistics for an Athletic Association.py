"""
Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. There are no traps in this format.

To compare the results of the teams you are asked for giving three statistics; range, average and median.

Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

Mean or Average : To calculate mean, add together all of the numbers in a set and then divide the sum by the total count of numbers.

Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above, the string result will be

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

of the form:

"Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"

where hh, mm, ss are integers (represented by strings) with each 2 digits.

Remarks:

if a result in seconds is ab.xy... it will be given truncated as ab.

if the given string is "" you will return ""
"""

import time


def seconds_to_hms(sec):
	return time.strftime("%H|%M|%S", time.gmtime(sec))


def hours_to_seconds(hms):
	# Transform input into seconds

	lst = hms.split(",")

	lst2 = []
	for i in lst:
		lst2.append(tuple(map(int, i.split("|"))))

	lst3 = []
	for i in lst2:
		lst3.append((i[0] * 3600) + (i[1] * 60) + i[2])

	return lst3


def myrange(seconds):
	# difference between the lowest and highest values

	minim = min(seconds)
	maxim = max(seconds)

	result = maxim - minim

	return seconds_to_hms(result)


def average(seconds):
	# add together all of the numbers in a set and then divide the sum by the total count of numbers

	sum = 0
	for i in seconds:
		sum += i

	no = len(seconds)
	result = sum / no
	return seconds_to_hms(result)


def median(seconds):
	# the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values

	n = len(seconds)
	if n % 2 == 1:
		result = sorted(seconds)[n // 2]
	else:
		result = sum(sorted(seconds)[n // 2 - 1:n // 2 + 1]) / 2.0
	return seconds_to_hms(result)


def stat(strg):
	rng = myrange(hours_to_seconds(strg))
	avg = average(hours_to_seconds(strg))
	med = median(hours_to_seconds(strg))

	return "Range: {} Average: {} Median: {}".format(rng, avg, med)


print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))  # Range: 01|01|18 Average	: 01|38|05 Median: 01|32|34
print(stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))  # Range: 01|01|18 Average: 01|38|05 Median: 01|32|34
print(stat(
	"02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"))  # Range: 00|31|17 Average: 02|26|18 Median: 02|22|00
