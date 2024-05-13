from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quizzler_ui:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.minsize(height=600,width=400)
        self.window.config(background=THEME_COLOR)


        self.scores = Label(text="Score : 0",font=("arial",12,"bold"),background=THEME_COLOR,foreground="White")
        self.scores.place(x=270,y=20)

        self.canvas = Canvas(height=300,width=340,background="white")
        self.ques = self.canvas.create_text(150,125,text="hello",width=280,fill=THEME_COLOR,font=('Ariel',20,'italic'))
        self.canvas.place(x=30,y=80)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, command=self.true_clicked)
        self.true_btn.place(x=50,y=450)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, command=self.false_clicked)
        self.false_btn.place(x=250,y=450)

        self.get_next_ques()

        self.window.mainloop()


#--------------------------------------------- Functions --------------------------------------------------------#
    def get_next_ques(self):
        self.canvas.config(background='white')

        if self.quiz.still_has_questions():
            current_ques = self.quiz.next_question()
            self.canvas.itemconfig(self.ques,text =f"{current_ques}")
        else:
            self.canvas.itemconfig(self.ques,text = "You have reached to the End of the Quiz.")
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)

    def true_clicked(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        self.scores.config(text=f"Score : {self.quiz.score}")

    def false_clicked(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right :
            self.canvas.config(background="Green")
        else:
            self.canvas.config(background="Red")

        self.window.after(1000,self.get_next_ques)

# get_ques()
# o = Quizzler_ui()
