from datetime import *

def customer_use(name, s_room, s_employee, s_promotion):
    tnow = datetime.today()
    n_tnow = tnow.strftime("%d/%m/%Y %H:%M:%S") 
    print(n_tnow + " คุณ: " + name + " , ใช้ห้อง: " + s_room + " , พนักงาน : " + s_employee + " , โปรโมชั่น: " + s_promotion)
