
from tkinter import*


root=Tk()
root.geometry("1500x800")

text_Input = StringVar()
operator = ""

Tops = Frame(root, width=500,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=500,height=2000,relief=SUNKEN)
f1.pack(side=RIGHT)

f2 = Frame(root,width=500, height=2000,bg="pink", relief=SUNKEN)
f2.pack(side=RIGHT)

def btnclick(numbers):
    global operator
    operator =operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup= str(eval(operator))
    text_Input.set(sumup)
    operator = ""

txtDisplay = Entry(f2,font=('arail', 20, 'bold'), textvariable=text_Input, bd=20, insertwidth=6, bg="pink")
txtDisplay.grid(columnspan=5)

btn7=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="7", bg="pink", command=lambda: btnclick(7))
btn7.grid(row=2,column=0)

btn8=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="8", bg="pink", command=lambda: btnclick(8))
btn8.grid(row=2,column=1)

btn9=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="9", bg="pink", command=lambda: btnclick(9))
btn9.grid(row=2,column=2)

Addition=Button(f2,padx=20,pady=20, fg="white", font=('arail',20,'bold'),text="+", bg="black", command=lambda: btnclick("+"))
Addition.grid(row=2,column=3)

btn4=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="4", bg="pink", command=lambda: btnclick(4))
btn4.grid(row=3,column=0)

btn5=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="5", bg="pink", command=lambda: btnclick(5))
btn5.grid(row=3,column=1)

btn6=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="6", bg="pink", command=lambda: btnclick(6))
btn6.grid(row=3,column=2)


Subtraction=Button(f2,padx=20,pady=20, fg="white", font=('arail',20,'bold'),text="-", bg="black", command=lambda: btnclick("-"))
Subtraction.grid(row=3,column=3)

btn1=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="1", bg="pink", command=lambda: btnclick(1))
btn1.grid(row=4,column=0)

btn2=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="2", bg="pink", command=lambda: btnclick(2))
btn2.grid(row=4,column=1)

btn3=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="3", bg="pink", command=lambda: btnclick(3))
btn3.grid(row=4,column=2)

Multiply=Button(f2,padx=20,pady=20, fg="white", font=('arail',20,'bold'),text="*", bg="black", command=lambda: btnclick("*"))
Multiply.grid(row=4,column=3)

btn0=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="0", bg="pink", command=lambda: btnclick(0))
btn0.grid(row=5,column=0)

btnClear=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="C", bg="pink", command=btnClearDisplay)
btnClear.grid(row=5,column=1)

btnEquals=Button(f2,padx=20,pady=20, fg="black", font=('arail',20,'bold'),text="=", bg="pink", command=btnEqualsInput)
btnEquals.grid(row=5,column=2)

Division=Button(f2,padx=20,pady=20, fg="white", font=('arail',20,'bold'),text="/", bg="black", command=lambda: btnclick("/"))
Division.grid(row=5,column=3)

root.mainloop()