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

        self.studyTime = 0
        self.minutesText = tk.StringVar()
        self.seconds = 0
        self.running = False
        self.cycles = 0
        self.longBreak  = 0
        self.shortBreak = 0

        self.timeLabel = tk.Label(master, text="0:00", font=(font_name, 25))
        self.label2 = tk.Label(master, textvariable=self.minutesText, font=(font_name, 25))

        studyLabel = tk.Label(master, text="Study Time: ", font=(font_name, 25))
        shortBreakLabel = tk.Label(master, text="Short Break: ", font=(font_name, 25))
        longBreakLabel = tk.Label(master, text="Long Break: ", font=(font_name, 25))
        cyclesLabel = tk.Label(master, text="Cycles: ", font=(font_name, 25))



        #Buttons for selecting short break time
        shortBreakTimeButton1 = ttk.Button(master, text="4 Minutes", command=lambda: self.setShortBreakTime(4))
        shortBreakTimeButton2 = ttk.Button(master, text="5 Minutes", command=lambda: self.setShortBreakTime(5))
        shortBreakTimeButton3 = ttk.Button(master, text="6 Minutes", command=lambda: self.setShortBreakTime(6))

        #Buttons for selecting long break time
        longBreakTimeButton1 = ttk.Button(master, text="15 Minutes", command=lambda: self.setLongBreakTime(15))
        longBreakTimeButton2 = ttk.Button(master, text="20 Minutes", command=lambda: self.setLongBreakTime(20))
        longBreakTimeButton3 = ttk.Button(master, text="25 Minutes", command=lambda: self.setLongBreakTime(25))


        #Buttons for selecting number of study cycles
        studyCyclesButton1 = ttk.Button(master, text="3 Cycles", command=lambda: self.setCycles(3))
        studyCyclesButton2 = ttk.Button(master, text="4 Cycles", command=lambda: self.setCycles(4))
        studyCyclesButton3 = ttk.Button(master, text="5 Cycles", command=lambda: self.setCycles(5))


        startButton = tk.Button(master, text="Start", command=self.start)
        resetButton = tk.Button(master, text="Reset", command=self.reset)
        self.timeLabel.grid(row=0, column=2)
        self.label2.grid(row=1, column=2)

        cyclesLabel.grid(row=2, column=1)
        studyCyclesButton1.grid(row=2, column=2)
        studyCyclesButton2.grid(row=2, column=3)
        studyCyclesButton3.grid(row=2, column=4)

        shortBreakLabel.grid(row=3, column=1)
        shortBreakTimeButton1.grid(row = 3, column= 2)
        shortBreakTimeButton2.grid(row=3, column=3)
        shortBreakTimeButton3.grid(row=3, column=4)

        longBreakLabel.grid(row=4, column=1)
        shortBreakTimeButton1.grid(row = 4, column= 2)
        shortBreakTimeButton2.grid(row=4, column=3)
        shortBreakTimeButton3.grid(row=4, column=4)

       


        startButton.grid(row = 4, column=1)
        resetButton.grid(row=4, column=3)


    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.countdown , daemon=True).start()


    def countdown(self):
        studyTotal = self.studyTime * 60
        shortBreakTotal = self.shortBreak * 60
        longBreakTotal = self.longBreak * 60


        for x in range(self.cycles):
            while studyTotal >= 0 and self.running:
                mins, secs = divmod(studyTotal, 60)
                self.timeLabel.config(text=f"{mins:02}:{secs:02}")
                time.sleep(1)
                studyTotal -= 1
            studyTotal = self.minutes * 60
            while shortBreakTotal >= 0 and self.running:
                mins, secs = divmod(studyTotal, 60)
                self.timeLabel.config(text=f"{mins:02}:{secs:02}")
                time.sleep(1)
                studyTotal -= 1
            shortBreakTotal = self.shortBreak * 60
            while studyTotal >= 0 and self.running:
                mins, secs = divmod(studyTotal, 60)
                self.timeLabel.config(text=f"{mins:02}:{secs:02}")
                time.sleep(1)
                studyTotal -= 1
            studyTotal = self.minutes * 60
        self.running = False
        self.minutes = 0
        self.cycles = 0

    def reset(self):
        self.running = False
        self.minutes, self.seconds = 1, 0
        self.timeLabel.config(text="0:00")

    def setShortBreakTime(self, value):
        self.shortBreak = value
        #self.minutesText.set(value)

    def setLongBreakTime(self, value):
        self.longBreak = value
        #self.minutesText.set(value)
    
    def setCycles(self,value):
        self.cycles = value
        print("Cycles set to:", self.cycles)
        




if __name__ == "__main__":
    root = tk.Tk()
    app = Pomodoro(root)
    root.mainloop()