class Exam:
    def __init__(self, exam_name, questions):
        self.exam_name = exam_name
        self.questions = questions

    def conduct_exam(self, student_name):
        score = 0

        print("\n================================")
        print("       EXAMINATION STARTED")
        print("================================")
        print("Student:", student_name)
        print("Exam:", self.exam_name)

        for i, question in enumerate(self.questions, start=1):
            question.display_question(i)

            answer = input("Enter your answer (A/B/C/D): ").strip().upper()

            while answer not in ["A", "B", "C", "D"]:
                print("Invalid option! Enter A, B, C or D.")
                answer = input("Your answer: ").strip().upper()

            if question.check_answer(answer):
                print("Correct Answer!")
                score += 1
            else:
                print("Incorrect Answer!")

        total = len(self.questions)
        percentage = (score / total) * 100

        print("\n================================")
        print("         EXAM RESULT")
        print("================================")
        print("Student Name:", student_name)
        print("Examination:", self.exam_name)
        print("Total Questions:", total)
        print("Correct Answers:", score)
        print("Wrong Answers:", total - score)
        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

        print("================================")
