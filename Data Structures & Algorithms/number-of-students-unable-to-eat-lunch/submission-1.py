class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        k = 0
        studentqueue = deque(students)
        sandwiches = deque(sandwiches)

        while studentqueue:
            student = studentqueue.popleft()

            if student == sandwiches[0]:
                sandwiches.popleft()
                k = 0
            else:
                studentqueue.append(student)
                k += 1
            
            # Stuck
            if k > len(studentqueue) + 1:
                return len(studentqueue)
        
        return 0