import tkinter as tk
from tkinter import Label, Button
import time

class TransparentClock(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Transparent Digital Clock")
        self.geometry("300x150")

        self.overrideredirect(True)  # Remove window decorations (title bar, close button, etc.)
        self.wm_attributes("-topmost", True)  # Keep the window on top of all other windows
        self.wm_attributes("-alpha", 0.8)  # Set the window transparency (0.0 is fully transparent, 1.0 is fully opaque)

        self.time_label = Label(self, font=('Helvetica', 20), fg='white', bg='black')
        self.time_label.pack(expand=True, fill='both')

        self.day_label = Label(self, font=('Helvetica', 20), fg='white', bg='black')
        self.day_label.pack(expand=True, fill='both', anchor='center')

        self.close_button = Button(self, text="Close", command=self.close_window)
        self.close_button.pack()

        # Disable geometry propagation
        self.pack_propagate(False)

        self.update_clock()

        # Bind mouse events to enable dragging
        self.time_label.bind("<Button-1>", self.start_move)
        self.time_label.bind("<B1-Motion>", self.do_move)
        self.day_label.bind("<Button-1>", self.start_move)
        self.day_label.bind("<B1-Motion>", self.do_move)
        self.close_button.bind("<Button-1>", self.start_move)
        self.close_button.bind("<B1-Motion>", self.do_move)

    def update_clock(self):
        current_time = time.strftime('%d %b %y %H:%M:%S')
        current_day = time.strftime('%A')
        self.time_label.config(text=current_time)
        self.day_label.config(text=current_day)
        
        # Update the size of the window to fit the content
        self.update_idletasks()
        self.geometry(f"{self.time_label.winfo_reqwidth()}x{self.time_label.winfo_reqheight() + self.day_label.winfo_reqheight() + self.close_button.winfo_reqheight()}")

        self.after(1000, self.update_clock)  # Update the clock every 1000 milliseconds (1 second)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self.x
        y = self.winfo_pointery() - self.y
        self.geometry(f"+{x}+{y}")

    def close_window(self):
        self.destroy()  # Destroy the window
        self.master.destroy()  # Destroy the root (main) window
        import sys; sys.exit()  # Exit the script

def create_clock():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    clock = TransparentClock(master=root)
    clock.mainloop()

if __name__ == "__main__":
    create_clock()
