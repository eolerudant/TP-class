from student import Student

class Classe:

    def __init__(self, classname: str):
        self.classname = classname
        self.students = []
    def add_student(self, student: Student):
        self.students.append(student)

    def __len__(self):
        return len(self.students)

    def __repr__(self):
        return f"Classe {self.classname} - {self.__len__()} student(s)"

try:
    classe = Classe("P20")
    student = Student("Matthieu", "Mazière")
    classe.add_student(student)
    if len(classe) != 1:
        raise Exception('OOPS - There is an issue in your __len__ method.')
    if repr(classe) != "Classe P20 - 1 student(s)":
        raise Exception('OOPS - There is an issue in your __repr__ method.')
except Exception as e:
    print("OOPS - Something's wrong")
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')