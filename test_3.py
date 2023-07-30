"""
Third stage of MOJ take home assessment


Prompt:
The below function doesn't work correctly. It should sum all the numbers at the
current time. For example, 01:02:03 should return 6. Improve and fix the function,
and write unit test(s) for it. Use any testing framework you're familiar with.

Question/Note:
Am I overthinking things, or does the prompt imply that I should be using
something like datetime's .now() method to get the current time?
That's what I do in the name == main block, but I've 
left datetime out of the actual function so that I can test it more easily
"""

from datetime import datetime

MAX_SUM = 141  # On a 24 hour clock, the max sum you can get is 23 + 59 + 59  == 141


def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    if not isinstance(time_str, str):
        raise TypeError("input must be a string")

    list_of_nums = time_str.split(":")

    if len(list_of_nums) == 1:
        raise ValueError("Wrong / No separator used")

    list_of_nums_as_int = [int(num) for num in list_of_nums]
    sum_of_numbers = sum(list_of_nums_as_int)

    if sum_of_numbers > MAX_SUM:
        raise ValueError("Sum too large - Invalid Time")

    if sum_of_numbers < 0:
        raise ValueError("Sum was negative - Invalid Time")

    return sum_of_numbers


if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(sum_current_time(current_time))
