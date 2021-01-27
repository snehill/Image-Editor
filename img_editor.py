import tkinter as tk
import os
from tkinter import ttk, filedialog, Scale, messagebox
from PIL import Image, ImageEnhance,ImageFilter, ImageTk
win=tk.Tk()
win.title("Image Editor")
win.geometry("515x200")
win.resizable(0,0)
win.config(bg="#fffff0")
img_sharp=tk.PhotoImage(file="sharp.png")
img_color=tk.PhotoImage(file="color_filter.png")
img_bright=tk.PhotoImage(file="brightness.png")
img_contrast=tk.PhotoImage(file="contrast.png")
# img_p=tk.PhotoImage(file="p.png")

# label frame > left

label_l=tk.LabelFrame(win, width=200, height=190, bg="#f5f5f5",bd=0)
label_l.pack(side=tk.LEFT,padx=10)

# label frame > right

label_r=tk.LabelFrame(win, width=390, height=190, bg="#f0e68c",bd=0)
label_r.pack(side=tk.RIGHT,padx=10)

#entry

var=tk.StringVar()
path_entry=ttk.Entry(win,width=20,textvariable=var)
path_entry.place(x=239,y=14)
path_entry.focus()

#btn

d=None
def open_file():
    try:
        global d
        path_entry.delete(0,tk.END)
        url = filedialog.askopenfilename( title = 'Select file' )
        path_entry.insert(tk.END, url)
        f_nam,f_ext=os.path.splitext(url)        
        imgg=Image.open(url)
        d=imgg        
        img=imgg.resize((200,183), Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img)
        pannel=tk.Label(label_l, image=img)
        pannel.image = img
        pannel.grid(row=2)
        win.title(os.path.basename(url))        
        sd(imgg,f_ext)
    except:
        messagebox.showerror("Error re baabaaa!","Somthing went wrong.")
btn1=tk.Button(win, width=10,text="Select Image", bd=0,bg="#fffff0",fg="black",font=('serif',9), command=open_file)
btn1.place(x=380, y=14)

def change(z):
    img=z
    img=img.resize((200,183), Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    pannel=tk.Label(label_l, image=img)
    pannel.image = img  
    pannel.grid(row=2)   
 
l=1   #__l__
o=None  #__o__
D=None
def lev(b,ds):
    global D             
    master=tk.Tk()
    D=master
    master.geometry("210x140")
    w =tk.Scale(master, from_=0, to=100, highlightcolor="blue",command=bri)
    w.set(l)
    w.pack(anchor=tk.CENTER) 
    lk=ttk.Label(master, text=ds)
    lk.pack()            
def bri(e):
    global d
    global l
    global o
    l=int(e)
    x=o.enhance(l)
    d=x
    change(x)

# editing tools >>>>
    
def sharpness():
    nn="Sharpness"
    global d
    global o        
    global l
    img=d
    enhancer = ImageEnhance.Sharpness(img)
    b=enhancer
    o=enhancer
    lev(b,nn)
btn2=tk.Button(win,text="Sharpness",image=img_sharp,compound=tk.TOP, command=sharpness, bd=0, bg="#f0e68c")
btn2.place(x=250, y=90)

def color():
    nn="Color"
    global d
    global o
    img=d
    enhancer = ImageEnhance.Color(img)
    b = enhancer
    o = enhancer
    lev(b,nn)
btn2=tk.Button(win,text="Color",image=img_color,compound=tk.TOP, command=color,bg="#f0e68c",bd=0)
btn2.place(x=257, y=142)    

def brightness():
    nn="Brightness"
    global d
    global o
    img=d
    enhancer =ImageEnhance.Brightness(img)
    b = enhancer
    o = enhancer
    lev(b,nn)
btn2=tk.Button(win,text="Brightness",image=img_bright,compound=tk.TOP,command=brightness,bg="#f0e68c",bd=0)
btn2.place(x=320, y=90)

def contrast():
    nn="Contrast"
    global d
    global o
    img=d
    enhancer = ImageEnhance.Contrast(img)
    b = enhancer
    o = enhancer
    lev(b,nn)

btn2=tk.Button(win,text="Contrast",image=img_contrast,compound=tk.TOP, command=contrast, bg="#f0e68c",bd=0)
btn2.place(x=322, y=142)

#combobox

label_1=tk.Label(label_r, text="Compress Size ",bd=0,bg="#f0e68c",font=("Serif",10))
label_1.place(x=157,y=68)
label_2=tk.Label(label_r,text="x",bg="#f0e68c",font=("bold"))
label_2.place(x=201,y=88)
var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
formats=(
    ".png",".jpg",".pdf",".tiff",".ico",".jpeg"
)
box1=ttk.Combobox(label_r,width=4,textvariable=var1)
box2=ttk.Combobox(label_r,width=4,textvariable=var2)
box3=ttk.Combobox(label_r,width=10,textvariable=var3)
box1['values'] = tuple(range(1,4001))
box2['values'] = tuple(range(1,4001))
box3['values'] = formats

box1.place(x=152,y=90)
box2.place(x=217,y=90)
box3.place(x=168,y=125)

def sd(x,gf):        
    width,height=x.size
    dd=width
    ddd=height
    box1.current(dd)
    box2.current(ddd)                
    bb=0    
    for i in formats:
        if i==gf:

            box3.current(bb)
        else:
            bb+=1                    

def save():
    a=var3.get()

    url=filedialog.asksaveasfile(mode='wb',defaultextension=f"{a}")   
    x=var1.get()
    y=var2.get()
    max_size=(int(x),int(y))    
    if not url:
        return
    d.thumbnail(max_size)
    t=d.save(url)
    messagebox.showinfo('Ho gyA BHAIYA', "Img Saved congo..")

save_button=ttk.Button(label_r,text="Save",width=7, command=save)
save_button.place(x=217,y=157)

def dosomething():
    if d:
        try:
            a=messagebox.askyesno("wanna cancel!","Sochh le <*!*>"  )
            if a:
                win.destroy()    
                D.destroy()    
        except:
            pass
    else:
        win.destroy()    
win.protocol("WM_DELETE_WINDOW",dosomething)
win.mainloop()



