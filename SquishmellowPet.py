import pyautogui
import random
import tkinter as tk

path = '/Gifs/'

def main() -> None:
    window = tk.Tk()

    # Each Squishmellows Gif Arrays
    manny = []
    chip = []
    timmy = []
    berry = []
    pip = []
    Squishmellows = {'Manny':manny, 'Chip':chip, 'Timmy':timmy, 'Berry':berry, 'Pip':pip}
    Actions = GifPull(Squishmellows)




def GifPull(Squishmellows):
    for Squish in Squishmellows:
        idle = [tk.PhotoImage(file=path + Squish + 'idle.gif', format = 'gif --index %i'%(i)) for i in range()]
        idle_to_sleep = [tk.PhotoImage(file=path + Squish + 'idle_to_sleep.gif', format = 'gif --index %i'%(i)) for i in range()]
        sleep = [tk.PhotoImage(file=path + Squish + 'sleep.gif', format = 'gif --index %i'%(i)) for i in range()]
        sleep_to_idle =[tk.PhotoImage(file=path + Squish + 'sleep_to_idle.gif', format = 'gif --index %i'%(i)) for i in range()]
        walk_pos =[tk.PhotoImage(file=path + Squish + 'walk_pos.gif', format = 'gif --index %i'%(i)) for i in range()]
        walk_neg =[tk.PhotoImage(file=path + Squish + 'walk_neg.gif', format = 'gif --index %i'%(i)) for i in range()]
        f'{Squish}'.append(idle, idle_to_sleep, sleep, sleep_to_idle, walk_pos, walk_neg)


if __name__ == '__main__':
    main()
