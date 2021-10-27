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
    def rating(self):
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
               f'Средняя оценка за домашнии задания: {self.rating()} \n' \
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
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.medium_grades()}'

# сравнение лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не можем сравнить!')
            return
        return self.medium_grades() < other.medium_grades()

    def medium_grades(self):
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
first_student = Student('Ruoy', 'Eman', 'boy')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Введение в программирование']

# студент_2
second_student = Student('Bob', 'Grenn', 'girl')
second_student.courses_in_progress += ['Geology']

# проверяющий_1
first_reviewer = Reviewer('Svetlana', 'Pletneva')
first_reviewer.courses_attached += ['Python']

# проверяющий_2
second_reviewer = Reviewer('Some', 'Buddy')
second_reviewer.courses_attached += ['Python']
second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(first_student, 'Python', 10)
second_reviewer.rate_hw(second_student, 'Geology', 8)

# лектор_1
first_lecturer = Lecturer('Artur', 'Red')

# лектор_2
second_lecturer = Lecturer('Sam', 'Smith')
second_lecturer.courses_attached += ['Geology']

# оцениваем лектора_2
second_student.grade_for_lectur(second_lecturer, 'Geology', 9)
second_student.grade_for_lectur(second_lecturer, 'Geology', 8)


print(second_reviewer, '\n')
print(second_lecturer, '\n')
print(first_student, '\n')

print(first_lecturer < second_lecturer)
print(second_lecturer < first_lecturer)






