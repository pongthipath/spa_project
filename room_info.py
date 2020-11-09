from tkinter import *
from datetime import *
from rooms.rooms_data_read import *
from add_room import *

def room_info():
    room_info_window = Toplevel()
    room_info_window.title("Spa - ข้อมูลห้อง!")


    all_name_e_listbox = Listbox(room_info_window)
    all_name_e_listbox.grid(row=1, column=0, padx=20, pady=10)

    all_name_e = get_room_all_name()
    for name in all_name_e:
        all_name_e_listbox.insert(END, name)

    add_r_button = Button(room_info_window, text="ตั้งค่า", command=room_add)
    add_r_button.grid(row=3, column=0, columnspan=3, padx=20, pady=5)
