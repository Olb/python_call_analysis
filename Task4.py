"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Checks if number is in the records O(n)
"""
def check_if_number_in_record(number, records):
    for record in records:
        if number == record[0] or number == record[1]:
            return True
    return False

"""
Checks if number is in outgoing O(n)
"""
def check_if_number_in_incoming(number, records):
    for record in records:
        if number == record[1]:
            return True
    return False

"""
Check if number exists in texts O(n^2)
"""
def all_non_texts(calls, texts):
    tally = []
    for call in calls:
        if not check_if_number_in_record(call[0], texts) and not check_if_number_in_record(call[1], texts):
            tally.append(call)
    return tally

"""
Get list of all possibe telemarketers O(n^2)
"""
def get_possible_telemarketer_numbers(calls, texts):
    possible_numbers = all_non_texts(calls, texts)
    result = []
    for possibility in possible_numbers:
        if not check_if_number_in_incoming(possibility[0], possible_numbers):
            result.append(possibility[0])
    return result

def print_possible_telemarketers(calls, texts):
    possible_numbers = get_possible_telemarketer_numbers(calls, texts)
    possible_numbers.sort()
    print('These numbers could be telemarketers:')
    for possibility in possible_numbers:
        print(possibility)

def test():
    print_possible_telemarketers(calls, texts)

def tests():
    test_cases_calls = [['97424 22395', '90365 06212', '01-09-2026 06:03:22', '1'],
    ['94489 72078', '78983 92058', '01-09-2016 06:05:35', '2'],
    ['78983 92058','92412 96415','30-09-2016 23:14:19', '3'],
    ['78993 92058','92413 96415','30-08-2016 23:14:19', '4'],
    ['94689 72078','92414 96415','30-09-2016 23:14:19', '5']]

    test_cases_texts = [
    ['78993 92058','92413 96415','30-08-2016 23:14:19', '4'],
    ['94689 72078','92414 96415','30-09-2016 23:14:19', '5']]

    assert(len(all_non_texts(test_cases_calls, test_cases_texts)) == 3)

    assert(check_if_number_in_record('78993 92058', test_cases_calls) == True)
    assert(check_if_number_in_record('34521 92058', test_cases_calls) == False)

    assert(check_if_number_in_incoming('92414 96415', test_cases_calls) == True)
    assert(check_if_number_in_incoming('90004 96415', test_cases_calls) == False)

    expect = ['97424 22395','94489 72078']
    assert(get_possible_telemarketer_numbers(test_cases_calls, test_cases_texts) == expect)

test()
