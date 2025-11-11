import tkinter as tk
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

        self.label = tk.Label(master, text="1:00", font=(font_name, 25))
        self.label.pack(pady=20)
        #tk.Button(master, text="1", comm)
        tk.Button(master, text="Start", command=self.start).pack(side="left", padx=20)
        tk.Button(master, text="Reset", command=self.reset).pack(side="right", padx=20)


    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.countdown , daemon=True).start()


    def countdown(self):
        total = self.minutes * 60 + self.seconds
        while total >= 0 and self.running:
            mins, secs = divmod(total, 60)
            self.label.config(text=f"{mins:02}:{secs:02}")
            time.sleep(1)
            total -= 1
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