from abc import ABC, abstractmethod


class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        return answer.strip().lower() == self.correct_answer.strip().lower()


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = bool(correct_answer)

    def evaluate_answer(self, answer):
        return answer.strip().lower() in ("true", "false") and (answer.strip().lower() == str(self.correct_answer).lower())


class DescriptiveQuestion(Question):
    def __init__(self, keywords):
        self.keywords = keywords

    def evaluate_answer(self, answer):
        answer = answer.lower()
        return all(keyword.lower() in answer for keyword in self.keywords)


print("MCQ correct:", MCQQuestion("Python").evaluate_answer("Python"))
print("True/False correct:", TrueFalseQuestion(True).evaluate_answer("true"))
print("Descriptive answer acceptable:", DescriptiveQuestion(["inheritance", "class"]).evaluate_answer("Inheritance allows a class to reuse another class."))
