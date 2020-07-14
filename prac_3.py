#the lists below are comprised of 3 strings 
sunday=['Refuel your soul','Take it slow!','Read a good book!']
monday=['Monday is a state of mind','Hello Monday','New Monday, New Week']
tuesday=['There will always be Tuesday','Tuesday is cleaning day','Tuesday is not so bad']
wednesday=['Keep at it!','Consistency is key','Patience is a virtue']
thursday=['Think positive Thursday!','Thankful Thursday','Friday Eve']
friday=['Good news:it is Friday!','It all works out!','End of the week!']
saturday=['Enjoy nature','Take a walk','Get some sunshine!']

# the functions below are meant to tell python to print each element
# in the related strings separately. Working to accomplish this
def sun_func():
	for element in range(0, len(sunday)):
		print(sunday[element])
def mon_func():
	for element in range(0,len(monday)):
		print(monday[element])
def tues_func():
	for element in range(0,len(tuesday)):
		print(tuesday[element])

 
from tkinter import *
from tkinter import ttk
rw=Tk()
btn1=ttk.Button(rw,text="Sunday")
btn1.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn1.config(command=sun_func)
btn2=ttk.Button(rw,text="Monday")
btn2.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn2.config(command=mon_func)
btn3=ttk.Button(rw,text="Tuesday")
btn3.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn3.config(command=tues_func)
rw.mainloop()