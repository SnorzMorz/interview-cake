

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
