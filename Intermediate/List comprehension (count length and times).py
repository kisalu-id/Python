"""
This script helps me check my other program's results by counting the total length and adding up times in m:s format. 
It converts each time to seconds, adds them up, and then converts the total into h:m:s format so I can easily see and compare the result.
ChatGPT was unfortunatly unreliable for that, so here's my quick script TwT
"""

def seconds_to_hh_mm_ss(total_seconds):
    total_time_hh = total_seconds // 3600
    total_time_mm = (total_seconds % 3600) // 60
    total_time_ss = total_seconds % 60
    print(f"{total_time_hh:02}:{total_time_mm:02}:{total_time_ss:02}")


def time_to_seconds(t):
    minutes, seconds = map(int, t.split(":"))
    return minutes * 60 + seconds


nums = [
    5.491,
    3.127,
    6.291,
    2.629,
    2.573,
    4.941,
    4.775,
    1.849,
    1.849,
    2.573,
    5.175,
    5.175,
    2.629,
    2.553,
    4.941,
    2.317,
    2.649,
    4.941,
    2.317,
    4.775,
    2.443,
    4.941,
    2.553,
    2.381,
    2.061,
    4.661,
    3.353,
    3.429
]

times = [
    "05:45",
    "03:24",
    "06:18",
    "02:52",
    "02:35",
    "04:57",
    "04:48",
    "01:52",
    "01:52",
    "02:35",
    "05:12",
    "05:13",
    "02:39",
    "02:50",
    "04:57",
    "02:21",
    "02:40",
    "04:57",
    "02:20",
    "04:48",
    "02:28",
    "04:58",
    "02:34",
    "02:26",
    "02:21",
    "04:41",
    "03:23",
    "03:28"
]

#time
#list comprehension
total_seconds = sum(time_to_seconds(t) for t in times)

seconds_to_hh_mm_ss(total_seconds)

#length
sum_length = sum(nums)
print(sum_length)

"""
List comprehension is a quick and elegant way to create lists in Python.
It lets you generate a new list by looping through an existing one and applying a transformation or filter—all in a single line of code.
It's shorter, faster, and more readable than a traditional for loop.
[expression for item in list if condition]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
"""
