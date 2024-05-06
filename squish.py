# pet.py
import os
import tkinter as tk
from PIL import Image


class Squish:
    def __init__(self, name, initial_position, gifs_folder):
        self.name = name
        self.position = initial_position
        self.state = 'idle'
        self.animation_index = 0
        self.gifs = self.load_gifs(gifs_folder)


    def laod_gifs(self, gifs_folder):
        gifs = {}
        for state in ['idle', 'idle_to_sleep', 'sleep', 'sleep_to_idle', 'walk']:
            gifs[state] = [
                tk.PhotoImage(filw=os.path.join(gifs_folder, self.name, f'{self.name}_{state}_{i}.gif'))
                for i in range(self.frame_count(os.path.join(gifs_folder, self.name, f'{self.name}_{state}_0.gif')))
            ]
        return gifs
        
    def frame_count(self, gif_file):
        Gif = Image.open(gif_file)
        return Gif.n_frames
    
    def next_frame(self):
        self.animation_index = (self.animation_index + 1) % len(self.gifs[self.state])

    def draw(self, canvas):
        canvas.create_image(self.position[0], self.position[1], image=self.gifs[self.state][self.animation_idex], anchor=tk.CENTER)
        