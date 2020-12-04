data = open("Praktikum7.2.txt","r")
int_1 = int(data.readline())
int_2 = int(data.readline())

try:
    result = int_1 / int_2
    print("Bilangan {} dibagi  dengan bilangan {} hasilnya adalah {}".format(int_1,int_2,result))
except ZeroDivisionError:
    print("Bilangan Tidak bisa dibagi dengan nol")