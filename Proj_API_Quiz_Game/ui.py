import tkinter as tk

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI(tk.Tk):
    def __init__(self, quiz_brain: QuizBrain) -> None:
        super().__init__()
        self.title("Quizzler")
        self.quiz = quiz_brain
        self.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_board = tk.Label(
            self, text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white"
        )
        self.score_board.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=270, font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_img = tk.PhotoImage(file=r"images\true.png")
        self.true_button = tk.Button(
            image=self.true_img,
            highlightthickness=0,
            command=lambda: self.answer_button("True"),
        )
        self.true_button.grid(row=2, column=0)

        self.false_img = tk.PhotoImage(file=r"images\false.png")
        self.false_button = tk.Button(
            image=self.false_img,
            highlightthickness=0,
            command=lambda: self.answer_button("False"),
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
        else:
            question_text = f"Your Score was {self.quiz.score}/10"
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.itemconfig(self.question_text, text=question_text)

    def answer_button(self, answer: str):
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="Green")
            self.score_board.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="Red")
        self.after(1000, self.get_next_question)


if __name__ == "__main__":
    window = QuizUI()
    window.mainloop()
