sunday=['Refuel your soul','Take it slow!','Read a good book!']
monday=['Monday is a state of mind','Hello Monday','New Monday, New Week']
tuesday=['There will always be Tuesday','Tuesday is cleaning day','Tuesday is not so bad']
wednesday=['Keep at it!','Consistency is key','Patience is a virtue']
thursday=['Think positive Thursday!','Thankful Thursday','Friday Eve']
friday=['Good news:it is Friday!','It all works out!','End of the week!']
saturday=['Enjoy nature','Take a walk','Get some sunshine!']


def sun_func():
	for element in range(0, len(sunday)):
		print(sunday[element])

 
from tkinter import *
from tkinter import ttk
rw=Tk()
btn1=ttk.Button(rw,text="Sunday")
btn1.pack()
btn1.config(command=sun_func)
rw.mainloop()