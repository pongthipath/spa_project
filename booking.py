from tkinter import *
from datetime import *

def booking_to_db():
    return

def booking():
    booking_window = Toplevel()
    booking_window.title("Spa - จองคิว!")
    booking_window.geometry("400x800")

    c_name_label = Label(booking_window, text="ชื่อ: ")
    c_name_label.grid(row=0, column=0, padx=5, pady=5)

    c_name = Entry(booking_window, width=30)
    c_name.grid(row=0, column=1, padx=5, pady=5)

    booking_btn = Button(booking_window, text="จอง", command=booking_to_db)
    booking_btn.grid(row=1, column=1, padx=5, pady=5)
