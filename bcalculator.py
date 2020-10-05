from tkinter import*

root= Tk()
root.title('simple Calculator')

display=Entry(root,width=40,borderwidth=5,justify=CENTER)
display.grid(row=0,columnspan=4)

def b_click(number):
   
    display.get()
    display.insert(len(display.get()),str(number))

def clear():
    display.delete(0,END)

def equal():
    text=display.get()
    display.delete(0,END)
    if '+' in text:
        a=text.index('+')     
        fn= float(text[0:a])
        sn= float(text[a+1:len(text)])
        result=fn+sn
        display.insert(0,str(result))
        END
    if  '-' in text:
        a=text.index('-')     
        fn= float(text[0:a])
        sn= float(text[a+1:len(text)])
        result=fn-sn
        display.insert(0,str(result))
        END

    if '*' in text:
        a=text.index('*')     
        fn= float(text[0:a])
        sn= float(text[a+1:len(text)])
        result=fn*sn
        display.insert(0,str(result))
        END
    if '/' in text:
        a=text.index('/')     
        fn=float(text[0:a])
        sn=float(text[a+1:len(text)])
        result=fn/sn
        display.insert(0,str(result))
        END
#define buttons

button_1=Button(root,text='1',padx=40,pady=20,command=lambda:b_click(1))
button_2=Button(root,text='2',padx=40,pady=20,command= lambda:b_click(2))
button_3=Button(root,text='3',padx=40,pady=20,command= lambda:b_click(3))
button_4=Button(root,text='4',padx=40,pady=20,command= lambda:b_click(4))
button_5=Button(root,text='5',padx=40,pady=20,command= lambda:b_click(5))
button_6=Button(root,text='6',padx=40,pady=20,command= lambda:b_click(6))
button_7=Button(root,text='7',padx=40,pady=20,command= lambda:b_click(7))
button_8=Button(root,text='8',padx=40,pady=20,command= lambda:b_click(8))
button_9=Button(root,text='9',padx=40,pady=20,command= lambda:b_click(9))
button_0=Button(root,text='0',padx=40,pady=20,command= lambda:b_click(0))

button_add=Button(root,text='+',padx=24,pady=20,command=lambda:b_click('+'))
button_sub=Button(root,text='-',padx=24,pady=20,command=lambda:b_click('-'))
button_mul=Button(root,text='*',padx=40,pady=20,command=lambda:b_click('*'))
button_div=Button(root,text='/',padx=40,pady=20,command=lambda:b_click('/'))
button_equal=Button(root,text='=',padx=23,pady=20,command=equal)
button_clear=Button(root,text='CLR',padx=18,pady=20,command=clear)

#define buttons 
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_clear.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_add.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_sub.grid(row=3,column=3)

button_0.grid(row=4,column=0)
button_mul.grid(row=4,column=1)
button_div.grid(row=4,column=2)
button_equal.grid(row=4,column=3)


root.mainloop()
