print("------ STUDENT MANAGEMENT SYSTEM --------")


class Student:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll = input("ENTER ROLL NUMBER: ")
        name = input("ENTER NAME: ")

        subjects = ["maths", "physics", "biology", "social"]
        marks = {}

        for sub in subjects:
            while True:
                try:
                    mark = int(input(f"ENTER MARKS FOR {sub.upper()}: "))
                    if 0 <= mark <= 100:
                        marks[sub] = mark
                        break
                    else:
                        print("Enter marks between 0 and 100")
                except:
                    print("Invalid input. Enter numbers only.")

        student = Student(roll, name, marks)
        self.students.append(student)
        print("STUDENT ADDED SUCCESSFULLY")

    
    def calculate_grade(self, avg):
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"

    
    def view_student(self):
        if not self.students:
            print("NO STUDENTS AVAILABLE")
            return

        for s in self.students:
            print("\nROLL:", s.rollno)
            print("NAME:", s.name)

            total = sum(s.marks.values())
            avg = total / len(s.marks)
            grade = self.calculate_grade(avg)

            print("MARKS:")
            for sub, mark in s.marks.items():
                print(f"  {sub}: {mark}")

            print("TOTAL:", total)
            print("AVERAGE:", round(avg, 2))
            print("GRADE:", grade)

    
    def search_student(self):
        roll = input("ENTER ROLL NUMBER: ")
        for s in self.students:
            if s.rollno == roll:
                print("\nSTUDENT FOUND")
                print("ROLL NUMBER:", s.rollno)
                print("NAME:", s.name)

                total = sum(s.marks.values())
                avg = total / len(s.marks)
                grade = self.calculate_grade(avg)

                print("MARKS:")
                for sub, mark in s.marks.items():
                    print(f"  {sub}: {mark}")

                print("TOTAL:", total)
                print("AVERAGE:", round(avg, 2))
                print("GRADE:", grade)
                return

        print("STUDENT NOT FOUND")

    
    def delete_student(self):
        roll = input("ENTER THE ROLL NUMBER: ")
        for s in self.students:
            if s.rollno == roll:
                self.students.remove(s)
                print("STUDENT DELETED SUCCESSFULLY")
                return
        print("STUDENT NOT FOUND")


shankar = StudentManagement()

while True:
    print("\n------ MENU ------")
    print("1. ADD STUDENT")
    print("2. VIEW STUDENT")
    print("3. SEARCH STUDENT")
    print("4. DELETE STUDENT")
    print("5. EXIT")

    choice = input("ENTER CHOICE: ")

    if choice == "1":
        shankar.add_student()
    elif choice == "2":
        shankar.view_student()
    elif choice == "3":
        shankar.search_student()
    elif choice == "4":
        shankar.delete_student()
    elif choice == "5":
        print("EXITING... THANK YOU!")
        break
    else:
        print("INVALID CHOICE")
