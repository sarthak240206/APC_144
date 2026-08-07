student_list = ["Sarthak","Athrava","Prathm","balaji","Vivek","Prassana"]
print("Student list before deletion")
print(student_list)
del student_list[0]
print("Student list after deletion of first student")
print(student_list)
student_list.pop()
print("Student list after deletion of last student")
print(student_list)
student_list.remove("Prathm")
print("Student list after deletion of  student named Prathm")
print(student_list)
