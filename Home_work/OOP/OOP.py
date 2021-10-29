# Класс студенты
class Student:
    def __init__(self, name, surname, gender):
        self.name = name # имя студента
        self.surname = surname # фамилия студента
        self.gender = gender # пол студента
        self.finished_courses = [] # курсы, которые окончил студент
        self.courses_in_progress = [] # курсы, на которых учится студент
        self.grades = {} # оценки за  ДЗ

# выставление оценок лектору
    def grade_for_lectur(self, lecturer, course, grade):
        # если объект принадлежит классу лектор и курс совпадает с курсом студента и курсом лектора
        if isinstance(lecturer,Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            # если курс есть в словаре курсов лектора, то добавляем значение оценки
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            'Ошибка'

        # подсчет средней оценки студента
    def rating_st(self):
            sum = 0
            quantity = 0
            if len(self.grades) != 0:
                for val in self.grades.values():
                    for grade in val:
                        sum += grade
                        quantity += 1
                        average = sum / quantity
                        return average
            else:
                return 0

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \n' \
               f'Средняя оценка за домашнии задания: {self.rating_st()} \n' \
               f'Курсы в процессе обучения: {self.courses_in_progress} \n' \
               f'Завершённые курсы: {self.finished_courses}'


# Класс преподаватели
class Mentor:
    def __init__(self, name, surname):
        self.name = name # Имя преподавателя
        self.surname = surname # Фаимилия преподавателя

# Инициализируем дочерний класс Lecturer (читают лекции)  и Review (проверяют ДЗ)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []  # Курсы преподавателя
        self.grades = {}


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.raiting_lec()}'

# сравнение лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не можем сравнить!')
            return
        return self.raiting_lec() < other.raiting_lec()

    def raiting_lec(self):
        sum = 0
        quantity = 0
        if len(self.grades) != 0:
            for val in self.grades.values():
                for grade in val:
                    sum += grade
                    quantity += 1
                    average = sum / quantity
                return average
        else:
            return 0
    def average_raiting_lec(self):
        sum_lec = 0
        count = 0
        for course in self.grades.values():
            sum_lec += sum(course)
            count += len(course)
        return round(sum_lec/count,2)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \n Фамилия: {self.surname} \n'



# студент_1
first_student = Student('Иван', 'Иванов', 'муж')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Введение в программирование']

# студент_2
second_student = Student('Анна', 'Васильевна', 'жен')
second_student.courses_in_progress += ['Geology']

# проверяющий_1
first_reviewer = Reviewer('Сетлана', 'Плетнева')
first_reviewer.courses_attached += ['Python']

# проверяющий_2
second_reviewer = Reviewer('Петр', 'Петров')
second_reviewer.courses_attached += ['Python']
second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Geology', 8)

# лектор_1
first_lecturer = Lecturer('Гарри', 'Поттер')
first_lecturer.courses_attached += ['Python']

# лектор_2
second_lecturer = Lecturer('Гермиона', 'Уизли')
second_lecturer.courses_attached += ['Geology']

# оцениваем лектора_1
first_student.grade_for_lectur(second_lecturer, 'Python', 9)
first_student.grade_for_lectur(second_lecturer, 'python', 8)


# оцениваем лектора_2
second_student.grade_for_lectur(second_lecturer, 'Geology', 9)
second_student.grade_for_lectur(second_lecturer, 'Geology', 8)


student_list = [first_student, second_student]
lecturer_list = [first_lecturer, second_lecturer]
reviewer_list = [first_reviewer, second_reviewer]

def student_average_grade(student_list, course_name):
  for student in student_list:
    if course_name in student.courses_in_progress:
      if course_name in student.grades:
        all_course_grade = []
        avg = sum(student.grades.get(course_name)) / len(student.grades.get(course_name))
        all_course_grade.append(avg)
  all_avg = sum(all_course_grade) / len(all_course_grade)
  res = print(f'Средний балл за ДЗ по курсу {course_name} = {round(all_avg, 2)}')
  return res

def lecturer_average_grade(lecturer_list, course_name):
  for lecturer in lecturer_list:
    if course_name in lecturer.courses_attached:
      if course_name in lecturer.grades:
        all_course_grade = []
        avg = sum(lecturer.grades.get(course_name)) / len(lecturer.grades.get(course_name))
        all_course_grade.append(avg)
  all_avg = sum(all_course_grade) / len(all_course_grade)
  res = print(f'Средний балл за лекции по курсу {course_name} = {round(all_avg, 2)}')
  return res


# Проверка
print(second_reviewer, '\n') #
print(second_lecturer, '\n') #
print(first_student, '\n') #

print(first_lecturer < second_lecturer, '\n') #
print(second_lecturer < first_lecturer, '\n') #

student_average_grade(student_list, 'Python')
lecturer_average_grade(lecturer_list, 'Geology')


