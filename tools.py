#centre
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import StringVar
from tkinter import IntVar
from tkinter import BooleanVar
def centre(frm):
    frm.update()
    sw=frm.winfo_screenwidth()
    sh=frm.winfo_screenheight()
    w=frm.winfo_width()
    h=frm.winfo_height()
    x=(sw-w)/2
    y=(sh-h)/2
    frm.geometry('%dx%d+%d+%d' %(w,h,x,y))



def strvar():
    return StrinVar()

def intvar():
    return IntVar()

def boolvar():
    return BooleanVar()
#!!!!!!!!!!!!!!!!!!!!!!!!!    

def form(geometry='350x200',is_center=True):
    frm=Tk()
    frm.geometry(geometry)
    if is_center:centre(frm)
    return frm

#!!!!!!!!!!!!!
def bgall(frm,bg):
    frm.update()
    ctrls=frm.winfo_children()
    frm.config(bg=bg)
    for c in ctrls:
        ci=c.winfo_class()
        if (ci=='Label' or ci=='Button' or ci=='Entry'
            or ci=='Radiobutton' or ci=='Checkbutton'):
            c['bg']=bg
        if (ci=='TLabel' or ci=='TButton' or ci=='TEntry'
            or ci=='TRadiobutton' or ci=='TCheckbutton'):
            my=ttk.Style()
            my.configure('TLabel',background=bg)
            my.configure('TButton',background=bg)
            my.configure('TEntry',background=bg)
            my.configure('TRadiobutton',background=bg)
            my.configure('TCheckbutton',background=bg)
            
#!!!!!!
def button(form,text='Button',command=None):
    btn=ttk.Button(form,text=text)
    if command!=None:
        btn.config(command=command)
    return btn    

def label(form,text='Button'):
    return ttk.Label(form,text=text)

def textbox(form,variable=None,is_number_only=False):

    def number_only(text):
        if str.isdigit(text):
            return True
        elif text is '':
            return True
        else:
            return False
    reg_fun = form.register(number_only) #tassgil dala 


    txt=ttk.Entry(form)
    if is_number_only:
        txt.config(validate='key',validatecommand=(reg_fun,'%P'))
    if variable!=None:
        txt.config(textvariable=variable)
    return txt

def radio(form,text='Radio',value=0,variable=None):
    rdo=ttk.Radiobutton(form,text=text,value=value)
    if variable!=None:
        rdo.config(variable=variable)
    return rdo

def checkbox(form,text='Checkbox',variable=None):
    cbx=ttk.Checkbutton(form,text=text)
    if variable!=None:
        cbx.config(variable=variable)
    return cbx 
#!!!!!!           
def fontall(frm,font):
    frm.update()
    ctrls=frm.winfo_children()
    for c in ctrls:
        ci=c.winfo_class()
        if (ci=='Label' or ci=='Button' or ci=='Entry' or ci=='TEntry'
            or ci=='Radiobutton' or ci=='Checkbutton'):
            c['font']=font
        if (ci=='TLabel' or ci=='TButton' or ci=='TRadiobutton'
            or ci=='TCheckbutton'):
            my=ttk.Style()
            my.configure('TLabel',font=font)
            my.configure('TButton',font=font)
            my.configure('TRadiobutton',font=font)
            my.configure('TCheckbutton',font=font)
            #my.configure('TEntry',font=font)

def fgall(frm,fg):
    frm.update()
    ctrls=frm.winfo_children()
    for c in ctrls:
        ci=c.winfo_class()
        if (ci=='Label' or ci=='Button' or ci=='Entry'
            or ci=='Radiobutton' or ci=='Checkbutton'):
            c['fg']=fg
        if (ci=='TLabel' or ci=='TButton' or ci=='TEntry'
            or ci=='TRadiobutton' or ci=='TCheckbutton'):
            my=ttk.Style()
            my.configure('TLabel',foreground=fg)
            my.configure('TButton',foreground=fg)
            my.configure('TEntry',foreground=fg)
            my.configure('TRadiobutton',foreground=fg)
            my.configure('TCheckbutton',foreground=fg)

def msgbox(text,vr=''):
    messagebox.showinfo(vr,text)

def msgask(text):
    return messagebox.askyesno('',text) #ayroturni lak true ola false l9ima

def inbox(text,is_number_only=False):
    f=Toplevel()
    f.title(text)
    f.geometry('400x300')
    f.resizable(False,False)
    centre(f)
    ttk.Label(f,text=text,font='None 15').pack(pady=10)
    sv=StringVar()

    def number_only(text):
        if str.isdigit(text):
            return True
        elif text is '':
            return True
        else:
            return False

    reg_fun = f.register(number_only) #tassgil dala 


    txt=ttk.Entry(f,font='None 15',width=35,textvariable=sv)
    if is_number_only:
        txt.config(validate='key',validatecommand=(reg_fun,'%P'))
        
    txt.pack(pady=10)
    txt.bind('<Return>',lambda my:f.destroy()) #mili ghadi tklicer enter 
    ttk.Style().configure('inbox.TButton',font='None 15')#inbox ghi smiya
    ttk.Button(f,text='OK',command=lambda:f.destroy(),style='inbox.TButton').pack(pady=10)
    f.grab_set()
    f.wait_window() #katgolih tssanah tay9fal
    return sv.get()
    
