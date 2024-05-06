# app.py
import tkinter as tk
from pet import Pet
from os import walk
from Settings import SquishSettings


class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()
        self.Squishmellows: list[Pet] = []
        self.setup_squishmellows()
        self.pet_visibility = {key: True for key in self.Squishmellows}
        self.setup_settings_button()
    
    def switch_frames(self):
        ...

    def setup_squishmellows(self):
        Squishmellows = next(walk('.\\Gifs'))[1]
        for Squish in Squishmellows:
            Squishy = Pet(Squish,(0,0),f'.\\Gifs\\{Squish}')
            self.Squishmellows.append(Squishy)
            Squishy.draw(self.canvas) # draw the pet on the canvas
            print(Squishmellows)

    def update_visibility(self, visibility_dict):
        for pet_name, visible in visibility_dict.items():
            if pet_name in self.pet_visibility:
                self.pet_visibility[pet_name] = visible
        self.redraw_pets()
        self.switch_frames()

    def redraw_pets(self):
        print(self.canvas)
        # self.canvas.delete('all')   # Clear canvas
        for pet in self.Squishmellows:
            if self.pet_visibility.get(pet.name, False):
                try:
                    print(pet, pet.name)
                    pet.draw(self.canvas) # Draw visible pets
                except Exception as e:
                    print(f"Error drawing pet {pet.name}: {e}")

    def setup_settings_button(self):
        settings_button = tk.Button(self.master, text='Settings', command=self.open_settings)
        settings_button.pack()

    def open_settings(self):
        # ssettings_window = tk.Toplevel(self.master)
        SquishSettings(self.Squishmellows, self.pet_visibility)
        self.update_visibility(self.pet_visibility)