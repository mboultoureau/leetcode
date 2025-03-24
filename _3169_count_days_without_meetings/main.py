class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ## SOLUTION 3: runtime 224ms (16.87%), memory: 53.02mb (19.65%)
        meetings.sort()

        # Constraints: 1 <= meetings.length <= 105
        current_meeting = meetings[0]
        current_day = 1
        available_days = 0

        for i in range(1, len(meetings)):
            start, end = meetings[i]
            if (start >= current_meeting[0] and start <= current_meeting[1]) or (end >= current_meeting[0] and end <= current_meeting[1]):
                current_meeting = [min(start, current_meeting[0]), max(end, current_meeting[1])]
            else:
                available_days += (current_meeting[0] - current_day)
                current_day = current_meeting[1] + 1
                current_meeting = [start, end]


        available_days += (current_meeting[0] - current_day)
        current_day = current_meeting[1] + 1
        available_days += days - current_day + 1

        return available_days




        ## SOLUTION 2: runtime 223ms (25.19%), memory: 52.81mb (55.42%)
        # merged_meetings = []
        # meetings.sort()

        # # Constraints: 1 <= meetings.length <= 105
        # current = meetings[0]
        # for i in range(1, len(meetings)):
        #     start, end = meetings[i]
        #     if (start >= current[0] and start <= current[1]) or (end >= current[0] and end <= current[1]):
        #         current = [min(start, current[0]), max(end, current[1])]
        #     else:
        #         merged_meetings.append(current)
        #         current = [start, end]

        # merged_meetings.append(current)

        # current = 1
        # available_days = 0
        # for start, end in merged_meetings:
        #     available_days += (start - current)
        #     current = end + 1

        # available_days += days - current + 1

        # return available_days




        ## SOLUTION 1: Memory Limit Exceeded
        # start = [0] * days
        # end = [0] * days

        # for s, e in meetings:
        #     start[s - 1] += 1
        #     end[e - 1] += 1

        # available_days = 0
        # current = 0
        # for d in range(days):
        #     current += start[d]
        #     if current == 0:
        #         available_days += 1
        #     current -= end[d]

        # return available_days