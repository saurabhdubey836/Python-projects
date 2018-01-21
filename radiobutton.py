from tkinter import *
root = Tk()


def mmmm():
         a = v.get()
         if (a==1):  
                     a1 = Tk()
                     a1.title('python')
                     l1=Label(a1,text = "welcome to python group",font=10)
                     l1.pack()
         elif(a==2):
                      a2 = Tk()
                      a2.title("pearl")
                      l2=Label(a2,text="welcome to pearl group",font=10)
                      l2.pack()
         elif(a==4):
                      a3 = Tk()
                      a3.title("c++ Language")
                      l3=Label(a3,text="welcome to c++ Language group",font=10)
                      l3.pack()
      

root.title("radio button")
v = IntVar()
v.set(3)
Label(root,text='choose a programming language\n Language',padx=25,justify=LEFT).pack()
Radiobutton(root,text = "python",padx=25,indicatoron=0,variable=v,value=1,command=mmmm).pack(anchor = W)
Radiobutton(root,text = "perl",padx=25,indicatoron=0,variable=v,value=2,command=mmmm ).pack(anchor = W)
Radiobutton(root,text = "c Language",padx=25,indicatoron=0,variable=v,value=3 ,command=mmmm).pack(anchor = W)
Radiobutton(root,text = "c++ Language",padx=25,indicatoron=0,variable=v,value=4,command=mmmm).pack(anchor = W)





root.mainloop()
