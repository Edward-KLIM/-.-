Student_list = ["Maria Ptrova","Emma Still","Ruoy Jo","Jim Brown"]
Courses_list = ["Python","Git","Java"]



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
class Mentor:
  def __init__(self,name,surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
    
class Reviewer(Mentor):
  def __init__(self,name,surname,grades):
    super(). __init__(name,surname)
    self.courses_attached = []
    self.grades = {}

  def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Возникла Ошибка'  

class Lecturer(Mentor):
  def __init__(self,name,surname):
    super(). __init__(name,surname)
    self.courses_attached = []
    self.lecture_grades = {}

  def rete_lecture(self,lectures,student,course,grade):
    if isinstance (lectures,Lecturer) and course in self.courses_attached and course in student.courses_in_progress:
      if course in lectures.grades:
        lectures.grades[course] += [grade]
      else:
        lectures.grades[course] = [grade]
    else:
      return 'Возникла Ошибка'

L = Lecturer
print(L.rete_lecture)  
