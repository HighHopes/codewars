def format_duration(seconds):
	one_sec = 1
	one_min = one_sec * 60
	one_hour = one_min * 60
	one_day = one_hour * 24
	one_year = one_day * 365

	year, day, hour, minute, sec = 0, 0, 0, 0, 0

	if seconds >= one_year:
		year = seconds // one_year

	if seconds >= one_day:
		day = seconds % one_year // one_day

	if seconds >= one_hour:
		hour = seconds % one_year % one_day // one_hour

	if seconds >= one_min:
		minute = seconds % one_year % one_day % one_hour // one_min

	sec = seconds % one_min

	construct = [year, day, hour, minute, sec]

	result = ""

	return result



print(format_duration(1))  # "1 second"
print(format_duration(62))  # "1 minut	e and 2 seconds"
print(format_duration(120))  # "2 minutes"
print(format_duration(3600))  # "1 hour"
print(format_duration(3662))  # "1 hour, 1 minute and 2 seconds"
print(format_duration(242062374))  # "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"