import tkinter as tk
from app import App


def main() -> None:
    root = tk.Tk()
    root.title('Squishmellows')
    app = App(root)
    print(root.winfo_children())
    root.mainloop()

if __name__ == '__main__':
    main()