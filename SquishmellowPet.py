import random
import tkinter as tk
from PIL import Image
from SquishSettings import SquishSettings

# Each Squishmellows Gif Lists
manny = []
chip = []
timmy = []
berry = []
pip = []
Squishmellows = {'Manny':manny, 'Chip':chip, 'Timmy':timmy, 'Berry':berry, 'Pip':pip}
SquishStates ={key: True for key in Squishmellows}

def main() -> None:
    window = tk.Tk()

    Actions = GifPull(Squishmellows)

    # Fixes window look
    window.config(hiughlightbackground='black')
    window.overrideredirect(True)
    window.wm_attributes('-transparentcolor','black')

    for Squish in Squishmellows:
        Squish = tk.Label(window,bd=0,bg='black')
        Squish.pack()
        window.mainloop()

    if ...:
        SquishSettings(Squishmellows, SquishStates)
        


if __name__ == '__main__':
    main()
