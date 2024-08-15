class Student:
# Атрибуты студента    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
# Оценка лекторов
    def rate_lecturer(self, lecturer, course, grade):
        if not(0 <= grade <=10):
            return 'Ошибка: Оценка должна быть от 0 до 10'
        if not isinstance(lecturer, Lecturer):
           return 'Ошибка: Лектор не найден' 
        if course not in lecturer.courses_attached:
            return 'Ошибка: Курс не приклеплен к лектору'
        if course not in self.finished_courses and course not in self.courses_in_progress:
            return 'Ошибка: Курс не найден у студента'       
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and grade in range(0, 11)
            and (course in self.finished_courses or course in self.courses_in_progress)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
# Расчет средней оценки  
    def average_hw(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return f'{sum(all_grades) / len(all_grades):.2f}' if all_grades else 'Нет оценок'

# Сравнение
    def __gt__(self, student):
        return self.average_hw() > student.average_hw()
# Вывод строки
    def __str__(self):
        result = f'Имя: \033[31m{self.name}\033[0m\n'
        result += f'Фамилия: \033[31m{self.surname}\033[0m\n'
        result += f'Средняя оценка за домашние задания: \033[34m{self.average_hw()}\033[0m\n'
        result += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        result += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return result

class Mentor:
# Атрибуты преподавателя
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):
# Расчет средней оценки    
    def average_lect(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return f'{sum(all_grades) / len(all_grades):.2f}' if all_grades else 'Нет оценок'

# Сравнение
    def __gt__(self, lecturer):
        return self.average_lect() > lecturer.average_lect()
# Вывод строки
    def __str__(self):
        result = f'Имя: \033[31m{self.name}\033[0m\n'
        result += f'Фамилия: \033[31m{self.surname}\033[0m\n'
        result += f'Средняя оценка за лекции: \033[34m{self.average_lect()}\033[0m\n'
        return result

class Reviewer (Mentor):
# Оценка студентов   
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and grade in range(0, 11)
            and (course in student.finished_courses or course in student.courses_in_progress)):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
# Вывод строки            
    def __str__(self):
        result = f'Имя: \033[31m{self.name}\033[0m\n'
        result += f'Фамилия: \033[31m{self.surname}\033[0m\n'
        return result

# Функция расчета средней оценки по студентам или лекторам на курсе

def average_grades(person_list, course):
    sum_grades = 0
    count_grades = 0
    for person in person_list:
        if course in person.grades.keys():
            for grades in person.grades[course]:
                sum_grades += grades
                count_grades += 1
    if count_grades > 0:
        return f'{sum_grades / count_grades:.2f}'
    else:
        return f'Нет оценок'
# def average_grades(person_list, course):
#     for person in person_list:
#         all_grades = [grade for grades in person.grades[course] for grade in grades]
#         return f'{sum(all_grades) / len(all_grades):.2f}' if all_grades else 'Нет оценок'
# Ввод данных   
     
courses_list=['Введение в программирование', 'Python', 'GIT']

student_1 = Student('Ruoy', 'Eman', 'Male')
student_1.finished_courses.append(courses_list[0])
student_1.courses_in_progress.append(courses_list[1])
student_1.courses_in_progress.append(courses_list[2])

student_2 = Student('Helen', 'Eman', 'Female')
student_2.finished_courses.append(courses_list[0])
student_2.courses_in_progress.append(courses_list[1])
student_2.courses_in_progress.append(courses_list[2])

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached.append(courses_list[0])
lecturer_1.courses_attached.append(courses_list[1])
lecturer_1.courses_attached.append(courses_list[2])
lecturer_2 = Lecturer('Nick', 'Buddy')
lecturer_2.courses_attached.append(courses_list[1])
lecturer_2.courses_attached.append(courses_list[2])

reviewer_1 = Reviewer('Aleks', 'First')
reviewer_1.courses_attached.append(courses_list[0])
reviewer_1.courses_attached.append(courses_list[1])
reviewer_1.courses_attached.append(courses_list[2])

reviewer_2 = Reviewer('Boris', 'Second')
reviewer_2.courses_attached.append(courses_list[0])
reviewer_2.courses_attached.append(courses_list[1])
reviewer_2.courses_attached.append(courses_list[2])

student_1.rate_lecturer(lecturer_1, courses_list[0], 10)
student_2.rate_lecturer(lecturer_1, courses_list[0], 9)
student_1.rate_lecturer(lecturer_2, courses_list[1], 8)
student_2.rate_lecturer(lecturer_2, courses_list[1], 9)
student_1.rate_lecturer(lecturer_2, courses_list[2], 8)
student_2.rate_lecturer(lecturer_2,courses_list[2], 8)

reviewer_1.rate_hw(student_1, courses_list[0], 9)
reviewer_2.rate_hw(student_2, courses_list[0], 10)
reviewer_1.rate_hw(student_1, courses_list[1], 7)
reviewer_1.rate_hw(student_2, courses_list[1], 8)
reviewer_2.rate_hw(student_1, courses_list[2], 9)
reviewer_2.rate_hw(student_2, courses_list[2], 9)

# Тестирование

print('Проверяющие:')
print(reviewer_1)
print(reviewer_2)

print('Лекторы:')
print(lecturer_1)
print(lecturer_2)

if lecturer_1 > lecturer_2:
    print(f'Лектор \033[31m{lecturer_1.name} {lecturer_1.surname}\033[0m лучший.\n')
else:
    print(f'Лектор \033[31m{lecturer_2.name} {lecturer_2.surname}\033[0m лучший.\n')

print('Студенты:')
print(student_1)
print(student_2)

if student_1 > student_2:
    print(f'Студент \033[31m{student_1.name} {student_1.surname}\033[0m лучший.\n')
else:
    print(f'Студент \033[31m{student_2.name} {student_2.surname}\033[0m лучший.\n')

student_list = [student_1, student_2]

for curses in courses_list:
    print(f'Средняя оценка за домашние задания у студентов на курсе {curses}: '
    f'\033[34m{average_grades(student_list, curses)}\033[0m')
print('')

lecturer_list = [lecturer_1, lecturer_2]

for curses in courses_list:
    print(f'Средняя оценка за лекции у лекторов на курсе {curses}: \033[34m{average_grades(lecturer_list, curses)}\033[0m')
