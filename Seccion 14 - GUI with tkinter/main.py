from tkinter import *


window=Tk()
gui = None

def km_to_mile():
	miles = float(gui.e1_value.get())*1.606
	gui.t1.insert(END, miles)

class UI:
	def __init__(self):
		self.b1=Button(window, text="Execute", command=km_to_mile)
		self.b1.grid(row=0, column=0)
		
		
		self.e1_value = StringVar()
		self.e1=Entry(window,textvariable=self.e1_value)
		self.e1.grid(row=0, column=1)
		
		self.t1=Text(window, height=1, width=20)
		self.t1.grid(row=0, column=2)

def main():
	global gui 
	gui = UI()
	window.mainloop()
	
	
main()
