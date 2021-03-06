#Arayüz paketinin eklenmesi
from tkinter import *
from random import randint

ekran = Tk()
ekran.title('Sayısal Loto')
ekran.geometry("1000x200")
ekran.configure(bg= "pink")

baslik = Label(ekran, text="Sayısal Lotoya Hoş Geldiniz <3")
baslik.config(font=("Times New Roman", 15), fg="white", bg="purple")
baslik.grid(row=0, column=0)

def sayisal():
    i = 0
    secilenler = [0, 0, 0, 0, 0, 0]
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 99)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i += 1
        sirali = sorted(secilenler)
        i = 0

        numaralar = Label (ekran, text=sirali)
        numaralar.grid(row=0, column=100)

goster = Button(ekran, text="Numaraları Yazdır!", command=sayisal, fg="white", bg="purple")
goster.grid(row=1, column=0)

def getint():
    yardim =Label(ekran, text= "Sayılarda bir sorun olduğunu düşünüyorsan Sayısal Loto Resmi Sitesini ziyaret etmelisin :)")
    yardim.grid(row=2, column=1)

yardim = Button(ekran, text="Yardım", command=getint, fg= "white", bg="purple")
yardim.grid(row=2, column=0)

cikis = Button(ekran, text="Çıkış!", command=ekran.quit, fg="white", bg="purple")
cikis.grid(row=3, column=0)

ekran.mainloop()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
