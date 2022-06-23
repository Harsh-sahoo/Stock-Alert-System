from tkinter import *
from yahoo_fin import stock_info
from win10toast import ToastNotifier
from PIL import Image, ImageTk


def Take_input():
    brand_name=brand_entry.get()
    lower_lt=int(fall_entry.get())
    upper_lt=int(rise_entry.get())

    def stock_range(ul,ll,pr):
        if (pr < ll):
            flag=1
        elif (pr>ll and pr<ul):
            flag=2
        else:
            flag=0
        return flag

    val=True
    while val:
        price=stock_info.get_live_price(brand_name)
        x= stock_range(upper_lt,lower_lt,price)
        if (x==1):
            hr=ToastNotifier()
            hr.show_toast("Loss!!",f"Your Stock {brand_name} is below {lower_lt}₹")
        elif (x==2):
            pass
        else:
            hr=ToastNotifier()
            hr.show_toast("Profit!!",f"Your Stock {brand_name} is above {upper_lt}₹")

root=Tk()
root.title("STOCK ALERT SYSTEM")


label1=Label(root,text="Stock Alert System",font=("Ariel",16))
label1.grid(row=0, columnspan=5)

label2=Label(root,text="Enter your stock name : ",font=("Ariel",16))
label2.grid(row=1,column=0,sticky=W)

label3=Label(root,text="Fall Below                    :",font=("Ariel",16))
label3.grid(row=2,column=0,sticky=W)

label3a=Label(root,text="₹",font=("Ariel",16))
label3a.grid(row=2,column=2)

label4=Label(root,text="Rise Above                  :",font=("Ariel",16))
label4.grid(row=3,column=0,sticky=W)

label4a=Label(root,text="₹",font=("Ariel",16))
label4a.grid(row=3,column=2)

label5=Label(root,text="Do you want to exit the process? :",font=("Ariel",16))
label5.grid(row=6,column=0,sticky=W)

label6=Label(root,text="Select Company Symbol from the given Refrence Table :",font=("Ariel",16))
label6.grid(row=7,columnspan=10,sticky=W)


data1=StringVar()
brand_entry=Entry(root,textvariable="data1",bg="Powder Blue",font=("Ariel",15),width=15)
brand_entry.grid(row=1,column=1)

data2=StringVar()
fall_entry=Entry(root,textvariable="data2",bg="Powder Blue",font=("Ariel",15),width=15)
fall_entry.grid(row=2,column=1)

data3=StringVar()
rise_entry=Entry(root,textvariable="data3",bg="Powder Blue",font=("Ariel",15),width=15)
rise_entry.grid(row=3,column=1)


btn1=Button(root,text="Submit",font=("Ariel",12,"bold"),bd=3,height=1,width=8,command=Take_input)
btn1.grid(row=4,column=4)


btn2=Button(root,text="Yes",font=("Ariel",12,"bold"),bd=3,height=1,width=8,command=root.quit)
btn2.grid(row=6,column=1)

btn3=Button(root,text="No",font=("Ariel",12,"bold"),bd=3,height=1,width=8)
btn3.grid(row=6,column=2)

image = Image.open('chart.jpg')

resized=image.resize((800,300),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)

label7 = Label(root, image = photo)
label7.image = photo
label7.grid(row=8,columnspan=100)

image = Image.open('lnct.png')

resized=image.resize((100,100),Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(resized)

label7 = Label(root, image = photo1)
label7.image = photo1
label7.grid(row=1,column=3)


root.geometry("800x500+400+150")
root.resizable(0,0)
root.mainloop()