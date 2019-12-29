#CALCULATRICE
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tools
frm=Tk()
frm.geometry("1100x650")
tools.centre(frm)
frm.iconbitmap('Hop.ico')
fnt='None 30 bold'
bg='#baf'
fgc='#ffffff'
bgtxt='lightblue'
fg='#fc3'
pad=1
frm.title('Claculatrice by Python')
frm.config(bg=bg)
frm.resizable(False,False)


frame=Frame(frm,bg=bg)
frame.pack(pady=pad,padx=40)

liste =[]
txt=''
def calc(f):
    if f=='=':
        global txt
        for i in liste:
            txt=txt+i
        svnum.set(eval(txt))
        liste[:] = []
        liste.append(str(eval(txt)))
        txt=''
    elif f=='AC':
        txt=''
        #3ad dir txt=txt+f
        liste[:] = []
        
        svnum.set(liste)
        
    elif f=='C':
        a=len(liste)
        del liste[a-1]
        svnum.set(liste)
        #txt='%'
        #liste.append(txt)

    elif f=='0':
        a=len(liste)
        if liste[a-1]=='/':
            messagebox.showwarning('Error','On ne peut pas diviser par 0')
        else:
            liste.append(f)
            svnum.set(liste)
            
    else :
        liste.append(f)
        svnum.set(liste)

svnum=StringVar()

txtnum=Entry(frame,bg=bgtxt,fg=fg,font=fnt,textvariable=svnum)
svnum.set('0')
txtnum.grid(row=1,column=0,columnspan=5,pady=30,padx=20)
Label(frame,bg=bg,fg=fg,font=fnt).grid(row=0,column=0,columnspan=5)

#.grid(row=0,column=1,pady=pad)
btnstyle=ttk.Style()
btnstyle.configure('TButton',font=fnt,pady=pad,padding=pad)

ttk.Button(frame,text='%',command=lambda:calc('%')).grid(row=3,column=1)
ttk.Button(frame,text='C',command=lambda:calc('C')).grid(row=3,column=2)
tkinter.Button(frame,text='AC',font='arial 10 bold',command=lambda:calc('AC'),bg='orange',padx=110,pady=15).grid(row=3,column=3)
ttk.Button(frame,text='/',command=lambda:calc('/')).grid(row=3,column=4)

ttk.Button(frame,text='7',command=lambda:calc('7')).grid(row=4,column=1)
ttk.Button(frame,text='8',command=lambda:calc('8')).grid(row=4,column=2)
ttk.Button(frame,text='9',command=lambda:calc('9')).grid(row=4,column=3)
ttk.Button(frame,text='x',command=lambda:calc('*')).grid(row=4,column=4)

ttk.Button(frame,text='4',command=lambda:calc('4')).grid(row=5,column=1)
ttk.Button(frame,text='5',command=lambda:calc('5')).grid(row=5,column=2)
ttk.Button(frame,text='6',command=lambda:calc('6')).grid(row=5,column=3)
ttk.Button(frame,text='-',command=lambda:calc('-')).grid(row=5,column=4)

ttk.Button(frame,text='1',command=lambda:calc('1')).grid(row=6,column=1)
ttk.Button(frame,text='2',command=lambda:calc('2')).grid(row=6,column=2)
ttk.Button(frame,text='3',command=lambda:calc('3')).grid(row=6,column=3)
btn1=ttk.Button(frame,text='+',command=lambda:calc('+'))
btn1.configure(padding=(2,25,2,33))
btn1.grid(row=6,column=4,rowspan=2)

ttk.Button(frame,text='0',command=lambda:calc('0')).grid(row=7,column=1)
ttk.Button(frame,text=',',command=lambda:calc('.')).grid(row=7,column=2)
ttk.Button(frame,text='=',command=lambda:calc('=')).grid(row=7,column=3)

ttk.Button(frm,text='        Exit Now        ',command=frm.destroy).pack(pady=30)



frm.mainloop()
input('Press enter to exit...')
