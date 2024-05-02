import pyautogui
import random
import tkinter as tk
from PIL import Image


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

    # Fixes window look
    window.config(hiughlightbackground='black')
    window.overrideredirect(True)
    window.wm_attributes('-transparentcolor','black')

    for Squish in Squishmellows:
        Squish = tk.Label(window,bd=0,bg='black')
        Squish.pack()
        window.mainloop()



def GifPull(Squishmellows):
    for Squish in Squishmellows:
        FilePath = '/Gifs/' + Squish + '/' + Squish
        idle = [tk.PhotoImage(file=FilePath+'idle.gif', format='gif --index %i' % (i)) for i in range(FramePull(FilePath+'idle.gif'))]
        idle_to_sleep = [tk.PhotoImage(file=FilePath+'idle_to_sleep.gif', format='gif --index %i' % (i)) for i in FramePull(FilePath+'idle_to_sleep.gif')]
        sleep = [tk.PhotoImage(file=FilePath+'sleep.gif', format='gif --index %i' % (i)) for i in FramePull(FilePath+'sleep.gif')]
        sleep_to_idle = [tk.PhotoImage(file=FilePath+'sleep_to_idle.gif', format='gif --index %i' % (i)) for i in FramePull(FilePath+'sleep_to_idle.gif')]
        walk_pos = [tk.PhotoImage(file=FilePath+'walk_pos.gif', format='gif --index %i' % (i)) for i in FramePull(FilePath+'walk_pos.gif')]
        walk_neg = [tk.PhotoImage(file=FilePath+'walk_neg.gif',format='gif --index %i' % (i)) for i in FramePull(FilePath+'walk_neg.gif')]
        f'{Squish}'.append(idle, idle_to_sleep, sleep, sleep_to_idle, walk_pos, walk_neg)


def FramePull(FilePath):
    Gif = Image.open(FilePath)
    return Gif.n_frames

if __name__ == '__main__':
    main()
