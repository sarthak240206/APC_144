# Create two sets representing technical skills of two employees. Find common skills, skills unique to Employee 1, skills unique to Employee 2, and all available skills.
# Program: Employee Skills

emp1 = {"Python", "SQL", "AWS", "Docker"}
emp2 = {"Python", "Java", "AWS", "Kubernetes"}
print("Common:", emp1 & emp2)
print("Unique to Emp1:", emp1 - emp2)
print("Unique to Emp2:", emp2 - emp1)
print("All skills:", emp1 | emp2)
