from tkinter import *
from tkinter import ttk
from datetime import *
from customer_service.customer_service_read import *
import os, fnmatch
import time

path = os.path.abspath('../spa_project') + '/data/history/'
filename_list = list()

width_en = 30

def history():
    history_window = Toplevel()
    history_window.title("Spa - ประวัติการใช้บริการ!")

    def start_label():
        e1 = Entry(history_frame, width=width_en)
        e1.grid(row=0, column=0)
        e1.insert(END, 'ลำดับ')
        e1.config(state='disabled')
        e2 = Entry(history_frame, width=width_en)
        e2.grid(row=0, column=1)
        e2.insert(END, 'เวลา')
        e2.config(state='disabled')
        e3 = Entry(history_frame, width=width_en)
        e3.grid(row=0, column=2)
        e3.insert(END, 'ชื่อ')
        e3.config(state='disabled')
        e4 = Entry(history_frame, width=width_en)
        e4.grid(row=0, column=3)
        e4.insert(END, 'นามสกุล')
        e4.config(state='disabled')
        e5 = Entry(history_frame, width=width_en)
        e5.grid(row=0, column=4)
        e5.insert(END, 'ไอดี')
        e5.config(state='disabled')
        e6 = Entry(history_frame, width=width_en)
        e6.grid(row=0, column=5)
        e6.insert(END, 'เวลาที่ใช้บริการ(นาที)')
        e6.config(state='disabled')
        e7 = Entry(history_frame, width=width_en)
        e7.grid(row=0, column=6)
        e7.insert(END, 'พนักงาน')
        e7.config(state='disabled')
        e8 = Entry(history_frame, width=width_en)
        e8.grid(row=0, column=7)
        e8.insert(END, 'ห้อง')
        e8.config(state='disabled')
        e9 = Entry(history_frame, width=width_en)
        e9.grid(row=0, column=8)
        e9.insert(END, 'ทรีทเม้นท์')
        e9.config(state='disabled')

    def search_history(request, filename, data):
        for widget in history_frame.winfo_children():
            widget.destroy()
        canvas = Canvas(history_frame, width=100, height=100)
        scrollable_frame = Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        if(request == 'ทั้งหมด'):
            raw_c = get_customer_service_info_all(filename)
        if(request == 'ชื่อ'):
            raw_c = get_customer_service_info_by_name(data, filename)
        if(request == 'นามสกุล'):
            raw_c = get_customer_service_info_by_sur(data, filename)
        if(request == 'ไอดี'):
            raw_c = get_customer_service_info_by_id(data, filename)

        start_label()

        r_data_list = list()
        for r in raw_c:
            c_data_list = []
            c_data_list.append(r['time'])
            c_data_list.append(r['id'])
            c_data_list.append(r['fname'])
            c_data_list.append(r['sname'])
            c_data_list.append(r['service_time'])
            c_data_list.append(r['employee'])
            c_data_list.append(r['room'])
            t_data_list = list()
            for t in r['treatments']:
                t_data = t['treatment'] + ':' + t['amount']
                t_data_list.append(t_data)
            c_data_list.append(t_data_list)
            r_data_list.append(c_data_list)

        total_rows = len(r_data_list)
        total_columns = len(r_data_list[0])

        h = Scrollbar(history_frame, orient="vertical")
        h.grid(row=0, column=total_columns+1)
        v = Scrollbar(history_frame, orient='horizontal')
        v.grid(row=total_rows+1, column=0)

        canvas.configure(yscrollcommand=h.set, xscrollcommand=v.set)

        for i in range(total_rows):
            e = Entry(history_frame, width=width_en)
            e.grid(row=i+1, column=0)
            e.insert(END, i+1)
            e.configure(state='disabled')
            for j in range(total_columns):
                e = Entry(history_frame, width=width_en)
                e.grid(row=i+1, column=j+1)
                e.insert(END, r_data_list[i][j])
                e.configure(state='disabled')
        v.config(command=e.xview)
        h.config(command=e.yview)

    listOfFiles = os.listdir(path)
    pattern = "*.json"
    for entry in reversed(listOfFiles):
        if fnmatch.fnmatch(entry, pattern):
                day = entry.split('.')
                filename_list.append(day[0])

    filename_label = Label(history_window, text="เลือกวันที่")
    filename_label.grid(row=1, column=0, padx=5, pady=5)
    filename_drop = ttk.Combobox(history_window, value=filename_list)
    filename_drop.current(0)
    filename_drop.grid(row=1, column=1, padx=5, pady=5)

    data_entry = Entry(history_window, width=30)
    data_entry.grid(row=0, column=1, padx=5, pady=5)

    search_c_drop = ttk.Combobox(history_window, value=["ทั้งหมด", "ชื่อ", "นามสกุล", "ไอดี"])
    search_c_drop.current(0)
    search_c_drop.grid(row=0, column=0, padx=5, pady=5)

    add_r_button = Button(history_window, text="ค้นหา", command=lambda: search_history(search_c_drop.get(), filename_drop.get(), data_entry.get()))
    add_r_button.grid(row=2, column=0, columnspan=3, padx=20, pady=5)

    history_frame = LabelFrame(history_window, text="ประวัติการใช้บริการ", width=100, height=100)
    history_frame.grid(row=3, column=0, columnspan=3, padx=20, pady=5)

    # c_scrollbar_y = Scrollbar(history_frame, orient=VERTICAL)
    # c_scrollbar_x = Scrollbar(history_frame, orient=HORIZONTAL)

    # all_name_e_listbox = Listbox(history_frame, width=100, height=50, yscrollcommand=c_scrollbar_y.set, xscrollcommand=c_scrollbar_x.set)
    # c_scrollbar_y.config(command=all_name_e_listbox.yview)
    # c_scrollbar_y.grid(row=0, column=1, sticky='nwes')
    # c_scrollbar_x.config(command=all_name_e_listbox.xview)
    # c_scrollbar_x.grid(row=1, column=0, sticky='nwes')
    # all_name_e_listbox.grid(row=0, column=0, pady=10)

    start_label()
