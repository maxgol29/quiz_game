from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")

        self.text = self.canvas.create_text(150, 125, width = 300, text="Hello", font=("Arial", 20, "italic"))

        self.canvas.grid(row=1, columnspan=2, column=0, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.config(pady=10, padx=10)
        self.score_label.grid(row=0, column=1)

        self.buttons()

        self.next_question()

        self.window.mainloop()


    def buttons(self):

        self.right_btn_img = PhotoImage(file="images/true.png")
        self.wrong_btn_img = PhotoImage(file="images/false.png")

        self.right_btn = Button(image=self.right_btn_img, highlightthickness=0, command=self.correct)
        self.right_btn.grid(row=2, column=0)

        self.wrong_btn = Button(image=self.wrong_btn_img, highlightthickness=0, command=self.wrong)
        self.wrong_btn.grid(row=2, column=1)

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def wrong(self):
        if self.quiz.check_answer("False"):
            self.score_label.config(text=f"Score: {self.quiz.score}")
        self.next_question()

    def correct(self):
        if self.quiz.check_answer("True"):
            self.score_label.config(text=f"Score: {self.quiz.score}")
        self.next_question()