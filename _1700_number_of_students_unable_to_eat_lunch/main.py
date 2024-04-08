class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches = deque(sandwiches)
        students = deque(students)

        while sandwiches:
            sandwich = sandwiches.popleft()
            length = len(students)
            found = False

            for _ in range(length):
                student = students.popleft()
                if student == sandwich:
                    found = True
                    break
                else:
                    students.append(student)

            if not found:
                return len(students)

        return 0