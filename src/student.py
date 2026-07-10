class Student:
    school_name = "Python AI Learning Center"

    def __init__(self, name, score, attendance):
        self.name = name
        self.score = score
        self.attendance = attendance

    def get_result(self):
        if self.score >= 50:
            return "Pass"
        else:
            return "Fail"

    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"

    def get_risk_level(self):
        if self.score >= 70 and self.attendance >= 80:
            return "Low Risk"
        elif self.score >= 50 and self.attendance >= 60:
            return "Medium Risk"
        else:
            return "High Risk"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Attendance: {self.attendance}%")
        print(f"Result: {self.get_result()}")
        print(f"Grade: {self.get_grade()}")
        print(f"Risk Level: {self.get_risk_level()}")

    def __str__(self):
        return f"{self.name} - Score: {self.score}, Result: {self.get_result()}"
