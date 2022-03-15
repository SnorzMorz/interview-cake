

def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    for i in range(len(list_of_chars)//2):
        list_of_chars[i], list_of_chars[len(list_of_chars)-1-i] = list_of_chars[len(list_of_chars)-1-i], list_of_chars[i]


    return list_of_chars


def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1)

    # This gives us the right word order
    # but with each word backward

    # Now we'll make the words forward again
    # by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # Found the end of the current word!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1

def reverse_characters(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index  += 1
        right_index -= 1


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_num = 0
    dine_in_num = 0
    for order in served_orders:
        if (take_out_num < len(take_out_orders) and order == take_out_orders[take_out_num]):
            take_out_num += 1
        elif (dine_in_num < len(dine_in_orders) and order == dine_in_orders[dine_in_num]):
            dine_in_num += 1
        else:
            return False

    if (take_out_num < len(take_out_orders) or dine_in_num < len(dine_in_orders)):
        return False
    return True
