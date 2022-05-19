from tkinter import *
from matplotlib.figure import Figure
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from validation import validate_in
from tkinter import messagebox


window = Tk()
window.configure(bg="white")
window.geometry("900x600")
window.resizable(False, False)
window.title("function plotter")
logo= PhotoImage(file="Master Micro.png")
window.iconphoto(True,logo)

def get_max():

    return Range_max.get()
Range_min=Entry(window,font=("Comic sans",20,"bold"),fg="black",width=3,border=4,)
def get_min():
    return Range_min.get()
def get_input():
    return input_txt.get()
def fun():
    try:
     l.destroy()
     res=[]
     MAx=eval(Range_max.get())
     MIn=eval(Range_min.get())
     rangearr=[]
     if(MAx>MIn):
        rangearr = numpy.linspace(MAx,MIn,100)
     else:
        validate_in("2*x",MIn,MAx)

     for i in range (0,len(rangearr)):
       res.append(formula(float(rangearr[i])))
     fig = plt.Figure(figsize=(5, 5), dpi=100)

     fig.add_subplot(111).plot(rangearr, res)
     fig.add_gridspec()
     chart = FigureCanvasTkAgg(fig)
     chart.get_tk_widget().place(x=400, y=50)
    except:

        txt = input_txt.get()
        min=get_min()
        max=get_max()
        validate_in(txt,min,max)








def formula(x):
   x=x
   try:

    txt=input_txt.get()
    txt=txt.lower()
    txt=txt.replace("^","**")
    txt =eval(txt)
    return txt
   except:
       from validation import validate_in
       txt = input_txt.get()
       validate_in(txt)






Range_text=Label(window,text="Range", font=("Comic Sans MS",20,"bold"),fg="#212cc4",bg="white")
Range_text.place(x=70,y=300)
Range_min=Entry(window,font=("Comic sans",20,"bold"),fg="black",width=3,border=4,)
Range_min.place(x=70,y=350)
range_sign=Label(window,text=":", font=("Comic Sans MS",20,"bold"),fg="#212cc4",bg="white")
range_sign.place(x=130,y=350)
Range_max=Entry(window,font=("Comic sans",20,"bold"),fg="black",width=3,border=4,)
Range_max.place(x=150,y=350)
formula_word=Label(window,text="Formula", font=("Comic Sans MS",20,"bold"),fg="#212cc4",bg="white")
formula_word.place(x=40,y=400)
input_txt=Entry(window,font=("Arial",20,"bold"),fg="black",bg="white",bd=5,relief="groove")
input_txt.place(x=40,y=450)
input_button=Button(text="Submit",font=("Comic Sans MS",15,"bold"),bg="#212cc4",fg="white",command=fun)
input_button.place(x=40,y=500)
logo_can=Canvas(window,height=250,width=400,bg="white",highlightthickness=0)
logo_can.create_oval(-50,-50,250,250,fill="#212cc4")
logo_can.create_oval(-50,-50,200,200,fill="white")
logo_can.place(x=0,y=0)
logo_label=Label(bg="white",text="Function \n plotter",font=("Comic Sans MS", 28, "bold"),fg="#212cc4",padx=0)
logo_label.place(x=0,y=30)
text="instructions\n1.the input must be a function of x\n2.all text fields must be fullfiled\n3.only the following operators are supported + - * / ^"
l=Label(text=text,bg="white",font=("Comic Sans MS",14,"bold"),fg="#212cc4",padx=0,justify="left",anchor='w',bd=10)
l.place(x=350,y=0)
window.mainloop()