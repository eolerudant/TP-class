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
    
    def followed_topics(self):
       return list(self.grades.keys())
    
    def compute_average(self, topic: str) -> float:
        S=0
        if topic not in self.grades or len(self.grades[topic]) == 0 :
            return -1
        else :
            for note in self.grades[topic] :
                S+= note
        return S/len(self.grades[topic])

    def report(self):
        report_lines =[]
        header = f"Report for student {self.first_name} {self.last_name}"
        report_lines.append(header)
        report_lines.append("+===============+===============+")
        report_lines.append("|     Topic     |    Average    |")
        report_lines.append("+===============+===============+")
        
        for topic in self.followed_topics():
            average = self.compute_average(topic)
            report_lines.append(f"|  {topic:<13}|    {average:>6.2f}     |") # Format topic left-aligned in 13 spaces, average right-aligned in 6 spaces with 2 decimals
            report_lines.append("+---------------+---------------+")
        
        return "\n".join(report_lines)
    

    
    
        


