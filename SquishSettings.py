import tkinter as tk
from tkinter import messagebox
class SquishSettings:
    def __init__(self, Squishmellows, SquishStates):
        Lav = '#E6E6FA'
        Pin = '#FAE6E6'
        Gre = '#E6FAE6'
        Blu = '#E6FAFA'

        self.settings = tk.Tk()

        self.settings.geometry('500x200')
        self.settings.title('Squismellow Settings')
        self.settings.configure(bg=Lav)

        self.frame1 = tk.Frame(self.settings, bg='#B1B1EF', bd=2, relief=tk.SOLID)
        self.frame1.pack(padx=10, pady=10)
        self.frame2 = tk.Frame(self.frame1, bg=Gre, bd=2, relief=tk.SOLID)
        self.frame2.pack(padx=10, pady=10)
        self.frame3 = tk.Frame(self.frame2, bg=Blu, bd=2, relief=tk.SOLID)
        self.frame3.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame3,
                              text='    Squish Settings    ',
                              font=('Arial', 24),
                              bg=Pin,
                              height=3,
                              bd=5,
                              relief=tk.GROOVE)
                              
        self.label.pack(padx=20,
                        pady=20)

        self.checkframe = tk.Frame(self.frame3,
                                   bg=Pin,
                                   bd=5,
                                   relief=tk.GROOVE)
        for i in range(len(Squishmellows)):
            self.checkframe.columnconfigure(i, weight=1)


        self.changes_made = False
        self.checked_state = []
        row_num = 0
        for squish, state in SquishStates.items():
            label_text = 'Show ' + squish

            self.checked_state.append(tk.BooleanVar(value=state))

            label = tk.Label(self.checkframe,
                             text=label_text,
                             font=('Arial', 16),
                             padx=25,
                             pady=15,
                             bg=Pin)
            
            label.grid(row=row_num,
                       column=0,
                       sticky=tk.W)

            check = tk.Checkbutton(self.checkframe,
                                   variable=self.checked_state[row_num],
                                   bg=Pin,
                                   font=('Arial', 22),
                                   command=self.CheckBox_Changed)
            check.grid(row=row_num,
                       column=1,
                       sticky=tk.W)

            row_num += 1


        self.checkframe.pack()

        self.save = tk.Button(self.frame3,
                              text='Save',
                              font=('Arial', 16),
                              bg=Blu,
                              activebackground=Gre,
                              bd=3,
                              command=self.Save_Settings)
        self.save.pack(anchor='se',
                        padx=20,
                        pady=20)

        self.settings.protocol("WM_DELETE_WINDOW", self.On_Closing)
        self.settings.mainloop()

    def CheckBox_Changed(self):
        self.changes_made = True

    def Save_Settings(self):
        if self.changes_made:
            checkbox_states = [var.get() for var in self.checked_state]
            print("Changes Detected.", checkbox_states)
            self.changes_made = False
        else:
            print("No changes")
        
    def On_Closing(self):
        if self.changes_made:
            if messagebox.askyesno(title='Exit', message='You have unsaved changes. Would you like to still exit?'):
                self.setings.destroy()
        else:
            self.settings.destroy()

manny = []
chip = []
timmy = []
berry = []
pip = []
Squishmellows = {'Manny':manny, 'Chip':chip, 'Timmy':timmy, 'Berry':berry, 'Pip':pip}
SquishStates ={key: True for key in Squishmellows}

SquishSettings(Squishmellows, SquishStates)
