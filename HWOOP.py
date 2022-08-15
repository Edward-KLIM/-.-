class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

        #  Блок выставления оценки Лекторам.

    def rete_lc(self,lecturer,course,grade):
      if isinstance (lecturer,Lecturer) and course in lecturer.courses_attaached and course in self.courses_in_progress:
        if course in lecturer.grades:
          lecturer.grades[course] += [grade]
        else:
          lecturer.grades[course] = [grade]
      else:
        return "Ошибка"     
        #  Блок расчет средней оценки студента за ДЗ. 
    def student_grade (self):
      self.stud_grade = [grade for grades in self.grades.values() for grade in grades]
      if self.stud_grade:
        self.midl_grade = (sum(self.stud_grade)/len(self.stud_grade)) 
        return self.midl_grade
      else:
        print ("Пока нет оценок")

        #  Блок сравнения среднего балла у студента. 
  
    def __eq__(self, other):
        if not isinstance (other,Student):
          print ("Ошибка : сравнивать можно только студентов")
          return
        elif isinstance (self,Student):
          return self.student_grade() == other.student_grade

    def __lt__(self, other):
        if not isinstance (other,Student):
          print ("Ошибка : сравнивать можно только студентов")
          return
        elif isinstance (self,Student):
          return self.student_grade() < other.student_grade

    def __gt__(self, other):
        if not isinstance (other,Student):
          print ("Ошибка : сравнивать можно только студентов")
          return
        elif isinstance (self,Student):
          return self.student_grade() < other.student_grade 

        #  Блок вывод на экран информации о студенте.


    def __str__(self):
        return (f"Имя Студента: {self.name} \nФамилия Студента: {self.surname} \nСредний балл за ДЗ : {self.student_grade()} \nКурсы в процессе изучени:{self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses} ")

class Mentor:
  def __init__(self,name,surname,):
    self.name = name
    self.surname = surname
    self.courses_attached = []

class Reviewer(Mentor):
  def __init__(self,name,surname,):
    super(). __init__(name,surname,)
    self.courses_attaached = []

        # Блок выставления оценки Студентам.
  
  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  


        # Блок вывод на экран информации о Ревьюерe.

  def __str__(self):
    return f" Имя и Фамилия Ревьюера :{self.name} {self.surname}"

class Lecturer(Mentor):
  def __init__(self,name,surname,):
    super(). __init__(name,surname,)
    self.courses_attaached = []
    self.lecturer_grade = {}

        # Блок расчет средней оценки у Лекторов.

  def lectur_grade (self):
    self.lect_grade = [grade for grades in self.grades.values() for grade in grades]
    if self.lect_grade:
      self.midl_grade_lect = (sum(self.lect_grade)/len(self.lect_grade)) 
      return self.midl_grade_lect
    else:
      print ("Пока нет оценок")
      
        # Блок сравнения среднего балла у Лекторов.


  def __eq__(self, other):
        if not isinstance (other,Lecturer):
          print ("Ошибка : сравнивать можно только Лекторов")
          return
        elif isinstance (self,Lecturer):
          return self.lector_grades() == other.lector_grades

  def __lt__(self, other):
        if not isinstance (other,Lecturer):
          print ("Ошибка : сравнивать можно только Лекторов")
          return
        elif isinstance (self,Lecturer):
          return self.lector_grades() < other.lector_grades

  def __gt__(self, other):
        if not isinstance (other,Lecturer):
          print ("Ошибка : сравнивать можно только Лекторов")
          return
        elif isinstance (self,Lecturer):
          return self.lector_grades() > other.lector_grades
  
        # Блок вывод на экран информации о Лекторах.
  
  def __str__(self):
    return (f"Имя Лектора: {self.name} \nФамилия Лектора: {self.surname} \nСредний балл : {self.lecturer_grade}")

        # Список студентов.  

Student1 = Student("Maria","Petrova","woman")
Student1.courses_in_progress += ["Python"]
Student1.courses_in_progress += ["Java"]
Student1.finished_courses += ["Git"]

Student2 = Student("Emma","Still","woman")
Student2.courses_in_progress += ["Git"]
Student2.courses_in_progress += ["Java"]
Student2.finished_courses += ["Python"]

Student3 = Student("Ruoy","Jo","man")
Student3.courses_in_progress += ["Python"]
Student3.courses_in_progress += ["Git"]
Student3.finished_courses += ["Java"]

        # Список Лекторов.


Lecturer1 = Lecturer ("Max","Brown")
Lecturer1.courses_attached += ["Java"]
Lecturer2 = Lecturer ("Rita", "Smirnova")
Lecturer2.courses_attached += ["Python"]
Lecturer3 = Lecturer ("Tim","Jonson")
Lecturer3.courses_attached += ["Git"]

        # Список Ревьюеров.

Reviewer1 = Reviewer ("Bill","Stoke")
Reviewer1.courses_attached += ["Java"]
Reviewer2 = Reviewer ("Eddy","Koks")
Reviewer2.courses_attached += ["Git"]
Reviewer3 = Reviewer ("Edward","Well")
Reviewer3.courses_attached += ["Python"]

        # Оценка студентов за ДЗ.

Reviewer1.rate_hw(Student2,"Java",7)
Reviewer1.rate_hw(Student2,"Java",7)
Reviewer1.rate_hw(Student2,"Java",8)

Reviewer1.rate_hw(Student1,"Java",10)
Reviewer1.rate_hw(Student1,"Java",10)
Reviewer1.rate_hw(Student1,"Java",9)

Reviewer2.rate_hw(Student2,"Git", 5)
Reviewer2.rate_hw(Student2,"Git", 10)
Reviewer2.rate_hw(Student2,"Git", 10)

Reviewer2.rate_hw(Student3,"Git", 6)
Reviewer2.rate_hw(Student3,"Git", 6)
Reviewer2.rate_hw(Student3,"Git", 9)


Reviewer3.rate_hw(Student1,"Python",8)
Reviewer3.rate_hw(Student1,"Python",10)
Reviewer3.rate_hw(Student1,"Python",9)

Reviewer3.rate_hw(Student3,"Python",7)
Reviewer3.rate_hw(Student3,"Python",10)
Reviewer3.rate_hw(Student3,"Python",10)

      # Оценка Лекторам за лекцию.

Student1.rete_lc(Lecturer2,"Python",7)
Student1.rete_lc(Lecturer2,"Python",8)
Student1.rete_lc(Lecturer2,"Python",10)  

Student2.rete_lc(Lecturer3,"Git",6)
Student2.rete_lc(Lecturer3,"Git",10)
Student2.rete_lc(Lecturer3,"Git",10)

Student3.rete_lc(Lecturer1,"Java",9)
Student3.rete_lc(Lecturer1,"Java",10)
Student3.rete_lc(Lecturer1,"Java",9)

print (f'Список студентов и средний бал за Домашнее задание по их курсу: \n{Student1} \n{Student2} \n{Student3}')

print (f'Список проверяющих Домашние задания : \n{Reviewer1} \n{Reviewer2} \n{Reviewer3}')

print (f' Список Лекторов и средние оценки за лекцию : \n{Lecturer1} \n{Lecturer1} \n{Lecturer3} ')
