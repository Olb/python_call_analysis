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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
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
Returns the call prefix O(1)
"""
def call_prefix(call):
    if call[0:1] == '(':
        idx = call.index(')')
        return call[1:idx]
    if call[0:3] == "140":
        return call[0:3]
    return call[0:4]

"""
Returns a list of calls from Bangalore numbers O(n)
"""
def called_by_bangalore(calls):
    tally = []
    for call in calls:
        if call_prefix(call[0]) == "080":
            if not is_in_list(call_prefix(call[1]), tally):
                tally.append(call_prefix(call[1]))
    return tally

"""
Prints the percentage of calls made from and to numbers in Bangalore O(n)
"""
def percentage_calls_bangalore(calls):
    totalOut = 0
    totalIn = 0
    for call in calls:
        if call_prefix(call[0]) == '080':
            totalOut += 1
            if call_prefix(call[1]) == '080':
                totalIn += 1
    return '{:.2f}'.format(totalIn / totalOut * 100)


"""
Prints the calls from Bangalore to other phones in lexical order
Prints the calls from Bangalore and to Bangalore numbers
"""
def print_bangalore_calls(calls):
    # Part A
    print('The numbers called by people in Bangalore have codes:')
    # O(n)
    tally = called_by_bangalore(calls)
    tally.sort()
    # O(n)
    for prefix in tally:
        print(prefix)

    # Part B
    print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percentage_calls_bangalore(calls)))

def test():
    print_bangalore_calls(calls)

def tests():
    test_number_three_digit = "(080)45687418"
    test_number_not_three_digit = "(04344)316423"
    test_number_mobile = "90083"
    test_number_tele = "1408371942"

    test_cases = [['(044)49481100','(080)69245029','01-09-2016 10:15:06,385'],
    ['(080)29435303','98447 12671','01-09-2016 10:15:24,9'],
    ['(080)29435303','(12345) 57063','01-09-2016 10:17:21,46'],
    ['(080)29435303','(080)43685310','01-09-2016 10:25:39,236'],
    ['95264 40233','982340 68457','01-09-2016 10:28:48,692'],
    ['(080)29435303','98447 12671','01-09-2016 10:15:24,9'],]

    test_cases_percent = [['(044)49481100','(080)69245029','01-09-2016 10:15:06,385'],
    ['(080)29435303','98447 12671','01-09-2016 10:15:24,9'],
    ['(080)29435303','(12345) 57063','01-09-2016 10:17:21,46'],
    ['(080)29435303','(080)43685310','01-09-2016 10:25:39,236'],
    ['95264 40233','982340 68457','01-09-2016 10:28:48,692'],
    ['(080)29435303','98447 12671','01-09-2016 10:15:24,9'],
    ['(080)29435303','9844743685310','01-09-2016 10:25:39,236'],
    ['(080)29435303','(080)43685310','01-09-2016 10:25:39,236']]

    test_cases_order = ['9844', '12345', '080']
    # Test call_prefix 3 digit landline
    assert(call_prefix(test_number_three_digit) == "080")
    print('test call_prefix return correct number for 3 digit passed')

    # Test call_prefix non-3 digit landline
    assert(call_prefix(test_number_not_three_digit) == "04344")
    print('test call_prefix return correct number for 5 digit passed')

    # Test call_prefix mobile e.g. 090083
    assert(call_prefix(test_number_mobile) == "9008")
    print('test call_prefix return correct number for mobile passed')

    # Test call_prefix mobile e.g. 1408371942
    assert(call_prefix(test_number_tele) == "140")
    print('test call_prefix return correct number telemarketers passed')

    # Test called_by_bangalore returns correct number
    assert(len(called_by_bangalore(test_cases)) == 3)
    print('test called_by_bangalore return correct number passed')

    # Test called_by_bangalore returns correct result
    assert(called_by_bangalore(test_cases) == test_cases_order)
    print('test called_by_bangalore return correct result passed')

    # Test that calls within Bangalore return the correct percentage
    assert(percentage_calls_bangalore(test_cases_percent) == '33.33')
    print('percentage_calls_bangalore prints correct percentages passed')

test()
