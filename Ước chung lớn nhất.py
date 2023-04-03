def UCLN(x,y):
    if x == 0:
        return y
    else:
        r = y % x
        return UCLN(r,x)

x = int(input("Nhập giá trị x: "))
y = int(input("Nhập giá trị y: "))

print("ước chung lớn nhất của x và y là: ",UCLN(x,y))