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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
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
Returns a list of numbers of unique items in the given record O(n^2)
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

def test():
    print('There are {} different telephone numbers in the records.'.format(len(unique_numbers(calls, texts))))

def tests():
    test_records = ['97424 22395', '90365 06212', '92415 91418']

    test_cases = [['97424 22395', '90365 06212', '01-09-2016 06:03:22'],
                  ['94489 72078', '92415 91418', '01-09-2016 06:05:35'],
    ['78993 92058','92411 96415','30-09-2016 23:14:19'],
['1234 4567','92411 96415','30-09-2016 23:14:19']]

    # Tests that the number is not in the record
    assert(is_in_list('1234 4567', test_records) == False)
    print('is_in_list does not contain record passed')

    # Tests that the number is in the record
    assert(is_in_list('90365 06212', test_records) == True)
    print('is_in_list does contain record passed')

    # Tests that the count is correct unique
    assert(len(unique_numbers(test_cases, test_cases)) == 7)
    print('unique_numbers returns correct count passed ')

test()
