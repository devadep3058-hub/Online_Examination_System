
from question import Question
from exam import Exam


def main():

    # Python Examination Questions
    python_questions = [
        Question(
            "Who developed Python?",
            {
                "A": "James Gosling",
                "B": "Guido van Rossum",
                "C": "Dennis Ritchie",
                "D": "Bjarne Stroustrup"
            },
            "B"
        ),

        Question(
            "Which keyword is used to define a function in Python?",
            {
                "A": "function",
                "B": "define",
                "C": "def",
                "D": "fun"
            },
            "C"
        ),

        Question(
            "Which data type is used to store True or False?",
            {
                "A": "Integer",
                "B": "String",
                "C": "Float",
                "D": "Boolean"
            },
            "D"
        ),

        Question(
            "Which symbol is used for comments in Python?",
            {
                "A": "#",
                "B": "//",
                "C": "/*",
                "D": "&"
            },
            "A"
        ),

        Question(
            "Which function is used to display output in Python?",
            {
                "A": "input()",
                "B": "print()",
                "C": "display()",
                "D": "show()"
            },
            "B"
        )
    ]

    # Create Examination
    python_exam = Exam("Python Programming", python_questions)

    print("\n================================")
    print("    ONLINE EXAMINATION SYSTEM")
    print("================================")

    student_name = input("Enter Student Name: ").strip()

    if not student_name:
        print("Student name cannot be empty.")
        return

    while True:
        print("\n1. Start Examination")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            python_exam.conduct_exam(student_name)
            break

        elif choice == "2":
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
