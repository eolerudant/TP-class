from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = defaultdict(list)
        

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def add_grade(self, topic: str, grade: float) -> None:
        if not (0 <= grade <= 20):
            raise ValueError("grade must be between 0 and 20")
        self.grades[topic].append(grade)
    
    #def followed_topics():
       # return
        

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
except Exception as e:
    print('OOPS - There is an issue in your add_grade method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')

