from tkinter import *
from random import *

class Quiz:
    def __init__(self, parent):
        self.parent = parent

        self.question_text = "What is the capital\nof Mongolia?"
        self.correct_answer = "Ulaanbaatar"
        self.answers = ["Ulaanbaatar", "Astana", "Lhasa", "Vladivostok"]
        shuffle(self.answers)

        self.question_title = Label(self.parent, text="Question:")
        self.question_title.grid(row=0, column=0)

        self.question = Label(self.parent, text=self.question_text)
        self.question.grid(row=0, column=1, sticky=W)

        self.answer_var = StringVar()
        self.answer_var.set(None)

        for i, answer in enumerate(self.answers):
            ans = Radiobutton(self.parent,
                              variable=self.answer_var,
                              value=answer,
                              text=answer,
                              command=self.display_answer)
            ans.grid(row=i + 1, column=1, sticky=W)

        self.result = Label(self.parent, text="", font=("Helvetica bold", 20))
        self.result.grid(row=len(self.answers) + 1, column=1, columnspan=3)

        
    def display_answer(self):
        if self.answer_var.get():
            if self.answer_var.get() == self.correct_answer:
                self.result.configure(text="Correct!")
            else:
                self.result.configure(text="Incorrect!")


root = Tk()
root.geometry("200x180")
quiz = Quiz(root)
root.mainloop()