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

#practice attempting to iterate each line
def sun_func():
	for element in range(0,len(sunday)):
		print(sunday[element])
def mon_func():
	for element in range(0,len(monday)):
		print(monday[element])
def tues_func():
	for element in range(0,len(tuesday)):
		print(tuesday[element])
def wed_func():
	for element in range(0,len(wednesday)):
		print(wednesday[element])
def thurs_func():
	for element in range(0,len(thursday)):
		print(thursday[element])
def fri_func():
	for element in range(0,len(friday)):
		print(friday[element])
def sat_func():
	for element in range(0,len(saturday)):
		print(saturday[element])


 
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
btn4=ttk.Button(rw,text="Wednesday")
btn4.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn4.config(command=wed_func)
btn5=ttk.Button(rw,text="Thursday")
btn5.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn5.config(command=thurs_func)
btn6=ttk.Button(rw,text="Friday")
btn6.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn6.config(command=fri_func)
btn7=ttk.Button(rw,text="Saturday")
btn7.pack()
#the command is needed to call the fucntion and tell the button what to
#print
btn7.config(command=sat_func)
rw.mainloop()