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
