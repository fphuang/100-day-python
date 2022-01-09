class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def display(self):
        print(f"question: {self.text}, answer: {self.answer}")


