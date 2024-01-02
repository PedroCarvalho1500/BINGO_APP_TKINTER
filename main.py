import sqlite3
import time
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#0D0D0D"
timer = None
current_french_word = ""



     
    

class Application():
    def __init__(self, window):
        self.drawn_numbers_labels = []
        self.labels_created = []
        self.current_number = 0
        self.current_label_pos = 0
        self.at_least_one_drawn = False
        self.x_position = 0.006
        self.y_position = 0.02
        #screen_functions = ScreenFunctions()
        self.main_window = window
        self.main_window.title("BINGO")
        self.main_window.config(background=BACKGROUND_COLOR, height=800, width=1400)
        self.main_window.resizable(True,True)
        self.bingo_canvas()
        self.load_buttons()
        
        
        self.main_window.mainloop()

    def start_new_draw(self):
        self.drawn_numbers_labels = []
        self.canvas.itemconfig(self.canvas_text, text="SORTEAR", fill="white", font=('Arial', 15, "bold"))
        self.x_position = 0.006
        self.y_position = 0.02
        self.current_label_pos = 0
        self.at_least_one_drawn = False
        self.clean_labels()

    def draw_number(self):
        #print(len(self.drawn_numbers_labels))
        if len(self.drawn_numbers_labels) == 90:
            self.canvas.itemconfig(self.canvas_text, text='NÚMERO \nMÁXIMO \nATINGIDO', font=('Arial', 15, "bold"))

        else:
            while(self.current_number in self.drawn_numbers_labels or self.at_least_one_drawn == False):
                self.current_number = random.randint(1,90)
                self.current_number = random.randint(1,90)
                self.at_least_one_drawn = True

            self.canvas.itemconfig(self.canvas_text, text=str(self.current_number), font=('Arial', 75, "bold"))
            #print(self.current_number)
            self.drawn_numbers_labels.append(self.current_number)
            self.load_labels()


    def load_buttons(self):
        self.draw_bt = Button(text="Sortear Número", background="gray80", foreground='black', activebackground='blue', activeforeground='white', command=lambda: self.draw_number())
        self.draw_bt.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.09)

        self.quit_bt = Button(text="Fechar", background="gray80", foreground='black', activebackground='blue', activeforeground='white', command=lambda: self.main_window.destroy())
        self.quit_bt.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.09)

        self.begin_new_draw_button = Button(text="Iniciar Novo Sorteio", background="gray30", foreground='black', activebackground='green', activeforeground='white', command=lambda: self.start_new_draw())
        self.begin_new_draw_button.place(relx=0.73, rely=0.55, relwidth=0.2, relheight=0.09)

    def bingo_canvas(self):
        self.canvas = Canvas(width=700, height=230, highlightthickness=0, background='#0D0D0D')
        self.circle_img = PhotoImage(file="circle.png")
        self.id_img = self.canvas.create_image(260,270, image=self.circle_img)
        self.canvas.place(relx=0.65, rely=0.01, relwidth=0.4, relheight=0.7)

        self.canvas_text = self.canvas.create_text(250, 260, text="SORTEAR", fill="white", font=('Arial', 15, "bold"))

    def load_labels(self):
        for current_drawn_number in range(self.current_label_pos,len(self.drawn_numbers_labels)):
            new_label = Label(text=str(self.current_number),font=('Arial', 12, "bold"))
            new_label.place(relx=self.x_position, rely=self.y_position, relwidth=0.04, relheight=0.04)
            self.labels_created.append(new_label)

            if(self.x_position >= 0.5):
                self.y_position+=0.07
                self.x_position = 0.006
                
            else: self.x_position+=0.05
        
        self.current_label_pos+=1

    def clean_labels(self):
        for label in self.labels_created:
            label.destroy()
        self.labels_created = []

            
            



if __name__ == '__main__':
    new_window = Tk()
    Application(new_window)
    