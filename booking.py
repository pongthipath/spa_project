from tkinter import *
from datetime import *
from tkinter import ttk
from tkinter import messagebox
from rooms.rooms_data_read import *
from booking_io.booking_write import *
from booking_io.booking_read import *
import os, fnmatch

path = os.path.abspath('../spa_project') + '/data/booking/'

def booking():
    booking_window = Toplevel()
    booking_window.title("Spa - จองคิว!")
    b_width = 20
    time_list = [
        "7:00-7:30", "7:30-8:00", "8:00-8:30", "8:30-9:00", "9:00-9:30", "9:30:-10:00", "9:30:-10:00", "10:00-10:30", "10:30-11:00", "11:00-11:30",
        "11:30-12:00", "12:00-12:30", "12:30-13:00", "13:00-13:30", "13:30-14:00", "14:00-14:30", "14:30-15:00", "15:00-15:30", "15:30-16:00",
        "16:00-16:30", "16:30-17:00", "17:00-17:30", "17:30-18:00", "18:00-18:30", "18:30-19:00", "19:00-19:30", "19:30-20:00", "20:00-20:30", "20:30-21:00"
    ]
    total_rows = len(time_list)
    total_columns = len(get_room_all_name())
    entry_list = list()

    g_r_list = list()
    for i in range(total_rows):
        g_c_list = list()
        for j in range(total_columns):
            empty_data = ''
            g_c_list.append(empty_data)
        g_r_list.append(g_c_list)

    today = datetime.today()

    next_date = datetime.today()
    for i in range(30):
        next_date += timedelta(days=1)
        add_booking(next_date.strftime("%d_%m_%Y"), total_rows, total_columns, g_r_list)

    def save_booking(filename):
        first_l = total_columns
        last_l = total_columns + total_columns
        # for i in range(total_rows):
        #     for j in range(total_columns):
        r_list = list()
        c_list = list()

        for i in range(0, total_columns):
            c_list.append(entry_list[i].get())
        r_list.append(c_list)
        c_list = []
        for j in range(total_rows-2):
            c_list = []     
            for i in range(first_l, last_l):
                c_list.append(entry_list[i].get())
            first_l += total_columns
            last_l += total_columns
            r_list.append(c_list)
            c_list = []
        for i in range((total_rows*total_columns)-total_columns, total_rows*total_columns):
            c_list.append(entry_list[i].get())
        r_list.append(c_list)
        c_list = []
        
        add_booking(filename, total_rows, total_columns, r_list)

        messagebox.showinfo('บันทึก!', 'บันทึกเรียบร้อย!')

        data_list = get_booking_table(filename)

        for i in range(total_rows):
            for j in range(total_columns):
                b_e = Entry(table_frame, width=b_width)
                b_e.grid(row=i+1, column=j+1)
                b_e.insert(END, data_list[i][j])

    def search_booking(filename):
        data_list = get_booking_table(filename)

        for i in range(total_rows):
            for j in range(total_columns):
                b_e = Entry(table_frame, width=b_width)
                b_e.grid(row=i+1, column=j+1)
                b_e.insert(END, data_list[i][j])
                entry_list.append(b_e)

    filename_list = list()

    listOfFiles = os.listdir(path)
    pattern = "*.json"
    for entry in reversed(listOfFiles):
        if fnmatch.fnmatch(entry, pattern):
                day = entry.split('.')
                filename_list.append(day[0])

    filename_label = Label(booking_window, text="เลือกวันที่")
    filename_label.grid(row=0, column=0, padx=5, pady=5)
    filename_drop = ttk.Combobox(booking_window, value=filename_list)
    drop_today_index = filename_list.index(today.strftime("%d_%m_%Y"))
    filename_drop.current(drop_today_index)
    filename_drop.grid(row=0, column=1, padx=5, pady=5)
    search_button = Button(booking_window, text='ค้นหา', command=lambda: search_booking(filename_drop.get()))
    search_button.grid(row=0, column=2, columnspan=3, padx=5, pady=5)
    save_button = Button(booking_window, text='บันทึก', command=lambda: save_booking(filename_drop.get()))
    save_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    table_frame = LabelFrame(booking_window, text='ตารางการจอง')
    table_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    data_list = get_booking_table(filename_drop.get())

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
            b_e = Entry(table_frame, width=b_width)
            b_e.grid(row=i+1, column=j+1)
            b_e.insert(END, data_list[i][j])
            entry_list.append(b_e)

