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

        self.studyTime = 1
        self.stepLabel = tk.StringVar()
        self.seconds = 0
        self.running = False
        self.cycles = 0
        self.longBreak  = 0
        self.shortBreak = 0

        self.timeLabel = tk.Label(master, text="0:00", font=(font_name, 25))
        self.stepStudyLabel = tk.Label(master, textvariable=self.stepLabel, font=(font_name, 25))

        studyLabel = tk.Label(master, text="Study Time: ", font=(font_name, 25))
        shortBreakLabel = tk.Label(master, text="Short Break: ", font=(font_name, 25))
        longBreakLabel = tk.Label(master, text="Long Break: ", font=(font_name, 25))
        cyclesLabel = tk.Label(master, text="Cycles: ", font=(font_name, 25))



        #Buttons for selecting short break time
        shortBreakTimeButton1 = ttk.Button(master, text="4 Minutes", command=lambda: self.setShortBreakTime(1))
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
        pauseButton = tk.Button(master, text="Pause", command=self.pause)
        resumeButton = tk.Button(master, text="Resume", command=self.resume)


        self.timeLabel.grid(row=1, column=2)
        self.stepStudyLabel.grid(row=0, column=2)

        cyclesLabel.grid(row=2, column=1)
        studyCyclesButton1.grid(row=2, column=2)
        studyCyclesButton2.grid(row=2, column=3)
        studyCyclesButton3.grid(row=2, column=4)

        shortBreakLabel.grid(row=3, column=1)
        shortBreakTimeButton1.grid(row = 3, column= 2)
        shortBreakTimeButton2.grid(row=3, column=3)
        shortBreakTimeButton3.grid(row=3, column=4)

        longBreakLabel.grid(row=4, column=1)
        longBreakTimeButton1.grid(row = 4, column= 2)
        longBreakTimeButton2.grid(row=4, column=3)
        longBreakTimeButton3.grid(row=4, column=4)

       


        startButton.grid(row = 5, column=1)
        resetButton.grid(row=5, column=3)
        pauseButton.grid(row=6, column=1)
        resumeButton.grid(row=6, column=3)


    def updateStudyTime(self):
        if self.running:
            studyTotal = self.studyTime * 60
            if studyTotal > 0:
                mins, secs = divmod(studyTotal, 60)
                self.timeLabel.config(text=f"{mins:02}:{secs:02}")
                self.master.after(1000,self.updateStudyTime)

    def updateShortBreak(self):
        if self.running:
            shortBreakTotal = self.shortBreak * 60
            if shortBreakTotal > 0:
                mins, secs = divmod(shortBreakTotal, 60)
                self.timeLabel.config(text=f"{mins:02}:{secs:02}")


    def countdown(self):
        longBreakTotal = self.longBreak * 60
        stepInterval = 0

        for x in range(self.cycles):
            print("Entered for loop")
            stepInterval += 1
            studyText = "Study Time #" + str(stepInterval)
            self.stepLabel.set(studyText)
            self.updateStudyTime()
            print("ended study time")

            shortBreakText = "Short Break #" + str(stepInterval)
            self.stepLabel.set(shortBreakText)
            self.updateShortBreak()
        while longBreakTotal >= 0 and self.running:
                longBreakText = "Long Break"
                self.stepLabel.set(longBreakText)
                mins, secs = divmod(longBreakTotal, 60)
                self.timeLabel.config(text=f"{mins:02}:{secs:02}")
                time.sleep(1)
                longBreakTotal -= 1
        longBreakTotal = self.longBreak * 60   
        self.running = False
        self.cycles = 0

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.countdown , daemon=True).start()

    def reset(self):
        self.running = False
        self.minutes, self.seconds = 1, 0
        self.timeLabel.config(text="0:00")

    def pause(self):
        self.running = False

    def resume(self):
        self.running = True

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