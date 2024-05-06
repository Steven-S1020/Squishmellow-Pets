# pet.py
import os
import tkinter as tk
from PIL import Image, ImageTk


class Pet:
    def __init__(self, name, initial_position, pets_folder):
        self.name = name
        self.position = initial_position
        self.state = 'idle'
        self.animation_index = 0
        self.gifs = self.load_gifs(pets_folder)


    def load_gifs(self, pets_folder):
        gifs = {}
        for filename in os.listdir(pets_folder):
            if filename.endswith('.gif'):
                try:
                    state = filename.split("_")[1]  # Extract state from filename
                    if state not in gifs:
                        gifs[state] = []
                    img_path = os.path.join(pets_folder, filename)
                    img = Image.open(img_path)
                    resized_img = img.resize((1000, 1000))
                    photo = ImageTk.PhotoImage(resized_img)
                    gifs[state].append(photo)
                except Exception as e:
                    print(f"Error loading GIF file: {filename} - {e}")
        return gifs


        
    def frame_count(self, gif_file):
        Gif = Image.open(gif_file)
        return Gif.n_frames
    
    def next_frame(self):
        self.animation_index = (self.animation_index + 1) % len(self.gifs[self.state])

    def draw(self, canvas: tk.Canvas):
        gif = self.gifs[self.state][self.animation_index]
        canvas.create_image(self.position[0], self.position[1], image=gif, anchor=tk.CENTER)
        