import os
import sys

sys.path.insert(0, os.path.abspath("college_project"))

from student.details import get_student_details
from student.marks import get_student_marks
from faculty.details import get_faculty_details

s_info = get_student_details("S101", "Rohan Verma", "Computer Science")
s_marks = get_student_marks([88, 92, 79, 95])
f_info = get_faculty_details("F201", "Dr. Sharma", "Data Structures")

print("Student Details:", s_info)
print("Student Marks:", s_marks)
print("Faculty Details:", f_info)
