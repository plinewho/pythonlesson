# импортируем класс
class Student:
    students = []

    def __init__(self, name, secondname, course, score):
        self.__name = name
        self.__secondname = secondname
        self.__course = course
        self.__score = score

    @property
    def name(self):
        return self.__name
    @property
    def secondname(self):
        return self.__secondname
    @property
    def course(self):
        return self.__course
    @property
    def score(self):
        return self.__score

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

    @staticmethod
    def print_info(obj):
        print('-------------------')
        print('ФИ:', obj.name, obj.secondname)
        print('Курс:', obj.course)
        print('Средний бал:', obj.score)
        print('-------------------')

    @classmethod
    def print_students(cls):
        for i in cls.students:
            Student.print_info(i)


    def change_course(self, course):
        self.__course = course

    @classmethod
    def search_student(cls, student):
        for i in cls.students:
            if i.secondname == student:
                print('Найденный студент: ')
                Student.print_info(i)
    


# создаем объекты студентов
student1 = Student("Иван", "Иванов", 3, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student1)
Student.add_student(student2)
Student.add_student(student3)

# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
Student.print_students()

# ищем студента по фамилии
Student.search_student("Иванов")