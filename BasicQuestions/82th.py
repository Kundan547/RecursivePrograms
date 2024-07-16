from typing import List, Optional, Dict

class Student:
    def __init__(self, name: str):
        self.name = name
        self.subjects: Dict[str, 'Teacher'] = {}

    def assign_subject(self, subject: str, teacher: 'Teacher'):
        self.subjects[subject] = teacher

class Teacher:
    def __init__(self, name: str, subjects: Optional[List[str]] = None):
        self.name = name
        self.subjects = subjects or []
        self.students: Dict[str, List[Student]] = {subject: [] for subject in self.subjects}
    
    def add_subject(self, subject: str) -> None:
        if subject not in self.subjects:
            self.subjects.append(subject)
            self.students[subject] = []

    def remove_subject(self, subject: str) -> None:
        if subject in self.subjects:
            self.subjects.remove(subject)
            del self.students[subject]

    def assign_student(self, student: Student, subject: str) -> None:
        if subject in self.subjects:
            self.students[subject].append(student)
            student.assign_subject(subject, self)

class HeadOfDepartment:
    def __init__(self, name: str, subject: str):
        self.name = name
        self.subject = subject

class Department:
    def __init__(self, name: str, head_of_department: HeadOfDepartment):
        self.name = name
        self.head_of_department = head_of_department
        self.teachers: List[Teacher] = []
        self.students: List[Student] = []

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_student(self, student: Student):
        self.students.append(student)

    def assign_student_to_subject(self, student: Student, subject: str):
        for teacher in self.teachers:
            if subject in teacher.subjects:
                teacher.assign_student(student, subject)
                break
        else:
            print(f"No teacher found for subject: {subject} in department: {self.name}")

class Program:
    def __init__(self, name: str):
        self.name = name
        self.departments: List[Department] = []

    def add_department(self, department: Department):
        self.departments.append(department)

class University:
    def __init__(self, name: str):
        self.name = name
        self.programs: List[Program] = []

    def add_program(self, program: Program):
        self.programs.append(program)

    def print_data(self):
        print(f"University: {self.name}")
        for program in self.programs:
            print(f"\nProgram: {program.name}")
            for department in program.departments:
                print(f"  Department: {department.name}")
                print(f"  Head of Department: {department.head_of_department.name}")
                print("  Teachers and their students:")
                for teacher in department.teachers:
                    print(f"\n    Teacher: {teacher.name}")
                    for subject, students in teacher.students.items():
                        print(f"      Subject: {subject}")
                        for student in students:
                            print(f"        - {student.name}")

# Example usage
def main():
    # Create a university
    university = University("Medicaps University")

    # Create a program
    cs_program = Program("Computer Science")
    university.add_program(cs_program)

    # Create a department
    hod = HeadOfDepartment("Dr. Vinayak", "Computer Science")
    cs_department = Department("Computer Science", hod)
    cs_program.add_department(cs_department)

    # Create teachers
    teacher1 = Teacher("Prof. Kunal", ["Programming", "Databases"])
    teacher2 = Teacher("Dr. Vikram", ["Blockchain", "Cybersecurity"])

    # Add teachers to the department
    cs_department.add_teacher(teacher1)
    cs_department.add_teacher(teacher2)

    # Create students
    students = [Student(f"Student_{i}") for i in range(1, 6)]
    for student in students:
        cs_department.add_student(student)

    # Assign students to subjects
    subjects = ["Programming", "Databases", "Blockchain", "Programming", "Databases"]
    for student, subject in zip(students, subjects):
        cs_department.assign_student_to_subject(student, subject)

    # Print the data
    university.print_data()

if __name__ == "__main__":
    main()