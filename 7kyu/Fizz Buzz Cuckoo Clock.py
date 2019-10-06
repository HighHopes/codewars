"""
When a minute is evenly divisible by three, the clock will say the word "Fizz".
When a minute is evenly divisible by five, the clock will say the word "Buzz".
When a minute is evenly divisible by both, the clock will say "Fizz Buzz", with two exceptions:
On the hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo bird will come out and "Cuckoo" between one and twelve times depending on the hour.
On the half hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo will come out and "Cuckoo" just once.
With minutes that are not evenly divisible by either three or five, at first you had intended to have the clock just say the numbers ala Fizz Buzz, but then you decided at least for version 1.0 to just have the clock make a quiet, subtle "tick" sound for a little more clock nature and a little less noise.
Your input will be a string containing hour and minute values in 24-hour time, separated by a colon, and with leading zeros. For example, 1:34 pm would be "13:34"."""


def fizz_buzz_cuckoo_clock(time):
    hour_dict = {"00": 12, "12": 12, "13": 1, "14": 2, "15": 3, "16": 4, "17": 5, "18": 6, "19": 7, "20": 8, "21": 9,
                 "22": 10, "23": 11, "24": 12}
    
    h = time[:2]
    m = time[-2:]
    
    if m == "30":
        return "Cuckoo"
    elif m == "00":
        if h in hour_dict:
            result = "Cuckoo " * hour_dict[h]
            return result.strip()
        else:
            result = "Cuckoo " * int(h)
            return result.strip()
    else:
        if int(m) % 5 == 0 and int(m) % 3 == 0:
            return "Fizz Buzz"
        elif int(m) % 5 == 0:
            return "Buzz"
        elif int(m) % 3 == 0:
            return "Fizz"
        else:
            return "tick"


print(fizz_buzz_cuckoo_clock("00:01"))
