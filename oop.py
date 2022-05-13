all_students = []
all_grades_stud = []
all_lecturers = []
all_grades_lect = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mean_grades = 0
        all_students.append(self)
    
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        for grade in self.grades.values():
            self.mean_grades += sum(grade)/len(grade)
        res = f'Имя: {self.name}\n' f'Фамилия: {self.surname}' f'\nСредняя оценка за домашние задания: {round(self.mean_grades,1)}' f'\nКурсы в процессе изучения: ' + ', '.join(self.courses_in_progress) + f'\nЗавершенные курсы:: ' + ', '.join(self.finished_courses)
        return res
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.mean_grades = 0
        all_lecturers.append(self)
    def __str__(self):
        for grade in self.grades.values():
            self.mean_grades += sum(grade)/len(grade)
        res = f'Имя: {self.name}\n' f'Фамилия: {self.surname}\n' f'Средняя оценка за лекции: {round(self.mean_grades,1)}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        else:
            return self.mean_grades < other.mean_grades
    def __gt__(self, other):
        if not isinstance(other, Student):
            return
        else:
            return self.mean_grades > other.mean_grades    

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
        return res
def mean_grades_stud(student_list, course):
    for student in student_list:
        if course in student.courses_in_progress:
            all_grades_stud.append(sum(student.grades[course]))
    print(sum(all_grades_stud) / len(all_grades_stud))

def mean_grades_lect(lecturers_list, course):
    for lecturer in lecturers_list:
        if course in lecturer.courses_attached:
            all_grades_lect.append(sum(lecturer.grades[course]) / len(lecturer.grades[course]))
    print(sum(all_grades_lect) / len(all_grades_lect))

student1 = Student('Иван', 'Иванов', 'M')
student2 = Student('Мария', 'Петрова', 'F')
lecturer1 = Lecturer('Михаил', 'Андреев')
lecturer2 = Lecturer('Кирилл', 'Сидоров')
reviewer1 = Reviewer('Марина', 'Власова')
reviewer2 = Reviewer('Ангелина', 'Иванова')

student1.finished_courses = ['Git']
student1.courses_in_progress = ['Python']

student2.finished_courses = ['UX']
student2.courses_in_progress = ['Html']


lecturer1.courses_attached = ['Python']
lecturer2.courses_attached = ['Html']

reviewer1.courses_attached = ['Python']
reviewer2.courses_attached = ['Html']

student1.rate_lect(lecturer1,'Python',9)
student2.rate_lect(lecturer2,'Html',8)

reviewer1.rate_hw(student1,'Python',10)
reviewer2.rate_hw(student2,'Html',7)


mean_grades_stud(all_students, 'Python')
mean_grades_lect(all_lecturers, 'Html')

# print(student1)
# print(student2)
# print(lecturer1)
# print(lecturer2)
# print(reviewer1)
# print(reviewer2)

