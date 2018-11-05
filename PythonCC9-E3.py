# Playing around with instances and lists
# not an actual program
# Maybe a structure will be used in one of my later projects?

class Student():

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


ryuuji = Student('ryuuji', 'male')
taiga = Student('taiga', 'female')
yusaku = Student('yusaku', 'male')
minori = Student('minori', 'female')
ami = Student('ami', 'female')

students = [ryuuji, taiga, yusaku, minori, ami]

for i in range(len(students)):
    student = students[i]
    if student.gender == 'male':
        print(student.name)

print('')

students.append(Student('haruta', 'male'))

for i in range(len(students)):
    student = students[i]
    if student.gender == 'male':
        print(student.name)

print('')

for student in students:
    print(student.name.title() + ': ' + student.gender.title())

# I think all of this could be done with a dictionary...