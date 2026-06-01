from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, background="white", highlightbackground=THEME_COLOR)
        self.question_text = self.question_canvas.create_text(150, 125,
                                                              width=280,
                                                              text="[Insert Text]",
                                                              font=("Arial", 20, "italic"),
                                                              fill="black")
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.true_selection)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightbackground=THEME_COLOR, highlightthickness=0, command=self.false_selection)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.configure(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You've Reached the end of the quiz.\n"
                                                                     f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_selection(self):
        is_right = self.quiz.check_answer("True")
        self.user_feedback(is_right)


    def false_selection(self):
        is_right = self.quiz.check_answer("False")
        self.user_feedback(is_right)



    def user_feedback(self, is_right):
        if is_right:
            self.question_canvas.configure(background="green")
            self.score_label.configure(text=f"Score: {self.quiz.score}")
        else:
            self.question_canvas.configure(background="red")

        self.window.after(2000, self.get_next_question)