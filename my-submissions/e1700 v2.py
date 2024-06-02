# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        squareStudents = sum(students)

        currStudent = 0
        while True:
            if sandwiches[0] :
                if not squareStudents :
                    break
                elif students[currStudent] :
                    students.pop(currStudent)
                    sandwiches.pop(0)
                    squareStudents -= 1
                else :
                    currStudent += 1
            else :
                if not (len(students) - squareStudents) :
                    break
                elif not students[currStudent] :
                    students.pop(currStudent)
                    sandwiches.pop(0)
                else :
                    currStudent += 1
            
            if len(students) == 0 :
                break
            
            currStudent %= len(students)

        return len(students)