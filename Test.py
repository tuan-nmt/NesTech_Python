variable = -5
variable1 = -5
variable2 = -5
variable3 = -5

def is_float(s):
    result = False
    if s.count(".") == 1:
        if s.replace(".", "").isdigit():
            result = True
    return result

def tbc():
    global variable,variable1,variable2,variable3

    while variable < 0 :
        variable = input("Nhập vào điểm môn Toán :")
        if is_float(variable):
            variable = float(variable)
        else:
            variable = -5
    else:
        print (variable) 

    while variable1 <0 :
        variable1 = float(input("Nhập vào điểm môn Văn :"))
    else:
        print (variable1) 

    while variable2  <0 :
        variable2  = float(input("Nhập vào điểm môn Hoá :"))
    else:
        print (variable2) 

    while variable3 <0 :
        variable3 = float(input("Nhập vào điểm môn Lý :"))
    else:
        print (variable3) 

    diemTB=(variable+variable1+variable2+variable3)/4
    print("Điểm TB của 4 môn học là :",diemTB)
    
diemtoan=tbc()