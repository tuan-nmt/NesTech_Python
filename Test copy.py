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

    while variable  <0 :
        variable  =(input("Nhập vào điểm môn Toán :"))
        if is_float(variable):
            variable =float(variable)
        else:
            variable =-5
            print("Nhập sai rồi, nhập lại cho đúng đi")
    else:
        print ("Điểm toán là :",variable)

    while variable1 < 0 :
        variable1 = (input("Nhập vào điểm môn Văn :"))
        if is_float(variable1):
            variable1=float(variable1)
        else:
            variable1=-5
            print("Nhập sai rồi, nhập lại đi") 
    else:
         print ("Điêrm môn văn là:",variable1)

    while variable2  <0 :
        variable2  =(input("Nhập vào điểm môn Hoá :"))
        if is_float(variable2):
            variable2=float(variable2)
        else:
            variable2 = -5
            print("Nhập sai rồi, nhập lại đi")
    else:
        print("Điểm môn Hoá là",variable2) 

    while variable3 <0 :
        variable3 = (input("Nhập vào điểm môn Lý :"))
        if is_float(variable):
            variable3=float(variable3)
        else:
            variable3= -2
            print("Nhập sai rồi,nhập lại đi") 
    else:
        print ("Điểm môn Lý là",variable3)

    diemTB=(variable+variable1+variable2+variable3)/4
    print("Điểm TB của 4 môn học là :",diemTB)

a=tbc()
print(a)