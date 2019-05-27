"""
Read file into texts and calls.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
Returns True if time1 comes after time2
"""
def first_time_after_second(time1, time2):
	# Assuming all times have same length
	if (len(time1) != len(time2)):
		assert(len(time1) == len(time2))
	time1 = time1.replace('-', '').replace(' ', '').replace(':', '')
	time2 = time2.replace('-', '').replace(' ', '').replace(':', '')
	return time1 > time2

"""
Returns the index of the element that satisfies the chronological order requested by `reveresed`
"""
def index_for_element(record, reversed):
    idx = 0
    for i in range(len(record)):
        if first_time_after_second(record[idx][2], record[i][2]) != reversed:
            idx = i
    return idx

"""
Returns the first(chronologically) record of texts in the input. O(n)
"""
def earliest_text_record(record):
    return index_for_element(record, False)

"""
Returns the last(chronologically) record of texts in the input. O(n)
"""
def last_text_record(record):
	return index_for_element(record, True)

"""
Returns first record of texts and what is the last record of calls. O(n)
"""
def print_occurrences_first_last(texts, calls):
    idx = earliest_text_record(texts)
    print('First record of texts, {} texts {} at time {}'.format(texts[idx][0], texts[idx][1], texts[idx][2]))
    idx = last_text_record(calls)
    print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(calls[idx][0], calls[idx][1], calls[idx][2], calls[idx][3]))

def test():
    print_occurrences_first_last(texts, calls)

def tests():
    test_cases = [['97424 22395', '90365 06212', '01-09-2016 06:03:22'],
                  ['94489 72078', '92415 91418', '01-09-2016 06:05:35'],
    ['78993 92058','92411 96415','30-09-2016 23:14:19']]
    test_cases_rev = [['78993 92058','92411 96415','30-09-2016 23:14:19'],['94489 72078', '92415 91418', '01-09-2016 06:05:35'],
    ['97424 22395', '90365 06212', '01-09-2016 06:03:22']]

    test_cases_middle = [['94489 72078', '92415 91418', '01-09-2016 06:05:35'], ['78993 92058','92411 96415','30-09-2016 23:14:19'],
    ['97424 22395', '90365 06212', '01-09-2016 06:03:22']]

    # Test that first_time_after returns the correct value asc
    assert(first_time_after_second(test_cases[0][2], test_cases[1][2]) == False)
    print('first_time_after_second  asc test passed')

    # Test that first_time_after returns the correct value desc
    assert(first_time_after_second(test_cases[1][2], test_cases[0][2]) == True)
    print('first_time_after_second desc test passed')

    # Test that first_record_texts returns correct value ascending
    assert(earliest_text_record(test_cases) == 0)
    print('first_record_texts test passed asc')

    # Test that first_record_texts returns correct value descending
    assert(earliest_text_record(test_cases_rev) == 2)
    print('first_record_texts test passed desc')

    # Test data set first element is smallest
    assert(earliest_text_record(texts) == 0)
    print('first_record_texts real data test passed')

    # Test data set last element is smallest
    texts_rev = list(reversed(texts))
    assert(earliest_text_record(texts_rev) == len(texts)-1)
    print('first_record_texts real data reversed test passed')

    # Final message for texts
    idx = earliest_text_record(texts)
    print('First record of texts, {} texts {} at time {}'.format(texts[idx][0], texts[idx][1], texts[idx][2]))

    # Test that last_text_record returns correct value asc
    assert(last_text_record(test_cases) == len(test_cases) - 1)
    print('last_text_record asc passed')

    # Test that last_text_record returns correct value desc
    assert(last_text_record(test_cases_rev) == 0)
    print('last_text_record desc passed')

    # Test that last_text_record returns correct value when correct vaue is in center
    assert(last_text_record(test_cases_middle) == 1)
    print('last_text_record value in middle passed')

    # Final message for texts
    idx = last_text_record(calls)
    print('Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(calls[idx][0], calls[idx][1], calls[idx][2], calls[idx][3]))

test()
