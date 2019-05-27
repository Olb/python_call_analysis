"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

"""
Returns true if is in list O(n)
"""
def is_in_list(number, records):
    for record in records:
        if record == number:
            return True
    return False


"""
Returns a count of the number of unique items in the given record O(n^2)
"""
def unique_numbers(calls, texts):
    tally = []
    for call in calls:
        if not is_in_list(call[0], tally):
            tally.append(call[0])
        if not is_in_list(call[1], tally):
            tally.append(call[1])
    for text in texts:
        if not is_in_list(call[0], tally):
            tally.append(call[0])
        if not is_in_list(call[1], tally):
            tally.append(call[1])
    return tally

"""
Returns a dictionary of calls in a given period
"""
def calls_in_period(calls, period):
    # unique_numbers could be n^2
    uniques = unique_numbers(calls, [])
    unique_dictionary = {key: 0 for key in uniques}
    # could be n^2
    for key in unique_dictionary:
        for call in calls:
            if (call[0] == key or call[1] == key) and (call[2][3:10] == period):
                unique_dictionary[key] += int(call[3])
    return unique_dictionary


"""
Retuns the number and time in seconds of the longest time
by a given number on calls in a given period O(n^2)

Parameters: str, format '09-2016' for September 2016
"""
def longest_call_in_period(calls, period):
    dict = calls_in_period(calls, period)
    maxValue = 0
    maxKey = ''
    # Worse case dict could hold n
    for key in dict:
        if dict[key] > maxValue:
            maxValue = dict[key]
            maxKey = key
    return maxKey, maxValue

def test():
    result = longest_call_in_period(calls, '09-2016')
    message = '{} spent the longest time, {} seconds, on the phone during September 2016.'.format(result[0], result[1])
    print(message)

def tests():
    test_cases = [['97424 22395', '90365 06212', '01-09-2026 06:03:22', '1'],
    ['94489 72078', '92415 91418', '01-09-2016 06:05:35', '2'],
    ['78993 92058','92411 96415','30-09-2016 23:14:19', '3'],
    ['78993 92058','92411 96415','30-08-2016 23:14:19', '3'],
    ['94489 72078','92411 96415','30-09-2016 23:14:19', '4']]

    # Test total durations
    assert(calls_in_period(test_cases, '09-2016')['97424 22395'] == 0)
    assert(calls_in_period(test_cases, '09-2016')['78993 92058'] == 3)
    assert(calls_in_period(test_cases, '09-2016')['94489 72078'] == 6)

    result = longest_call_in_period(test_cases, '09-2016')
    message = '{} spent the longest time, {} seconds, on the phone during September 2016.'.format(result[0], result[1])
    assert(message == '92411 96415 spent the longest time, 7 seconds, on the phone during September 2016.')

test()
