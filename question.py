class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.__correct_answer = correct_answer

    def display_question(self, number):
        print(f"\nQ{number}. {self.question}")

        for option, value in self.options.items():
            print(f"{option}. {value}")

    def check_answer(self, answer):
        return answer.upper() == self.__correct_answer
