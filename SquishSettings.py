import tkinter as tk
from SquishmellowPet import Squishmellows, SquishStates


class SquishSettings:
    def __init__(self):
        print(SquishStates)

        self.settings = tk.Tk()

        self.settings.geometry('500x200')
        self.settings.title('Squismellow Settings')

        self.label = tk.Label(self.settings,
                              text='Squish Settings',
                              font=('Arial', 18))
        self.label.pack(anchor='w', padx=20, pady=20)

        self.checkframe = tk.Frame(self.settings)
        for i in range(len(Squishmellows)):
            self.checkframe.columnconfigure(i, weight=1)

        self.checked_state = []
        row_num = 0
        for squish, state in SquishStates.items():
            label_text = 'Show ' + squish

            self.checked_state.append(tk.BooleanVar(value=state))

            label = tk.Label(self.checkframe,
                             text=label_text,
                             font=('Arial', 16))
            label.grid(row=row_num, column=0, sticky=tk.W)

            check = tk.Checkbutton(self.checkframe,
                                   variable=self.checked_state[row_num])
            check.grid(row=row_num, column=1, sticky=tk.W)

            row_num += 1

        self.checkframe.pack(anchor='w')

        self.settings.mainloop()


SquishSettings()
