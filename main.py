import tkinter as tk
from tkinter import ttk as ttk
import time
import pyglet
import threading

class Pomodoro:
    def __init__ (self,master):
        font_path = 'PressStart2P-Regular.ttf'
        pyglet.font.add_file(font_path)
        font_name = 'PressStart2P-Regular'
        self.master = master
        master.title  = ("Productivity Jam")

        self.minutes = 0
        self.seconds = 0
        self.running = False
        self.cycles = 2
        self.longBreak  = 0
        self.shortBreak = 0

        self.label1 = tk.Label(master, text="1:00", font=(font_name, 25))
        #tk.Button(master, text="1", comm)
        studyTimer1Button = ttk.Button(master, text="1", command=self.setTime1)
        studyTimer2Button = ttk.Button(master, text="2", command=self.setTime2)
        studyTimer3Button = ttk.Button(master, text="3", command=self.setTime3)
        startButton = tk.Button(master, text="Start", command=self.start)
        resetButton = tk.Button(master, text="Reset", command=self.reset)
        self.label1.grid(row=0, column=2)
        studyTimer1Button.grid(row = 1, column= 1)
        studyTimer2Button.grid(row=1, column=2)
        studyTimer3Button.grid(row=1, column=3)
        startButton.grid(row = 4, column=1)
        resetButton.grid(row=4, column=3)


    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.countdown , daemon=True).start()


    def countdown(self):
        studyTotal = self.minutes * 60 + self.seconds
        for x in self.cycles:
            while studyTotal >= 0 and self.running:
                mins, secs = divmod(total, 60)
                self.label1.config(text=f"{mins:02}:{secs:02}")
                time.sleep(1)
                total -= 1
            self.cycles -=1
        self.running = False

    def reset(self):
        self.running = False
        self.minutes, self.seconds = 1, 0
        self.label.config(text="0:00")

    def setTime1(self):
        self.minutes = 1
    
    def setTime2(self):
        self.minutes = 2

    def setTime3(self):
        self.minutes = 3




if __name__ == "__main__":
    root = tk.Tk()
    app = Pomodoro(root)
    root.mainloop()