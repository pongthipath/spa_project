from tkinter import *
from datetime import *
from tkinter import ttk
from rooms.rooms_data_read import *
import os, fnmatch

path = os.path.abspath('../spa_project') + '/data/history/'

def booking():
    booking_window = Toplevel()
    booking_window.title("Spa - จองคิว!")
    b_width = 20

    filename_list = list()

    listOfFiles = os.listdir(path)
    pattern = "*.json"
    for entry in reversed(listOfFiles):
        if fnmatch.fnmatch(entry, pattern):
                day = entry.split('.')
                filename_list.append(day[0])

    time_list = [
        "7:00-7:30", "7:30-8:00", "8:00-8:30", "8:30-9:00", "9:00-9:30", "9:30:-10:00", "9:30:-10:00", "10:00-10:30", "10:30-11:00", "11:00-11:30",
        "11:30-12:00", "12:00-12:30", "12:30-13:00", "13:00-13:30", "13:30-14:00", "14:00-14:30", "14:30-15:00", "15:00-15:30", "15:30-16:00",
        "16:00-16:30", "16:30-17:00", "17:00-17:30", "17:30-18:00", "18:00-18:30", "18:30-19:00", "19:00-19:30", "19:30-20:00", "20:00-20:30", "20:30-21:00"
    ]

    filename_label = Label(booking_window, text="เลือกวันที่")
    filename_label.grid(row=1, column=0, padx=5, pady=5)
    filename_drop = ttk.Combobox(booking_window, value=filename_list)
    filename_drop.current(0)
    filename_drop.grid(row=1, column=1, padx=5, pady=5)

    table_frame = LabelFrame(booking_window, text='ตารางการจอง')
    table_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    total_rows = len(time_list)
    total_columns = len(get_room_all_name())

    for j in range(total_columns):
        e = Entry(table_frame, width=b_width)
        e.grid(row=0, column=j+1, padx=5, pady=5)
        e.insert(END, get_room_all_name()[j])
        e.configure(state='disabled')

    for i in range(total_rows):
        e = Entry(table_frame, width=b_width)
        e.grid(row=i+1, column=0, padx=5, pady=5)
        e.insert(END, time_list[i])
        e.configure(state='disabled')

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(table_frame, width=b_width)
            e.grid(row=i+1, column=j+1)
