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
Returns set of unique calls that are outgoing O(n)
"""
def outgoing_calls(calls):
    outgoing_unique = set([])
    for call in calls:
        outgoing_unique.add(call[0])
    return outgoing_unique

"""
Returns a set of text numbers from the record O(n)
"""
def text_numbers(texts):
    texts_unique = set([])
    for text in texts:
        texts_unique.add(text[0])
        texts_unique.add(text[1])
    return texts_unique

"""
Returns only incoming calls from the record O(n)
"""
def incoming_calls(calls):
    incoming = set([])
    for call in calls:
        incoming.add(call[1])
    return incoming

"""
Returns a list of possibe telemarketers
"""
def possible_telemarketers(calls, texts):
    outgoing_unique = set(outgoing_calls(calls))
    texts_unique = set(text_numbers(texts))
    incoming_unique = set(incoming_calls(calls))
    return [outgoing for outgoing in outgoing_unique if outgoing not in texts_unique and outgoing not in incoming_unique]

"""
Prints a lexicographic list of possible telemarketers O(nlogn)due to .sort()
"""
def print_possible_telemarketers(calls, texts):
    print("These numbers could be telemarketers: ")
    for possibility in sorted(possible_telemarketers(calls, texts)):
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
    ['94689 72078','92414 96415','30-09-2016 23:14:19', '5'],
    ['94689 72078','92414 96415','30-09-2016 23:14:19', '5']]

    expectation = {'97424 22395', '94489 72078', '78983 92058', '94689 72078', '78993 92058'}
    assert(outgoing_calls(test_cases_calls) == expectation)

    expectation = {'78993 92058', '92413 96415', '92414 96415', '94689 72078', '94689 72078'}
    assert(text_numbers(test_cases_texts) == expectation)

    expectation = {'90365 06212', '78983 92058', '92412 96415', '92413 96415', '92414 96415'}
    assert(incoming_calls(test_cases_calls) == expectation)

    print(possible_telemarketers(test_cases_calls, test_cases_texts))
    expectation = ['97424 22395', '94489 72078']
    assert(possible_telemarketers(test_cases_calls, test_cases_texts) == expectation)
test()
