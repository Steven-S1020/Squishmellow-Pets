# app.py
import tkinter as tk
from squish import Squish

class App:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=800, height=600)
        self. canvas.pack()
        self.Squishmellows = []
        self.setup_squishmellows()

    def setup_squishmellows(self):
        