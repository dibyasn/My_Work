# Transparent Digital Clock ⏰

Welcome to the Transparent Digital Clock project! This project creates a transparent, always-on-top digital clock using Python's Tkinter library. The clock displays the current time and can be moved around the screen by dragging it.

## Table of Contents
- [Transparent Digital Clock ⏰](#transparent-digital-clock-)
  - [Table of Contents](#table-of-contents)
  - [📖 Introduction](#-introduction)
  - [🔧 Features](#-features)
  - [🔌 Requirements](#-requirements)
  - [🚀 Setup Instructions](#-setup-instructions)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Run the Script](#2-run-the-script)
  - [💡 Code Explanation](#-code-explanation)
    - [Main Features:](#main-features)
  - [🖥️ Usage](#️-usage)
  - [🎉 Acknowledgments](#-acknowledgments)
  - [Contributing](#contributing)
  - [Contact](#contact)

## 📖 Introduction
This project demonstrates how to create a digital clock with a transparent background that stays on top of all other windows. The clock can be easily dragged around the screen, providing a convenient and customizable way to keep track of time.

## 🔧 Features
- **Transparent Window:** The clock window is semi-transparent and blends seamlessly with your desktop.
- **Always on Top:** The clock window stays on top of all other windows.
- **Movable:** You can drag the clock to any position on the screen.
- **Customizable Appearance:** The font and colors of the clock can be customized.

## 🔌 Requirements
- **Python 3.x**
- **Tkinter:** Tkinter is usually included with Python installations. If it's not installed, you can install it using your package manager .

## 🚀 Setup Instructions
### 1. Clone the Repository
```sh
git clone https://github.com/dibyasn/Python.git
cd Python/Clock
```

### 2. Run the Script
```sh
python Clock.py
```

## 💡 Code Explanation
Here's a brief overview of the code:

```python
import tkinter as tk
from tkinter import Label
import time

class TransparentClock(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Transparent Digital Clock")
        self.geometry("180x50")

        self.overrideredirect(True)  # Remove window decorations (title bar, close button, etc.)
        self.wm_attributes("-topmost", True)  # Keep the window on top of all other windows
        self.wm_attributes("-alpha", 0.8)  # Set the window transparency (0.0 is fully transparent, 1.0 is fully opaque)

        self.time_label = Label(self, font=('Helvetica', 20), fg='white', bg='black')
        self.time_label.pack(expand=True, fill='both')

        self.update_clock()

        # Bind mouse events to enable dragging
        self.time_label.bind("<Button-1>", self.start_move)
        self.time_label.bind("<B1-Motion>", self.do_move)

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.after(1000, self.update_clock)  # Update the clock every 1000 milliseconds (1 second)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.winfo_pointerx() - self.x
        y = self.winfo_pointery() - self.y
        self.geometry(f"+{x}+{y}")

def create_clock():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    clock = TransparentClock(master=root)
    clock.mainloop()

if __name__ == "__main__":
    create_clock()
```

### Main Features:
- **TransparentClock Class:** This class creates a top-level window with no decorations, keeps it on top of other windows, and sets its transparency.
- **update_clock Method:** Updates the displayed time every second.
- **start_move and do_move Methods:** Allow the clock window to be dragged around the screen.

## 🖥️ Usage
Run the script, and a transparent digital clock will appear on your screen. You can drag the clock to any position by clicking and holding the left mouse button on the clock, then moving your mouse.

## 🎉 Acknowledgments
This project is inspired by various digital clock and Tkinter projects. Special thanks to the developers and contributors of Python and Tkinter for making GUI development accessible and straightforward.

## Contributing
We welcome contributions! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Contact

<p align="center">
    <img src="https://64.media.tumblr.com/tumblr_lp0f2fIhnF1qa2ip8o1_1280.gif" alt="Thank You">
</p>

---

For any questions or suggestions, feel free to open an issue or contact us directly.

<p align="center">
    <a href="https://github.com/dibyasn/Python/tree/main/Clock"><img src="https://img.icons8.com/color/48/000000/github.png" alt="Contribute Icon"></a>
</p>