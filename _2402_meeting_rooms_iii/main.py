class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = [i for i in range(n)]
        used = []
        nb_meetings = [0 for _ in range(n)]

        for meeting in meetings:
            # Check if rooms finished their meetings
            while len(used) > 0 and used[0][0] <= meeting[0]:
                _, room_index = heapq.heappop(used)
                heapq.heappush(free, room_index)

            # Room available
            if len(free) > 0:
                room_index = heapq.heappop(free)
                heapq.heappush(used, (meeting[1], room_index))
            else:
                # Get the first room available
                end_time, room_index = heapq.heappop(used)
                heapq.heappush(used, (end_time + (meeting[1] - meeting[0]), room_index))

            nb_meetings[room_index] += 1

        index = 0
        maximum = 0
        for i in range(len(nb_meetings)):
            if nb_meetings[i] > maximum:
                index = i
                maximum = nb_meetings[i]

        return index