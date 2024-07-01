class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cycleCounter = 0
        currStudent = 0
        while cycleCounter < len(students) :
            if students[currStudent] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(currStudent)
                cycleCounter = 0
            else :
                currStudent += 1
                cycleCounter += 1
            
            if len(sandwiches) == 0 or len(students) == 0 :
                break
            
            currStudent %= len(students)

        return len(students)